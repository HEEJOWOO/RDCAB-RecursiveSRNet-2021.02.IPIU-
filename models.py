from torch import nn
import torch

class DenseLayer(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(DenseLayer, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=3 // 2)
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        return torch.cat([x, self.relu(self.conv(x))], 1)

class RDCAB(nn.Module):
    def __init__(self, in_channels, growth_rate, num_layers):
        super(RDCAB, self).__init__()
        self.layers = nn.Sequential(*[DenseLayer(in_channels + growth_rate * i, growth_rate) for i in range(num_layers)])
        # global average pooling: feature --> point
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        # feature channel downscale and upscale --> channel weight
        self.conv_du = nn.Sequential(
                nn.Conv2d(in_channels+growth_rate*num_layers, (in_channels+growth_rate*num_layers)//16, 1, padding=0, bias=True),
                nn.ReLU(inplace=True),
                nn.Conv2d((in_channels+growth_rate*num_layers)//16, in_channels+growth_rate*num_layers, 1, padding=0, bias=True),
                nn.Sigmoid()
        )
        # local feature fusion
        self.lff = nn.Conv2d(in_channels + growth_rate * num_layers, growth_rate, kernel_size=1)

    def forward(self, x, sfe_residual): 
        local_x = x
        x = self.layers(x)
        CA_x =x
        y = self.avg_pool(x)
        y = self.conv_du(y)
        x = x*y
        #x = x+CA_x
        return local_x + self.lff(x) + sfe_residual

class RecursiveBlock(nn.Module):
    def __init__(self,num_channels, num_features, growth_rate, num_layers, B, U):
        super(RecursiveBlock, self).__init__()
        self.U = U
        self.G0 = num_features
        self.G = growth_rate
        self.C = num_layers
        self.rdcabs = RDCAB(self.G0, self.G, self.C) #residual dense channel attention block 생성
        
    def forward(self, sfe2):
        global concat_LF
        x=sfe2
        local_features = []
        for i in range(self.U):
            x = self.rdcabs(x, sfe2)
            local_features.append(x)
        concat_LF = torch.cat(local_features, 1)
        return x

class Net(nn.Module):
    def __init__(self, scale_factor, num_channels, num_features, growth_rate, num_layers, B, U):
        super(Net, self).__init__()
        self.B = B
        self.G0 = num_features
        self.G = growth_rate
        self.U = U
        self.C = num_layers
        
        self.sfe1 = nn.Conv2d(num_channels, num_features, kernel_size=3, padding=3 // 2)
        self.sfe2 = nn.Conv2d(num_features, num_features, kernel_size=3, padding=3 // 2)
        
        self.recursive_SR = nn.Sequential(*[RecursiveBlock(num_channels if i==0 else num_features,
        num_features,
        growth_rate, 
        num_layers, 
        B, 
        U) for i in range(B)])
        # global feature fusion
        self.gff = nn.Sequential(
            nn.Conv2d(self.G * self.U * self.B, self.G0, kernel_size=1),
            nn.Conv2d(self.G0, self.G0, kernel_size=3, padding=3 // 2)
        )
        # up-sampling
        assert 2 <= scale_factor <= 4
        if scale_factor == 2 or scale_factor ==3 or scale_factor == 4:
            self.upscale = nn.Sequential(
                nn.Conv2d(self.G0, self.G0 * (scale_factor ** 2), kernel_size=3, padding=3 // 2),
                nn.PixelShuffle(scale_factor)
            )
        self.output = nn.Conv2d(self.G0, num_channels, kernel_size=3, padding=3 // 2)
        
    def forward(self, x):
        sfe1 = self.sfe1(x)
        sfe2 = self.sfe2(sfe1)
        local_global_features=[]
        for i in range(self.B):
            if i==0:
                x= self.recursive_SR(sfe2)
                local_global_features.append(concat_LF)
            elif i>0:
                x= self.recursive_SR(x)
                local_global_features.append(concat_LF)
        x = self.gff(torch.cat(local_global_features, 1)) + sfe1
        x = self.upscale(x)
        x = self.output(x)
        return x
