## MXNet Installation

### Setup Steps
1. CUDA&cuDNN
```
They are CUDA 11.2 and cuDNN 8.2, skips installing&setups here
```
2. Anaconda
```
Skips installing, only setups
$ conda create --name mxnet-binary
$ conda activate mxnet-binary
```
3. NCCL
```
$ wget https://developer.nvidia.com/compute/machine-learning/nccl/secure/2.8.3/agnostic/x64/nccl_2.8.3-1+cuda11.2_x86_64.txz
$ xz -d nccl_2.8.3-1+cuda11.2_x86_64.txz
$ tar xf nccl_2.8.3-1+cuda11.2_x86_64.txz
# deploy to directory of CUDA
$ cp nccl_2.8.3-1+cuda11.2_x86_64/include/nccl* /usr/local/cuda/include/
$ cp -P nccl_2.8.3-1+cuda11.2_x86_64/lib/libnccl* /usr/local/cuda/lib64/
$ chmod a+r /usr/local/cuda/include/nccl* /usr/local/cuda/lib64/libnccl*
```
4. Installing MXNet with Binary
```
			# version with CUDA 11.2
			$ pip install mxnet-cu112
			# try with
			$ python
			>>> import mxnet as mx
			>>> a = mx.nd.ones((2, 3), mx.gpu())
			>>> b = a * 2 + 1
			>>> b.asnumpy()
			array([[ 3.,  3.,  3.],
				[ 3.,  3.,  3.]], dtype=float32)
```
## Issues
		None
### Solution
		None
## References
		None
