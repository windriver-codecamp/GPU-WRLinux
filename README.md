# GPU-WRLinux
Exploring NVIDIA GPU-Accelerated Ecosystem on Wind River Linux

## Overview
<img src="./1_Overview/Overview_1.JPG" width="600">

## Hardware
<img src="./2_Hardware/Hardware_1.JPG" width="500"><img src="./2_Hardware/Hardware_2.JPG" width="200">

## Software
	Illustration 1:
### Wind River Linux
	Illustration 1:
### Architecture Overview:
	Illustration 1:
### Kernel and Device Drivers
		Overview Picture:
		Setup Steps:
		Issues:
		Solution:
		References:
### X Windows Desktop (XFCE)
		Setup Steps:
		Issues:
		Solution:
		References:
### Toolkit and SDK (CUDA, CUDA-X, Game Engines, etc.)
#### CUDA
			Setup Steps:
			Issues:
			Solution:
			References:
#### CUDA-X
			Setup Steps:
			Issues:
			Solution:
			References:
#### Unreal Engine
			Setup Steps:
			Issues:
			Solution:
			References:
#### Unity
	Setup Steps:
	1. register an account on unity
	https://id.unity.com/en/conversations/aec46371-1052-4108-afdf-c7f8312edfb2018f?view=register

	2. Download Unity Editor

	http://beta.unity3d.com/download/fe82a0e88406/LinuxEditorInstaller/Unity.tar.xz
	tar xf Unity.tar.xz

	3. Download Unity Hub
	https://public-cdn.cloud.unity3d.com/hub/prod/UnityHub.AppImage?_gl=1*8s7rkd*_ga*OTMwMjEzMTk4LjE2MjIwODY0ODc.*_ga_1S78EFL1W5*MTYyMjUzODA2MC42LjEuMTYyMjUzODM5NS4w&_ga=2.51340841.1006021791.1622517514-930213198.1622086487

	4. Run Unity Hub and login
	./UnityHub.AppImage

	5. Active new license
	License Management --> Active new license

	6. Install Unity Editor
	Installs --> Locate, select Unity Editor (tar the Unity.tar.xz)

	7. Run projects
	Projects --> New --> 3D --> create  

	Issues: Failed to login with company website.
	Solution: Use WIFI from telphone.
	References: https://blog.csdn.net/qq_30448401/article/details/104576125

#### Video Codec SDK (TODO)
			Setup Steps:
			Issues:
			Solution:
			References:
#### TensorFlow
			Setup Steps:
			Issues:
			Solution:
			References:
#### PyTorch
			Setup Steps:
			Issues:
			Solution:
			References:
#### Transfer Learning Toolkit (TODO)
			Setup Steps:
			Issues:
			Solution:
			References:
### Applications
#### CUDA examples
			Demo Video 1:
			Demo Source Codes:
			Setup Steps:
			Issues:
			Solution:
			References:
#### CUDA-X Example (NeMo)
			Demo Video:
			Demo Source Codes:
			Setup Steps:
			Issues:
			Solution:
			References:
#### Unreal Demo (Metahuman)
			Demo Video:
			Demo Source Codes:
			Setup Steps:
			Issues:
			Solution:
			References:
#### Unity App (TODO)
			Demo Video:
			Demo Source Codes:
			Setup Steps:
			Issues:
			Solution:
			References:
#### Tensorflow (TODO)
			Demo Video:
			Demo Source Codes:
			Setup Steps:
			Issues:
			Solution:
			References:
#### PyTorch
	Demo Video:
		None

	Demo Source Codes:
		https://github.com/pytorch/examples/tree/master/word_language_model

	Setup Steps:
		1. Installing Anaconda3
			$ mkdir /mnt/sdb/xhou/HOME
			$ export HOME=/mnt/sdb/xhou/HOME
			$ wget --no-check-certificate https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
			$ bash Anaconda3-2021.05-Linux-x86_64.sh
			$ source ~/.bashrc
		2. Building&Installting PyTorch
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
		3. Example Code
			(pytorch-build) $ git clone https://github.com/pytorch/examples.git
			(pytorch-build) $ cd examples/word_language_model
			(pytorch-build) $ python main.py --cuda --emsize 650 --nhid 650 --dropout 0.5 --epochs 40 --tied # 40 epoches, 141 minutes
			(pytorch-build) $ python generate.py --cuda --words 100
			| Generated 0/100 words
			(pytorch-build) $ cat generated.txt
			to the present of stabilized fountains , because they did not do so by the time they did contribute to
			the personal structure . Additionally , the rate of the entire event was often survives at projects of homes .
			<eos> The work records different as of 2009 . The front music guides erected all the style of several "
			<unk> " and " <unk> " <unk> ( proper water ) . In 2007 , Pflueger created the " More
			coded balanced " at this point and recorded a primary event played in a US 2 , which was the

	Issues:
		None

	Solution:
		None

	References:
		None
## Q/A
#### How to verify the GPU works well on Wind River Linux?
#### How about GPU performance comparisons between Wind River Linux and Ubuntu?
