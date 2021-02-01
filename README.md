# RDCAB-RecursiveSRNet

## Single Image Super Resolution Based on Residual Dense Channel Attention Block-RecursiveSRNet (2021.02)
## Abstract
With the recent development of deep convolutional neural network learning, deep learning techniques applied to the super-resolution of single images are showing good results. One of the existing deep learning-based super-resolution techniques is RDN (Residual Dense Network), in which initial feature information is transmitted to the last layer using residual dense blocks, and subsequent layers are restored using input information of previous layers. . However, if all hierarchical features are connected and learned and a large number of residual dense blocks are stacked, despite good performance, a large number of parameters is obtained, so it takes a lot of time to learn the network, and it is difficult to apply it to a mobile system. In this paper, we propose a single image super-resolution network based on a recursive lightweight network with a residual dense structure and a channel concentration scheme. As a result of the experiment, the proposed network produced similar performance with 1.18 times faster processing speed compared to RDN, and it was able to reduce the computation amount by having about 10 times fewer parameters.

## Network
### RDCAB-RecursiveSRNet
![RDCAN-RecursivSRNet](https://user-images.githubusercontent.com/61686244/106457120-dafeb480-64d1-11eb-8c89-f8446afbf0ec.png)
### RDCAB
![RDCAB](https://user-images.githubusercontent.com/61686244/106457205-f8cc1980-64d1-11eb-8645-2327f04d305d.png)

### Train
|Dataset|Scale|
|Div2K|x2|

