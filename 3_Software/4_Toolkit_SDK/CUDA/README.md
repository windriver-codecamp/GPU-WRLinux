# How to install CUDA and verify?

## Setup steps (CUDA Toolkit Installation)
### Download CUDA Toolkit
```
Go to https://developer.nvidia.com/cuda-11.2.2-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=2004&target_type=runfilelocal

CUDA Toolkit (CUDA Toolkit 11.2 Update 2 Downloads)

wget https://developer.download.nvidia.com/compute/cuda/11.2.2/local_installers/cuda_11.2.2_460.32.03_linux.run
```
### Install CUDA
```
root@intel-x86-64:/# sh ./cuda_11.2.2_460.32.03_linux.run 
===========
= Summary =
===========

Driver:   Not Selected
Toolkit:  Installed in /usr/local/cuda-11.2/
Samples:  Installed in /root/, but missing recommended libraries

Please make sure that
 -   PATH includes /usr/local/cuda-11.2/bin
 -   LD_LIBRARY_PATH includes /usr/local/cuda-11.2/lib64, or, add /usr/local/cuda-11.2/lib64 to /etc/ld.so.conf and run ldconfig as root

To uninstall the CUDA Toolkit, run cuda-uninstaller in /usr/local/cuda-11.2/bin
***WARNING: Incomplete installation! This installation did not install the CUDA Driver. A driver of version at least 460.00 is required for CUDA 11.2 functionality to work.
To install the driver using this installer, run the following command, replacing <CudaInstaller> with the name of this run file:
    sudo <CudaInstaller>.run --silent --driver

Logfile is /var/log/cuda-installer.log
root@intel-x86-64:/#
```

### Set up CUDA environment
```
root@intel-x86-64:/# vi /var/log/cuda-installer.log 
root@intel-x86-64:/# vi ~/.bashrc
root@intel-x86-64:/# source ~/.bashrc
root@intel-x86-64:/# cat ~/.bashrc
export PATH=$PATH:/usr/local/cuda-11.2/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-11.2/lib64
export CUDA_HOME=$CUDA_HOME:/usr/local/cuda
```
                         
### Build CUDA examples 

