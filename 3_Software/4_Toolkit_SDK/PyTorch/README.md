## PyTorch Installation

### Setup Steps:
1. Installing Anaconda3
```
$ mkdir /mnt/sdb/xhou/HOME
$ export HOME=/mnt/sdb/xhou/HOME
$ wget --no-check-certificate https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
$ bash Anaconda3-2021.05-Linux-x86_64.sh
$ source ~/.bashrc
```
2. Building&Installting PyTorch
```
$ conda create --name pytorch-build
$ conda activate pytorch-build
(pytorch-build) $ conda install astunparse numpy ninja pyyaml mkl mkl-include setuptools cmake cffi typing_extensions future six requests dataclasses
(pytorch-build) $ conda install -c pytorch magma-cuda112
(pytorch-build) $ git clone --recursive https://github.com/pytorch/pytorch
(pytorch-build) $ cd pytorch
(pytorch-build) $ git submodule sync
(pytorch-build) $ git submodule update --init --recursive
(pytorch-build) $ cat ~/cuda.env
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64
export PATH=$PATH:/usr/local/cuda/bin
export CUDA_HOME="/usr/local/cuda"
export CUDA_NVCC_EXECUTABLE="/usr/local/cuda/bin/nvcc"
export CUDNN_INCLUDE_PATH="/usr/local/cuda/include/"
export CUDNN_LIBRARY_PATH="/usr/local/cuda/lib64/"
(pytorch-build) $ cat ~/pytorch_build.env
export LIBRARY_PATH="/usr/local/cuda/lib64"
export CMAKE_PREFIX_PATH=${CONDA_PREFIX:-"$(dirname $(which conda))/../"}
(pytorch-build) $ source ~/cuda.env
(pytorch-build) $ source ~/pytorch_build.env
## with CUDNN
(pytorch-build) $ export USE_CUDA=1 USE_CUDNN=1 USE_MKLDNN=1
## building branch master
(pytorch-build) $ python setup.py install # about 1.5hrs
(pytorch-build) $ python
Python 3.9.5 (default, May 18 2021, 19:34:48)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.cuda.current_device()
0
>>> torch.cuda.get_device_name(0)
'GeForce GTX 1650 SUPER'
>>>
>>> from torch.backends import cudnn
>>> cudnn.is_available()
True
>>>
```
### Issues:
		None

#### Solution:
		None

## References:
		None
