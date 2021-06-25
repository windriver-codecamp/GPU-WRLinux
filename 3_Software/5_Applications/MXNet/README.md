# Image Superresolution
## Introdution
This example trains a **convolutional neural network** with BSDS500 dataset to enhance the resolution of images (also known as **superresolution**)

* [Demo Source Codes](https://github.com/apache/incubator-mxnet/tree/master/example/gluon/super_resolution)

### MXMet Setup Steps

* [Setup Steps](https://github.com/windriver-codecamp/GPU-WRLinux/tree/main/3_Software/4_Toolkit_SDK/MXNet)

### Demo Setup Steps:

#### 1. Getting Source
```
$ git clone --recursive https://github.com/apache/incubator-mxnet.git mxnet
$ cd mxnet/example/gluon/super_resolution
```
#### 2. Updates (written by Xinlong Hou)
``` python
$ cat 0001-Update-super_resolution.py.patch
From f4305b7944ab61a5b9a18a8bd627578279d9442f Mon Sep 17 00:00:00 2001
From: test <test@test.com>
Date: Sun, 6 Jun 2021 11:35:39 +0000
Subject: [PATCH] Update super_resolution.py

---
example/gluon/super_resolution/super_resolution.py | 2 +-
1 file changed, 1 insertion(+), 1 deletion(-)

diff --git a/example/gluon/super_resolution/super_resolution.py b/example/gluon/super_resolution/super_resolution.py
index 52bfc2241..4a3e8d92a 100644
--- a/example/gluon/super_resolution/super_resolution.py
+++ b/example/gluon/super_resolution/super_resolution.py
@@ -156,7 +156,7 @@ class SuperResolutionNet(gluon.HybridBlock):
		return x

net = SuperResolutionNet(upscale_factor)
-metric = mx.gluon.metric.MSE()
+metric = mx.metric.MSE()

def test(ctx):
	val_data.reset()
--
2.31.1
```
#### 3. Apply the patch
```
$ git am 0001-Update-super_resolution.py.patch
```
#### Train and generate new image

##### Train Model
```
$ time python super_resolution.py --epochs 200 --use-gpu
Namespace(upscale_factor=3, batch_size=4, test_batch_size=100, epochs=200, lr=0.001, use_gpu=True, seed=123, resolve_img=None)
Directory /mnt/sdb/xhou/HOME/.mxnet/datasets/BSDS500 already exists, skipping.
To force download and extraction, delete the directory and re-run.
[08:32:10] ../src/base.cc:80: cuDNN lib mismatch: linked-against version 8200 != compiled-against version 8100.  Set MXNET_CUDNN_LIB_CHECKING=0 to quiet this warning.
[08:32:12] ../src/operator/nn/./cudnn/./cudnn_algoreg-inl.h:97: Running performance tests to find the best convolution algorithm, this can take a while... (set the environment variable MXNET_CUDNN_AUTOTUNE_DEFAULT to 0 to disable)
training mse at epoch 0: mse=0.020209
validation avg psnr: 20.432425
......
training mse at epoch 199: mse=0.004085
validation avg psnr: 23.290054

real    6m36.315s
user    15m1.850s
sys 0m16.327s
```

##### Generate New Image
```
$ python super_resolution.py --resolve_img test.jpeg
```
#### Result
##### Original picture

> <img src="./MXNet-test-resolved.png" width="290">

##### New generated resolution increased image

> <img src="./MXNet-test-resolved.png" width="870">