```
root@intel-x86-64:/# which nvcc
root@intel-x86-64:/# nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2021 NVIDIA Corporation
Built on Sun_Feb_14_21:12:58_PST_2021
Cuda compilation tools, release 11.2, V11.2.152
Build cuda_11.2.r11.2/compiler.29618528_0
root@intel-x86-64:/# 
root@intel-x86-64:/# cd /usr/local/cuda-11.2/samples/
root@intel-x86-64:/usr/local/cuda-11.2/samples# ls
0_Simple  1_Utilities  2_Graphics  3_Imaging  4_Finance  5_Simulations	6_Advanced  7_CUDALibraries  EULA.txt  Makefile  common
root@intel-x86-64:/usr/local/cuda-11.2/samples# make
make[1]: Entering directory '/usr/local/cuda-11.2/samples/0_Simple/simpleLayeredTexture'
/usr/local/cuda/bin/nvcc -ccbin g++ -I../../common/inc -m64 --threads 0 -gencode arch=compute_35,code=sm_35 -gencode arch=compute_37,code=sm_37 -gencode arch=compute_50,code=sm_50 -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -gencode arch=compute_86,code=sm_86 -gencode arch=compute_86,code=compute_86 -o simpleLayeredTexture.o -c simpleLayeredTexture.cu
nvcc warning : The 'compute_35', 'compute_37', 'compute_50', 'sm_35', 'sm_37' and 'sm_50' architectures are deprecated, and may be removed in a future release (Use -Wno-deprecated-gpu-targets to suppress warning).
/usr/local/cuda/bin/nvcc -ccbin g++ -m64 -gencode arch=compute_35,code=sm_35 -gencode arch=compute_37,code=sm_37 -gencode arch=compute_50,code=sm_50 -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -gencode arch=compute_86,code=sm_86 -gencode arch=compute_86,code=compute_86 -o simpleLayeredTexture simpleLayeredTexture.o 
nvcc warning : The 'compute_35', 'compute_37', 'compute_50', 'sm_35', 'sm_37' and 'sm_50' architectures are deprecated, and may be removed in a future release (Use -Wno-deprecated-gpu-targets to suppress warning).
mkdir -p ../../bin/x86_64/linux/release
cp simpleLayeredTexture ../../bin/x86_64/linux/release
make[1]: Leaving directory '/usr/local/cuda-11.2/samples/0_Simple/simpleLayeredTexture'
make[1]: Entering directory '/usr/local/cuda-11.2/samples/0_Simple/streamOrderedAllocation'
/usr/local/cuda/bin/nvcc -ccbin g++ -I../../common/inc -m64 --threads 0 -gencode arch=compute_35,code=sm_35 -gencode arch=compute_37,code=sm_37 -gencode arch=compute_50,code=sm_50 -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -gencode arch=compute_86,code=sm_86 -gencode arch=compute_86,code=compute_86 -o streamOrderedAllocation.o -c streamOrderedAllocation.cu
nvcc warning : The 'compute_35', 'compute_37', 'compute_50', 'sm_35', 'sm_37' and 'sm_50' architectures are deprecated, and may be removed in a future release (Use -Wno-deprecated-gpu-targets to suppress warning).
/usr/local/cuda/bin/nvcc -ccbin g++ -m64 -gencode arch=compute_35,code=sm_35 -gencode arch=compute_37,code=sm_37 -gencode arch=compute_50,code=sm_50 -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -gencode arch=compute_86,code=sm_86 -gencode arch=compute_86,code=compute_86 -o streamOrderedAllocation streamOrderedAllocation.o 
nvcc warning : The 'compute_35', 'compute_37', 'compute_50', 'sm_35', 'sm_37' and 'sm_50' architectures are deprecated, and may be removed in a future release (Use -Wno-deprecated-gpu-targets to suppress warning).
mkdir -p ../../bin/x86_64/linux/release
cp streamOrderedAllocation ../../bin/x86_64/linux/release
make[1]: Leaving directory '/usr/local/cuda-11.2/samples/0_Simple/streamOrderedAllocation'
make[1]: Entering directory '/usr/local/cuda-11.2/samples/0_Simple/vectorAdd'
/usr/local/cuda/bin/nvcc -ccbin g++ -I../../common/inc -m64 --threads 0 -gencode arch=compute_35,code=sm_35 -gencode arch=compute_37,code=sm_37 -gencode arch=compute_50,code=sm_50 -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -gencode arch=compute_86,code=sm_86 -gencode arch=compute_86,code=compute_86 -o vectorAdd.o -c vectorAdd.cu
nvcc warning : The 'compute_35', 'compute_37', 'compute_50', 'sm_35', 'sm_37' and 'sm_50' architectures are deprecated, and may be removed in a future release (Use -Wno-deprecated-gpu-targets to suppress warning).
/usr/local/cuda/bin/nvcc -ccbin g++ -m64 -gencode arch=compute_35,code=sm_35 -gencode arch=compute_37,code=sm_37 -gencode arch=compute_50,code=sm_50 -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -gencode arch=compute_86,code=sm_86 -gencode arch=compute_86,code=compute_86 -o vectorAdd vectorAdd.o 
nvcc warning : The 'compute_35', 'compute_37', 'compute_50', 'sm_35', 'sm_37' and 'sm_50' architectures are deprecated, and may be removed in a future release (Use -Wno-deprecated-gpu-targets to suppress warning).
mkdir -p ../../bin/x86_64/linux/release
cp vectorAdd ../../bin/x86_64/linux/release
make[1]: Leaving directory '/usr/local/cuda-11.2/samples/0_Simple/vectorAdd'
…
```

### Running CUDA examples

