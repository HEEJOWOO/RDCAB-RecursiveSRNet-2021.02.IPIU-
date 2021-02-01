# RDCAB-RecursiveSRNet

## Single Image Super Resolution Based on Residual Dense Channel Attention Block-RecursiveSRNet (IPIU, 2021.02.03~05)
## Abstract
With the recent development of deep convolutional neural network learning, deep learning techniques applied to the super-resolution of single images are showing good results. One of the existing deep learning-based super-resolution techniques is RDN (Residual Dense Network), in which initial feature information is transmitted to the last layer using residual dense blocks, and subsequent layers are restored using input information of previous layers. . However, if all hierarchical features are connected and learned and a large number of residual dense blocks are stacked, despite good performance, a large number of parameters is obtained, so it takes a lot of time to learn the network, and it is difficult to apply it to a mobile system. In this paper, we propose a single image super-resolution network based on a recursive lightweight network with a residual dense structure and a channel concentration scheme. As a result of the experiment, the proposed network produced similar performance with 1.18 times faster processing speed compared to RDN, and it was able to reduce the computation amount by having about 10 times fewer parameters.

## Network
* RDCAB-RecursiveSRNet
![RDCAN-RecursivSRNet](https://user-images.githubusercontent.com/61686244/106457120-dafeb480-64d1-11eb-8c89-f8446afbf0ec.png)
* RDCAB
![RDCAB](https://user-images.githubusercontent.com/61686244/106457205-f8cc1980-64d1-11eb-8645-2327f04d305d.png)

## Train
The DIV2K, Set5 dataset converted to HDF5 can be downloaded from the links below.
|Dataset|Scale|Type|Link|
|-------|-----|----|----|
|Div2K|x2|Train|[Down](https://www.dropbox.com/s/41sn4eie37hp6rh/DIV2K_x2.h5?dl=0)|
|Div2K|x3|Train|[Down](https://www.dropbox.com/s/4piy2lvhrjb2e54/DIV2K_x3.h5?dl=0)|
|Div2K|x4|Train|[Down](https://www.dropbox.com/s/ie4a6t7f9n5lgco/DIV2K_x4.h5?dl=0)|
|Set5|x2|Eval|[Down](https://www.dropbox.com/s/b7v5vis8duh9vwd/Set5_x2.h5?dl=0)|
|Set5|x3|Eval|[Down](https://www.dropbox.com/s/768b07ncpdfmgs6/Set5_x3.h5?dl=0)|
|Set5|x4|Eval|[Down](https://www.dropbox.com/s/rtu89xyatbb71qv/Set5_x4.h5?dl=0)|

## Test
Evaluation of Set5, Set14, BSD100, Urban100 using PSNR, SSIM

## Experiment Result
* PSNR, SSIM for Test Set
![image](https://user-images.githubusercontent.com/61686244/106460006-07b4cb00-64d6-11eb-8e31-ab64a6416f8b.png)
* Comparison of the number of parameters in each network
![image](https://user-images.githubusercontent.com/61686244/106460063-1d29f500-64d6-11eb-885f-8402c9af46a5.png)
![image](https://user-images.githubusercontent.com/61686244/106460133-3468e280-64d6-11eb-9a94-f169507960f9.png)
* Performance comparison for training time and execution time
![image](https://user-images.githubusercontent.com/61686244/106460196-4ba7d000-64d6-11eb-88cc-1509fc9b2faa.png)
* Comparison of number of parameters and performance according to the number of recursions
![image](https://user-images.githubusercontent.com/61686244/106460243-5e220980-64d6-11eb-97c7-af3f7ab6c580.png)

* Comparison of performance by technique                                                                       
![image](https://user-images.githubusercontent.com/61686244/106460273-6f6b1600-64d6-11eb-9b39-2da2482d8848.png)
* Scale 2
![image](https://user-images.githubusercontent.com/61686244/106460365-97f31000-64d6-11eb-8a26-155eabab0d97.png)
* Scale 3
![image](https://user-images.githubusercontent.com/61686244/106460388-a0e3e180-64d6-11eb-80e6-214827332930.png)
* Scale 4
![image](https://user-images.githubusercontent.com/61686244/106460418-af31fd80-64d6-11eb-8e40-293803ade496.png)