```
root@intel-x86-64:/usr/local/cuda-11.2/samples/1_Utilities/deviceQuery# ./deviceQuery 
./deviceQuery Starting...

 CUDA Device Query (Runtime API) version (CUDART static linking)

Detected 1 CUDA Capable device(s)

Device 0: "GeForce GTX 1650 SUPER"
  CUDA Driver Version / Runtime Version          11.2 / 11.2
  CUDA Capability Major/Minor version number:    7.5
  Total amount of global memory:                 3878 MBytes (4066574336 bytes)
  (20) Multiprocessors, ( 64) CUDA Cores/MP:     1280 CUDA Cores
  GPU Max Clock rate:                            1755 MHz (1.75 GHz)
  Memory Clock rate:                             6001 Mhz
  Memory Bus Width:                              128-bit
  L2 Cache Size:                                 1048576 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        65536 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  1024
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 3 copy engine(s)
  Run time limit on kernels:                     Yes
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Disabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 1 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 11.2, CUDA Runtime Version = 11.2, NumDevs = 1
Result = PASS
root@intel-x86-64:/usr/local/cuda-11.2/samples/1_Utilities/deviceQuery# cd ..
root@intel-x86-64:/usr/local/cuda-11.2/samples/1_Utilities# ls
UnifiedMemoryPerf  bandwidthTest  deviceQuery  deviceQueryDrv  p2pBandwidthLatencyTest	topologyQuery
root@intel-x86-64:/usr/local/cuda-11.2/samples/1_Utilities# cd ..
root@intel-x86-64:/usr/local/cuda-11.2/samples# ls
0_Simple  1_Utilities  2_Graphics  3_Imaging  4_Finance  5_Simulations	6_Advanced  7_CUDALibraries  EULA.txt  Makefile  bin  common
```
```
root@intel-x86-64:/usr/local/cuda-11.2/samples# cd 0_Simple/
root@intel-x86-64:/usr/local/cuda-11.2/samples/0_Simple# ls
UnifiedMemoryStreams  cppIntegration	      immaTensorCoreGemm  simpleAWBarrier		simpleCubemapTexture  simpleOccupancy		 simpleTemplates_nvrtc	     systemWideAtomics
asyncAPI	      cppOverload	      inlinePTX		  simpleAssert			simpleCudaGraphs      simpleP2P			 simpleTexture		     template
bf16TensorCoreGemm    cudaNvSci		      inlinePTX_nvrtc	  simpleAssert_nvrtc		simpleDrvRuntime      simplePitchLinearTexture	 simpleTextureDrv	     tf32TensorCoreGemm
binaryPartitionCG     cudaOpenMP	      matrixMul		  simpleAtomicIntrinsics	simpleIPC	      simplePrintf		 simpleVoteIntrinsics	     vectorAdd
cdpSimplePrint	      cudaTensorCoreGemm      matrixMulCUBLAS	  simpleAtomicIntrinsics_nvrtc	simpleLayeredTexture  simpleSeparateCompilation  simpleVoteIntrinsics_nvrtc  vectorAddDrv
cdpSimpleQuicksort    dmmaTensorCoreGemm      matrixMulDrv	  simpleAttributes		simpleMPI	      simpleStreams		 simpleZeroCopy		     vectorAddMMAP
clock		      fp16ScalarProduct       matrixMul_nvrtc	  simpleCallback		simpleMultiCopy       simpleSurfaceWrite	 streamOrderedAllocation     vectorAdd_nvrtc
clock_nvrtc	      globalToShmemAsyncCopy  memMapIPCDrv	  simpleCooperativeGroups	simpleMultiGPU	      simpleTemplates		 streamOrderedAllocationP2P
root@intel-x86-64:/usr/local/cuda-11.2/samples/0_Simple# cd asyncAPI/
root@intel-x86-64:/usr/local/cuda-11.2/samples/0_Simple/asyncAPI# ls
Makefile  NsightEclipse.xml  asyncAPI  asyncAPI.cu  asyncAPI.o	readme.txt
```
```
root@intel-x86-64:/usr/local/cuda-11.2/samples/0_Simple/asyncAPI# ./asyncAPI 
[./asyncAPI] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER]
time spent executing by the GPU: 11.47
time spent by CPU in CUDA calls: 0.03
CPU executed 92476 iterations while waiting for GPU to finish

```
```
root@intel-x86-64:/usr/local/cuda-11.2/samples/0_Simple/asyncAPI# cd ..
root@intel-x86-64:/usr/local/cuda-11.2/samples/0_Simple# ls
UnifiedMemoryStreams  cppIntegration	      immaTensorCoreGemm  simpleAWBarrier		simpleCubemapTexture  simpleOccupancy		 simpleTemplates_nvrtc	     systemWideAtomics
asyncAPI	      cppOverload	      inlinePTX		  simpleAssert			simpleCudaGraphs      simpleP2P			 simpleTexture		     template
bf16TensorCoreGemm    cudaNvSci		      inlinePTX_nvrtc	  simpleAssert_nvrtc		simpleDrvRuntime      simplePitchLinearTexture	 simpleTextureDrv	     tf32TensorCoreGemm
binaryPartitionCG     cudaOpenMP	      matrixMul		  simpleAtomicIntrinsics	simpleIPC	      simplePrintf		 simpleVoteIntrinsics	     vectorAdd
cdpSimplePrint	      cudaTensorCoreGemm      matrixMulCUBLAS	  simpleAtomicIntrinsics_nvrtc	simpleLayeredTexture  simpleSeparateCompilation  simpleVoteIntrinsics_nvrtc  vectorAddDrv
cdpSimpleQuicksort    dmmaTensorCoreGemm      matrixMulDrv	  simpleAttributes		simpleMPI	      simpleStreams		 simpleZeroCopy		     vectorAddMMAP
clock		      fp16ScalarProduct       matrixMul_nvrtc	  simpleCallback		simpleMultiCopy       simpleSurfaceWrite	 streamOrderedAllocation     vectorAdd_nvrtc
clock_nvrtc	      globalToShmemAsyncCopy  memMapIPCDrv	  simpleCooperativeGroups	simpleMultiGPU	      simpleTemplates		 streamOrderedAllocationP2P
root@intel-x86-64:/usr/local/cuda-11.2/samples/0_Simple# cd matrixMulCUBLAS/
root@intel-x86-64:/usr/local/cuda-11.2/samples/0_Simple/matrixMulCUBLAS# ls
Makefile  NsightEclipse.xml  matrixMulCUBLAS  matrixMulCUBLAS.cpp  matrixMulCUBLAS.o  readme.txt
```
```
root@intel-x86-64:/usr/local/cuda-11.2/samples/0_Simple/matrixMulCUBLAS# ./matrixMulCUBLAS 
[Matrix Multiply CUBLAS] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

GPU Device 0: "GeForce GTX 1650 SUPER" with compute capability 7.5

MatrixA(640,480), MatrixB(480,320), MatrixC(640,320)
Computing result using CUBLAS...done.
Performance= 1932.89 GFlop/s, Time= 0.102 msec, Size= 196608000 Ops
Computing result using host CPU...done.
Comparing CUBLAS Matrix Multiply with CPU results: PASS

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
root@intel-x86-64:/usr/local/cuda-11.2/samples/0_Simple/matrixMulCUBLAS# cd ..
root@intel-x86-64:/usr/local/cuda-11.2/samples/0_Simple# ls
UnifiedMemoryStreams  cppIntegration	      immaTensorCoreGemm  simpleAWBarrier		simpleCubemapTexture  simpleOccupancy		 simpleTemplates_nvrtc	     systemWideAtomics
asyncAPI	      cppOverload	      inlinePTX		  simpleAssert			simpleCudaGraphs      simpleP2P			 simpleTexture		     template
bf16TensorCoreGemm    cudaNvSci		      inlinePTX_nvrtc	  simpleAssert_nvrtc		simpleDrvRuntime      simplePitchLinearTexture	 simpleTextureDrv	     tf32TensorCoreGemm
binaryPartitionCG     cudaOpenMP	      matrixMul		  simpleAtomicIntrinsics	simpleIPC	      simplePrintf		 simpleVoteIntrinsics	     vectorAdd
cdpSimplePrint	      cudaTensorCoreGemm      matrixMulCUBLAS	  simpleAtomicIntrinsics_nvrtc	simpleLayeredTexture  simpleSeparateCompilation  simpleVoteIntrinsics_nvrtc  vectorAddDrv
cdpSimpleQuicksort    dmmaTensorCoreGemm      matrixMulDrv	  simpleAttributes		simpleMPI	      simpleStreams		 simpleZeroCopy		     vectorAddMMAP
clock		      fp16ScalarProduct       matrixMul_nvrtc	  simpleCallback		simpleMultiCopy       simpleSurfaceWrite	 streamOrderedAllocation     vectorAdd_nvrtc
clock_nvrtc	      globalToShmemAsyncCopy  memMapIPCDrv	  simpleCooperativeGroups	simpleMultiGPU	      simpleTemplates		 streamOrderedAllocationP2P
root@intel-x86-64:/usr/local/cuda-11.2/samples/0_Simple# cd ..
root@intel-x86-64:/usr/local/cuda-11.2/samples# ls
0_Simple  1_Utilities  2_Graphics  3_Imaging  4_Finance  5_Simulations	6_Advanced  7_CUDALibraries  EULA.txt  Makefile  bin  common
root@intel-x86-64:/usr/local/cuda-11.2/samples# cd 7_CUDALibraries/
root@intel-x86-64:/usr/local/cuda-11.2/samples/7_CUDALibraries# ls
FilterBorderControlNPP	MC_SingleAsianOptionP			   boxFilterNPP			conjugateGradientPrecond  cuSolverSp_LinearSolver      nvJPEG	       simpleCUFFT
MC_EstimatePiInlineP	MersenneTwisterGP11213			   cannyEdgeDetectorNPP		conjugateGradientUM	  cuSolverSp_LowlevelCholesky  nvJPEG_encoder  simpleCUFFT_2d_MGPU
MC_EstimatePiInlineQ	batchCUBLAS				   common			cuHook			  cuSolverSp_LowlevelQR        randomFog       simpleCUFFT_MGPU
MC_EstimatePiP		batchedLabelMarkersAndLabelCompressionNPP  conjugateGradient		cuSolverDn_LinearSolver   freeImageInteropNPP	       simpleCUBLAS    simpleCUFFT_callback
MC_EstimatePiQ		boundSegmentsNPP			   conjugateGradientCudaGraphs	cuSolverRf		  histEqualizationNPP	       simpleCUBLASXT  watershedSegmentationNPP
root@intel-x86-64:/usr/local/cuda-11.2/samples/7_CUDALibraries# cd batchCUBLAS/
root@intel-x86-64:/usr/local/cuda-11.2/samples/7_CUDALibraries/batchCUBLAS# ls
Makefile  NsightEclipse.xml  batchCUBLAS  batchCUBLAS.cpp  batchCUBLAS.h  batchCUBLAS.o  readme.txt
```
```
root@intel-x86-64:/usr/local/cuda-11.2/samples/7_CUDALibraries/batchCUBLAS# ./batchCUBLAS 
batchCUBLAS Starting...

GPU Device 0: "Turing" with compute capability 7.5


 ==== Running single kernels ==== 

Testing sgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0xbf800000, -1) beta= (0x40000000, 2)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00031304 sec  GFLOPS=13.3985
@@@@ sgemm test OK
Testing dgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0x0000000000000000, 0) beta= (0x0000000000000000, 0)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00003123 sec  GFLOPS=134.291
@@@@ dgemm test OK

 ==== Running N=10 without streams ==== 

Testing sgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0xbf800000, -1) beta= (0x00000000, 0)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00011182 sec  GFLOPS=375.1
@@@@ sgemm test OK
Testing dgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0xbff0000000000000, -1) beta= (0x0000000000000000, 0)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00058913 sec  GFLOPS=71.1946
@@@@ dgemm test OK

 ==== Running N=10 with streams ==== 

Testing sgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0x40000000, 2) beta= (0x40000000, 2)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00011420 sec  GFLOPS=367.269
@@@@ sgemm test OK
Testing dgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0xbff0000000000000, -1) beta= (0x0000000000000000, 0)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00041294 sec  GFLOPS=101.572
@@@@ dgemm test OK

 ==== Running N=10 batched ==== 

Testing sgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0x3f800000, 1) beta= (0xbf800000, -1)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00006294 sec  GFLOPS=666.371
@@@@ sgemm test OK
Testing dgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0xbff0000000000000, -1) beta= (0x4000000000000000, 2)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00038695 sec  GFLOPS=108.393
@@@@ dgemm test OK

Test Summary
0 error(s)
```

## FAQ
* How to uninstall/reinstall CUDA?
```
Uninstall cuda
root@wind-OptiPlex-9020:/usr/local/cuda-11.2/bin# ./cuda-uninstaller
```
```
Reinstall cuda
# sh cuda_11.2.2_460.32.03_linux.run 
```

### References

* https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#recommended-post
