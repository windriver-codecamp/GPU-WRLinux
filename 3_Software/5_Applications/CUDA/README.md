## Demo Video:
> None

## Run CUDA Examples Steps
### 1. Get CUDA installed information
```
root@intel-x86-64:~# nvidia-smi 
Fri Jun 18 01:59:14 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.73.01    Driver Version: 460.73.01    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce GTX 165...  Off  | 00000000:01:00.0  On |                  N/A |
| 29%   31C    P8     5W / 100W |    337MiB /  3878MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A       452      G   /usr/bin/X                        332MiB |
|    0   N/A  N/A       624      G   xfwm4                               2MiB |
+-----------------------------------------------------------------------------+
root@intel-x86-64:~#
```

### 1. Find all execuable cuda sample binaries
```
root@intel-x86-64:~# cd /usr/local/cuda-11.2/samples
root@intel-x86-64:/usr/local/cuda-11.2/samples# find . -executable -type f | sort > /tmp/e
root@intel-x86-64:/usr/local/cuda-11.2/samples# cat /tmp/e
./0_Simple/UnifiedMemoryStreams/UnifiedMemoryStreams
./0_Simple/asyncAPI/asyncAPI
./0_Simple/bf16TensorCoreGemm/bf16TensorCoreGemm
./0_Simple/binaryPartitionCG/binaryPartitionCG
./0_Simple/cdpSimplePrint/cdpSimplePrint
./0_Simple/cdpSimpleQuicksort/cdpSimpleQuicksort
./0_Simple/clock/clock
./0_Simple/clock_nvrtc/clock_nvrtc
./0_Simple/cppIntegration/cppIntegration
./0_Simple/cppOverload/cppOverload
./0_Simple/cudaOpenMP/cudaOpenMP
./0_Simple/cudaTensorCoreGemm/cudaTensorCoreGemm
./0_Simple/dmmaTensorCoreGemm/dmmaTensorCoreGemm
./0_Simple/fp16ScalarProduct/fp16ScalarProduct
./0_Simple/globalToShmemAsyncCopy/globalToShmemAsyncCopy
./0_Simple/immaTensorCoreGemm/immaTensorCoreGemm
./0_Simple/inlinePTX/inlinePTX
./0_Simple/inlinePTX_nvrtc/inlinePTX_nvrtc
./0_Simple/matrixMul/matrixMul
./0_Simple/matrixMulCUBLAS/matrixMulCUBLAS
./0_Simple/matrixMulDrv/matrixMulDrv
./0_Simple/matrixMul_nvrtc/matrixMul_nvrtc
./0_Simple/memMapIPCDrv/memMapIPCDrv
./0_Simple/simpleAWBarrier/simpleAWBarrier
./0_Simple/simpleAssert/simpleAssert
./0_Simple/simpleAssert_nvrtc/simpleAssert_nvrtc
./0_Simple/simpleAtomicIntrinsics/simpleAtomicIntrinsics
./0_Simple/simpleAtomicIntrinsics_nvrtc/simpleAtomicIntrinsics_nvrtc
./0_Simple/simpleAttributes/simpleAttributes
./0_Simple/simpleCallback/simpleCallback
./0_Simple/simpleCooperativeGroups/simpleCooperativeGroups
./0_Simple/simpleCubemapTexture/simpleCubemapTexture
./0_Simple/simpleCudaGraphs/simpleCudaGraphs
./0_Simple/simpleDrvRuntime/simpleDrvRuntime
./0_Simple/simpleIPC/simpleIPC
./0_Simple/simpleLayeredTexture/simpleLayeredTexture
./0_Simple/simpleMultiCopy/simpleMultiCopy
./0_Simple/simpleMultiGPU/simpleMultiGPU
./0_Simple/simpleOccupancy/simpleOccupancy
./0_Simple/simpleP2P/simpleP2P
./0_Simple/simplePitchLinearTexture/simplePitchLinearTexture
./0_Simple/simplePrintf/simplePrintf
./0_Simple/simpleSeparateCompilation/simpleSeparateCompilation
./0_Simple/simpleStreams/simpleStreams
./0_Simple/simpleSurfaceWrite/simpleSurfaceWrite
./0_Simple/simpleTemplates/simpleTemplates
./0_Simple/simpleTemplates_nvrtc/simpleTemplates_nvrtc
./0_Simple/simpleTexture/simpleTexture
./0_Simple/simpleTextureDrv/simpleTextureDrv
./0_Simple/simpleVoteIntrinsics/simpleVoteIntrinsics
./0_Simple/simpleVoteIntrinsics_nvrtc/simpleVoteIntrinsics_nvrtc
./0_Simple/simpleZeroCopy/simpleZeroCopy
./0_Simple/streamOrderedAllocation/streamOrderedAllocation
./0_Simple/streamOrderedAllocationP2P/streamOrderedAllocationP2P
./0_Simple/systemWideAtomics/systemWideAtomics
./0_Simple/template/template
./0_Simple/tf32TensorCoreGemm/tf32TensorCoreGemm
./0_Simple/vectorAdd/vectorAdd
./0_Simple/vectorAddDrv/vectorAddDrv
./0_Simple/vectorAddMMAP/vectorAddMMAP
./0_Simple/vectorAdd_nvrtc/vectorAdd_nvrtc
./1_Utilities/UnifiedMemoryPerf/UnifiedMemoryPerf
./1_Utilities/bandwidthTest/bandwidthTest
./1_Utilities/deviceQuery/deviceQuery
./1_Utilities/deviceQueryDrv/deviceQueryDrv
./1_Utilities/p2pBandwidthLatencyTest/p2pBandwidthLatencyTest
./1_Utilities/topologyQuery/topologyQuery
./3_Imaging/HSOpticalFlow/HSOpticalFlow
./3_Imaging/NV12toBGRandResize/NV12toBGRandResize
./3_Imaging/convolutionFFT2D/convolutionFFT2D
./3_Imaging/convolutionSeparable/convolutionSeparable
./3_Imaging/convolutionTexture/convolutionTexture
./3_Imaging/dct8x8/dct8x8
./3_Imaging/dwtHaar1D/dwtHaar1D
./3_Imaging/dxtc/dxtc
./3_Imaging/histogram/histogram
./3_Imaging/stereoDisparity/stereoDisparity
./4_Finance/BlackScholes/BlackScholes
./4_Finance/BlackScholes_nvrtc/BlackScholes_nvrtc
./4_Finance/MonteCarloMultiGPU/MonteCarloMultiGPU
./4_Finance/SobolQRNG/SobolQRNG
./4_Finance/binomialOptions/binomialOptions
./4_Finance/binomialOptions_nvrtc/binomialOptions_nvrtc
./4_Finance/quasirandomGenerator/quasirandomGenerator
./4_Finance/quasirandomGenerator_nvrtc/quasirandomGenerator_nvrtc
./6_Advanced/FDTD3d/FDTD3d
./6_Advanced/StreamPriorities/StreamPriorities
./6_Advanced/alignedTypes/alignedTypes
./6_Advanced/c++11_cuda/c++11_cuda
./6_Advanced/cdpAdvancedQuicksort/cdpAdvancedQuicksort
./6_Advanced/cdpBezierTessellation/cdpBezierTessellation
./6_Advanced/cdpQuadtree/cdpQuadtree
./6_Advanced/concurrentKernels/concurrentKernels
./6_Advanced/conjugateGradientMultiBlockCG/conjugateGradientMultiBlockCG
./6_Advanced/conjugateGradientMultiDeviceCG/conjugateGradientMultiDeviceCG
./6_Advanced/cudaCompressibleMemory/cudaCompressibleMemory
./6_Advanced/eigenvalues/eigenvalues
./6_Advanced/fastWalshTransform/fastWalshTransform
./6_Advanced/interval/interval
./6_Advanced/jacobiCudaGraphs/jacobiCudaGraphs
./6_Advanced/lineOfSight/lineOfSight
./6_Advanced/matrixMulDynlinkJIT/matrixMulDynlinkJIT
./6_Advanced/mergeSort/mergeSort
./6_Advanced/newdelete/newdelete
./6_Advanced/ptxjit/ptxjit
./6_Advanced/radixSortThrust/radixSortThrust
./6_Advanced/reduction/reduction
./6_Advanced/reductionMultiBlockCG/reductionMultiBlockCG
./6_Advanced/scalarProd/scalarProd
./6_Advanced/scan/scan
./6_Advanced/segmentationTreeThrust/segmentationTreeThrust
./6_Advanced/shfl_scan/shfl_scan
./6_Advanced/simpleHyperQ/simpleHyperQ
./6_Advanced/sortingNetworks/sortingNetworks
./6_Advanced/threadFenceReduction/threadFenceReduction
./6_Advanced/threadMigration/threadMigration
./6_Advanced/transpose/transpose
./6_Advanced/warpAggregatedAtomicsCG/warpAggregatedAtomicsCG
./7_CUDALibraries/MC_EstimatePiInlineP/MC_EstimatePiInlineP
./7_CUDALibraries/MC_EstimatePiInlineQ/MC_EstimatePiInlineQ
./7_CUDALibraries/MC_EstimatePiP/MC_EstimatePiP
./7_CUDALibraries/MC_EstimatePiQ/MC_EstimatePiQ
./7_CUDALibraries/MC_SingleAsianOptionP/MC_SingleAsianOptionP
./7_CUDALibraries/MersenneTwisterGP11213/MersenneTwisterGP11213
./7_CUDALibraries/batchCUBLAS/batchCUBLAS
./7_CUDALibraries/batchedLabelMarkersAndLabelCompressionNPP/batchedLabelMarkersAndCompressionNPP
./7_CUDALibraries/conjugateGradient/conjugateGradient
./7_CUDALibraries/conjugateGradientCudaGraphs/conjugateGradientCudaGraphs
./7_CUDALibraries/conjugateGradientPrecond/conjugateGradientPrecond
./7_CUDALibraries/conjugateGradientUM/conjugateGradientUM
./7_CUDALibraries/cuHook/cuHook
./7_CUDALibraries/cuHook/libcuhook.so.1
./7_CUDALibraries/cuSolverDn_LinearSolver/cuSolverDn_LinearSolver
./7_CUDALibraries/cuSolverRf/cuSolverRf
./7_CUDALibraries/cuSolverSp_LinearSolver/cuSolverSp_LinearSolver
./7_CUDALibraries/cuSolverSp_LowlevelCholesky/cuSolverSp_LowlevelCholesky
./7_CUDALibraries/cuSolverSp_LowlevelQR/cuSolverSp_LowlevelQR
./7_CUDALibraries/nvJPEG/nvJPEG
./7_CUDALibraries/nvJPEG_encoder/nvJPEG_encoder
./7_CUDALibraries/simpleCUBLAS/simpleCUBLAS
./7_CUDALibraries/simpleCUBLASXT/simpleCUBLASXT
./7_CUDALibraries/simpleCUFFT/simpleCUFFT
./7_CUDALibraries/simpleCUFFT_2d_MGPU/simpleCUFFT_2d_MGPU
./7_CUDALibraries/simpleCUFFT_MGPU/simpleCUFFT_MGPU
./7_CUDALibraries/simpleCUFFT_callback/simpleCUFFT_callback
./7_CUDALibraries/watershedSegmentationNPP/watershedSegmentationNPP
./bin/x86_64/linux/release/BlackScholes
./bin/x86_64/linux/release/BlackScholes_nvrtc
./bin/x86_64/linux/release/FDTD3d
./bin/x86_64/linux/release/HSOpticalFlow
./bin/x86_64/linux/release/MC_EstimatePiInlineP
./bin/x86_64/linux/release/MC_EstimatePiInlineQ
./bin/x86_64/linux/release/MC_EstimatePiP
./bin/x86_64/linux/release/MC_EstimatePiQ
./bin/x86_64/linux/release/MC_SingleAsianOptionP
./bin/x86_64/linux/release/MersenneTwisterGP11213
./bin/x86_64/linux/release/MonteCarloMultiGPU
./bin/x86_64/linux/release/NV12toBGRandResize
./bin/x86_64/linux/release/SobolQRNG
./bin/x86_64/linux/release/StreamPriorities
./bin/x86_64/linux/release/UnifiedMemoryPerf
./bin/x86_64/linux/release/UnifiedMemoryStreams
./bin/x86_64/linux/release/alignedTypes
./bin/x86_64/linux/release/asyncAPI
./bin/x86_64/linux/release/bandwidthTest
./bin/x86_64/linux/release/batchCUBLAS
./bin/x86_64/linux/release/batchedLabelMarkersAndCompressionNPP
./bin/x86_64/linux/release/bf16TensorCoreGemm
./bin/x86_64/linux/release/binaryPartitionCG
./bin/x86_64/linux/release/binomialOptions
./bin/x86_64/linux/release/binomialOptions_nvrtc
./bin/x86_64/linux/release/c++11_cuda
./bin/x86_64/linux/release/cdpAdvancedQuicksort
./bin/x86_64/linux/release/cdpBezierTessellation
./bin/x86_64/linux/release/cdpQuadtree
./bin/x86_64/linux/release/cdpSimplePrint
./bin/x86_64/linux/release/cdpSimpleQuicksort
./bin/x86_64/linux/release/clock
./bin/x86_64/linux/release/clock_nvrtc
./bin/x86_64/linux/release/concurrentKernels
./bin/x86_64/linux/release/conjugateGradient
./bin/x86_64/linux/release/conjugateGradientCudaGraphs
./bin/x86_64/linux/release/conjugateGradientMultiBlockCG
./bin/x86_64/linux/release/conjugateGradientMultiDeviceCG
./bin/x86_64/linux/release/conjugateGradientPrecond
./bin/x86_64/linux/release/conjugateGradientUM
./bin/x86_64/linux/release/convolutionFFT2D
./bin/x86_64/linux/release/convolutionSeparable
./bin/x86_64/linux/release/convolutionTexture
./bin/x86_64/linux/release/cppIntegration
./bin/x86_64/linux/release/cppOverload
./bin/x86_64/linux/release/cuHook
./bin/x86_64/linux/release/cuSolverDn_LinearSolver
./bin/x86_64/linux/release/cuSolverRf
./bin/x86_64/linux/release/cuSolverSp_LinearSolver
./bin/x86_64/linux/release/cuSolverSp_LowlevelCholesky
./bin/x86_64/linux/release/cuSolverSp_LowlevelQR
./bin/x86_64/linux/release/cudaCompressibleMemory
./bin/x86_64/linux/release/cudaOpenMP
./bin/x86_64/linux/release/cudaTensorCoreGemm
./bin/x86_64/linux/release/dct8x8
./bin/x86_64/linux/release/deviceQuery
./bin/x86_64/linux/release/deviceQueryDrv
./bin/x86_64/linux/release/dmmaTensorCoreGemm
./bin/x86_64/linux/release/dwtHaar1D
./bin/x86_64/linux/release/dxtc
./bin/x86_64/linux/release/eigenvalues
./bin/x86_64/linux/release/fastWalshTransform
./bin/x86_64/linux/release/fp16ScalarProduct
./bin/x86_64/linux/release/globalToShmemAsyncCopy
./bin/x86_64/linux/release/histogram
./bin/x86_64/linux/release/immaTensorCoreGemm
./bin/x86_64/linux/release/inlinePTX
./bin/x86_64/linux/release/inlinePTX_nvrtc
./bin/x86_64/linux/release/interval
./bin/x86_64/linux/release/jacobiCudaGraphs
./bin/x86_64/linux/release/libcuhook.so.1
./bin/x86_64/linux/release/lineOfSight
./bin/x86_64/linux/release/matrixMul
./bin/x86_64/linux/release/matrixMulCUBLAS
./bin/x86_64/linux/release/matrixMulDrv
./bin/x86_64/linux/release/matrixMulDynlinkJIT
./bin/x86_64/linux/release/matrixMul_nvrtc
./bin/x86_64/linux/release/memMapIPCDrv
./bin/x86_64/linux/release/mergeSort
./bin/x86_64/linux/release/newdelete
./bin/x86_64/linux/release/nvJPEG
./bin/x86_64/linux/release/nvJPEG_encoder
./bin/x86_64/linux/release/p2pBandwidthLatencyTest
./bin/x86_64/linux/release/ptxjit
./bin/x86_64/linux/release/quasirandomGenerator
./bin/x86_64/linux/release/quasirandomGenerator_nvrtc
./bin/x86_64/linux/release/radixSortThrust
./bin/x86_64/linux/release/reduction
./bin/x86_64/linux/release/reductionMultiBlockCG
./bin/x86_64/linux/release/scalarProd
./bin/x86_64/linux/release/scan
./bin/x86_64/linux/release/segmentationTreeThrust
./bin/x86_64/linux/release/shfl_scan
./bin/x86_64/linux/release/simpleAWBarrier
./bin/x86_64/linux/release/simpleAssert
./bin/x86_64/linux/release/simpleAssert_nvrtc
./bin/x86_64/linux/release/simpleAtomicIntrinsics
./bin/x86_64/linux/release/simpleAtomicIntrinsics_nvrtc
./bin/x86_64/linux/release/simpleAttributes
./bin/x86_64/linux/release/simpleCUBLAS
./bin/x86_64/linux/release/simpleCUBLASXT
./bin/x86_64/linux/release/simpleCUFFT
./bin/x86_64/linux/release/simpleCUFFT_2d_MGPU
./bin/x86_64/linux/release/simpleCUFFT_MGPU
./bin/x86_64/linux/release/simpleCUFFT_callback
./bin/x86_64/linux/release/simpleCallback
./bin/x86_64/linux/release/simpleCooperativeGroups
./bin/x86_64/linux/release/simpleCubemapTexture
./bin/x86_64/linux/release/simpleCudaGraphs
./bin/x86_64/linux/release/simpleDrvRuntime
./bin/x86_64/linux/release/simpleHyperQ
./bin/x86_64/linux/release/simpleIPC
./bin/x86_64/linux/release/simpleLayeredTexture
./bin/x86_64/linux/release/simpleMultiCopy
./bin/x86_64/linux/release/simpleMultiGPU
./bin/x86_64/linux/release/simpleOccupancy
./bin/x86_64/linux/release/simpleP2P
./bin/x86_64/linux/release/simplePitchLinearTexture
./bin/x86_64/linux/release/simplePrintf
./bin/x86_64/linux/release/simpleSeparateCompilation
./bin/x86_64/linux/release/simpleStreams
./bin/x86_64/linux/release/simpleSurfaceWrite
./bin/x86_64/linux/release/simpleTemplates
./bin/x86_64/linux/release/simpleTemplates_nvrtc
./bin/x86_64/linux/release/simpleTexture
./bin/x86_64/linux/release/simpleTextureDrv
./bin/x86_64/linux/release/simpleVoteIntrinsics
./bin/x86_64/linux/release/simpleVoteIntrinsics_nvrtc
./bin/x86_64/linux/release/simpleZeroCopy
./bin/x86_64/linux/release/sortingNetworks
./bin/x86_64/linux/release/stereoDisparity
./bin/x86_64/linux/release/streamOrderedAllocation
./bin/x86_64/linux/release/streamOrderedAllocationP2P
./bin/x86_64/linux/release/systemWideAtomics
./bin/x86_64/linux/release/template
./bin/x86_64/linux/release/tf32TensorCoreGemm
./bin/x86_64/linux/release/threadFenceReduction
./bin/x86_64/linux/release/threadMigration
./bin/x86_64/linux/release/topologyQuery
./bin/x86_64/linux/release/transpose
./bin/x86_64/linux/release/vectorAdd
./bin/x86_64/linux/release/vectorAddDrv
./bin/x86_64/linux/release/vectorAddMMAP
./bin/x86_64/linux/release/vectorAdd_nvrtc
./bin/x86_64/linux/release/warpAggregatedAtomicsCG
./bin/x86_64/linux/release/watershedSegmentationNPP
```
### 2. CUDA All of CUDA Examples 

The outputs were as below.

```
root@intel-x86-64:/usr/local/cuda-11.2/samples# sh -x /tmp/e
+ ./0_Simple/UnifiedMemoryStreams/UnifiedMemoryStreams
GPU Device 0: "Turing" with compute capability 7.5

Executing tasks on host / device
Task [3], thread [0] executing on device (718)
Task [0], thread [3] executing on device (839)
Task [1], thread [2] executing on device (601)
Task [2], thread [1] executing on device (442)
Task [4], thread [3] executing on device (580)
Task [5], thread [2] executing on device (638)
Task [6], thread [3] executing on device (207)
Task [7], thread [0] executing on device (115)
Task [8], thread [1] executing on device (554)
Task [9], thread [1] executing on device (219)
Task [10], thread [3] executing on device (821)
Task [11], thread [2] executing on device (259)
Task [12], thread [0] executing on device (235)
Task [13], thread [1] executing on device (659)
Task [14], thread [3] executing on device (224)
Task [15], thread [2] executing on device (586)
Task [16], thread [3] executing on device (368)
Task [17], thread [2] executing on device (746)
Task [18], thread [0] executing on device (549)
Task [19], thread [1] executing on device (833)
Task [20], thread [3] executing on device (127)
Task [21], thread [1] executing on device (656)
Task [22], thread [2] executing on device (702)
Task [23], thread [0] executing on device (451)
Task [24], thread [3] executing on device (412)
Task [25], thread [2] executing on device (942)
Task [26], thread [3] executing on device (282)
Task [27], thread [0] executing on device (329)
Task [28], thread [3] executing on device (216)
Task [29], thread [0] executing on device (261)
Task [30], thread [1] executing on device (870)
Task [31], thread [3] executing on device (478)
Task [32], thread [2] executing on device (512)
Task [33], thread [0] executing on host (78)
Task [34], thread [3] executing on device (830)
Task [35], thread [0] executing on device (622)
Task [36], thread [2] executing on device (888)
Task [37], thread [1] executing on device (502)
Task [38], thread [3] executing on device (842)
Task [39], thread [0] executing on device (863)
All Done!
[./0_Simple/asyncAPI/asyncAPI] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER]
time spent executing by the GPU: 11.53
time spent by CPU in CUDA calls: 0.02
CPU executed 92858 iterations while waiting for GPU to finish
Initializing...
GPU Device 0: "Turing" with compute capability 7.5

bf16TensorCoreGemm requires requires SM 8.0 or higher to use Tensor Cores.  Exiting...
GPU Device 0: "Turing" with compute capability 7.5


Launching 100 blocks with 1024 threads...

Array size = 102400 Num of Odds = 50945 Sum of Odds = 1272565 Sum of Evens 1233938

...Done.

starting Simple Print (CUDA Dynamic Parallelism)
GPU Device 0: "Turing" with compute capability 7.5

***************************************************************************
The CPU launches 2 blocks of 2 threads each. On the device each thread will
launch 2 blocks of 2 threads each. The GPU we will do that recursively
until it reaches max_depth=2

In total 2+8=10 blocks are launched!!! (8 from the GPU)
***************************************************************************

Launching cdp_kernel() with CUDA Dynamic Parallelism:

BLOCK 0 launched by the host
BLOCK 1 launched by the host
|  BLOCK 5 launched by thread 0 of block 1
|  BLOCK 3 launched by thread 0 of block 0
|  BLOCK 4 launched by thread 0 of block 1
|  BLOCK 2 launched by thread 0 of block 0
|  BLOCK 7 launched by thread 1 of block 0
|  BLOCK 6 launched by thread 1 of block 0
|  BLOCK 8 launched by thread 1 of block 1
|  BLOCK 9 launched by thread 1 of block 1
GPU Device 0: "Turing" with compute capability 7.5

Initializing data:
Running quicksort on 128 elements
Launching kernel on the GPU
Validating results: OK
CUDA Clock sample
GPU Device 0: "Turing" with compute capability 7.5

Average clocks/block = 2575.500000
CUDA Clock sample

error: unable to open GPU Device 0: "Turing" with compute capability 7.5

Hello World.
Hello World.
C++ Function Overloading starting...
DevicecheckCudaErrors Count: 1
GPU Device 0: "Turing" with compute capability 7.5

Shared Size:   1024
Constant Size: 0
Local Size:    0
Max Threads Per Block: 1024
Number of Registers: 12
PTX Version: 75
Binary Version: 75
simple_kernel(const int *pIn, int *pOut, int a) PASSED

Shared Size:   2048
Constant Size: 0
Local Size:    0
Max Threads Per Block: 1024
Number of Registers: 12
PTX Version: 75
Binary Version: 75
simple_kernel(const int2 *pIn, int *pOut, int a) PASSED

Shared Size:   2048
Constant Size: 0
Local Size:    0
Max Threads Per Block: 1024
Number of Registers: 16
PTX Version: 75
Binary Version: 75
simple_kernel(const int *pIn1, const int *pIn2, int *pOut, int a) PASSED

./0_Simple/cudaOpenMP/cudaOpenMP Starting...

number of host CPUs:	8
number of CUDA devices:	1
   0: GeForce GTX 1650 SUPER
---------------------------
CPU thread 0 (of 1) uses CUDA device 0
---------------------------
Initializing...
GPU Device 0: "Turing" with compute capability 7.5

M: 4096 (16 x 256)
N: 4096 (16 x 256)
K: 4096 (16 x 256)
Preparing data for GPU...
Required shared memory size: 64 Kb
Computing... using high performance kernel compute_gemm 
Time: 198.240250 ms
TFLOPS: 0.69
Initializing...
GPU Device 0: "Turing" with compute capability 7.5

dmmaTensorCoreGemm requires SM 8.0 or higher.  Exiting...
GPU Device 0: "Turing" with compute capability 7.5

Result native operators	: 662827.000000 
Result intrinsics	: 662827.000000 
&&&& fp16ScalarProduct PASSED
[globalToShmemAsyncCopy] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

MatrixA(1280,1280), MatrixB(1280,1280)
Running kernel = 0 - AsyncCopyMultiStageLargeChunk
Computing result using CUDA Kernel...
done
Performance= 204.82 GFlop/s, Time= 20.478 msec, Size= 4194304000 Ops, WorkgroupSize= 256 threads/block
Checking computed result for correctness: Result = PASS

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
Initializing...
GPU Device 0: "Turing" with compute capability 7.5

M: 4096 (16 x 256)
N: 4096 (16 x 256)
K: 4096 (16 x 256)
Preparing data for GPU...
Required shared memory size: 64 Kb
Computing... using high performance kernel compute_gemm_imma 
Time: 71.115776 ms
TOPS: 1.93
CUDA inline PTX assembler sample
GPU Device 0: "Turing" with compute capability 7.5

Test Successful.
CUDA inline PTX assembler sample

error: unable to open [Matrix Multiply Using CUDA] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

MatrixA(320,320), MatrixB(640,320)
Computing result using CUDA Kernel...
done
Performance= 613.20 GFlop/s, Time= 0.214 msec, Size= 131072000 Ops, WorkgroupSize= 1024 threads/block
Checking computed result for correctness: Result = PASS

NOTE: The CUDA Samples are not meant for performancemeasurements. Results may vary when GPU Boost is enabled.
[Matrix Multiply CUBLAS] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

GPU Device 0: "GeForce GTX 1650 SUPER" with compute capability 7.5

MatrixA(640,480), MatrixB(480,320), MatrixC(640,320)
Computing result using CUBLAS...done.
Performance= 2345.28 GFlop/s, Time= 0.084 msec, Size= 196608000 Ops
Computing result using host CPU...done.
Comparing CUBLAS Matrix Multiply with CPU results: PASS

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
[ matrixMulDrv (Driver API) ]
> Using CUDA Device [0]: GeForce GTX 1650 SUPER
> GPU Device has SM 7.5 compute capability
  Total amount of global memory:     4066574336 bytes
> findModulePath found file at <./0_Simple/matrixMulDrv/data/matrixMul_kernel64.fatbin>
> initCUDA loading module: <./0_Simple/matrixMulDrv/data/matrixMul_kernel64.fatbin>
Processing time: 0.080000 (ms)
Checking computed result for correctness: Result = PASS

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
[Matrix Multiply Using CUDA] - Starting...
MatrixA(320,320), MatrixB(640,320)

error: unable to open > findModulePath found file at <./0_Simple/memMapIPCDrv/data/memMapIpc_kernel64.fatbin>
> initCUDA loading module: <./0_Simple/memMapIPCDrv/data/memMapIpc_kernel64.fatbin>
Step 0 done
Process 0: verifying...
./0_Simple/simpleAWBarrier/simpleAWBarrier starting...
GPU Device 0: "Turing" with compute capability 7.5

Launching normVecByDotProductAWBarrier kernel with numBlocks = 20 blockSize = 1024
Result = PASSED
./0_Simple/simpleAWBarrier/simpleAWBarrier completed, returned OK
simpleAssert.cu:47: void testKernel(int): block: [1,0,0], thread: [28,0,0] Assertion `gtid < N` failed.
simpleAssert.cu:47: void testKernel(int): block: [1,0,0], thread: [29,0,0] Assertion `gtid < N` failed.
simpleAssert.cu:47: void testKernel(int): block: [1,0,0], thread: [30,0,0] Assertion `gtid < N` failed.
simpleAssert.cu:47: void testKernel(int): block: [1,0,0], thread: [31,0,0] Assertion `gtid < N` failed.
simpleAssert starting...
OS_System_Type.release = 5.12.0-yoctodev-standard
OS Info: <#1 SMP PREEMPT Sat May 8 03:46:47 UTC 2021>

GPU Device 0: "Turing" with compute capability 7.5

Launch kernel to generate assertion failures

-- Begin assert output


-- End assert output

Device assert failed as expected, CUDA error message is: device-side assert triggered

simpleAssert completed, returned OK
simpleAssert_nvrtc starting...
Launch kernel to generate assertion failures

error: unable to open simpleAtomicIntrinsics starting...
GPU Device 0: "Turing" with compute capability 7.5

Processing time: 69.394997 (ms)
simpleAtomicIntrinsics completed, returned OK
simpleAtomicIntrinsics_nvrtc starting...

error: unable to open ./0_Simple/simpleAttributes/simpleAttributes Starting...

GPU Device 0: "Turing" with compute capability 7.5

Waiving execution as device 0 does not support persisting L2 Caching
Starting simpleCallback
Found 1 CUDA capable GPUs
GPU[0] GeForce GTX 1650 SUPER supports SM 7.5, capable GPU Callback Functions
1 GPUs available to run Callback Functions
Starting 8 heterogeneous computing workloads
Total of 8 workloads finished:
Success

Launching a single block with 64 threads...

 Sum of all ranks 0..63 in threadBlockGroup is 2016 (expected 2016)

 Now creating 4 groups, each of size 16 threads:

   Sum of all ranks 0..15 in this tiledPartition16 group is 120 (expected 120)
   Sum of all ranks 0..15 in this tiledPartition16 group is 120 (expected 120)
   Sum of all ranks 0..15 in this tiledPartition16 group is 120 (expected 120)
   Sum of all ranks 0..15 in this tiledPartition16 group is 120 (expected 120)

...Done.

GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER] has 20 Multi-Processors SM 7.5
Covering Cubemap data array of 64~3 x 1: Grid size is 8 x 8, each block has 8 x 8 threads
Processing time: 0.008 msec
3072.00 Mtexlookups/sec
Comparing kernel output to expected data
GPU Device 0: "Turing" with compute capability 7.5

16777216 elements
threads per block  = 512
Graph Launch iterations = 3

Num of nodes in the graph created manually = 6
[cudaGraphsManual] final reduced sum = 0.996214
[cudaGraphsManual] final reduced sum = 0.996214
[cudaGraphsManual] final reduced sum = 0.996214
Cloned Graph Output.. 
[cudaGraphsManual] final reduced sum = 0.996214
[cudaGraphsManual] final reduced sum = 0.996214
[cudaGraphsManual] final reduced sum = 0.996214

Num of nodes in the graph created using stream capture API = 6
[cudaGraphsUsingStreamCapture] final reduced sum = 0.996214
[cudaGraphsUsingStreamCapture] final reduced sum = 0.996214
[cudaGraphsUsingStreamCapture] final reduced sum = 0.996214
Cloned Graph Output.. 
[cudaGraphsUsingStreamCapture] final reduced sum = 0.996214
[cudaGraphsUsingStreamCapture] final reduced sum = 0.996214
[cudaGraphsUsingStreamCapture] final reduced sum = 0.996214
simpleDrvRuntime..
GPU Device 0: "Turing" with compute capability 7.5

> findModulePath found file at <./0_Simple/simpleDrvRuntime/data/vectorAdd_kernel64.fatbin>
> initCUDA loading module: <./0_Simple/simpleDrvRuntime/data/vectorAdd_kernel64.fatbin>
Result = PASS
Process 0: Starting on device 0...
Step 0 done
Process 0: verifying...
Process 0 complete!
[simpleLayeredTexture] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER] has 20 Multi-Processors SM 7.5
Covering 2D data array of 512 x 512: Grid size is 64 x 64, each block has 8 x 8 threads
Processing time: 0.081 msec
16181.73 Mtexlookups/sec
Comparing kernel output to expected data
[simpleMultiCopy] - Starting...
> Using CUDA device [0]: GeForce GTX 1650 SUPER
[GeForce GTX 1650 SUPER] has 20 MP(s) x 64 (Cores/MP) = 1280 (Cores)
> Device name: GeForce GTX 1650 SUPER
> CUDA Capability 7.5 hardware with 20 multi-processors
> scale_factor = 1.00
> array_size   = 4194304


Relevant properties of this CUDA device
(X) Can overlap one CPU<>GPU data transfer with GPU kernel execution (device property "deviceOverlap")
(X) Can overlap two CPU<>GPU data transfers with GPU kernel execution
    (Compute Capability >= 2.0 AND (Tesla product OR Quadro 4000/5000/6000/K5000)

Measured timings (throughput):
 Memcpy host to device	: 1.354816 ms (12.383391 GB/s)
 Memcpy device to host	: 1.319584 ms (12.714019 GB/s)
 Kernel			: 0.215424 ms (778.799758 GB/s)

Theoretical limits for speedup gained from overlapped data transfers:
No overlap at all (transfer-kernel-transfer): 2.889824 ms 
Compute can overlap with one transfer: 2.674400 ms
Compute can overlap with both data transfers: 1.354816 ms

Average measured timings over 10 repetitions:
 Avg. time when execution fully serialized	: 2.893376 ms
 Avg. time when overlapped using 4 streams	: 1.681277 ms
 Avg. speedup gained (serialized - overlapped)	: 1.212099 ms

Measured throughput:
 Fully serialized execution		: 11.596983 GB/s
 Overlapped using 4 streams		: 19.957707 GB/s
Starting simpleMultiGPU
CUDA-capable device count: 1
Generating input data...

Computing with 1 GPUs...
  GPU Processing time: 12.394000 (ms)

Computing with Host CPU...

Comparing GPU and Host CPU results...
  GPU sum: 16777296.000000
  CPU sum: 16777294.395033
  Relative difference: 9.566307E-08 

starting Simple Occupancy

[ Manual configuration with 32 threads per block ]
Potential occupancy: 50%
Elapsed time: 0.088ms

[ Automatic, occupancy-based configuration ]
Suggested block size: 1024
Minimum grid size for maximum occupancy: 20
Potential occupancy: 100%
Elapsed time: 0.057792ms

Test PASSED

[./0_Simple/simpleP2P/simpleP2P] - Starting...
Checking for multiple GPUs...
CUDA-capable device count: 1
Two or more GPUs with Peer-to-Peer access capability are required for ./0_Simple/simpleP2P/simpleP2P.
Waiving test.
simplePitchLinearTexture starting...

GPU Device 0: "Turing" with compute capability 7.5


Bandwidth (GB/s) for pitch linear: 1.51e+02; for array: 1.57e+02

Texture fetch rate (Mpix/s) for pitch linear: 1.89e+04; for array: 1.96e+04

simplePitchLinearTexture completed, returned OK
GPU Device 0: "Turing" with compute capability 7.5

Device 0: "GeForce GTX 1650 SUPER" with Compute 7.5 capability
printf() is called. Output:

[0, 0]:		Value is:10
[0, 1]:		Value is:10
[0, 2]:		Value is:10
[0, 3]:		Value is:10
[0, 4]:		Value is:10
[0, 5]:		Value is:10
[0, 6]:		Value is:10
[0, 7]:		Value is:10
[1, 0]:		Value is:10
[1, 1]:		Value is:10
[1, 2]:		Value is:10
[1, 3]:		Value is:10
[1, 4]:		Value is:10
[1, 5]:		Value is:10
[1, 6]:		Value is:10
[1, 7]:		Value is:10
[3, 0]:		Value is:10
[3, 1]:		Value is:10
[3, 2]:		Value is:10
[3, 3]:		Value is:10
[3, 4]:		Value is:10
[3, 5]:		Value is:10
[3, 6]:		Value is:10
[3, 7]:		Value is:10
[2, 0]:		Value is:10
[2, 1]:		Value is:10
[2, 2]:		Value is:10
[2, 3]:		Value is:10
[2, 4]:		Value is:10
[2, 5]:		Value is:10
[2, 6]:		Value is:10
[2, 7]:		Value is:10
simpleSeparateCompilation starting...
GPU Device 0: "Turing" with compute capability 7.5

simpleSeparateCompilation completed, returned OK
[ simpleStreams ]

Device synchronization method set to = 0 (Automatic Blocking)
Setting reps to 100 to demonstrate steady state

> GPU Device 0: "Turing" with compute capability 7.5

Device: <GeForce GTX 1650 SUPER> canMapHostMemory: Yes
> CUDA Capable: SM 7.5 hardware
> 20 Multiprocessor(s) x 64 (Cores/Multiprocessor) = 1280 (Cores)
> scale_factor = 1.0000
> array_size   = 16777216

> Using CPU/GPU Device Synchronization method (cudaDeviceScheduleAuto)
> mmap() allocating 64.00 Mbytes (generic page-aligned system memory)
> cudaHostRegister() registering 64.00 Mbytes of generic allocated system memory

Starting Test
memcopy:	5.27
kernel:		0.92
non-streamed:	6.12
4 streams:	5.65
-------------------------------
simpleSurfaceWrite starting...
GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER] has 20 Multi-Processors, SM 7.5
Loaded 'lena_bw.pgm', 512 x 512 pixels
Processing time: 0.020000 (ms)
13107.20 Mpixels/sec
Wrote 'output.pgm'
Comparing files
	output:    <output.pgm>
	reference: <./0_Simple/simpleSurfaceWrite/data/ref_rotated.pgm>
simpleSurfaceWrite completed, returned OK
> runTest<float,32>
GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER] has 20 Multi-Processors
Processing time: 71.218002 (ms)
Compare OK

> runTest<int,64>
GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER] has 20 Multi-Processors
Processing time: 0.114000 (ms)
Compare OK


[simpleTemplates] -> Test Results: 0 Failures
> runTest<float,32>

error: unable to open simpleTexture starting...
GPU Device 0: "Turing" with compute capability 7.5

Loaded 'lena_bw.pgm', 512 x 512 pixels
Processing time: 0.021000 (ms)
12483.05 Mpixels/sec
Wrote './0_Simple/simpleTexture/data/lena_bw_out.pgm'
Comparing files
	output:    <./0_Simple/simpleTexture/data/lena_bw_out.pgm>
	reference: <./0_Simple/simpleTexture/data/ref_rotated.pgm>
simpleTexture completed, returned OK
> Using CUDA Device [0]: GeForce GTX 1650 SUPER
> GPU Device has SM 7.5 compute capability
> findModulePath found file at <./0_Simple/simpleTextureDrv/data/simpleTexture_kernel64.fatbin>
> initCUDA loading module: <./0_Simple/simpleTextureDrv/data/simpleTexture_kernel64.fatbin>
Loaded 'lena_bw.pgm', 512 x 512 pixels
Processing time: 0.020000 (ms)
13107.20 Mpixels/sec
Wrote './0_Simple/simpleTextureDrv/data/lena_bw_out.pgm'
Comparing files
	output:    <./0_Simple/simpleTextureDrv/data/lena_bw_out.pgm>
	reference: <./0_Simple/simpleTextureDrv/data/ref_rotated.pgm>
[simpleVoteIntrinsics]
GPU Device 0: "Turing" with compute capability 7.5

> GPU device has 20 Multi-Processors, SM 7.5 compute capabilities

[VOTE Kernel Test 1/3]
	Running <<Vote.Any>> kernel1 ...
	OK

[VOTE Kernel Test 2/3]
	Running <<Vote.All>> kernel2 ...
	OK

[VOTE Kernel Test 3/3]
	Running <<Vote.Any>> kernel3 ...
	OK
	Shutting down...

error: unable to open   Device 0: <          Turing >, Compute SM 7.5 detected
> Using CUDA Host Allocated (cudaHostAlloc)
> vectorAddGPU kernel will add vectors using mapped CPU memory...
> Checking the results from vectorAddGPU() ...
> Releasing CPU memory...
GPU Device 0: "Turing" with compute capability 7.5

Starting basicStreamOrderedAllocation()
> Checking the results from vectorAddGPU() ...
basicStreamOrderedAllocation PASSED
Starting streamOrderedAllocationPostSync()
Total elapsed time = 34.167393 ms over 20 iterations
> Checking the results from vectorAddGPU() ...
streamOrderedAllocationPostSync PASSED
No Two or more GPUs with same architecture capable of cuda Memory Pools found.
Waiving the sample
GPU Device 0: "Turing" with compute capability 7.5

CANNOT access pageable memory
systemWideAtomics completed, returned OK 
./0_Simple/template/template Starting...

GPU Device 0: "Turing" with compute capability 7.5

Processing time: 58.036999 (ms)
Initializing...
GPU Device 0: "Turing" with compute capability 7.5

tf32TensorCoreGemm requires requires SM 8.0 or higher to use Tensor Cores.  Exiting...
[Vector addition of 50000 elements]
Copy input data from the host memory to the CUDA device
CUDA kernel launch with 196 blocks of 256 threads
Copy output data from the CUDA device to the host memory
Test PASSED
Done
Vector Addition (Driver API)
> Using CUDA Device [0]: GeForce GTX 1650 SUPER
> findModulePath found file at <./0_Simple/vectorAddDrv/data/vectorAdd_kernel64.fatbin>
> initCUDA loading module: <./0_Simple/vectorAddDrv/data/vectorAdd_kernel64.fatbin>
Result = PASS
Vector Addition (Driver API)
> Using CUDA Device [0]: GeForce GTX 1650 SUPER
Device 0 VIRTUAL ADDRESS MANAGEMENT SUPPORTED = 1.
> findModulePath found file at <./0_Simple/vectorAddMMAP/data/vectorAdd_kernel64.fatbin>
> initCUDA loading module: <./0_Simple/vectorAddMMAP/data/vectorAdd_kernel64.fatbin>
Result = PASS

error: unable to open GPU Device 0: "Turing" with compute capability 7.5

Running ........................................................

Overall Time For matrixMultiplyPerf 

Printing Average of 20 measurements in (ms)
Size_KB	 UMhint	UMhntAs	 UMeasy	  0Copy	MemCopy	CpAsync	CpHpglk	CpPglAs
4	  0.260	  0.249	  0.315	  0.015	  0.027	  0.023	  0.032	  0.030
16	  0.241	  0.266	  0.436	  0.031	  0.048	  0.039	  0.048	  0.051
64	  0.404	  0.324	  0.693	  0.094	  0.113	  0.103	  0.114	  0.103
256	  0.810	  0.732	  1.147	  0.439	  0.403	  0.386	  0.362	  0.353
1024	  2.432	  2.377	  2.982	  2.551	  1.862	  1.740	  1.443	  1.471
4096	  9.824	  9.237	 12.028	 17.860	  8.601	  8.526	  7.657	  7.601
16384	 49.069	 48.574	 60.952	137.169	 46.855	 48.130	 43.501	 43.414

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
[CUDA Bandwidth Test] - Starting...
Running on...

 Device 0: GeForce GTX 1650 SUPER
 Quick Mode

 Host to Device Bandwidth, 1 Device(s)
 PINNED Memory Transfers
   Transfer Size (Bytes)	Bandwidth(GB/s)
   32000000			12.4

 Device to Host Bandwidth, 1 Device(s)
 PINNED Memory Transfers
   Transfer Size (Bytes)	Bandwidth(GB/s)
   32000000			12.7

 Device to Device Bandwidth, 1 Device(s)
 PINNED Memory Transfers
   Transfer Size (Bytes)	Bandwidth(GB/s)
   32000000			159.2

Result = PASS

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
./1_Utilities/deviceQuery/deviceQuery Starting...

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
./1_Utilities/deviceQueryDrv/deviceQueryDrv Starting...

CUDA Device Query (Driver API) statically linked version 
Detected 1 CUDA Capable device(s)

Device 0: "GeForce GTX 1650 SUPER"
  CUDA Driver Version:                           11.2
  CUDA Capability Major/Minor version number:    7.5
  Total amount of global memory:                 3878 MBytes (4066574336 bytes)
  (20) Multiprocessors, ( 64) CUDA Cores/MP:     1280 CUDA Cores
  GPU Max Clock rate:                            1755 MHz (1.75 GHz)
  Memory Clock rate:                             6001 Mhz
  Memory Bus Width:                              128-bit
  L2 Cache Size:                                 1048576 bytes
  Max Texture Dimension Sizes                    1D=(131072) 2D=(131072, 65536) 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  1024
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size (x,y,z):    (2147483647, 65535, 65535)
  Texture alignment:                             512 bytes
  Maximum memory pitch:                          2147483647 bytes
  Concurrent copy and kernel execution:          Yes with 3 copy engine(s)
  Run time limit on kernels:                     Yes
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Concurrent kernel execution:                   Yes
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
Result = PASS
[P2P (Peer-to-Peer) GPU Bandwidth Latency Test]
Device: 0, GeForce GTX 1650 SUPER, pciBusID: 1, pciDeviceID: 0, pciDomainID:0

***NOTE: In case a device doesn't have P2P access to other one, it falls back to normal memcopy procedure.
So you can see lesser Bandwidth (GB/s) and unstable Latency (us) in those cases.

P2P Connectivity Matrix
     D\D     0
     0	     1
Unidirectional P2P=Disabled Bandwidth Matrix (GB/s)
   D\D     0 
     0 144.46 
Unidirectional P2P=Enabled Bandwidth (P2P Writes) Matrix (GB/s)
   D\D     0 
     0 137.43 
Bidirectional P2P=Disabled Bandwidth Matrix (GB/s)
   D\D     0 
     0 148.25 
Bidirectional P2P=Enabled Bandwidth Matrix (GB/s)
   D\D     0 
     0 147.87 
P2P=Disabled Latency Matrix (us)
   GPU     0 
     0   1.35 

   CPU     0 
     0   1.67 
P2P=Enabled Latency (P2P Writes) Matrix (us)
   GPU     0 
     0   1.25 

   CPU     0 
     0   1.80 

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
GPU0 <-> CPU:
  * Atomic Supported: no
HSOpticalFlow Starting...

GPU Device 0: "Turing" with compute capability 7.5

Loading "frame10.ppm" ...
Loading "frame11.ppm" ...
Computing optical flow on CPU...
Computing optical flow on GPU...
L1 error : 0.044308
GPU Device 0: "Turing" with compute capability 7.5


TEST#1:
  CUDA resize nv12(1920x1080 --> 640x480), batch: 24, average time: 0.296 ms ==> 0.012 ms/frame
  CUDA convert nv12(640x480) to bgr(640x480), batch: 24, average time: 0.691 ms ==> 0.029 ms/frame

TEST#2:
  CUDA convert nv12(1920x1080) to bgr(1920x1080), batch: 24, average time: 4.699 ms ==> 0.196 ms/frame
  CUDA resize bgr(1920x1080 --> 640x480), batch: 24, average time: 3.386 ms ==> 0.141 ms/frame
[./3_Imaging/convolutionFFT2D/convolutionFFT2D] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

Testing built-in R2C / C2R FFT-based convolution
...allocating memory
...generating random input data
...creating R2C & C2R FFT plans for 2048 x 2048
...uploading to GPU and padding convolution kernel and input data
...transforming convolution kernel
...running GPU FFT convolution: 2305.475485 MPix/s (1.735000 ms)
...reading back GPU convolution results
...running reference CPU convolution
...comparing the results: rel L2 = 8.680021E-08 (max delta = 8.227172E-07)
L2norm Error OK
...shutting down
Testing custom R2C / C2R FFT-based convolution
...allocating memory
...generating random input data
...creating C2C FFT plan for 2048 x 1024
...uploading to GPU and padding convolution kernel and input data
...transforming convolution kernel
...running GPU FFT convolution: 2245.929230 MPix/s (1.781000 ms)
...reading back GPU FFT results
...running reference CPU convolution
...comparing the results: rel L2 = 1.067915E-07 (max delta = 9.817303E-07)
L2norm Error OK
...shutting down
Testing updated custom R2C / C2R FFT-based convolution
...allocating memory
...generating random input data
...creating C2C FFT plan for 2048 x 1024
...uploading to GPU and padding convolution kernel and input data
...transforming convolution kernel
...running GPU FFT convolution: 2890.173528 MPix/s (1.384000 ms)
...reading back GPU FFT results
...running reference CPU convolution
...comparing the results: rel L2 = 1.065127E-07 (max delta = 9.817303E-07)
L2norm Error OK
...shutting down
Test Summary: 0 errors
Test passed
[./3_Imaging/convolutionSeparable/convolutionSeparable] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

Image Width x Height = 3072 x 3072

Allocating and initializing host arrays...
Allocating and initializing CUDA arrays...
Running GPU convolution (16 identical iterations)...

convolutionSeparable, Throughput = 6947.7267 MPixels/sec, Time = 0.00136 s, Size = 9437184 Pixels, NumDevsUsed = 1, Workgroup = 0

Reading back GPU results...

Checking the results...
 ...running convolutionRowCPU()
 ...running convolutionColumnCPU()
 ...comparing the results
 ...Relative L2 norm: 0.000000E+00

Shutting down...
Test passed
[./3_Imaging/convolutionTexture/convolutionTexture] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

Initializing data...
Running GPU rows convolution (10 identical iterations)...
Average convolutionRowsGPU() time: 0.740700 msecs; //6370.449519 Mpix/s
Copying convolutionRowGPU() output back to the texture...
cudaMemcpyToArray() time: 0.254000 msecs; //18577.133265 Mpix/s
Running GPU columns convolution (10 iterations)
Average convolutionColumnsGPU() time: 0.715100 msecs; //6598.506591 Mpix/s
Reading back GPU results...
Checking the results...
...running convolutionRowsCPU()
...running convolutionColumnsCPU()
Relative L2 norm: 0.000000E+00
Shutting down...
Test passed
./3_Imaging/dct8x8/dct8x8 Starting...

GPU Device 0: "Turing" with compute capability 7.5

CUDA sample DCT/IDCT implementation
===================================
Loading test image: barbara.bmp... [512 x 512]... Success
Running Gold 1 (CPU) version... Success
Running Gold 2 (CPU) version... Success
Running CUDA 1 (GPU) version... Success
Running CUDA 2 (GPU) version... 17676.600651 MPix/s //0.014830 ms
Success
Running CUDA short (GPU) version... Success
Dumping result to barbara_gold1.bmp... Success
Dumping result to barbara_gold2.bmp... Success
Dumping result to barbara_cuda1.bmp... Success
Dumping result to barbara_cuda2.bmp... Success
Dumping result to barbara_cuda_short.bmp... Success
Processing time (CUDA 1)    : 0.071300 ms 
Processing time (CUDA 2)    : 0.014830 ms 
Processing time (CUDA short): 0.061000 ms 
PSNR Original    <---> CPU(Gold 1)    : 32.777073
PSNR Original    <---> CPU(Gold 2)    : 32.777046
PSNR Original    <---> GPU(CUDA 1)    : 32.777092
PSNR Original    <---> GPU(CUDA 2)    : 32.777077
PSNR Original    <---> GPU(CUDA short): 32.749447
PSNR CPU(Gold 1) <---> GPU(CUDA 1)    : 64.019310
PSNR CPU(Gold 2) <---> GPU(CUDA 2)    : 71.777740
PSNR CPU(Gold 2) <---> GPU(CUDA short): 42.258053

Test Summary...
Test passed
./3_Imaging/dwtHaar1D/dwtHaar1D Starting...

GPU Device 0: "Turing" with compute capability 7.5

source file    = "./3_Imaging/dwtHaar1D/data/signal.dat"
reference file = "result.dat"
gold file      = "./3_Imaging/dwtHaar1D/data/regression.gold.dat"
Reading signal from "./3_Imaging/dwtHaar1D/data/signal.dat"
Writing result to "result.dat"
Reading reference result from "./3_Imaging/dwtHaar1D/data/regression.gold.dat"
Test success!
./3_Imaging/dxtc/dxtc Starting...

GPU Device 0: "Turing" with compute capability 7.5

Image Loaded './3_Imaging/dxtc/data/lena_std.ppm', 512 x 512 pixels

Running DXT Compression on 512 x 512 image...

16384 Blocks, 64 Threads per Block, 1048576 Threads in Grid...

dxtc, Throughput = 92.0126 MPixels/s, Time = 0.00285 s, Size = 262144 Pixels, NumDevsUsed = 1, Workgroup = 64

Checking accuracy...
Deviation at (   9,   1):	0.791667 rms
Deviation at (  99,   1):	1.041667 rms
Deviation at (  33,   2):	2.645833 rms
Deviation at (  38,   4):	1.916667 rms
Deviation at (  57,   4):	0.854167 rms
Deviation at (  20,   7):	1.041667 rms
Deviation at (  57,   7):	0.458333 rms
Deviation at (   8,   9):	0.937500 rms
Deviation at (  31,   9):	0.770833 rms
Deviation at (  13,  11):	1.041667 rms
Deviation at (  88,  11):	0.729167 rms
Deviation at (   4,  13):	8.562500 rms
Deviation at (  28,  13):	0.562500 rms
Deviation at (  90,  13):	0.708333 rms
Deviation at (  25,  14):	0.520833 rms
Deviation at (  87,  16):	0.708333 rms
Deviation at (  24,  19):	0.916667 rms
Deviation at (  25,  19):	0.625000 rms
Deviation at (  26,  19):	1.041667 rms
Deviation at (  55,  20):	4.791667 rms
Deviation at (  20,  23):	1.541667 rms
Deviation at (  99,  23):	3.312500 rms
Deviation at (  45,  24):	18.104166 rms
Deviation at (   8,  28):	0.895833 rms
Deviation at (  21,  30):	1.562500 rms
Deviation at ( 115,  32):	24.104166 rms
Deviation at (   2,  33):	0.854167 rms
Deviation at ( 102,  33):	2.250000 rms
Deviation at (  50,  35):	26.958334 rms
Deviation at (  12,  38):	2.166667 rms
Deviation at (  96,  39):	1.041667 rms
Deviation at (  40,  40):	0.270833 rms
Deviation at (  43,  44):	2.250000 rms
Deviation at (  54,  44):	4.791667 rms
Deviation at (  46,  46):	2.875000 rms
Deviation at ( 116,  46):	0.604167 rms
Deviation at ( 117,  46):	6.833333 rms
Deviation at ( 117,  48):	0.937500 rms
Deviation at (  23,  51):	3.520833 rms
Deviation at (  67,  54):	5.687500 rms
Deviation at (  26,  55):	0.854167 rms
Deviation at (  21,  56):	5.000000 rms
Deviation at (  24,  56):	0.562500 rms
Deviation at (  30,  57):	0.937500 rms
Deviation at ( 126,  57):	1.208333 rms
Deviation at (  21,  59):	2.541667 rms
Deviation at ( 120,  59):	0.104167 rms
Deviation at ( 112,  60):	1.125000 rms
Deviation at (  76,  61):	1.666667 rms
Deviation at (  77,  61):	1.083333 rms
Deviation at (  75,  62):	0.937500 rms
Deviation at ( 121,  62):	0.937500 rms
Deviation at ( 124,  64):	2.854167 rms
Deviation at (  78,  66):	0.541667 rms
Deviation at ( 106,  68):	0.375000 rms
Deviation at (  16,  70):	3.104167 rms
Deviation at (  10,  71):	0.937500 rms
Deviation at ( 108,  71):	0.354167 rms
Deviation at (   0,  72):	0.854167 rms
Deviation at ( 118,  72):	5.562500 rms
Deviation at (  11,  73):	0.541667 rms
Deviation at (  68,  74):	1.937500 rms
Deviation at (  70,  76):	1.791667 rms
Deviation at ( 124,  76):	3.354167 rms
Deviation at ( 103,  78):	0.375000 rms
Deviation at (  74,  79):	0.270833 rms
Deviation at ( 108,  79):	0.083333 rms
Deviation at (  43,  82):	24.979166 rms
Deviation at (  58,  82):	2.833333 rms
Deviation at (  67,  82):	3.125000 rms
Deviation at (  78,  82):	2.437500 rms
Deviation at ( 123,  84):	0.541667 rms
Deviation at ( 127,  88):	0.229167 rms
Deviation at (  99,  89):	0.770833 rms
Deviation at (  93,  91):	0.666667 rms
Deviation at ( 118,  91):	1.125000 rms
Deviation at ( 115,  92):	0.083333 rms
Deviation at ( 115,  93):	0.083333 rms
Deviation at (  45,  94):	0.166667 rms
Deviation at (  14,  95):	1.937500 rms
Deviation at (  69,  95):	1.875000 rms
Deviation at ( 106,  95):	1.125000 rms
Deviation at ( 107,  95):	3.708333 rms
Deviation at (  13,  96):	1.354167 rms
Deviation at ( 115,  98):	0.187500 rms
Deviation at ( 118,  98):	0.187500 rms
Deviation at ( 116, 101):	0.187500 rms
Deviation at (  87, 106):	0.270833 rms
Deviation at (  67, 107):	0.708333 rms
Deviation at (  74, 107):	0.375000 rms
Deviation at (  65, 109):	0.770833 rms
Deviation at (  89, 109):	0.708333 rms
Deviation at ( 118, 109):	3.854167 rms
Deviation at (  88, 111):	0.208333 rms
Deviation at (  64, 113):	0.708333 rms
Deviation at (  84, 113):	0.333333 rms
Deviation at (  75, 114):	2.083333 rms
Deviation at (  66, 115):	0.770833 rms
Deviation at (  89, 116):	0.770833 rms
Deviation at (  19, 118):	5.270833 rms
Deviation at (  76, 121):	0.104167 rms
Deviation at (  70, 122):	0.708333 rms
Deviation at (  91, 122):	0.208333 rms
Deviation at (  75, 123):	0.854167 rms
Deviation at (  61, 124):	0.937500 rms
Deviation at (  91, 124):	0.270833 rms
Deviation at (  91, 125):	1.020833 rms
RMS(reference, result) = 0.015238

Test passed
[[histogram]] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER] has 20 Multi-Processors, Compute 7.5
Initializing data...
...allocating CPU memory.
...generating input data
...allocating GPU memory and copying input data

Starting up 64-bin histogram...

Running 64-bin GPU histogram for 67108864 bytes (16 runs)...

histogram64() time (average) : 0.00073 sec, 92396.6782 MB/sec

histogram64, Throughput = 92396.6782 MB/s, Time = 0.00073 s, Size = 67108864 Bytes, NumDevsUsed = 1, Workgroup = 64

Validating GPU results...
 ...reading back GPU results
 ...histogram64CPU()
 ...comparing the results...
 ...64-bin histograms match

Shutting down 64-bin histogram...


Initializing 256-bin histogram...
Running 256-bin GPU histogram for 67108864 bytes (16 runs)...

histogram256() time (average) : 0.00061 sec, 110855.0318 MB/sec

histogram256, Throughput = 110855.0318 MB/s, Time = 0.00061 s, Size = 67108864 Bytes, NumDevsUsed = 1, Workgroup = 192

Validating GPU results...
 ...reading back GPU results
 ...histogram256CPU()
 ...comparing the results
 ...256-bin histograms match

Shutting down 256-bin histogram...


Shutting down...

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.

[histogram] - Test Summary
Test passed
[stereoDisparity] Starting...

GPU Device 0: "Turing" with compute capability 7.5

> GPU device has 20 Multi-Processors, SM 7.5 compute capabilities

Loaded <./3_Imaging/stereoDisparity/data/stereo.im0.640x533.ppm> as image 0
Loaded <./3_Imaging/stereoDisparity/data/stereo.im1.640x533.ppm> as image 1
Launching CUDA stereoDisparityKernel()
Input Size  [640x533], Kernel size [17x17], Disparities [-16:0]
GPU processing time : 1.0705 (ms)
Pixel throughput    : 318.666 Mpixels/sec
GPU Checksum = 4293895789, GPU image: <output_GPU.pgm>
Computing CPU reference...
CPU Checksum = 4293895789, CPU image: <output_CPU.pgm>
[./4_Finance/BlackScholes/BlackScholes] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

Initializing data...
...allocating CPU memory for options.
...allocating GPU memory for options.
...generating input data in CPU mem.
...copying input data to GPU mem.
Data init done.

Executing Black-Scholes GPU kernel (512 iterations)...
Options count             : 8000000     
BlackScholesGPU() time    : 0.483299 msec
Effective memory bandwidth: 165.529055 GB/s
Gigaoptions per second    : 16.552906     

BlackScholes, Throughput = 16.5529 GOptions/s, Time = 0.00048 s, Size = 8000000 options, NumDevsUsed = 1, Workgroup = 128

Reading back GPU results...
Checking the results...
...running CPU calculations.

Comparing the results...
L1 norm: 1.741792E-07
Max absolute error: 1.192093E-05

Shutting down...
...releasing GPU memory.
...releasing CPU memory.
Shutdown done.

[BlackScholes] - Test Summary

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.

Test passed
[./4_Finance/BlackScholes_nvrtc/BlackScholes_nvrtc] - Starting...
Initializing data...
...allocating CPU memory for options.

error: unable to open ./4_Finance/MonteCarloMultiGPU/MonteCarloMultiGPU Starting...

Using single CPU thread for multiple GPUs
MonteCarloMultiGPU
==================
Parallelization method  = streamed
Problem scaling         = weak
Number of GPUs          = 1
Total number of options = 8192
Number of paths         = 262144
main(): generating input data...
main(): starting 1 host threads...
main(): GPU statistics, streamed
GPU Device #0: GeForce GTX 1650 SUPER
Options         : 8192
Simulation paths: 262144

Total time (ms.): 26.844999
	Note: This is elapsed time for all to compute.
Options per sec.: 305159.255338
main(): comparing Monte Carlo and Black-Scholes results...
Shutting down...
Test Summary...
L1 norm        : 4.825154E-04
Average reserve: 11.717557

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.

Test passed
Sobol Quasi-Random Number Generator Starting...

> number of vectors = 100000
> number of dimensions = 100
GPU Device 0: "Turing" with compute capability 7.5

Allocating CPU memory...
Allocating GPU memory...
Initializing direction numbers...
Copying direction numbers to device...
Executing QRNG on GPU...
Gsamples/s: 16.9205
Reading results from GPU...

Executing QRNG on CPU...
Gsamples/s: 0.248416
Checking results...
L1-Error: 0
Shutting down...
[./4_Finance/binomialOptions/binomialOptions] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

Generating input data...
Running GPU binomial tree...
Options count            : 1024     
Time steps               : 2048     
binomialOptionsGPU() time: 3.128000 msec
Options per second       : 327365.726704     
Running CPU binomial tree...
Comparing the results...
GPU binomial vs. Black-Scholes
L1 norm: 2.220214E-04
CPU binomial vs. Black-Scholes
L1 norm: 2.220920E-04
CPU binomial vs. GPU binomial
L1 norm: 7.997008E-07
Shutting down...

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.

Test passed
[./4_Finance/binomialOptions_nvrtc/binomialOptions_nvrtc] - Starting...
Generating input data...
Running GPU binomial tree...

error: unable to open ./4_Finance/quasirandomGenerator/quasirandomGenerator Starting...

Allocating GPU memory...
Allocating CPU memory...
Initializing QRNG tables...

Testing QRNG...

quasirandomGenerator, Throughput = 14.0215 GNumbers/s, Time = 0.00022 s, Size = 3145728 Numbers, NumDevsUsed = 1, Workgroup = 384

Reading GPU results...
Comparing to the CPU results...

L1 norm: 7.275964E-12

Testing inverseCNDgpu()...

quasirandomGenerator-inverse, Throughput = 30.3495 GNumbers/s, Time = 0.00010 s, Size = 3145728 Numbers, NumDevsUsed = 1, Workgroup = 128
Reading GPU results...

Comparing to the CPU results...
L1 norm: 9.439909E-08

Shutting down...
./4_Finance/quasirandomGenerator_nvrtc/quasirandomGenerator_nvrtc Starting...


error: unable to open ./6_Advanced/FDTD3d/FDTD3d Starting...

Set-up, based upon target device GMEM size...
 getTargetDeviceGlobalMemSize
 cudaGetDeviceCount
GPU Device 0: "Turing" with compute capability 7.5

 cudaGetDeviceProperties
 generateRandomData

FDTD on 376 x 376 x 376 volume with symmetric filter radius 4 for 5 timesteps...

fdtdReference...
 calloc intermediate
 Host FDTD loop
	t = 0
	t = 1
	t = 2
	t = 3
	t = 4

fdtdReference complete
fdtdGPU...
GPU Device 0: "Turing" with compute capability 7.5

 set block size to 32x16
 set grid size to 12x24
 GPU FDTD loop
	t = 0 launch kernel
	t = 1 launch kernel
	t = 2 launch kernel
	t = 3 launch kernel
	t = 4 launch kernel

fdtdGPU complete

CompareData (tolerance 0.000100)...
Starting [./6_Advanced/StreamPriorities/StreamPriorities]...
GPU Device 0: "Turing" with compute capability 7.5

CUDA stream priority range: LOW: 0 to HIGH: -2
elapsed time of kernels launched to LOW priority stream: 7.055 ms
elapsed time of kernels launched to HI  priority stream: 3.782 ms
[./6_Advanced/alignedTypes/alignedTypes] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

[GeForce GTX 1650 SUPER] has 20 MP(s) x 64 (Cores/MP) = 1280 (Cores)
> Compute scaling value = 1.00
> Memory Size = 49999872
Allocating memory...
Generating host input data array...
Uploading input data to GPU memory...
Testing misaligned types...
uint8...
Avg. time: 1.234031 ms / Copy throughput: 37.734872 GB/s.
	TEST OK
uint16...
Avg. time: 0.915812 ms / Copy throughput: 50.846663 GB/s.
	TEST OK
RGBA8_misaligned...
Avg. time: 0.775500 ms / Copy throughput: 60.046434 GB/s.
	TEST OK
LA32_misaligned...
Avg. time: 0.640344 ms / Copy throughput: 72.720334 GB/s.
	TEST OK
RGB32_misaligned...
Avg. time: 0.718156 ms / Copy throughput: 64.841053 GB/s.
	TEST OK
RGBA32_misaligned...
Avg. time: 0.667094 ms / Copy throughput: 69.804296 GB/s.
	TEST OK
Testing aligned types...
RGBA8...
Avg. time: 0.719000 ms / Copy throughput: 64.764966 GB/s.
	TEST OK
I32...
Avg. time: 0.717844 ms / Copy throughput: 64.869281 GB/s.
	TEST OK
LA32...
Avg. time: 0.640469 ms / Copy throughput: 72.706135 GB/s.
	TEST OK
RGB32...
Avg. time: 0.639656 ms / Copy throughput: 72.798491 GB/s.
	TEST OK
RGBA32...
Avg. time: 0.638219 ms / Copy throughput: 72.962458 GB/s.
	TEST OK
RGBA32_2...
Avg. time: 0.669312 ms / Copy throughput: 69.572899 GB/s.
	TEST OK

[alignedTypes] -> Test Results: 0 Failures
Shutting down...
Test passed
GPU Device 0: "Turing" with compute capability 7.5

Cannot find the input text file
. Exiting..
GPU Device 0: "Turing" with compute capability 7.5

GPU device GeForce GTX 1650 SUPER has compute capabilities (SM 7.5)
Running qsort on 5000 elements with seed 100, on GeForce GTX 1650 SUPER
    cdpAdvancedQuicksort PASSED
Sorted 5000 elems in 0.446 ms (11.199 Melems/sec)
Running on GPU 0 (GeForce GTX 1650 SUPER)
Computing Bezier Lines (CUDA Dynamic Parallelism Version) ... Done!
GPU Device 0: "Turing" with compute capability 7.5

GPU device GeForce GTX 1650 SUPER has compute capabilities (SM 7.5)
Launching CDP kernel to build the quadtree
Results: OK
[./6_Advanced/concurrentKernels/concurrentKernels] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

> Detected Compute SM 7.5 hardware with 20 multi-processors
Expected time for serial execution of 8 kernels = 0.080s
Expected time for concurrent execution of 8 kernels = 0.010s
Measured time for sample = 0.012s
Test passed
Starting [conjugateGradientMultiBlockCG]...
GPU Device 0: "Turing" with compute capability 7.5

> GPU device has 20 Multi-Processors, SM 7.5 compute capabilities

GPU Final, residual = 1.600115e-06, kernel execution time = 12.937216 ms
Test Summary:  Error amount = 0.000000 
&&&& conjugateGradientMultiBlockCG PASSED
Starting [conjugateGradientMultiDeviceCG]...
GPU Device 0: "GeForce GTX 1650 SUPER" with compute capability 7.5
No Two or more GPUs with same architecture capable of cooperativeMultiDeviceLaunch & concurrentManagedAccess found. 
Waiving the sample
GPU Device 0: "Turing" with compute capability 7.5

Device 0 doesn't support Generic memory compression, waiving the execution.
Starting eigenvalues
GPU Device 0: "Turing" with compute capability 7.5

Matrix size: 2048 x 2048
Precision: 0.000010
Iterations to be timed: 100
Result filename: 'eigenvalues.dat'
Gerschgorin interval: -2.894310 / 2.923303
Average time step 1: 1.779109 ms
Average time step 2, one intervals: 2.036231 ms
Average time step 2, mult intervals: 4.614792 ms
Average time TOTAL: 8.443171 ms
Test Succeeded!
./6_Advanced/fastWalshTransform/fastWalshTransform Starting...

GPU Device 0: "Turing" with compute capability 7.5

Initializing data...
...allocating CPU memory
...allocating GPU memory
...generating data
Data length: 8388608; kernel length: 128
Running GPU dyadic convolution using Fast Walsh Transform...
GPU time: 9.500000 ms; GOP/s: 30.463892
Reading back GPU results...
Running straightforward CPU dyadic convolution...
Comparing the results...
Shutting down...
L2 norm: 1.021579E-07
Test passed
[Interval Computing]  starting ...

GPU Device 0: "Turing" with compute capability 7.5

> GPU Device has Compute Capabilities SM 7.5

GPU naive implementation
Searching for roots in [0.01, 4]...
Found 2 intervals that may contain the root(s)
 i[0] = [0.999655515093009, 1.00011722206639]
 i[1] = [1.00011907576551, 1.00044661086269]
Number of equations solved: 65536
Time per equation: 21.2302627563477 us

Check against Host computation...

GPU Device 0: "Turing" with compute capability 7.5

CPU iterations : 2954
CPU error : 4.988e-03
CPU Processing time: 1807.119019 (ms)
GPU iterations : 2954
GPU error : 4.988e-03
GPU Processing time: 156.768997 (ms)
&&&& jacobiCudaGraphs PASSED
[./6_Advanced/lineOfSight/lineOfSight] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

Line of sight
Average time: 0.016650 ms

Test passed
[ matrixMulDynlinkJIT (CUDA dynamic linking) ]
> Device 0: "GeForce GTX 1650 SUPER" with Compute 7.5 capability
> Compiling CUDA module
> PTX JIT log:

Test run success!
./6_Advanced/mergeSort/mergeSort Starting...

GPU Device 0: "Turing" with compute capability 7.5

Allocating and initializing host arrays...

Allocating and initializing CUDA arrays...

Initializing GPU merge sort...
Running GPU merge sort...
Time: 8.851000 ms
Reading back GPU merge sort results...
Inspecting the results...
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: stable!
Shutting down...
newdelete Starting...

GPU Device 0: "Turing" with compute capability 7.5

 > Container = Vector test OK

 > Container = Vector, using placement new on SMEM buffer test OK

 > Container = Vector, with user defined datatype test OK

Test Summary: 3/3 succesfully run
[PTX Just In Time (JIT) Compilation (no-qatest)] - Starting...
> Using CUDA Device [0]: GeForce GTX 1650 SUPER
> findModulePath <./6_Advanced/ptxjit/data/ptxjit_kernel64.ptx>
> initCUDA loading module: <./6_Advanced/ptxjit/data/ptxjit_kernel64.ptx>
Loading ptxjit_kernel[] program
CUDA Link Completed in 0.000000ms. Linker Output:
info    : 0 bytes gmem
info    : Function properties for 'myKernel':
info    : used 8 registers, 0 stack, 0 bytes smem, 360 bytes cmem[0], 0 bytes lmem
CUDA kernel launched
./6_Advanced/radixSortThrust/radixSortThrust Starting...

GPU Device 0: "Turing" with compute capability 7.5


Sorting 1048576 32-bit unsigned int keys and values

radixSortThrust, Throughput = 912.7645 MElements/s, Time = 0.00115 s, Size = 1048576 elements
Test passed
./6_Advanced/reduction/reduction Starting...

GPU Device 0: "Turing" with compute capability 7.5

Using Device 0: GeForce GTX 1650 SUPER

Reducing array of type int

16777216 elements
256 threads (max)
64 blocks

Reduction, Throughput = 171.5330 GB/s, Time = 0.00039 s, Size = 16777216 Elements, NumDevsUsed = 1, Workgroup = 256

GPU result = 2139353471
CPU result = 2139353471

Test passed
reductionMultiBlockCG Starting...

GPU Device 0: "Turing" with compute capability 7.5

33554432 elements
numThreads: 1024
numBlocks: 20

Launching SinglePass Multi Block Cooperative Groups kernel
Average time: 1.009860 ms
Bandwidth:    132.907226 GB/s

GPU result = 1.992401599884
CPU result = 1.992401361465
./6_Advanced/scalarProd/scalarProd Starting...

GPU Device 0: "Turing" with compute capability 7.5

Initializing data...
...allocating CPU memory.
...allocating GPU memory.
...generating input data in CPU mem.
...copying input data to GPU mem.
Data init done.
Executing GPU kernel...
GPU time: 0.072000 msecs.
Reading back GPU result...
Checking GPU results...
..running CPU scalar product calculation
...comparing the results
Shutting down...
L1 error: 2.745062E-08
Test passed
./6_Advanced/scan/scan Starting...

GPU Device 0: "Turing" with compute capability 7.5

Allocating and initializing host arrays...
Allocating and initializing CUDA arrays...
Initializing CUDA-C scan...

*** Running GPU scan for short arrays (100 identical iterations)...

Running scan for 4 elements (1703936 arrays)...
Validating the results...
...reading back GPU results
 ...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 8 elements (851968 arrays)...
Validating the results...
...reading back GPU results
 ...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 16 elements (425984 arrays)...
Validating the results...
...reading back GPU results
 ...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 32 elements (212992 arrays)...
Validating the results...
...reading back GPU results
 ...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 64 elements (106496 arrays)...
Validating the results...
...reading back GPU results
 ...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 128 elements (53248 arrays)...
Validating the results...
...reading back GPU results
 ...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 256 elements (26624 arrays)...
Validating the results...
...reading back GPU results
 ...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 512 elements (13312 arrays)...
Validating the results...
...reading back GPU results
 ...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 1024 elements (6656 arrays)...
Validating the results...
...reading back GPU results
 ...scanExclusiveHost()
 ...comparing the results
 ...Results Match


scan, Throughput = 3.0055 MElements/s, Time = 0.00034 s, Size = 1024 Elements, NumDevsUsed = 1, Workgroup = 256

***Running GPU scan for large arrays (100 identical iterations)...

Running scan for 2048 elements (3328 arrays)...
Validating the results...
...reading back GPU results
...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 4096 elements (1664 arrays)...
Validating the results...
...reading back GPU results
...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 8192 elements (832 arrays)...
Validating the results...
...reading back GPU results
...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 16384 elements (416 arrays)...
Validating the results...
...reading back GPU results
...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 32768 elements (208 arrays)...
Validating the results...
...reading back GPU results
...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 65536 elements (104 arrays)...
Validating the results...
...reading back GPU results
...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 131072 elements (52 arrays)...
Validating the results...
...reading back GPU results
...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 262144 elements (26 arrays)...
Validating the results...
...reading back GPU results
...scanExclusiveHost()
 ...comparing the results
 ...Results Match


scan, Throughput = 378.3998 MElements/s, Time = 0.00069 s, Size = 262144 Elements, NumDevsUsed = 1, Workgroup = 256

Shutting down...
./6_Advanced/segmentationTreeThrust/segmentationTreeThrust Starting...

GPU Device 0: "Turing" with compute capability 7.5

* Building segmentation tree... done in 62.8379 (ms)
* Dumping levels for each tree...

Starting shfl_scan
GPU Device 0: "Turing" with compute capability 7.5

> Detected Compute SM 7.5 hardware with 20 multi-processors
Starting shfl_scan
GPU Device 0: "Turing" with compute capability 7.5

> Detected Compute SM 7.5 hardware with 20 multi-processors
Computing Simple Sum test
---------------------------------------------------
Initialize test data [1, 1, 1...]
Scan summation for 65536 elements, 256 partial sums
Partial summing 256 elements with 1 blocks of size 256
Test Sum: 65536
Time (ms): 0.028896
65536 elements scanned in 0.028896 ms -> 2267.995605 MegaElements/s
CPU verify result diff (GPUvsCPU) = 0
CPU sum (naive) took 0.025120 ms

Computing Integral Image Test on size 1920 x 1080 synthetic data
---------------------------------------------------
Method: Fast  Time (GPU Timer): 0.071680 ms Diff = 0
Method: Vertical Scan  Time (GPU Timer): 0.123712 ms 
CheckSum: 2073600, (expect 1920x1080=2073600)
starting hyperQ...
GPU Device 0: "Turing" with compute capability 7.5

> Detected Compute SM 7.5 hardware with 20 multi-processors
Expected time for serial execution of 32 sets of kernels is between approx. 0.330s and 0.640s
Expected time for fully concurrent execution of 32 sets of kernels is approx. 0.020s
Measured time for sample = 0.058s
./6_Advanced/sortingNetworks/sortingNetworks Starting...

Starting up CUDA context...
GPU Device 0: "Turing" with compute capability 7.5

Allocating and initializing host arrays...

Allocating and initializing CUDA arrays...

Running GPU bitonic sort (1 identical iterations)...

Testing array length 64 (16384 arrays per batch)...
Average time: 0.398000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 128 (8192 arrays per batch)...
Average time: 0.562000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 256 (4096 arrays per batch)...
Average time: 0.606000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 512 (2048 arrays per batch)...
Average time: 0.727000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 1024 (1024 arrays per batch)...
Average time: 0.858000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 2048 (512 arrays per batch)...
Average time: 1.081000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 4096 (256 arrays per batch)...
Average time: 1.365000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 8192 (128 arrays per batch)...
Average time: 1.813000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 16384 (64 arrays per batch)...
Average time: 2.412000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 32768 (32 arrays per batch)...
Average time: 3.038000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 65536 (16 arrays per batch)...
Average time: 3.810000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 131072 (8 arrays per batch)...
Average time: 4.655000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 262144 (4 arrays per batch)...
Average time: 5.673000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 524288 (2 arrays per batch)...
Average time: 6.699000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 1048576 (1 arrays per batch)...
Average time: 7.850000 ms

sortingNetworks-bitonic, Throughput = 133.5766 MElements/s, Time = 0.00785 s, Size = 1048576 elements, NumDevsUsed = 1, Workgroup = 512

Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Shutting down...
threadFenceReduction Starting...

GPU Device 0: "Turing" with compute capability 7.5

GPU Device supports SM 7.5 compute capability

1048576 elements
128 threads (max)
64 blocks
Average time: 0.034030 ms
Bandwidth:    123.253151 GB/s

GPU result = 0.062298238277
CPU result = 0.062298242003
Starting threadMigration
[ threadMigration ] API test...
> 1 CUDA device(s), 2 Thread(s)/device to launched

Device 0: "GeForce GTX 1650 SUPER" (Compute 7.5)
	sharedMemPerBlock: 49152
	constantMemory   : 65536
	regsPerBlock     : 65536
	clockRate        : 1755000

> findModulePath found file at <./6_Advanced/threadMigration/data/threadMigration_kernel64.fatbin>
> initCUDA loading module: <./6_Advanced/threadMigration/data/threadMigration_kernel64.fatbin>
<CUDA Device=0, Context=0x5593a7408040, Thread=0> - ThreadProc() Launched...
<CUDA Device=0, Context=0x5593a7408040, Thread=1> - ThreadProc() Launched...
<CUDA Device=0, Context=0x5593a7408040, Thread=1> - ThreadProc() Finished!

<CUDA Device=0, Context=0x5593a7408040, Thread=0> - ThreadProc() Finished!

Transpose Starting...

GPU Device 0: "Turing" with compute capability 7.5

> Device 0: "GeForce GTX 1650 SUPER"
> SM Capability 7.5 detected:
> [GeForce GTX 1650 SUPER] has 20 MP(s) x 64 (Cores/MP) = 1280 (Cores)
> Compute performance scaling factor = 1.00

Matrix size: 1024x1024 (64x64 tiles), tile size: 16x16, block size: 16x16

transpose simple copy       , Throughput = 146.9089 GB/s, Time = 0.05318 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose shared memory copy, Throughput = 147.2279 GB/s, Time = 0.05306 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose naive             , Throughput = 117.1236 GB/s, Time = 0.06670 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose coalesced         , Throughput = 138.1019 GB/s, Time = 0.05657 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose optimized         , Throughput = 147.8905 GB/s, Time = 0.05283 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose coarse-grained    , Throughput = 145.6539 GB/s, Time = 0.05364 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose fine-grained      , Throughput = 145.4863 GB/s, Time = 0.05370 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose diagonal          , Throughput = 122.3775 GB/s, Time = 0.06384 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
Test passed
GPU Device 0: "Turing" with compute capability 7.5

CPU max matches GPU max

Warp Aggregated Atomics PASSED 
Monte Carlo Estimate Pi (with inline PRNG)
==========================================

Estimating Pi on GPU (GeForce GTX 1650 SUPER)

Precision:      single
Number of sims: 100000
Tolerance:      1.000000e-02
GPU result:     3.140440e+00
Expected:       3.141593e+00
Absolute error: 1.152754e-03
Relative error: 3.669329e-04

MonteCarloEstimatePiInlineP, Performance = 1605187.97 sims/s, Time = 62.30(ms), NumDevsUsed = 1, Blocksize = 128
Monte Carlo Estimate Pi (with inline QRNG)
==========================================

Estimating Pi on GPU (GeForce GTX 1650 SUPER)

Precision:      single
Number of sims: 100000
Tolerance:      1.000000e-02
GPU result:     3.142520e+00
Expected:       3.141593e+00
Absolute error: 9.272099e-04
Relative error: 2.951401e-04

MonteCarloEstimatePiInlineQ, Performance = 1005904.66 sims/s, Time = 99.41(ms), NumDevsUsed = 1, Blocksize = 128
Monte Carlo Estimate Pi (with batch PRNG)
=========================================

Estimating Pi on GPU (GeForce GTX 1650 SUPER)

Precision:      single
Number of sims: 100000
Tolerance:      1.000000e-02
GPU result:     3.136320e+00
Expected:       3.141593e+00
Absolute error: 5.272627e-03
Relative error: 1.678329e-03

MonteCarloEstimatePiP, Performance = 619920.52 sims/s, Time = 161.31(ms), NumDevsUsed = 1, Blocksize = 128
Monte Carlo Estimate Pi (with batch QRNG)
=========================================

Estimating Pi on GPU (GeForce GTX 1650 SUPER)

Precision:      single
Number of sims: 100000
Tolerance:      1.000000e-02
GPU result:     3.141840e+00
Expected:       3.141593e+00
Absolute error: 2.472401e-04
Relative error: 7.869895e-05

MonteCarloEstimatePiQ, Performance = 1349728.06 sims/s, Time = 74.09(ms), NumDevsUsed = 1, Blocksize = 128
Monte Carlo Single Asian Option (with PRNG)
===========================================

Pricing option on GPU (GeForce GTX 1650 SUPER)

Precision:      single
Number of sims: 100000

   Spot    |   Strike   |     r      |   sigma    |   tenor    |  Call/Put  |   Value    |  Expected  |
-----------|------------|------------|------------|------------|------------|------------|------------|
        40 |         35 |       0.03 |        0.2 |   0.333333 |       Call |    5.17636 |    5.16253 |

MonteCarloSingleAsianOptionP, Performance = 1504981.51 sims/s, Time = 66.45(ms), NumDevsUsed = 1, Blocksize = 128
./7_CUDALibraries/MersenneTwisterGP11213/MersenneTwisterGP11213 Starting...

GPU Device 0: "Turing" with compute capability 7.5

Allocating data for 2400000 samples...
Seeding with 777 ...
Generating random numbers on GPU...


Reading back the results...
Generating random numbers on CPU...

Comparing CPU/GPU random numbers...

Max absolute error: 0.000000E+00
L1 norm: 0.000000E+00

MersenneTwisterGP11213, Throughput = 17.4165 GNumbers/s, Time = 0.00014 s, Size = 2400000 Numbers
Shutting down...
batchCUBLAS Starting...

GPU Device 0: "Turing" with compute capability 7.5


 ==== Running single kernels ==== 

Testing sgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0xbf800000, -1) beta= (0x40000000, 2)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00028491 sec  GFLOPS=14.7215
@@@@ sgemm test OK
Testing dgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0x0000000000000000, 0) beta= (0x0000000000000000, 0)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00003791 sec  GFLOPS=110.643
@@@@ dgemm test OK

 ==== Running N=10 without streams ==== 

Testing sgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0xbf800000, -1) beta= (0x00000000, 0)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00011086 sec  GFLOPS=378.327
@@@@ sgemm test OK
Testing dgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0xbff0000000000000, -1) beta= (0x0000000000000000, 0)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00219607 sec  GFLOPS=19.0991
@@@@ dgemm test OK

 ==== Running N=10 with streams ==== 

Testing sgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0x40000000, 2) beta= (0x40000000, 2)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00011396 sec  GFLOPS=368.037
@@@@ sgemm test OK
Testing dgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0xbff0000000000000, -1) beta= (0x0000000000000000, 0)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00041199 sec  GFLOPS=101.807
@@@@ dgemm test OK

 ==== Running N=10 batched ==== 

Testing sgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0x3f800000, 1) beta= (0xbf800000, -1)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00005984 sec  GFLOPS=700.884
@@@@ sgemm test OK
Testing dgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0xbff0000000000000, -1) beta= (0x4000000000000000, 2)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00039792 sec  GFLOPS=105.406
@@@@ dgemm test OK

Test Summary
0 error(s)
NPP Library Version 11.3.2
CUDA Driver  Version: 11.2
CUDA Runtime Version: 11.2

Input file load succeeded.
Lena_CompressedMarkerLabelsUF_8Way_512x512_32u succeeded, compressed label count is 553.
Input file load succeeded.
CT_Skull_CompressedMarkerLabelsUF_8Way_512x512_32u succeeded, compressed label count is 413.
Input file load succeeded.
PCB_METAL_CompressedMarkerLabelsUF_8Way_509x335_32u succeeded, compressed label count is 3731.
Input file load succeeded.
PCB2_CompressedMarkerLabelsUF_8Way_1024x683_32u succeeded, compressed label count is 1223.
Input file load succeeded.
PCB_CompressedMarkerLabelsUF_8Way_1280x720_32u succeeded, compressed label count is 1440.


Lena_CompressedMarkerLabelsUFBatch_8Way_512x512_32u succeeded, compressed label count is 553.
CT_Skull_CompressedMarkerLabelsUFBatch_8Way_512x512_32u succeeded, compressed label count is 416.
PCB_METAL_CompressedMarkerLabelsUFBatch_8Way_509x335_32u succeeded, compressed label count is 3731.
PCB2_CompressedMarkerLabelsUFBatch_8Way_1024x683_32u succeeded, compressed label count is 1222.
PCB_CompressedMarkerLabelsUFBatch_8Way_1280x720_32u succeeded, compressed label count is 1442.
GPU Device 0: "Turing" with compute capability 7.5

> GPU device has 20 Multi-Processors, SM 7.5 compute capabilities

iteration =   1, residual = 4.449882e+01
iteration =   2, residual = 3.245218e+00
iteration =   3, residual = 2.690220e-01
iteration =   4, residual = 2.307639e-02
iteration =   5, residual = 1.993140e-03
iteration =   6, residual = 1.846192e-04
iteration =   7, residual = 1.693378e-05
iteration =   8, residual = 1.600114e-06
Test Summary:  Error amount = 0.000000
GPU Device 0: "Turing" with compute capability 7.5

> GPU device has 20 Multi-Processors, SM 7.5 compute capabilities

iteration =   1, residual = 4.449882e+01
iteration =   2, residual = 3.245218e+00
iteration =   3, residual = 2.690220e-01
iteration =   4, residual = 2.307639e-02
iteration =   5, residual = 1.993140e-03
iteration =   6, residual = 1.846192e-04
iteration =   7, residual = 1.693378e-05
iteration =   8, residual = 1.600114e-06
Test Summary:  Error amount = 0.000000
conjugateGradientPrecond starting...
GPU Device 0: "Turing" with compute capability 7.5

GPU selected Device ID = 0 
> GPU device has 20 Multi-Processors, SM 7.5 compute capabilities

laplace dimension = 128
Convergence of CG without preconditioning: 
  iteration = 564, residual = 9.174634e-13 
  Convergence Test: OK 

Convergence of CG using ILU(0) preconditioning: 
  iteration = 188, residual = 9.079595e-13 
  Convergence Test: OK 

Test Summary:
   Counted total of 0 errors
   qaerr1 = 0.000005 qaerr2 = 0.000003

Starting [conjugateGradientUM]...
GPU Device 0: "Turing" with compute capability 7.5

> GPU device has 20 Multi-Processors, SM 7.5 compute capabilities

iteration =   1, residual = 4.449882e+01
iteration =   2, residual = 3.245218e+00
iteration =   3, residual = 2.690220e-01
iteration =   4, residual = 2.307639e-02
iteration =   5, residual = 1.993140e-03
iteration =   6, residual = 1.846192e-04
iteration =   7, residual = 1.693378e-05
iteration =   8, residual = 1.600114e-06
Final residual: 1.600114e-06
&&&& conjugateGradientUM PASSED
Test Summary:  Error amount = 0.000000, result = SUCCESS
Error: Condition (allocation_cb == 1) failed at cuHook.cpp:115
cuHook sample failed (Didn't receive the allocation callback)
/tmp/e: line 132:  6027 Segmentation fault      ./7_CUDALibraries/cuHook/libcuhook.so.1
GPU Device 0: "Turing" with compute capability 7.5

step 1: read matrix market format
Using default input file [./7_CUDALibraries/cuSolverDn_LinearSolver/gr_900_900_crg.mtx]
sparse matrix A is 900 x 900 with 7744 nonzeros, base=1
step 2: convert CSR(A) to dense matrix
step 3: set right hand side vector (b) to 1
step 4: prepare data on device
step 5: solve A*x = b 
timing: cholesky =   0.011131 sec
step 6: evaluate residual
|b - A*x| = 1.136868E-13 
|A| = 1.600000E+01 
|x| = 2.357708E+01 
|b - A*x|/(|A|*|x|) = 3.013701E-16 
step 1.1: preparation
step 1.1: read matrix market format
GPU Device 0: "Turing" with compute capability 7.5

Using default input file [./7_CUDALibraries/cuSolverRf/lap2D_5pt_n100.mtx]
WARNING: cusolverRf only works for base-0 
sparse matrix A is 10000 x 10000 with 49600 nonzeros, base=0
step 1.2: set right hand side vector (b) to 1
step 2: reorder the matrix to reduce zero fill-in
        Q = symrcm(A) or Q = symamd(A) 
step 3: B = Q*A*Q^T
step 4: solve A*x = b by LU(B) in cusolverSp
step 4.1: create opaque info structure
step 4.2: analyze LU(B) to know structure of Q and R, and upper bound for nnz(L+U)
step 4.3: workspace for LU(B)
step 4.4: compute Ppivot*B = L*U 
step 4.5: check if the matrix is singular 
step 4.6: solve A*x = b 
    i.e.  solve B*(Qx) = Q*b 
step 4.7: evaluate residual r = b - A*x (result on CPU)
(CPU) |b - A*x| = 4.547474E-12 
(CPU) |A| = 8.000000E+00 
(CPU) |x| = 7.513384E+02 
(CPU) |b - A*x|/(|A|*|x|) = 7.565621E-16 
step 5: extract P, Q, L and U from P*B*Q^T = L*U 
        L has implicit unit diagonal
nnzL = 671550, nnzU = 681550
step 6: form P*A*Q^T = L*U
step 6.1: P = Plu*Qreroder
step 6.2: Q = Qlu*Qreorder 
step 7: create cusolverRf handle
step 8: set parameters for cusolverRf 
step 9: assemble P*A*Q = L*U 
step 10: analyze to extract parallelism 
step 11: import A to cusolverRf 
step 12: refactorization 
step 13: solve A*x = b 
step 14: evaluate residual r = b - A*x (result on GPU)
(GPU) |b - A*x| = 4.320100E-12 
(GPU) |A| = 8.000000E+00 
(GPU) |x| = 7.513384E+02 
(GPU) |b - A*x|/(|A|*|x|) = 7.187340E-16 
===== statistics 
 nnz(A) = 49600, nnz(L+U) = 1353100, zero fill-in ratio = 27.280242

===== timing profile 
 reorder A   : 0.004806 sec
 B = Q*A*Q^T : 0.000578 sec

 cusolverSp LU analysis: 0.000305 sec
 cusolverSp LU factor  : 0.078271 sec
 cusolverSp LU solve   : 0.002441 sec
 cusolverSp LU extract : 0.005801 sec

 cusolverRf assemble : 0.007928 sec
 cusolverRf reset    : 0.000132 sec
 cusolverRf refactor : 0.087486 sec
 cusolverRf solve    : 0.097410 sec
GPU Device 0: "Turing" with compute capability 7.5

Using default input file [./7_CUDALibraries/cuSolverSp_LinearSolver/lap2D_5pt_n100.mtx]
step 1: read matrix market format
sparse matrix A is 10000 x 10000 with 49600 nonzeros, base=1
step 2: reorder the matrix A to minimize zero fill-in
        if the user choose a reordering by -P=symrcm, -P=symamd or -P=metis
step 2.1: no reordering is chosen, Q = 0:n-1 
step 2.2: B = A(Q,Q) 
step 3: b(j) = 1 + j/n 
step 4: prepare data on device
step 5: solve A*x = b on CPU 
step 6: evaluate residual r = b - A*x (result on CPU)
(CPU) |b - A*x| = 5.393685E-12 
(CPU) |A| = 8.000000E+00 
(CPU) |x| = 1.136492E+03 
(CPU) |b| = 1.999900E+00 
(CPU) |b - A*x|/(|A|*|x| + |b|) = 5.931079E-16 
step 7: solve A*x = b on GPU
step 8: evaluate residual r = b - A*x (result on GPU)
(GPU) |b - A*x| = 1.970424E-12 
(GPU) |A| = 8.000000E+00 
(GPU) |x| = 1.136492E+03 
(GPU) |b| = 1.999900E+00 
(GPU) |b - A*x|/(|A|*|x| + |b|) = 2.166745E-16 
timing chol: CPU =   0.111665 sec , GPU =   0.104070 sec
show last 10 elements of solution vector (GPU) 
consistent result for different reordering and solver 
x[9990] = 3.000016E+01
x[9991] = 2.807343E+01
x[9992] = 2.601354E+01
x[9993] = 2.380285E+01
x[9994] = 2.141866E+01
x[9995] = 1.883070E+01
x[9996] = 1.599668E+01
x[9997] = 1.285365E+01
x[9998] = 9.299423E+00
x[9999] = 5.147265E+00
GPU Device 0: "Turing" with compute capability 7.5

Using default input file [./7_CUDALibraries/cuSolverSp_LowlevelCholesky/lap2D_5pt_n100.mtx]
step 1: read matrix market format
sparse matrix A is 10000 x 10000 with 49600 nonzeros, base=1
step 2: create opaque info structure
step 3: analyze chol(A) to know structure of L
step 4: workspace for chol(A)
step 5: compute A = L*L^T 
step 6: check if the matrix is singular 
step 7: solve A*x = b 
step 8: evaluate residual r = b - A*x (result on CPU)
(CPU) |b - A*x| = 3.637979E-12 
(CPU) |A| = 8.000000E+00 
(CPU) |x| = 7.513384E+02 
(CPU) |b - A*x|/(|A|*|x|) = 6.052497E-16 
step 9: create opaque info structure
step 10: analyze chol(A) to know structure of L
step 11: workspace for chol(A)
step 12: compute A = L*L^T 
step 13: check if the matrix is singular 
step 14: solve A*x = b 
(GPU) |b - A*x| = 1.477929E-12 
(GPU) |b - A*x|/(|A|*|x|) = 2.458827E-16 
GPU Device 0: "Turing" with compute capability 7.5

Using default input file [./7_CUDALibraries/cuSolverSp_LowlevelQR/lap2D_5pt_n32.mtx]
step 1: read matrix market format
sparse matrix A is 1024 x 1024 with 3008 nonzeros, base=1
step 2: create opaque info structure
step 3: analyze qr(A) to know structure of L
step 4: workspace for qr(A)
step 5: compute A = L*L^T 
step 6: check if the matrix is singular 
step 7: solve A*x = b 
step 8: evaluate residual r = b - A*x (result on CPU)
(CPU) |b - A*x| = 5.329071E-15 
(CPU) |A| = 6.000000E+00 
(CPU) |x| = 5.000000E-01 
(CPU) |b - A*x|/(|A|*|x|) = 1.776357E-15 
step 9: create opaque info structure
step 10: analyze qr(A) to know structure of L
step 11: workspace for qr(A)
GPU buffer size = 336896 bytes
step 12: compute A = L*L^T 
step 13: check if the matrix is singular 
step 14: solve A*x = b 
(GPU) |b - A*x| = 4.218847E-15 
(GPU) |b - A*x|/(|A|*|x|) = 1.406282E-15 
GPU Device 0: "Turing" with compute capability 7.5

Using GPU 0 (GeForce GTX 1650 SUPER, 20 SMs, 1024 th/SM max, CC 7.5, ECC off)
Decoding images in directory: ./7_CUDALibraries/nvJPEG/images/, total 8, batchsize 1
Processing: ./7_CUDALibraries/nvJPEG/images/img5.jpg
Image is 3 channels.
Channel #0 size: 640 x 480
Channel #1 size: 320 x 240
Channel #2 size: 320 x 240
YUV 4:2:0 chroma subsampling
Processing: ./7_CUDALibraries/nvJPEG/images/img6.jpg
Image is 3 channels.
Channel #0 size: 640 x 480
Channel #1 size: 320 x 240
Channel #2 size: 320 x 240
YUV 4:2:0 chroma subsampling
Processing: ./7_CUDALibraries/nvJPEG/images/img2.jpg
Image is 3 channels.
Channel #0 size: 480 x 640
Channel #1 size: 240 x 320
Channel #2 size: 240 x 320
YUV 4:2:0 chroma subsampling
Processing: ./7_CUDALibraries/nvJPEG/images/img7.jpg
Image is 3 channels.
Channel #0 size: 480 x 640
Channel #1 size: 240 x 320
Channel #2 size: 240 x 320
YUV 4:2:0 chroma subsampling
Processing: ./7_CUDALibraries/nvJPEG/images/img8.jpg
Image is 3 channels.
Channel #0 size: 480 x 640
Channel #1 size: 240 x 320
Channel #2 size: 240 x 320
YUV 4:2:0 chroma subsampling
Processing: ./7_CUDALibraries/nvJPEG/images/img1.jpg
Image is 3 channels.
Channel #0 size: 480 x 640
Channel #1 size: 240 x 320
Channel #2 size: 240 x 320
YUV 4:2:0 chroma subsampling
Processing: ./7_CUDALibraries/nvJPEG/images/img3.jpg
Image is 3 channels.
Channel #0 size: 640 x 426
Channel #1 size: 320 x 213
Channel #2 size: 320 x 213
YUV 4:2:0 chroma subsampling
Processing: ./7_CUDALibraries/nvJPEG/images/img4.jpg
Image is 3 channels.
Channel #0 size: 640 x 426
Channel #1 size: 320 x 213
Channel #2 size: 320 x 213
YUV 4:2:0 chroma subsampling
Total decoding time: 28.2903
Avg decoding time per image: 3.53629
Avg images per sec: 0.282782
Avg decoding time per batch: 3.53629
GPU Device 0: "Turing" with compute capability 7.5

Using GPU 0 (GeForce GTX 1650 SUPER, 20 SMs, 1024 th/SM max, CC 7.5, ECC off)
Processing file: ./7_CUDALibraries/nvJPEG_encoder/images/img5.jpg
Image is 3 channels.
Channel #0 size: 640 x 480
Channel #1 size: 320 x 240
Channel #2 size: 320 x 240
YUV 4:2:0 chroma subsampling
Writing JPEG file: encode_output/img5.jpg
Processing file: ./7_CUDALibraries/nvJPEG_encoder/images/img6.jpg
Image is 3 channels.
Channel #0 size: 640 x 480
Channel #1 size: 320 x 240
Channel #2 size: 320 x 240
YUV 4:2:0 chroma subsampling
Writing JPEG file: encode_output/img6.jpg
Processing file: ./7_CUDALibraries/nvJPEG_encoder/images/img2.jpg
Image is 3 channels.
Channel #0 size: 480 x 640
Channel #1 size: 240 x 320
Channel #2 size: 240 x 320
YUV 4:2:0 chroma subsampling
Writing JPEG file: encode_output/img2.jpg
Processing file: ./7_CUDALibraries/nvJPEG_encoder/images/img7.jpg
Image is 3 channels.
Channel #0 size: 480 x 640
Channel #1 size: 240 x 320
Channel #2 size: 240 x 320
YUV 4:2:0 chroma subsampling
Writing JPEG file: encode_output/img7.jpg
Processing file: ./7_CUDALibraries/nvJPEG_encoder/images/img8.jpg
Image is 3 channels.
Channel #0 size: 480 x 640
Channel #1 size: 240 x 320
Channel #2 size: 240 x 320
YUV 4:2:0 chroma subsampling
Writing JPEG file: encode_output/img8.jpg
Processing file: ./7_CUDALibraries/nvJPEG_encoder/images/img1.jpg
Image is 3 channels.
Channel #0 size: 480 x 640
Channel #1 size: 240 x 320
Channel #2 size: 240 x 320
YUV 4:2:0 chroma subsampling
Writing JPEG file: encode_output/img1.jpg
Processing file: ./7_CUDALibraries/nvJPEG_encoder/images/img3.jpg
Image is 3 channels.
Channel #0 size: 640 x 426
Channel #1 size: 320 x 213
Channel #2 size: 320 x 213
YUV 4:2:0 chroma subsampling
Writing JPEG file: encode_output/img3.jpg
Processing file: ./7_CUDALibraries/nvJPEG_encoder/images/img4.jpg
Image is 3 channels.
Channel #0 size: 640 x 426
Channel #1 size: 320 x 213
Channel #2 size: 320 x 213
YUV 4:2:0 chroma subsampling
Writing JPEG file: encode_output/img4.jpg
Total images processed: 8
Total time spent on encoding: 3.26653
Avg time/image: 0.408316
GPU Device 0: "Turing" with compute capability 7.5

simpleCUBLAS test running..
simpleCUBLAS test passed.
Using 1 GPUs
GPU ID = 0, Name = GeForce GTX 1650 SUPER 
simpleCUBLASXT test running..
simpleCUBLASXT test passed.
[simpleCUFFT] is starting...
GPU Device 0: "Turing" with compute capability 7.5

Temporary buffer size 448 bytes
Transforming signal cufftExecC2C
Launching ComplexPointwiseMulAndScale<<< >>>
Transforming signal back cufftExecC2C

Poisson equation using CUFFT library on Multiple GPUs is starting...

No. of GPU on node 1
Two GPUs are required to run simpleCUFFT_2d_MGPU sample code

[simpleCUFFT_MGPU] is starting...

No. of GPU on node 1
Two GPUs are required to run simpleCUFFT_MGPU sample code
[simpleCUFFT_callback] is starting...
GPU Device 0: "Turing" with compute capability 7.5

Transforming signal cufftExecC2C
Transforming signal back cufftExecC2C
NPP Library Version 11.3.2
CUDA Driver  Version: 11.2
CUDA Runtime Version: 11.2

Input file load succeeded.
Lena_Segments_8Way_512x512_8u succeeded.
Lena_CompressedSegmentLabels_8Way_512x512_32u succeeded.
Lena_SegmentBoundaries_8Way_512x512_8u succeeded.
Lena_SegmentsWithContrastingBoundaries_8Way_512x512_8u succeeded.
Input file load succeeded.
CT_Skull_Segments_8Way_512x512_8u succeeded.
CT_Skull_CompressedSegmentLabels_8Way_512x512_32u succeeded.
CT_Skull_SegmentBoundaries_8Way_512x512_8u succeeded.
CT_Skull_SegmentsWithContrastingBoundaries_8Way_512x512_8u succeeded.
Input file load succeeded.
Rocks_Segments_8Way_512x512_8u succeeded.
Rocks_CompressedSegmentLabels_8Way_512x512_32u succeeded.
Rocks_SegmentBoundaries_8Way_512x512_8u succeeded.
Rocks_SegmentsWithContrastingBoundaries_8Way_512x512_8u succeeded.
[./bin/x86_64/linux/release/BlackScholes] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

Initializing data...
...allocating CPU memory for options.
...allocating GPU memory for options.
...generating input data in CPU mem.
...copying input data to GPU mem.
Data init done.

Executing Black-Scholes GPU kernel (512 iterations)...
Options count             : 8000000     
BlackScholesGPU() time    : 0.490791 msec
Effective memory bandwidth: 163.002166 GB/s
Gigaoptions per second    : 16.300217     

BlackScholes, Throughput = 16.3002 GOptions/s, Time = 0.00049 s, Size = 8000000 options, NumDevsUsed = 1, Workgroup = 128

Reading back GPU results...
Checking the results...
...running CPU calculations.

Comparing the results...
L1 norm: 1.741792E-07
Max absolute error: 1.192093E-05

Shutting down...
...releasing GPU memory.
...releasing CPU memory.
Shutdown done.

[BlackScholes] - Test Summary

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.

Test passed
[./bin/x86_64/linux/release/BlackScholes_nvrtc] - Starting...
Initializing data...
...allocating CPU memory for options.

error: unable to open ./bin/x86_64/linux/release/FDTD3d Starting...

Set-up, based upon target device GMEM size...
 getTargetDeviceGlobalMemSize
 cudaGetDeviceCount
GPU Device 0: "Turing" with compute capability 7.5

 cudaGetDeviceProperties
 generateRandomData

FDTD on 376 x 376 x 376 volume with symmetric filter radius 4 for 5 timesteps...

fdtdReference...
 calloc intermediate
 Host FDTD loop
	t = 0
	t = 1
	t = 2
	t = 3
	t = 4

fdtdReference complete
fdtdGPU...
GPU Device 0: "Turing" with compute capability 7.5

 set block size to 32x16
 set grid size to 12x24
 GPU FDTD loop
	t = 0 launch kernel
	t = 1 launch kernel
	t = 2 launch kernel
	t = 3 launch kernel
	t = 4 launch kernel

fdtdGPU complete

CompareData (tolerance 0.000100)...
HSOpticalFlow Starting...

GPU Device 0: "Turing" with compute capability 7.5

Loading "frame10.ppm" ...
Loading "frame11.ppm" ...
Computing optical flow on CPU...
Computing optical flow on GPU...
L1 error : 0.044308
Monte Carlo Estimate Pi (with inline PRNG)
==========================================

Estimating Pi on GPU (GeForce GTX 1650 SUPER)

Precision:      single
Number of sims: 100000
Tolerance:      1.000000e-02
GPU result:     3.140440e+00
Expected:       3.141593e+00
Absolute error: 1.152754e-03
Relative error: 3.669329e-04

MonteCarloEstimatePiInlineP, Performance = 1408668.99 sims/s, Time = 70.99(ms), NumDevsUsed = 1, Blocksize = 128
Monte Carlo Estimate Pi (with inline QRNG)
==========================================

Estimating Pi on GPU (GeForce GTX 1650 SUPER)

Precision:      single
Number of sims: 100000
Tolerance:      1.000000e-02
GPU result:     3.142520e+00
Expected:       3.141593e+00
Absolute error: 9.272099e-04
Relative error: 2.951401e-04

MonteCarloEstimatePiInlineQ, Performance = 1478830.54 sims/s, Time = 67.62(ms), NumDevsUsed = 1, Blocksize = 128
Monte Carlo Estimate Pi (with batch PRNG)
=========================================

Estimating Pi on GPU (GeForce GTX 1650 SUPER)

Precision:      single
Number of sims: 100000
Tolerance:      1.000000e-02
GPU result:     3.136320e+00
Expected:       3.141593e+00
Absolute error: 5.272627e-03
Relative error: 1.678329e-03

MonteCarloEstimatePiP, Performance = 1376538.15 sims/s, Time = 72.65(ms), NumDevsUsed = 1, Blocksize = 128
Monte Carlo Estimate Pi (with batch QRNG)
=========================================

Estimating Pi on GPU (GeForce GTX 1650 SUPER)

Precision:      single
Number of sims: 100000
Tolerance:      1.000000e-02
GPU result:     3.141840e+00
Expected:       3.141593e+00
Absolute error: 2.472401e-04
Relative error: 7.869895e-05

MonteCarloEstimatePiQ, Performance = 1430226.45 sims/s, Time = 69.92(ms), NumDevsUsed = 1, Blocksize = 128
Monte Carlo Single Asian Option (with PRNG)
===========================================

Pricing option on GPU (GeForce GTX 1650 SUPER)

Precision:      single
Number of sims: 100000

   Spot    |   Strike   |     r      |   sigma    |   tenor    |  Call/Put  |   Value    |  Expected  |
-----------|------------|------------|------------|------------|------------|------------|------------|
        40 |         35 |       0.03 |        0.2 |   0.333333 |       Call |    5.17636 |    5.16253 |

MonteCarloSingleAsianOptionP, Performance = 1385962.90 sims/s, Time = 72.15(ms), NumDevsUsed = 1, Blocksize = 128
./bin/x86_64/linux/release/MersenneTwisterGP11213 Starting...

GPU Device 0: "Turing" with compute capability 7.5

Allocating data for 2400000 samples...
Seeding with 777 ...
Generating random numbers on GPU...


Reading back the results...
Generating random numbers on CPU...

Comparing CPU/GPU random numbers...

Max absolute error: 0.000000E+00
L1 norm: 0.000000E+00

MersenneTwisterGP11213, Throughput = 21.4861 GNumbers/s, Time = 0.00011 s, Size = 2400000 Numbers
Shutting down...
./bin/x86_64/linux/release/MonteCarloMultiGPU Starting...

Using single CPU thread for multiple GPUs
MonteCarloMultiGPU
==================
Parallelization method  = streamed
Problem scaling         = weak
Number of GPUs          = 1
Total number of options = 8192
Number of paths         = 262144
main(): generating input data...
main(): starting 1 host threads...
main(): GPU statistics, streamed
GPU Device #0: GeForce GTX 1650 SUPER
Options         : 8192
Simulation paths: 262144

Total time (ms.): 26.843000
	Note: This is elapsed time for all to compute.
Options per sec.: 305181.979446
main(): comparing Monte Carlo and Black-Scholes results...
Shutting down...
Test Summary...
L1 norm        : 4.825154E-04
Average reserve: 11.717557

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.

Test passed
GPU Device 0: "Turing" with compute capability 7.5


TEST#1:
  CUDA resize nv12(1920x1080 --> 640x480), batch: 24, average time: 0.295 ms ==> 0.012 ms/frame
  CUDA convert nv12(640x480) to bgr(640x480), batch: 24, average time: 0.690 ms ==> 0.029 ms/frame

TEST#2:
  CUDA convert nv12(1920x1080) to bgr(1920x1080), batch: 24, average time: 4.707 ms ==> 0.196 ms/frame
  CUDA resize bgr(1920x1080 --> 640x480), batch: 24, average time: 3.385 ms ==> 0.141 ms/frame
Sobol Quasi-Random Number Generator Starting...

> number of vectors = 100000
> number of dimensions = 100
GPU Device 0: "Turing" with compute capability 7.5

Allocating CPU memory...
Allocating GPU memory...
Initializing direction numbers...
Copying direction numbers to device...
Executing QRNG on GPU...
Gsamples/s: 20.6612
Reading results from GPU...

Executing QRNG on CPU...
Gsamples/s: 0.250175
Checking results...
L1-Error: 0
Shutting down...
Starting [./bin/x86_64/linux/release/StreamPriorities]...
GPU Device 0: "Turing" with compute capability 7.5

CUDA stream priority range: LOW: 0 to HIGH: -2
elapsed time of kernels launched to LOW priority stream: 7.064 ms
elapsed time of kernels launched to HI  priority stream: 3.735 ms
GPU Device 0: "Turing" with compute capability 7.5

Running ........................................................

Overall Time For matrixMultiplyPerf 

Printing Average of 20 measurements in (ms)
Size_KB	 UMhint	UMhntAs	 UMeasy	  0Copy	MemCopy	CpAsync	CpHpglk	CpPglAs
4	  0.233	  0.224	  0.304	  0.013	  0.026	  0.022	  0.030	  0.029
16	  0.255	  0.260	  0.422	  0.029	  0.045	  0.038	  0.048	  0.090
64	  0.369	  0.316	  0.736	  0.090	  0.112	  0.102	  0.101	  0.098
256	  0.812	  0.768	  1.112	  0.440	  0.390	  0.397	  0.345	  0.336
1024	  2.340	  2.329	  2.859	  2.544	  1.771	  1.700	  1.447	  1.456
4096	  9.745	  9.382	 12.369	 17.891	  8.685	  8.566	  7.675	  7.644
16384	 49.078	 47.157	 61.577	131.331	 46.824	 46.890	 43.573	 43.443

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
GPU Device 0: "Turing" with compute capability 7.5

Executing tasks on host / device
Task [0], thread [0] executing on device (387)
Task [2], thread [1] executing on device (874)
Task [1], thread [2] executing on device (951)
Task [3], thread [3] executing on device (331)
Task [4], thread [2] executing on device (567)
Task [5], thread [3] executing on device (274)
Task [6], thread [0] executing on device (931)
Task [7], thread [1] executing on device (970)
Task [8], thread [0] executing on device (814)
Task [9], thread [1] executing on device (577)
Task [10], thread [2] executing on device (372)
Task [11], thread [1] executing on device (638)
Task [12], thread [3] executing on device (521)
Task [13], thread [0] executing on device (722)
Task [14], thread [2] executing on device (196)
Task [15], thread [3] executing on device (993)
Task [16], thread [1] executing on device (242)
Task [17], thread [0] executing on device (938)
Task [18], thread [2] executing on device (399)
Task [19], thread [0] executing on device (596)
Task [20], thread [3] executing on device (107)
Task [21], thread [1] executing on host (70)
Task [22], thread [2] executing on device (533)
Task [23], thread [0] executing on host (64)
Task [24], thread [1] executing on device (278)
Task [25], thread [3] executing on device (220)
Task [26], thread [0] executing on device (123)
Task [27], thread [2] executing on device (578)
Task [28], thread [0] executing on device (264)
Task [29], thread [1] executing on device (797)
Task [30], thread [3] executing on device (458)
Task [31], thread [2] executing on device (574)
Task [32], thread [1] executing on device (203)
Task [33], thread [0] executing on device (353)
Task [34], thread [3] executing on device (215)
Task [35], thread [1] executing on device (218)
Task [36], thread [0] executing on host (79)
Task [37], thread [3] executing on host (64)
Task [38], thread [2] executing on device (658)
Task [39], thread [0] executing on device (631)
All Done!
[./bin/x86_64/linux/release/alignedTypes] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

[GeForce GTX 1650 SUPER] has 20 MP(s) x 64 (Cores/MP) = 1280 (Cores)
> Compute scaling value = 1.00
> Memory Size = 49999872
Allocating memory...
Generating host input data array...
Uploading input data to GPU memory...
Testing misaligned types...
uint8...
Avg. time: 1.232875 ms / Copy throughput: 37.770261 GB/s.
	TEST OK
uint16...
Avg. time: 0.918156 ms / Copy throughput: 50.716867 GB/s.
	TEST OK
RGBA8_misaligned...
Avg. time: 0.781250 ms / Copy throughput: 59.604492 GB/s.
	TEST OK
LA32_misaligned...
Avg. time: 0.643906 ms / Copy throughput: 72.317997 GB/s.
	TEST OK
RGB32_misaligned...
Avg. time: 0.720500 ms / Copy throughput: 64.630132 GB/s.
	TEST OK
RGBA32_misaligned...
Avg. time: 0.666500 ms / Copy throughput: 69.866484 GB/s.
	TEST OK
Testing aligned types...
RGBA8...
Avg. time: 0.723437 ms / Copy throughput: 64.367703 GB/s.
	TEST OK
I32...
Avg. time: 0.706500 ms / Copy throughput: 65.910842 GB/s.
	TEST OK
LA32...
Avg. time: 0.627344 ms / Copy throughput: 74.227260 GB/s.
	TEST OK
RGB32...
Avg. time: 0.626437 ms / Copy throughput: 74.334647 GB/s.
	TEST OK
RGBA32...
Avg. time: 0.624875 ms / Copy throughput: 74.520518 GB/s.
	TEST OK
RGBA32_2...
Avg. time: 0.669969 ms / Copy throughput: 69.504751 GB/s.
	TEST OK

[alignedTypes] -> Test Results: 0 Failures
Shutting down...
Test passed
[./bin/x86_64/linux/release/asyncAPI] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER]
time spent executing by the GPU: 11.53
time spent by CPU in CUDA calls: 0.02
CPU executed 88744 iterations while waiting for GPU to finish
[CUDA Bandwidth Test] - Starting...
Running on...

 Device 0: GeForce GTX 1650 SUPER
 Quick Mode

 Host to Device Bandwidth, 1 Device(s)
 PINNED Memory Transfers
   Transfer Size (Bytes)	Bandwidth(GB/s)
   32000000			12.4

 Device to Host Bandwidth, 1 Device(s)
 PINNED Memory Transfers
   Transfer Size (Bytes)	Bandwidth(GB/s)
   32000000			12.7

 Device to Device Bandwidth, 1 Device(s)
 PINNED Memory Transfers
   Transfer Size (Bytes)	Bandwidth(GB/s)
   32000000			159.5

Result = PASS

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
batchCUBLAS Starting...

GPU Device 0: "Turing" with compute capability 7.5


 ==== Running single kernels ==== 

Testing sgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0xbf800000, -1) beta= (0x40000000, 2)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00028491 sec  GFLOPS=14.7215
@@@@ sgemm test OK
Testing dgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0x0000000000000000, 0) beta= (0x0000000000000000, 0)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00002694 sec  GFLOPS=155.683
@@@@ dgemm test OK

 ==== Running N=10 without streams ==== 

Testing sgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0xbf800000, -1) beta= (0x00000000, 0)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00010180 sec  GFLOPS=411.995
@@@@ sgemm test OK
Testing dgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0xbff0000000000000, -1) beta= (0x0000000000000000, 0)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00048900 sec  GFLOPS=85.7737
@@@@ dgemm test OK

 ==== Running N=10 with streams ==== 

Testing sgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0x40000000, 2) beta= (0x40000000, 2)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00010991 sec  GFLOPS=381.609
@@@@ sgemm test OK
Testing dgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0xbff0000000000000, -1) beta= (0x0000000000000000, 0)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00033283 sec  GFLOPS=126.019
@@@@ dgemm test OK

 ==== Running N=10 batched ==== 

Testing sgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0x3f800000, 1) beta= (0xbf800000, -1)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00005507 sec  GFLOPS=761.566
@@@@ sgemm test OK
Testing dgemm
#### args: ta=0 tb=0 m=128 n=128 k=128  alpha = (0xbff0000000000000, -1) beta= (0x4000000000000000, 2)
#### args: lda=128 ldb=128 ldc=128
^^^^ elapsed = 0.00031281 sec  GFLOPS=134.087
@@@@ dgemm test OK

Test Summary
0 error(s)
NPP Library Version 11.3.2
CUDA Driver  Version: 11.2
CUDA Runtime Version: 11.2

Input file load succeeded.
Lena_CompressedMarkerLabelsUF_8Way_512x512_32u succeeded, compressed label count is 554.
Input file load succeeded.
CT_Skull_CompressedMarkerLabelsUF_8Way_512x512_32u succeeded, compressed label count is 415.
Input file load succeeded.
PCB_METAL_CompressedMarkerLabelsUF_8Way_509x335_32u succeeded, compressed label count is 3731.
Input file load succeeded.
PCB2_CompressedMarkerLabelsUF_8Way_1024x683_32u succeeded, compressed label count is 1224.
Input file load succeeded.
PCB_CompressedMarkerLabelsUF_8Way_1280x720_32u succeeded, compressed label count is 1440.


Lena_CompressedMarkerLabelsUFBatch_8Way_512x512_32u succeeded, compressed label count is 553.
CT_Skull_CompressedMarkerLabelsUFBatch_8Way_512x512_32u succeeded, compressed label count is 416.
PCB_METAL_CompressedMarkerLabelsUFBatch_8Way_509x335_32u succeeded, compressed label count is 3731.
PCB2_CompressedMarkerLabelsUFBatch_8Way_1024x683_32u succeeded, compressed label count is 1224.
PCB_CompressedMarkerLabelsUFBatch_8Way_1280x720_32u succeeded, compressed label count is 1441.
Initializing...
GPU Device 0: "Turing" with compute capability 7.5

bf16TensorCoreGemm requires requires SM 8.0 or higher to use Tensor Cores.  Exiting...
GPU Device 0: "Turing" with compute capability 7.5


Launching 100 blocks with 1024 threads...

Array size = 102400 Num of Odds = 50945 Sum of Odds = 1272565 Sum of Evens 1233938

...Done.

[./bin/x86_64/linux/release/binomialOptions] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

Generating input data...
Running GPU binomial tree...
Options count            : 1024     
Time steps               : 2048     
binomialOptionsGPU() time: 3.124000 msec
Options per second       : 327784.883560     
Running CPU binomial tree...
Comparing the results...
GPU binomial vs. Black-Scholes
L1 norm: 2.220214E-04
CPU binomial vs. Black-Scholes
L1 norm: 2.220920E-04
CPU binomial vs. GPU binomial
L1 norm: 7.997008E-07
Shutting down...

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.

Test passed
[./bin/x86_64/linux/release/binomialOptions_nvrtc] - Starting...
Generating input data...
Running GPU binomial tree...

error: unable to open GPU Device 0: "Turing" with compute capability 7.5

Cannot find the input text file
. Exiting..
GPU Device 0: "Turing" with compute capability 7.5

GPU device GeForce GTX 1650 SUPER has compute capabilities (SM 7.5)
Running qsort on 5000 elements with seed 100, on GeForce GTX 1650 SUPER
    cdpAdvancedQuicksort PASSED
Sorted 5000 elems in 0.753 ms (6.637 Melems/sec)
Running on GPU 0 (GeForce GTX 1650 SUPER)
Computing Bezier Lines (CUDA Dynamic Parallelism Version) ... Done!
GPU Device 0: "Turing" with compute capability 7.5

GPU device GeForce GTX 1650 SUPER has compute capabilities (SM 7.5)
Launching CDP kernel to build the quadtree
Results: OK
starting Simple Print (CUDA Dynamic Parallelism)
GPU Device 0: "Turing" with compute capability 7.5

***************************************************************************
The CPU launches 2 blocks of 2 threads each. On the device each thread will
launch 2 blocks of 2 threads each. The GPU we will do that recursively
until it reaches max_depth=2

In total 2+8=10 blocks are launched!!! (8 from the GPU)
***************************************************************************

Launching cdp_kernel() with CUDA Dynamic Parallelism:

BLOCK 0 launched by the host
BLOCK 1 launched by the host
|  BLOCK 5 launched by thread 0 of block 1
|  BLOCK 3 launched by thread 0 of block 0
|  BLOCK 4 launched by thread 0 of block 1
|  BLOCK 2 launched by thread 0 of block 0
|  BLOCK 7 launched by thread 1 of block 0
|  BLOCK 6 launched by thread 1 of block 0
|  BLOCK 8 launched by thread 1 of block 1
|  BLOCK 9 launched by thread 1 of block 1
GPU Device 0: "Turing" with compute capability 7.5

Initializing data:
Running quicksort on 128 elements
Launching kernel on the GPU
Validating results: OK
CUDA Clock sample
GPU Device 0: "Turing" with compute capability 7.5

Average clocks/block = 2577.640625
CUDA Clock sample

error: unable to open [./bin/x86_64/linux/release/concurrentKernels] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

> Detected Compute SM 7.5 hardware with 20 multi-processors
Expected time for serial execution of 8 kernels = 0.080s
Expected time for concurrent execution of 8 kernels = 0.010s
Measured time for sample = 0.012s
Test passed
GPU Device 0: "Turing" with compute capability 7.5

> GPU device has 20 Multi-Processors, SM 7.5 compute capabilities

iteration =   1, residual = 4.449882e+01
iteration =   2, residual = 3.245218e+00
iteration =   3, residual = 2.690220e-01
iteration =   4, residual = 2.307639e-02
iteration =   5, residual = 1.993140e-03
iteration =   6, residual = 1.846192e-04
iteration =   7, residual = 1.693378e-05
iteration =   8, residual = 1.600114e-06
Test Summary:  Error amount = 0.000000
GPU Device 0: "Turing" with compute capability 7.5

> GPU device has 20 Multi-Processors, SM 7.5 compute capabilities

iteration =   1, residual = 4.449882e+01
iteration =   2, residual = 3.245218e+00
iteration =   3, residual = 2.690220e-01
iteration =   4, residual = 2.307639e-02
iteration =   5, residual = 1.993140e-03
iteration =   6, residual = 1.846192e-04
iteration =   7, residual = 1.693378e-05
iteration =   8, residual = 1.600114e-06
Test Summary:  Error amount = 0.000000
Starting [conjugateGradientMultiBlockCG]...
GPU Device 0: "Turing" with compute capability 7.5

> GPU device has 20 Multi-Processors, SM 7.5 compute capabilities

GPU Final, residual = 1.600115e-06, kernel execution time = 13.633248 ms
Test Summary:  Error amount = 0.000000 
&&&& conjugateGradientMultiBlockCG PASSED
Starting [conjugateGradientMultiDeviceCG]...
GPU Device 0: "GeForce GTX 1650 SUPER" with compute capability 7.5
No Two or more GPUs with same architecture capable of cooperativeMultiDeviceLaunch & concurrentManagedAccess found. 
Waiving the sample
conjugateGradientPrecond starting...
GPU Device 0: "Turing" with compute capability 7.5

GPU selected Device ID = 0 
> GPU device has 20 Multi-Processors, SM 7.5 compute capabilities

laplace dimension = 128
Convergence of CG without preconditioning: 
  iteration = 564, residual = 9.174634e-13 
  Convergence Test: OK 

Convergence of CG using ILU(0) preconditioning: 
  iteration = 188, residual = 9.079595e-13 
  Convergence Test: OK 

Test Summary:
   Counted total of 0 errors
   qaerr1 = 0.000005 qaerr2 = 0.000003

Starting [conjugateGradientUM]...
GPU Device 0: "Turing" with compute capability 7.5

> GPU device has 20 Multi-Processors, SM 7.5 compute capabilities

iteration =   1, residual = 4.449882e+01
iteration =   2, residual = 3.245218e+00
iteration =   3, residual = 2.690220e-01
iteration =   4, residual = 2.307639e-02
iteration =   5, residual = 1.993140e-03
iteration =   6, residual = 1.846192e-04
iteration =   7, residual = 1.693378e-05
iteration =   8, residual = 1.600114e-06
Final residual: 1.600114e-06
&&&& conjugateGradientUM PASSED
Test Summary:  Error amount = 0.000000, result = SUCCESS
[./bin/x86_64/linux/release/convolutionFFT2D] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

Testing built-in R2C / C2R FFT-based convolution
...allocating memory
...generating random input data
...creating R2C & C2R FFT plans for 2048 x 2048
...uploading to GPU and padding convolution kernel and input data
...transforming convolution kernel
...running GPU FFT convolution: 2222.222281 MPix/s (1.800000 ms)
...reading back GPU convolution results
...running reference CPU convolution
...comparing the results: rel L2 = 8.680021E-08 (max delta = 8.227172E-07)
L2norm Error OK
...shutting down
Testing custom R2C / C2R FFT-based convolution
...allocating memory
...generating random input data
...creating C2C FFT plan for 2048 x 1024
...uploading to GPU and padding convolution kernel and input data
...transforming convolution kernel
...running GPU FFT convolution: 2186.987429 MPix/s (1.829000 ms)
...reading back GPU FFT results
...running reference CPU convolution
...comparing the results: rel L2 = 1.067915E-07 (max delta = 9.817303E-07)
L2norm Error OK
...shutting down
Testing updated custom R2C / C2R FFT-based convolution
...allocating memory
...generating random input data
...creating C2C FFT plan for 2048 x 1024
...uploading to GPU and padding convolution kernel and input data
...transforming convolution kernel
...running GPU FFT convolution: 3039.513713 MPix/s (1.316000 ms)
...reading back GPU FFT results
...running reference CPU convolution
...comparing the results: rel L2 = 1.065127E-07 (max delta = 9.817303E-07)
L2norm Error OK
...shutting down
Test Summary: 0 errors
Test passed
[./bin/x86_64/linux/release/convolutionSeparable] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

Image Width x Height = 3072 x 3072

Allocating and initializing host arrays...
Allocating and initializing CUDA arrays...
Running GPU convolution (16 identical iterations)...

convolutionSeparable, Throughput = 6946.1283 MPixels/sec, Time = 0.00136 s, Size = 9437184 Pixels, NumDevsUsed = 1, Workgroup = 0

Reading back GPU results...

Checking the results...
 ...running convolutionRowCPU()
 ...running convolutionColumnCPU()
 ...comparing the results
 ...Relative L2 norm: 0.000000E+00

Shutting down...
Test passed
[./bin/x86_64/linux/release/convolutionTexture] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

Initializing data...
Running GPU rows convolution (10 identical iterations)...
Average convolutionRowsGPU() time: 0.740700 msecs; //6370.449519 Mpix/s
Copying convolutionRowGPU() output back to the texture...
cudaMemcpyToArray() time: 0.252000 msecs; //18724.571127 Mpix/s
Running GPU columns convolution (10 iterations)
Average convolutionColumnsGPU() time: 0.714700 msecs; //6602.199676 Mpix/s
Reading back GPU results...
Checking the results...
...running convolutionRowsCPU()
...running convolutionColumnsCPU()
Relative L2 norm: 0.000000E+00
Shutting down...
Test passed
GPU Device 0: "Turing" with compute capability 7.5

Hello World.
Hello World.
C++ Function Overloading starting...
DevicecheckCudaErrors Count: 1
GPU Device 0: "Turing" with compute capability 7.5

Shared Size:   1024
Constant Size: 0
Local Size:    0
Max Threads Per Block: 1024
Number of Registers: 12
PTX Version: 75
Binary Version: 75
simple_kernel(const int *pIn, int *pOut, int a) PASSED

Shared Size:   2048
Constant Size: 0
Local Size:    0
Max Threads Per Block: 1024
Number of Registers: 12
PTX Version: 75
Binary Version: 75
simple_kernel(const int2 *pIn, int *pOut, int a) PASSED

Shared Size:   2048
Constant Size: 0
Local Size:    0
Max Threads Per Block: 1024
Number of Registers: 16
PTX Version: 75
Binary Version: 75
simple_kernel(const int *pIn1, const int *pIn2, int *pOut, int a) PASSED

Error: Condition (allocation_cb == 1) failed at cuHook.cpp:115
cuHook sample failed (Didn't receive the allocation callback)
GPU Device 0: "Turing" with compute capability 7.5

step 1: read matrix market format
Using default input file [./7_CUDALibraries/cuSolverDn_LinearSolver/gr_900_900_crg.mtx]
sparse matrix A is 900 x 900 with 7744 nonzeros, base=1
step 2: convert CSR(A) to dense matrix
step 3: set right hand side vector (b) to 1
step 4: prepare data on device
step 5: solve A*x = b 
timing: cholesky =   0.010326 sec
step 6: evaluate residual
|b - A*x| = 1.136868E-13 
|A| = 1.600000E+01 
|x| = 2.357708E+01 
|b - A*x|/(|A|*|x|) = 3.013701E-16 
step 1.1: preparation
step 1.1: read matrix market format
GPU Device 0: "Turing" with compute capability 7.5

Using default input file [./7_CUDALibraries/cuSolverRf/lap2D_5pt_n100.mtx]
WARNING: cusolverRf only works for base-0 
sparse matrix A is 10000 x 10000 with 49600 nonzeros, base=0
step 1.2: set right hand side vector (b) to 1
step 2: reorder the matrix to reduce zero fill-in
        Q = symrcm(A) or Q = symamd(A) 
step 3: B = Q*A*Q^T
step 4: solve A*x = b by LU(B) in cusolverSp
step 4.1: create opaque info structure
step 4.2: analyze LU(B) to know structure of Q and R, and upper bound for nnz(L+U)
step 4.3: workspace for LU(B)
step 4.4: compute Ppivot*B = L*U 
step 4.5: check if the matrix is singular 
step 4.6: solve A*x = b 
    i.e.  solve B*(Qx) = Q*b 
step 4.7: evaluate residual r = b - A*x (result on CPU)
(CPU) |b - A*x| = 4.547474E-12 
(CPU) |A| = 8.000000E+00 
(CPU) |x| = 7.513384E+02 
(CPU) |b - A*x|/(|A|*|x|) = 7.565621E-16 
step 5: extract P, Q, L and U from P*B*Q^T = L*U 
        L has implicit unit diagonal
nnzL = 671550, nnzU = 681550
step 6: form P*A*Q^T = L*U
step 6.1: P = Plu*Qreroder
step 6.2: Q = Qlu*Qreorder 
step 7: create cusolverRf handle
step 8: set parameters for cusolverRf 
step 9: assemble P*A*Q = L*U 
step 10: analyze to extract parallelism 
step 11: import A to cusolverRf 
step 12: refactorization 
step 13: solve A*x = b 
step 14: evaluate residual r = b - A*x (result on GPU)
(GPU) |b - A*x| = 4.320100E-12 
(GPU) |A| = 8.000000E+00 
(GPU) |x| = 7.513384E+02 
(GPU) |b - A*x|/(|A|*|x|) = 7.187340E-16 
===== statistics 
 nnz(A) = 49600, nnz(L+U) = 1353100, zero fill-in ratio = 27.280242

===== timing profile 
 reorder A   : 0.003133 sec
 B = Q*A*Q^T : 0.000575 sec

 cusolverSp LU analysis: 0.000234 sec
 cusolverSp LU factor  : 0.082342 sec
 cusolverSp LU solve   : 0.002517 sec
 cusolverSp LU extract : 0.006360 sec

 cusolverRf assemble : 0.007779 sec
 cusolverRf reset    : 0.000124 sec
 cusolverRf refactor : 0.087451 sec
 cusolverRf solve    : 0.095880 sec
GPU Device 0: "Turing" with compute capability 7.5

Using default input file [./7_CUDALibraries/cuSolverSp_LinearSolver/lap2D_5pt_n100.mtx]
step 1: read matrix market format
sparse matrix A is 10000 x 10000 with 49600 nonzeros, base=1
step 2: reorder the matrix A to minimize zero fill-in
        if the user choose a reordering by -P=symrcm, -P=symamd or -P=metis
step 2.1: no reordering is chosen, Q = 0:n-1 
step 2.2: B = A(Q,Q) 
step 3: b(j) = 1 + j/n 
step 4: prepare data on device
step 5: solve A*x = b on CPU 
step 6: evaluate residual r = b - A*x (result on CPU)
(CPU) |b - A*x| = 5.393685E-12 
(CPU) |A| = 8.000000E+00 
(CPU) |x| = 1.136492E+03 
(CPU) |b| = 1.999900E+00 
(CPU) |b - A*x|/(|A|*|x| + |b|) = 5.931079E-16 
step 7: solve A*x = b on GPU
step 8: evaluate residual r = b - A*x (result on GPU)
(GPU) |b - A*x| = 1.970424E-12 
(GPU) |A| = 8.000000E+00 
(GPU) |x| = 1.136492E+03 
(GPU) |b| = 1.999900E+00 
(GPU) |b - A*x|/(|A|*|x| + |b|) = 2.166745E-16 
timing chol: CPU =   0.111090 sec , GPU =   0.103482 sec
show last 10 elements of solution vector (GPU) 
consistent result for different reordering and solver 
x[9990] = 3.000016E+01
x[9991] = 2.807343E+01
x[9992] = 2.601354E+01
x[9993] = 2.380285E+01
x[9994] = 2.141866E+01
x[9995] = 1.883070E+01
x[9996] = 1.599668E+01
x[9997] = 1.285365E+01
x[9998] = 9.299423E+00
x[9999] = 5.147265E+00
GPU Device 0: "Turing" with compute capability 7.5

Using default input file [./7_CUDALibraries/cuSolverSp_LowlevelCholesky/lap2D_5pt_n100.mtx]
step 1: read matrix market format
sparse matrix A is 10000 x 10000 with 49600 nonzeros, base=1
step 2: create opaque info structure
step 3: analyze chol(A) to know structure of L
step 4: workspace for chol(A)
step 5: compute A = L*L^T 
step 6: check if the matrix is singular 
step 7: solve A*x = b 
step 8: evaluate residual r = b - A*x (result on CPU)
(CPU) |b - A*x| = 3.637979E-12 
(CPU) |A| = 8.000000E+00 
(CPU) |x| = 7.513384E+02 
(CPU) |b - A*x|/(|A|*|x|) = 6.052497E-16 
step 9: create opaque info structure
step 10: analyze chol(A) to know structure of L
step 11: workspace for chol(A)
step 12: compute A = L*L^T 
step 13: check if the matrix is singular 
step 14: solve A*x = b 
(GPU) |b - A*x| = 1.477929E-12 
(GPU) |b - A*x|/(|A|*|x|) = 2.458827E-16 
GPU Device 0: "Turing" with compute capability 7.5

Using default input file [./7_CUDALibraries/cuSolverSp_LowlevelQR/lap2D_5pt_n32.mtx]
step 1: read matrix market format
sparse matrix A is 1024 x 1024 with 3008 nonzeros, base=1
step 2: create opaque info structure
step 3: analyze qr(A) to know structure of L
step 4: workspace for qr(A)
step 5: compute A = L*L^T 
step 6: check if the matrix is singular 
step 7: solve A*x = b 
step 8: evaluate residual r = b - A*x (result on CPU)
(CPU) |b - A*x| = 5.329071E-15 
(CPU) |A| = 6.000000E+00 
(CPU) |x| = 5.000000E-01 
(CPU) |b - A*x|/(|A|*|x|) = 1.776357E-15 
step 9: create opaque info structure
step 10: analyze qr(A) to know structure of L
step 11: workspace for qr(A)
GPU buffer size = 336896 bytes
step 12: compute A = L*L^T 
step 13: check if the matrix is singular 
step 14: solve A*x = b 
(GPU) |b - A*x| = 4.218847E-15 
(GPU) |b - A*x|/(|A|*|x|) = 1.406282E-15 
GPU Device 0: "Turing" with compute capability 7.5

Device 0 doesn't support Generic memory compression, waiving the execution.
./bin/x86_64/linux/release/cudaOpenMP Starting...

number of host CPUs:	8
number of CUDA devices:	1
   0: GeForce GTX 1650 SUPER
---------------------------
CPU thread 0 (of 1) uses CUDA device 0
---------------------------
Initializing...
GPU Device 0: "Turing" with compute capability 7.5

M: 4096 (16 x 256)
N: 4096 (16 x 256)
K: 4096 (16 x 256)
Preparing data for GPU...
Required shared memory size: 64 Kb
Computing... using high performance kernel compute_gemm 
Time: 180.350204 ms
TFLOPS: 0.76
./bin/x86_64/linux/release/dct8x8 Starting...

GPU Device 0: "Turing" with compute capability 7.5

CUDA sample DCT/IDCT implementation
===================================
Loading test image: barbara.bmp... [512 x 512]... Success
Running Gold 1 (CPU) version... Success
Running Gold 2 (CPU) version... Success
Running CUDA 1 (GPU) version... Success
Running CUDA 2 (GPU) version... 17845.065116 MPix/s //0.014690 ms
Success
Running CUDA short (GPU) version... Success
Dumping result to barbara_gold1.bmp... Success
Dumping result to barbara_gold2.bmp... Success
Dumping result to barbara_cuda1.bmp... Success
Dumping result to barbara_cuda2.bmp... Success
Dumping result to barbara_cuda_short.bmp... Success
Processing time (CUDA 1)    : 0.058500 ms 
Processing time (CUDA 2)    : 0.014690 ms 
Processing time (CUDA short): 0.060000 ms 
PSNR Original    <---> CPU(Gold 1)    : 32.777073
PSNR Original    <---> CPU(Gold 2)    : 32.777046
PSNR Original    <---> GPU(CUDA 1)    : 32.777092
PSNR Original    <---> GPU(CUDA 2)    : 32.777077
PSNR Original    <---> GPU(CUDA short): 32.749447
PSNR CPU(Gold 1) <---> GPU(CUDA 1)    : 64.019310
PSNR CPU(Gold 2) <---> GPU(CUDA 2)    : 71.777740
PSNR CPU(Gold 2) <---> GPU(CUDA short): 42.258053

Test Summary...
Test passed
./bin/x86_64/linux/release/deviceQuery Starting...

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
./bin/x86_64/linux/release/deviceQueryDrv Starting...

CUDA Device Query (Driver API) statically linked version 
Detected 1 CUDA Capable device(s)

Device 0: "GeForce GTX 1650 SUPER"
  CUDA Driver Version:                           11.2
  CUDA Capability Major/Minor version number:    7.5
  Total amount of global memory:                 3878 MBytes (4066574336 bytes)
  (20) Multiprocessors, ( 64) CUDA Cores/MP:     1280 CUDA Cores
  GPU Max Clock rate:                            1755 MHz (1.75 GHz)
  Memory Clock rate:                             6001 Mhz
  Memory Bus Width:                              128-bit
  L2 Cache Size:                                 1048576 bytes
  Max Texture Dimension Sizes                    1D=(131072) 2D=(131072, 65536) 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  1024
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size (x,y,z):    (2147483647, 65535, 65535)
  Texture alignment:                             512 bytes
  Maximum memory pitch:                          2147483647 bytes
  Concurrent copy and kernel execution:          Yes with 3 copy engine(s)
  Run time limit on kernels:                     Yes
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Concurrent kernel execution:                   Yes
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
Result = PASS
Initializing...
GPU Device 0: "Turing" with compute capability 7.5

dmmaTensorCoreGemm requires SM 8.0 or higher.  Exiting...
./bin/x86_64/linux/release/dwtHaar1D Starting...

GPU Device 0: "Turing" with compute capability 7.5

source file    = "./3_Imaging/dwtHaar1D/data/signal.dat"
reference file = "result.dat"
gold file      = "./3_Imaging/dwtHaar1D/data/regression.gold.dat"
Reading signal from "./3_Imaging/dwtHaar1D/data/signal.dat"
Writing result to "result.dat"
Reading reference result from "./3_Imaging/dwtHaar1D/data/regression.gold.dat"
Test success!
./bin/x86_64/linux/release/dxtc Starting...

GPU Device 0: "Turing" with compute capability 7.5

Image Loaded './3_Imaging/dxtc/data/lena_std.ppm', 512 x 512 pixels

Running DXT Compression on 512 x 512 image...

16384 Blocks, 64 Threads per Block, 1048576 Threads in Grid...

dxtc, Throughput = 116.5602 MPixels/s, Time = 0.00225 s, Size = 262144 Pixels, NumDevsUsed = 1, Workgroup = 64

Checking accuracy...
Deviation at (   9,   1):	0.791667 rms
Deviation at (  99,   1):	1.041667 rms
Deviation at (  33,   2):	2.645833 rms
Deviation at (  38,   4):	1.916667 rms
Deviation at (  57,   4):	0.854167 rms
Deviation at (  20,   7):	1.041667 rms
Deviation at (  57,   7):	0.458333 rms
Deviation at (   8,   9):	0.937500 rms
Deviation at (  31,   9):	0.770833 rms
Deviation at (  13,  11):	1.041667 rms
Deviation at (  88,  11):	0.729167 rms
Deviation at (   4,  13):	8.562500 rms
Deviation at (  28,  13):	0.562500 rms
Deviation at (  90,  13):	0.708333 rms
Deviation at (  25,  14):	0.520833 rms
Deviation at (  87,  16):	0.708333 rms
Deviation at (  24,  19):	0.916667 rms
Deviation at (  25,  19):	0.625000 rms
Deviation at (  26,  19):	1.041667 rms
Deviation at (  55,  20):	4.791667 rms
Deviation at (  20,  23):	1.541667 rms
Deviation at (  99,  23):	3.312500 rms
Deviation at (  45,  24):	18.104166 rms
Deviation at (   8,  28):	0.895833 rms
Deviation at (  21,  30):	1.562500 rms
Deviation at ( 115,  32):	24.104166 rms
Deviation at (   2,  33):	0.854167 rms
Deviation at ( 102,  33):	2.250000 rms
Deviation at (  50,  35):	26.958334 rms
Deviation at (  12,  38):	2.166667 rms
Deviation at (  96,  39):	1.041667 rms
Deviation at (  40,  40):	0.270833 rms
Deviation at (  43,  44):	2.250000 rms
Deviation at (  54,  44):	4.791667 rms
Deviation at (  46,  46):	2.875000 rms
Deviation at ( 116,  46):	0.604167 rms
Deviation at ( 117,  46):	6.833333 rms
Deviation at ( 117,  48):	0.937500 rms
Deviation at (  23,  51):	3.520833 rms
Deviation at (  67,  54):	5.687500 rms
Deviation at (  26,  55):	0.854167 rms
Deviation at (  21,  56):	5.000000 rms
Deviation at (  24,  56):	0.562500 rms
Deviation at (  30,  57):	0.937500 rms
Deviation at ( 126,  57):	1.208333 rms
Deviation at (  21,  59):	2.541667 rms
Deviation at ( 120,  59):	0.104167 rms
Deviation at ( 112,  60):	1.125000 rms
Deviation at (  76,  61):	1.666667 rms
Deviation at (  77,  61):	1.083333 rms
Deviation at (  75,  62):	0.937500 rms
Deviation at ( 121,  62):	0.937500 rms
Deviation at ( 124,  64):	2.854167 rms
Deviation at (  78,  66):	0.541667 rms
Deviation at ( 106,  68):	0.375000 rms
Deviation at (  16,  70):	3.104167 rms
Deviation at (  10,  71):	0.937500 rms
Deviation at ( 108,  71):	0.354167 rms
Deviation at (   0,  72):	0.854167 rms
Deviation at ( 118,  72):	5.562500 rms
Deviation at (  11,  73):	0.541667 rms
Deviation at (  68,  74):	1.937500 rms
Deviation at (  70,  76):	1.791667 rms
Deviation at ( 124,  76):	3.354167 rms
Deviation at ( 103,  78):	0.375000 rms
Deviation at (  74,  79):	0.270833 rms
Deviation at ( 108,  79):	0.083333 rms
Deviation at (  43,  82):	24.979166 rms
Deviation at (  58,  82):	2.833333 rms
Deviation at (  67,  82):	3.125000 rms
Deviation at (  78,  82):	2.437500 rms
Deviation at ( 123,  84):	0.541667 rms
Deviation at ( 127,  88):	0.229167 rms
Deviation at (  99,  89):	0.770833 rms
Deviation at (  93,  91):	0.666667 rms
Deviation at ( 118,  91):	1.125000 rms
Deviation at ( 115,  92):	0.083333 rms
Deviation at ( 115,  93):	0.083333 rms
Deviation at (  45,  94):	0.166667 rms
Deviation at (  14,  95):	1.937500 rms
Deviation at (  69,  95):	1.875000 rms
Deviation at ( 106,  95):	1.125000 rms
Deviation at ( 107,  95):	3.708333 rms
Deviation at (  13,  96):	1.354167 rms
Deviation at ( 115,  98):	0.187500 rms
Deviation at ( 118,  98):	0.187500 rms
Deviation at ( 116, 101):	0.187500 rms
Deviation at (  87, 106):	0.270833 rms
Deviation at (  67, 107):	0.708333 rms
Deviation at (  74, 107):	0.375000 rms
Deviation at (  65, 109):	0.770833 rms
Deviation at (  89, 109):	0.708333 rms
Deviation at ( 118, 109):	3.854167 rms
Deviation at (  88, 111):	0.208333 rms
Deviation at (  64, 113):	0.708333 rms
Deviation at (  84, 113):	0.333333 rms
Deviation at (  75, 114):	2.083333 rms
Deviation at (  66, 115):	0.770833 rms
Deviation at (  89, 116):	0.770833 rms
Deviation at (  19, 118):	5.270833 rms
Deviation at (  76, 121):	0.104167 rms
Deviation at (  70, 122):	0.708333 rms
Deviation at (  91, 122):	0.208333 rms
Deviation at (  75, 123):	0.854167 rms
Deviation at (  61, 124):	0.937500 rms
Deviation at (  91, 124):	0.270833 rms
Deviation at (  91, 125):	1.020833 rms
RMS(reference, result) = 0.015238

Test passed
Starting eigenvalues
GPU Device 0: "Turing" with compute capability 7.5

Matrix size: 2048 x 2048
Precision: 0.000010
Iterations to be timed: 100
Result filename: 'eigenvalues.dat'
Gerschgorin interval: -2.894310 / 2.923303
Average time step 1: 1.663421 ms
Average time step 2, one intervals: 1.905800 ms
Average time step 2, mult intervals: 4.320952 ms
Average time TOTAL: 7.903210 ms
Test Succeeded!
./bin/x86_64/linux/release/fastWalshTransform Starting...

GPU Device 0: "Turing" with compute capability 7.5

Initializing data...
...allocating CPU memory
...allocating GPU memory
...generating data
Data length: 8388608; kernel length: 128
Running GPU dyadic convolution using Fast Walsh Transform...
GPU time: 9.629000 ms; GOP/s: 30.055767
Reading back GPU results...
Running straightforward CPU dyadic convolution...
Comparing the results...
Shutting down...
L2 norm: 1.021579E-07
Test passed
GPU Device 0: "Turing" with compute capability 7.5

Result native operators	: 653330.000000 
Result intrinsics	: 653330.000000 
&&&& fp16ScalarProduct PASSED
[globalToShmemAsyncCopy] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

MatrixA(1280,1280), MatrixB(1280,1280)
Running kernel = 0 - AsyncCopyMultiStageLargeChunk
Computing result using CUDA Kernel...
done
Performance= 201.80 GFlop/s, Time= 20.784 msec, Size= 4194304000 Ops, WorkgroupSize= 256 threads/block
Checking computed result for correctness: Result = PASS

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
[[histogram]] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER] has 20 Multi-Processors, Compute 7.5
Initializing data...
...allocating CPU memory.
...generating input data
...allocating GPU memory and copying input data

Starting up 64-bin histogram...

Running 64-bin GPU histogram for 67108864 bytes (16 runs)...

histogram64() time (average) : 0.00057 sec, 117812.3531 MB/sec

histogram64, Throughput = 117812.3531 MB/s, Time = 0.00057 s, Size = 67108864 Bytes, NumDevsUsed = 1, Workgroup = 64

Validating GPU results...
 ...reading back GPU results
 ...histogram64CPU()
 ...comparing the results...
 ...64-bin histograms match

Shutting down 64-bin histogram...


Initializing 256-bin histogram...
Running 256-bin GPU histogram for 67108864 bytes (16 runs)...

histogram256() time (average) : 0.00054 sec, 124160.7138 MB/sec

histogram256, Throughput = 124160.7138 MB/s, Time = 0.00054 s, Size = 67108864 Bytes, NumDevsUsed = 1, Workgroup = 192

Validating GPU results...
 ...reading back GPU results
 ...histogram256CPU()
 ...comparing the results
 ...256-bin histograms match

Shutting down 256-bin histogram...


Shutting down...

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.

[histogram] - Test Summary
Test passed
Initializing...
GPU Device 0: "Turing" with compute capability 7.5

M: 4096 (16 x 256)
N: 4096 (16 x 256)
K: 4096 (16 x 256)
Preparing data for GPU...
Required shared memory size: 64 Kb
Computing... using high performance kernel compute_gemm_imma 
Time: 89.538559 ms
TOPS: 1.53
CUDA inline PTX assembler sample
GPU Device 0: "Turing" with compute capability 7.5

Test Successful.
CUDA inline PTX assembler sample

error: unable to open [Interval Computing]  starting ...

GPU Device 0: "Turing" with compute capability 7.5

> GPU Device has Compute Capabilities SM 7.5

GPU naive implementation
Searching for roots in [0.01, 4]...
Found 2 intervals that may contain the root(s)
 i[0] = [0.999655515093009, 1.00011722206639]
 i[1] = [1.00011907576551, 1.00044661086269]
Number of equations solved: 65536
Time per equation: 16.7000007629395 us

Check against Host computation...

GPU Device 0: "Turing" with compute capability 7.5

CPU iterations : 2954
CPU error : 4.988e-03
CPU Processing time: 1803.543945 (ms)
GPU iterations : 2954
GPU error : 4.988e-03
GPU Processing time: 158.470993 (ms)
&&&& jacobiCudaGraphs PASSED
/tmp/e: line 217:  6538 Segmentation fault      ./bin/x86_64/linux/release/libcuhook.so.1
[./bin/x86_64/linux/release/lineOfSight] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

Line of sight
Average time: 0.016710 ms

Test passed
[Matrix Multiply Using CUDA] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

MatrixA(320,320), MatrixB(640,320)
Computing result using CUDA Kernel...
done
Performance= 614.93 GFlop/s, Time= 0.213 msec, Size= 131072000 Ops, WorkgroupSize= 1024 threads/block
Checking computed result for correctness: Result = PASS

NOTE: The CUDA Samples are not meant for performancemeasurements. Results may vary when GPU Boost is enabled.
[Matrix Multiply CUBLAS] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

GPU Device 0: "GeForce GTX 1650 SUPER" with compute capability 7.5

MatrixA(640,480), MatrixB(480,320), MatrixC(640,320)
Computing result using CUBLAS...done.
Performance= 2339.56 GFlop/s, Time= 0.084 msec, Size= 196608000 Ops
Computing result using host CPU...done.
Comparing CUBLAS Matrix Multiply with CPU results: PASS

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
[ matrixMulDrv (Driver API) ]
> Using CUDA Device [0]: GeForce GTX 1650 SUPER
> GPU Device has SM 7.5 compute capability
  Total amount of global memory:     4066574336 bytes
> findModulePath found file at <./0_Simple/matrixMulDrv/data/matrixMul_kernel64.fatbin>
> initCUDA loading module: <./0_Simple/matrixMulDrv/data/matrixMul_kernel64.fatbin>
Processing time: 0.083000 (ms)
Checking computed result for correctness: Result = PASS

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
[ matrixMulDynlinkJIT (CUDA dynamic linking) ]
> Device 0: "GeForce GTX 1650 SUPER" with Compute 7.5 capability
> Compiling CUDA module
> PTX JIT log:

Test run success!
[Matrix Multiply Using CUDA] - Starting...
MatrixA(320,320), MatrixB(640,320)

error: unable to open > findModulePath found file at <./0_Simple/memMapIPCDrv/data/memMapIpc_kernel64.fatbin>
> initCUDA loading module: <./0_Simple/memMapIPCDrv/data/memMapIpc_kernel64.fatbin>
Step 0 done
Process 0: verifying...
./bin/x86_64/linux/release/mergeSort Starting...

GPU Device 0: "Turing" with compute capability 7.5

Allocating and initializing host arrays...

Allocating and initializing CUDA arrays...

Initializing GPU merge sort...
Running GPU merge sort...
Time: 10.237000 ms
Reading back GPU merge sort results...
Inspecting the results...
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: stable!
Shutting down...
newdelete Starting...

GPU Device 0: "Turing" with compute capability 7.5

 > Container = Vector test OK

 > Container = Vector, using placement new on SMEM buffer test OK

 > Container = Vector, with user defined datatype test OK

Test Summary: 3/3 succesfully run
GPU Device 0: "Turing" with compute capability 7.5

Using GPU 0 (GeForce GTX 1650 SUPER, 20 SMs, 1024 th/SM max, CC 7.5, ECC off)
Decoding images in directory: ./7_CUDALibraries/nvJPEG/images/, total 8, batchsize 1
Processing: ./7_CUDALibraries/nvJPEG/images/img5.jpg
Image is 3 channels.
Channel #0 size: 640 x 480
Channel #1 size: 320 x 240
Channel #2 size: 320 x 240
YUV 4:2:0 chroma subsampling
Processing: ./7_CUDALibraries/nvJPEG/images/img6.jpg
Image is 3 channels.
Channel #0 size: 640 x 480
Channel #1 size: 320 x 240
Channel #2 size: 320 x 240
YUV 4:2:0 chroma subsampling
Processing: ./7_CUDALibraries/nvJPEG/images/img2.jpg
Image is 3 channels.
Channel #0 size: 480 x 640
Channel #1 size: 240 x 320
Channel #2 size: 240 x 320
YUV 4:2:0 chroma subsampling
Processing: ./7_CUDALibraries/nvJPEG/images/img7.jpg
Image is 3 channels.
Channel #0 size: 480 x 640
Channel #1 size: 240 x 320
Channel #2 size: 240 x 320
YUV 4:2:0 chroma subsampling
Processing: ./7_CUDALibraries/nvJPEG/images/img8.jpg
Image is 3 channels.
Channel #0 size: 480 x 640
Channel #1 size: 240 x 320
Channel #2 size: 240 x 320
YUV 4:2:0 chroma subsampling
Processing: ./7_CUDALibraries/nvJPEG/images/img1.jpg
Image is 3 channels.
Channel #0 size: 480 x 640
Channel #1 size: 240 x 320
Channel #2 size: 240 x 320
YUV 4:2:0 chroma subsampling
Processing: ./7_CUDALibraries/nvJPEG/images/img3.jpg
Image is 3 channels.
Channel #0 size: 640 x 426
Channel #1 size: 320 x 213
Channel #2 size: 320 x 213
YUV 4:2:0 chroma subsampling
Processing: ./7_CUDALibraries/nvJPEG/images/img4.jpg
Image is 3 channels.
Channel #0 size: 640 x 426
Channel #1 size: 320 x 213
Channel #2 size: 320 x 213
YUV 4:2:0 chroma subsampling
Total decoding time: 10.6622
Avg decoding time per image: 1.33277
Avg images per sec: 0.750316
Avg decoding time per batch: 1.33277
GPU Device 0: "Turing" with compute capability 7.5

Using GPU 0 (GeForce GTX 1650 SUPER, 20 SMs, 1024 th/SM max, CC 7.5, ECC off)
Processing file: ./7_CUDALibraries/nvJPEG_encoder/images/img5.jpg
Image is 3 channels.
Channel #0 size: 640 x 480
Channel #1 size: 320 x 240
Channel #2 size: 320 x 240
YUV 4:2:0 chroma subsampling
Writing JPEG file: encode_output/img5.jpg
Processing file: ./7_CUDALibraries/nvJPEG_encoder/images/img6.jpg
Image is 3 channels.
Channel #0 size: 640 x 480
Channel #1 size: 320 x 240
Channel #2 size: 320 x 240
YUV 4:2:0 chroma subsampling
Writing JPEG file: encode_output/img6.jpg
Processing file: ./7_CUDALibraries/nvJPEG_encoder/images/img2.jpg
Image is 3 channels.
Channel #0 size: 480 x 640
Channel #1 size: 240 x 320
Channel #2 size: 240 x 320
YUV 4:2:0 chroma subsampling
Writing JPEG file: encode_output/img2.jpg
Processing file: ./7_CUDALibraries/nvJPEG_encoder/images/img7.jpg
Image is 3 channels.
Channel #0 size: 480 x 640
Channel #1 size: 240 x 320
Channel #2 size: 240 x 320
YUV 4:2:0 chroma subsampling
Writing JPEG file: encode_output/img7.jpg
Processing file: ./7_CUDALibraries/nvJPEG_encoder/images/img8.jpg
Image is 3 channels.
Channel #0 size: 480 x 640
Channel #1 size: 240 x 320
Channel #2 size: 240 x 320
YUV 4:2:0 chroma subsampling
Writing JPEG file: encode_output/img8.jpg
Processing file: ./7_CUDALibraries/nvJPEG_encoder/images/img1.jpg
Image is 3 channels.
Channel #0 size: 480 x 640
Channel #1 size: 240 x 320
Channel #2 size: 240 x 320
YUV 4:2:0 chroma subsampling
Writing JPEG file: encode_output/img1.jpg
Processing file: ./7_CUDALibraries/nvJPEG_encoder/images/img3.jpg
Image is 3 channels.
Channel #0 size: 640 x 426
Channel #1 size: 320 x 213
Channel #2 size: 320 x 213
YUV 4:2:0 chroma subsampling
Writing JPEG file: encode_output/img3.jpg
Processing file: ./7_CUDALibraries/nvJPEG_encoder/images/img4.jpg
Image is 3 channels.
Channel #0 size: 640 x 426
Channel #1 size: 320 x 213
Channel #2 size: 320 x 213
YUV 4:2:0 chroma subsampling
Writing JPEG file: encode_output/img4.jpg
Total images processed: 8
Total time spent on encoding: 1.5888
Avg time/image: 0.1986
[P2P (Peer-to-Peer) GPU Bandwidth Latency Test]
Device: 0, GeForce GTX 1650 SUPER, pciBusID: 1, pciDeviceID: 0, pciDomainID:0

***NOTE: In case a device doesn't have P2P access to other one, it falls back to normal memcopy procedure.
So you can see lesser Bandwidth (GB/s) and unstable Latency (us) in those cases.

P2P Connectivity Matrix
     D\D     0
     0	     1
Unidirectional P2P=Disabled Bandwidth Matrix (GB/s)
   D\D     0 
     0 148.51 
Unidirectional P2P=Enabled Bandwidth (P2P Writes) Matrix (GB/s)
   D\D     0 
     0 138.03 
Bidirectional P2P=Disabled Bandwidth Matrix (GB/s)
   D\D     0 
     0 148.45 
Bidirectional P2P=Enabled Bandwidth Matrix (GB/s)
   D\D     0 
     0 148.73 
P2P=Disabled Latency Matrix (us)
   GPU     0 
     0   1.86 

   CPU     0 
     0   1.75 
P2P=Enabled Latency (P2P Writes) Matrix (us)
   GPU     0 
     0   1.88 

   CPU     0 
     0   1.68 

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
[PTX Just In Time (JIT) Compilation (no-qatest)] - Starting...
> Using CUDA Device [0]: GeForce GTX 1650 SUPER
> findModulePath <./6_Advanced/ptxjit/data/ptxjit_kernel64.ptx>
> initCUDA loading module: <./6_Advanced/ptxjit/data/ptxjit_kernel64.ptx>
Loading ptxjit_kernel[] program
CUDA Link Completed in 0.000000ms. Linker Output:
info    : 0 bytes gmem
info    : Function properties for 'myKernel':
info    : used 8 registers, 0 stack, 0 bytes smem, 360 bytes cmem[0], 0 bytes lmem
CUDA kernel launched
./bin/x86_64/linux/release/quasirandomGenerator Starting...

Allocating GPU memory...
Allocating CPU memory...
Initializing QRNG tables...

Testing QRNG...

quasirandomGenerator, Throughput = 16.6133 GNumbers/s, Time = 0.00019 s, Size = 3145728 Numbers, NumDevsUsed = 1, Workgroup = 384

Reading GPU results...
Comparing to the CPU results...

L1 norm: 7.275964E-12

Testing inverseCNDgpu()...

quasirandomGenerator-inverse, Throughput = 31.6631 GNumbers/s, Time = 0.00010 s, Size = 3145728 Numbers, NumDevsUsed = 1, Workgroup = 128
Reading GPU results...

Comparing to the CPU results...
L1 norm: 9.439909E-08

Shutting down...
./bin/x86_64/linux/release/quasirandomGenerator_nvrtc Starting...


error: unable to open ./bin/x86_64/linux/release/radixSortThrust Starting...

GPU Device 0: "Turing" with compute capability 7.5


Sorting 1048576 32-bit unsigned int keys and values

radixSortThrust, Throughput = 905.9379 MElements/s, Time = 0.00116 s, Size = 1048576 elements
Test passed
./bin/x86_64/linux/release/reduction Starting...

GPU Device 0: "Turing" with compute capability 7.5

Using Device 0: GeForce GTX 1650 SUPER

Reducing array of type int

16777216 elements
256 threads (max)
64 blocks

Reduction, Throughput = 171.2267 GB/s, Time = 0.00039 s, Size = 16777216 Elements, NumDevsUsed = 1, Workgroup = 256

GPU result = 2139353471
CPU result = 2139353471

Test passed
reductionMultiBlockCG Starting...

GPU Device 0: "Turing" with compute capability 7.5

33554432 elements
numThreads: 1024
numBlocks: 20

Launching SinglePass Multi Block Cooperative Groups kernel
Average time: 1.009710 ms
Bandwidth:    132.926950 GB/s

GPU result = 1.992401599884
CPU result = 1.992401361465
./bin/x86_64/linux/release/scalarProd Starting...

GPU Device 0: "Turing" with compute capability 7.5

Initializing data...
...allocating CPU memory.
...allocating GPU memory.
...generating input data in CPU mem.
...copying input data to GPU mem.
Data init done.
Executing GPU kernel...
GPU time: 0.066000 msecs.
Reading back GPU result...
Checking GPU results...
..running CPU scalar product calculation
...comparing the results
Shutting down...
L1 error: 2.745062E-08
Test passed
./bin/x86_64/linux/release/scan Starting...

GPU Device 0: "Turing" with compute capability 7.5

Allocating and initializing host arrays...
Allocating and initializing CUDA arrays...
Initializing CUDA-C scan...

*** Running GPU scan for short arrays (100 identical iterations)...

Running scan for 4 elements (1703936 arrays)...
Validating the results...
...reading back GPU results
 ...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 8 elements (851968 arrays)...
Validating the results...
...reading back GPU results
 ...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 16 elements (425984 arrays)...
Validating the results...
...reading back GPU results
 ...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 32 elements (212992 arrays)...
Validating the results...
...reading back GPU results
 ...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 64 elements (106496 arrays)...
Validating the results...
...reading back GPU results
 ...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 128 elements (53248 arrays)...
Validating the results...
...reading back GPU results
 ...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 256 elements (26624 arrays)...
Validating the results...
...reading back GPU results
 ...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 512 elements (13312 arrays)...
Validating the results...
...reading back GPU results
 ...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 1024 elements (6656 arrays)...
Validating the results...
...reading back GPU results
 ...scanExclusiveHost()
 ...comparing the results
 ...Results Match


scan, Throughput = 3.0050 MElements/s, Time = 0.00034 s, Size = 1024 Elements, NumDevsUsed = 1, Workgroup = 256

***Running GPU scan for large arrays (100 identical iterations)...

Running scan for 2048 elements (3328 arrays)...
Validating the results...
...reading back GPU results
...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 4096 elements (1664 arrays)...
Validating the results...
...reading back GPU results
...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 8192 elements (832 arrays)...
Validating the results...
...reading back GPU results
...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 16384 elements (416 arrays)...
Validating the results...
...reading back GPU results
...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 32768 elements (208 arrays)...
Validating the results...
...reading back GPU results
...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 65536 elements (104 arrays)...
Validating the results...
...reading back GPU results
...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 131072 elements (52 arrays)...
Validating the results...
...reading back GPU results
...scanExclusiveHost()
 ...comparing the results
 ...Results Match

Running scan for 262144 elements (26 arrays)...
Validating the results...
...reading back GPU results
...scanExclusiveHost()
 ...comparing the results
 ...Results Match


scan, Throughput = 378.4489 MElements/s, Time = 0.00069 s, Size = 262144 Elements, NumDevsUsed = 1, Workgroup = 256

Shutting down...
./bin/x86_64/linux/release/segmentationTreeThrust Starting...

GPU Device 0: "Turing" with compute capability 7.5

* Building segmentation tree... done in 62.6691 (ms)
* Dumping levels for each tree...

Starting shfl_scan
GPU Device 0: "Turing" with compute capability 7.5

> Detected Compute SM 7.5 hardware with 20 multi-processors
Starting shfl_scan
GPU Device 0: "Turing" with compute capability 7.5

> Detected Compute SM 7.5 hardware with 20 multi-processors
Computing Simple Sum test
---------------------------------------------------
Initialize test data [1, 1, 1...]
Scan summation for 65536 elements, 256 partial sums
Partial summing 256 elements with 1 blocks of size 256
Test Sum: 65536
Time (ms): 0.030176
65536 elements scanned in 0.030176 ms -> 2171.792236 MegaElements/s
CPU verify result diff (GPUvsCPU) = 0
CPU sum (naive) took 0.024570 ms

Computing Integral Image Test on size 1920 x 1080 synthetic data
---------------------------------------------------
Method: Fast  Time (GPU Timer): 0.072832 ms Diff = 0
Method: Vertical Scan  Time (GPU Timer): 0.122848 ms 
CheckSum: 2073600, (expect 1920x1080=2073600)
./bin/x86_64/linux/release/simpleAWBarrier starting...
GPU Device 0: "Turing" with compute capability 7.5

Launching normVecByDotProductAWBarrier kernel with numBlocks = 20 blockSize = 1024
Result = PASSED
./bin/x86_64/linux/release/simpleAWBarrier completed, returned OK
simpleAssert.cu:47: void testKernel(int): block: [1,0,0], thread: [28,0,0] Assertion `gtid < N` failed.
simpleAssert.cu:47: void testKernel(int): block: [1,0,0], thread: [29,0,0] Assertion `gtid < N` failed.
simpleAssert.cu:47: void testKernel(int): block: [1,0,0], thread: [30,0,0] Assertion `gtid < N` failed.
simpleAssert.cu:47: void testKernel(int): block: [1,0,0], thread: [31,0,0] Assertion `gtid < N` failed.
simpleAssert starting...
OS_System_Type.release = 5.12.0-yoctodev-standard
OS Info: <#1 SMP PREEMPT Sat May 8 03:46:47 UTC 2021>

GPU Device 0: "Turing" with compute capability 7.5

Launch kernel to generate assertion failures

-- Begin assert output


-- End assert output

Device assert failed as expected, CUDA error message is: device-side assert triggered

simpleAssert completed, returned OK
simpleAssert_nvrtc starting...
Launch kernel to generate assertion failures

error: unable to open simpleAtomicIntrinsics starting...
GPU Device 0: "Turing" with compute capability 7.5

Processing time: 62.085999 (ms)
simpleAtomicIntrinsics completed, returned OK
simpleAtomicIntrinsics_nvrtc starting...

error: unable to open ./bin/x86_64/linux/release/simpleAttributes Starting...

GPU Device 0: "Turing" with compute capability 7.5

Waiving execution as device 0 does not support persisting L2 Caching
GPU Device 0: "Turing" with compute capability 7.5

simpleCUBLAS test running..
simpleCUBLAS test passed.
Using 1 GPUs
GPU ID = 0, Name = GeForce GTX 1650 SUPER 
simpleCUBLASXT test running..
simpleCUBLASXT test passed.
[simpleCUFFT] is starting...
GPU Device 0: "Turing" with compute capability 7.5

Temporary buffer size 448 bytes
Transforming signal cufftExecC2C
Launching ComplexPointwiseMulAndScale<<< >>>
Transforming signal back cufftExecC2C

Poisson equation using CUFFT library on Multiple GPUs is starting...

No. of GPU on node 1
Two GPUs are required to run simpleCUFFT_2d_MGPU sample code

[simpleCUFFT_MGPU] is starting...

No. of GPU on node 1
Two GPUs are required to run simpleCUFFT_MGPU sample code
[simpleCUFFT_callback] is starting...
GPU Device 0: "Turing" with compute capability 7.5

Transforming signal cufftExecC2C
Transforming signal back cufftExecC2C
Starting simpleCallback
Found 1 CUDA capable GPUs
GPU[0] GeForce GTX 1650 SUPER supports SM 7.5, capable GPU Callback Functions
1 GPUs available to run Callback Functions
Starting 8 heterogeneous computing workloads
Total of 8 workloads finished:
Success

Launching a single block with 64 threads...

 Sum of all ranks 0..63 in threadBlockGroup is 2016 (expected 2016)

 Now creating 4 groups, each of size 16 threads:

   Sum of all ranks 0..15 in this tiledPartition16 group is 120 (expected 120)
   Sum of all ranks 0..15 in this tiledPartition16 group is 120 (expected 120)
   Sum of all ranks 0..15 in this tiledPartition16 group is 120 (expected 120)
   Sum of all ranks 0..15 in this tiledPartition16 group is 120 (expected 120)

...Done.

GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER] has 20 Multi-Processors SM 7.5
Covering Cubemap data array of 64~3 x 1: Grid size is 8 x 8, each block has 8 x 8 threads
Processing time: 0.008 msec
3072.00 Mtexlookups/sec
Comparing kernel output to expected data
GPU Device 0: "Turing" with compute capability 7.5

16777216 elements
threads per block  = 512
Graph Launch iterations = 3

Num of nodes in the graph created manually = 6
[cudaGraphsManual] final reduced sum = 0.996214
[cudaGraphsManual] final reduced sum = 0.996214
[cudaGraphsManual] final reduced sum = 0.996214
Cloned Graph Output.. 
[cudaGraphsManual] final reduced sum = 0.996214
[cudaGraphsManual] final reduced sum = 0.996214
[cudaGraphsManual] final reduced sum = 0.996214

Num of nodes in the graph created using stream capture API = 6
[cudaGraphsUsingStreamCapture] final reduced sum = 0.996214
[cudaGraphsUsingStreamCapture] final reduced sum = 0.996214
[cudaGraphsUsingStreamCapture] final reduced sum = 0.996214
Cloned Graph Output.. 
[cudaGraphsUsingStreamCapture] final reduced sum = 0.996214
[cudaGraphsUsingStreamCapture] final reduced sum = 0.996214
[cudaGraphsUsingStreamCapture] final reduced sum = 0.996214
simpleDrvRuntime..
GPU Device 0: "Turing" with compute capability 7.5

> findModulePath found file at <./0_Simple/simpleDrvRuntime/data/vectorAdd_kernel64.fatbin>
> initCUDA loading module: <./0_Simple/simpleDrvRuntime/data/vectorAdd_kernel64.fatbin>
Result = PASS
starting hyperQ...
GPU Device 0: "Turing" with compute capability 7.5

> Detected Compute SM 7.5 hardware with 20 multi-processors
Expected time for serial execution of 32 sets of kernels is between approx. 0.330s and 0.640s
Expected time for fully concurrent execution of 32 sets of kernels is approx. 0.020s
Measured time for sample = 0.058s
Process 0: Starting on device 0...
Step 0 done
Process 0: verifying...
Process 0 complete!
[simpleLayeredTexture] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER] has 20 Multi-Processors SM 7.5
Covering 2D data array of 512 x 512: Grid size is 64 x 64, each block has 8 x 8 threads
Processing time: 0.098 msec
13374.69 Mtexlookups/sec
Comparing kernel output to expected data
[simpleMultiCopy] - Starting...
> Using CUDA device [0]: GeForce GTX 1650 SUPER
[GeForce GTX 1650 SUPER] has 20 MP(s) x 64 (Cores/MP) = 1280 (Cores)
> Device name: GeForce GTX 1650 SUPER
> CUDA Capability 7.5 hardware with 20 multi-processors
> scale_factor = 1.00
> array_size   = 4194304


Relevant properties of this CUDA device
(X) Can overlap one CPU<>GPU data transfer with GPU kernel execution (device property "deviceOverlap")
(X) Can overlap two CPU<>GPU data transfers with GPU kernel execution
    (Compute Capability >= 2.0 AND (Tesla product OR Quadro 4000/5000/6000/K5000)

Measured timings (throughput):
 Memcpy host to device	: 1.355072 ms (12.381051 GB/s)
 Memcpy device to host	: 1.320256 ms (12.707548 GB/s)
 Kernel			: 0.235264 ms (713.122950 GB/s)

Theoretical limits for speedup gained from overlapped data transfers:
No overlap at all (transfer-kernel-transfer): 2.910592 ms 
Compute can overlap with one transfer: 2.675328 ms
Compute can overlap with both data transfers: 1.355072 ms

Average measured timings over 10 repetitions:
 Avg. time when execution fully serialized	: 2.916160 ms
 Avg. time when overlapped using 4 streams	: 1.684854 ms
 Avg. speedup gained (serialized - overlapped)	: 1.231306 ms

Measured throughput:
 Fully serialized execution		: 11.506375 GB/s
 Overlapped using 4 streams		: 19.915331 GB/s
Starting simpleMultiGPU
CUDA-capable device count: 1
Generating input data...

Computing with 1 GPUs...
  GPU Processing time: 12.565000 (ms)

Computing with Host CPU...

Comparing GPU and Host CPU results...
  GPU sum: 16777296.000000
  CPU sum: 16777294.395033
  Relative difference: 9.566307E-08 

starting Simple Occupancy

[ Manual configuration with 32 threads per block ]
Potential occupancy: 50%
Elapsed time: 0.103008ms

[ Automatic, occupancy-based configuration ]
Suggested block size: 1024
Minimum grid size for maximum occupancy: 20
Potential occupancy: 100%
Elapsed time: 0.056896ms

Test PASSED

[./bin/x86_64/linux/release/simpleP2P] - Starting...
Checking for multiple GPUs...
CUDA-capable device count: 1
Two or more GPUs with Peer-to-Peer access capability are required for ./bin/x86_64/linux/release/simpleP2P.
Waiving test.
simplePitchLinearTexture starting...

GPU Device 0: "Turing" with compute capability 7.5


Bandwidth (GB/s) for pitch linear: 1.51e+02; for array: 1.57e+02

Texture fetch rate (Mpix/s) for pitch linear: 1.88e+04; for array: 1.96e+04

simplePitchLinearTexture completed, returned OK
GPU Device 0: "Turing" with compute capability 7.5

Device 0: "GeForce GTX 1650 SUPER" with Compute 7.5 capability
printf() is called. Output:

[0, 0]:		Value is:10
[0, 1]:		Value is:10
[0, 2]:		Value is:10
[0, 3]:		Value is:10
[0, 4]:		Value is:10
[0, 5]:		Value is:10
[0, 6]:		Value is:10
[0, 7]:		Value is:10
[1, 0]:		Value is:10
[1, 1]:		Value is:10
[1, 2]:		Value is:10
[1, 3]:		Value is:10
[1, 4]:		Value is:10
[1, 5]:		Value is:10
[1, 6]:		Value is:10
[1, 7]:		Value is:10
[3, 0]:		Value is:10
[3, 1]:		Value is:10
[3, 2]:		Value is:10
[3, 3]:		Value is:10
[3, 4]:		Value is:10
[3, 5]:		Value is:10
[3, 6]:		Value is:10
[3, 7]:		Value is:10
[2, 0]:		Value is:10
[2, 1]:		Value is:10
[2, 2]:		Value is:10
[2, 3]:		Value is:10
[2, 4]:		Value is:10
[2, 5]:		Value is:10
[2, 6]:		Value is:10
[2, 7]:		Value is:10
simpleSeparateCompilation starting...
GPU Device 0: "Turing" with compute capability 7.5

simpleSeparateCompilation completed, returned OK
[ simpleStreams ]

Device synchronization method set to = 0 (Automatic Blocking)
Setting reps to 100 to demonstrate steady state

> GPU Device 0: "Turing" with compute capability 7.5

Device: <GeForce GTX 1650 SUPER> canMapHostMemory: Yes
> CUDA Capable: SM 7.5 hardware
> 20 Multiprocessor(s) x 64 (Cores/Multiprocessor) = 1280 (Cores)
> scale_factor = 1.0000
> array_size   = 16777216

> Using CPU/GPU Device Synchronization method (cudaDeviceScheduleAuto)
> mmap() allocating 64.00 Mbytes (generic page-aligned system memory)
> cudaHostRegister() registering 64.00 Mbytes of generic allocated system memory

Starting Test
memcopy:	5.27
kernel:		0.92
non-streamed:	6.13
4 streams:	5.63
-------------------------------
simpleSurfaceWrite starting...
GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER] has 20 Multi-Processors, SM 7.5
Loaded 'lena_bw.pgm', 512 x 512 pixels
Processing time: 0.021000 (ms)
12483.05 Mpixels/sec
Wrote 'output.pgm'
Comparing files
	output:    <output.pgm>
	reference: <./0_Simple/simpleSurfaceWrite/data/ref_rotated.pgm>
simpleSurfaceWrite completed, returned OK
> runTest<float,32>
GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER] has 20 Multi-Processors
Processing time: 69.823997 (ms)
Compare OK

> runTest<int,64>
GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER] has 20 Multi-Processors
Processing time: 0.116000 (ms)
Compare OK


[simpleTemplates] -> Test Results: 0 Failures
> runTest<float,32>

error: unable to open simpleTexture starting...
GPU Device 0: "Turing" with compute capability 7.5

Loaded 'lena_bw.pgm', 512 x 512 pixels
Processing time: 0.021000 (ms)
12483.05 Mpixels/sec
Wrote './0_Simple/simpleTexture/data/lena_bw_out.pgm'
Comparing files
	output:    <./0_Simple/simpleTexture/data/lena_bw_out.pgm>
	reference: <./0_Simple/simpleTexture/data/ref_rotated.pgm>
simpleTexture completed, returned OK
> Using CUDA Device [0]: GeForce GTX 1650 SUPER
> GPU Device has SM 7.5 compute capability
> findModulePath found file at <./0_Simple/simpleTextureDrv/data/simpleTexture_kernel64.fatbin>
> initCUDA loading module: <./0_Simple/simpleTextureDrv/data/simpleTexture_kernel64.fatbin>
Loaded 'lena_bw.pgm', 512 x 512 pixels
Processing time: 0.021000 (ms)
12483.05 Mpixels/sec
Wrote './0_Simple/simpleTextureDrv/data/lena_bw_out.pgm'
Comparing files
	output:    <./0_Simple/simpleTextureDrv/data/lena_bw_out.pgm>
	reference: <./0_Simple/simpleTextureDrv/data/ref_rotated.pgm>
[simpleVoteIntrinsics]
GPU Device 0: "Turing" with compute capability 7.5

> GPU device has 20 Multi-Processors, SM 7.5 compute capabilities

[VOTE Kernel Test 1/3]
	Running <<Vote.Any>> kernel1 ...
	OK

[VOTE Kernel Test 2/3]
	Running <<Vote.All>> kernel2 ...
	OK

[VOTE Kernel Test 3/3]
	Running <<Vote.Any>> kernel3 ...
	OK
	Shutting down...

error: unable to open   Device 0: <          Turing >, Compute SM 7.5 detected
> Using CUDA Host Allocated (cudaHostAlloc)
> vectorAddGPU kernel will add vectors using mapped CPU memory...
> Checking the results from vectorAddGPU() ...
> Releasing CPU memory...
./bin/x86_64/linux/release/sortingNetworks Starting...

Starting up CUDA context...
GPU Device 0: "Turing" with compute capability 7.5

Allocating and initializing host arrays...

Allocating and initializing CUDA arrays...

Running GPU bitonic sort (1 identical iterations)...

Testing array length 64 (16384 arrays per batch)...
Average time: 0.320000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 128 (8192 arrays per batch)...
Average time: 0.565000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 256 (4096 arrays per batch)...
Average time: 0.607000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 512 (2048 arrays per batch)...
Average time: 0.723000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 1024 (1024 arrays per batch)...
Average time: 0.853000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 2048 (512 arrays per batch)...
Average time: 1.012000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 4096 (256 arrays per batch)...
Average time: 1.359000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 8192 (128 arrays per batch)...
Average time: 1.825000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 16384 (64 arrays per batch)...
Average time: 2.377000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 32768 (32 arrays per batch)...
Average time: 3.113000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 65536 (16 arrays per batch)...
Average time: 3.774000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 131072 (8 arrays per batch)...
Average time: 4.680000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 262144 (4 arrays per batch)...
Average time: 5.580000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 524288 (2 arrays per batch)...
Average time: 6.752000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 1048576 (1 arrays per batch)...
Average time: 7.948000 ms

sortingNetworks-bitonic, Throughput = 131.9295 MElements/s, Time = 0.00795 s, Size = 1048576 elements, NumDevsUsed = 1, Workgroup = 512

Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Shutting down...
[stereoDisparity] Starting...

GPU Device 0: "Turing" with compute capability 7.5

> GPU device has 20 Multi-Processors, SM 7.5 compute capabilities

Loaded <./3_Imaging/stereoDisparity/data/stereo.im0.640x533.ppm> as image 0
Loaded <./3_Imaging/stereoDisparity/data/stereo.im1.640x533.ppm> as image 1
Launching CUDA stereoDisparityKernel()
Input Size  [640x533], Kernel size [17x17], Disparities [-16:0]
GPU processing time : 1.0732 (ms)
Pixel throughput    : 317.839 Mpixels/sec
GPU Checksum = 4293895789, GPU image: <output_GPU.pgm>
Computing CPU reference...
CPU Checksum = 4293895789, CPU image: <output_CPU.pgm>
GPU Device 0: "Turing" with compute capability 7.5

Starting basicStreamOrderedAllocation()
> Checking the results from vectorAddGPU() ...
basicStreamOrderedAllocation PASSED
Starting streamOrderedAllocationPostSync()
Total elapsed time = 35.751617 ms over 20 iterations
> Checking the results from vectorAddGPU() ...
streamOrderedAllocationPostSync PASSED
No Two or more GPUs with same architecture capable of cuda Memory Pools found.
Waiving the sample
GPU Device 0: "Turing" with compute capability 7.5

CANNOT access pageable memory
systemWideAtomics completed, returned OK 
./bin/x86_64/linux/release/template Starting...

GPU Device 0: "Turing" with compute capability 7.5

Processing time: 58.780998 (ms)
Initializing...
GPU Device 0: "Turing" with compute capability 7.5

tf32TensorCoreGemm requires requires SM 8.0 or higher to use Tensor Cores.  Exiting...
threadFenceReduction Starting...

GPU Device 0: "Turing" with compute capability 7.5

GPU Device supports SM 7.5 compute capability

1048576 elements
128 threads (max)
64 blocks
Average time: 0.031950 ms
Bandwidth:    131.277133 GB/s

GPU result = 0.062298238277
CPU result = 0.062298242003
Starting threadMigration
[ threadMigration ] API test...
> 1 CUDA device(s), 2 Thread(s)/device to launched

Device 0: "GeForce GTX 1650 SUPER" (Compute 7.5)
	sharedMemPerBlock: 49152
	constantMemory   : 65536
	regsPerBlock     : 65536
	clockRate        : 1755000

> findModulePath found file at <./6_Advanced/threadMigration/data/threadMigration_kernel64.fatbin>
> initCUDA loading module: <./6_Advanced/threadMigration/data/threadMigration_kernel64.fatbin>
<CUDA Device=0, Context=0x5606f2a62040, Thread=0> - ThreadProc() Launched...
<CUDA Device=0, Context=0x5606f2a62040, Thread=1> - ThreadProc() Launched...
<CUDA Device=0, Context=0x5606f2a62040, Thread=0> - ThreadProc() Finished!

<CUDA Device=0, Context=0x5606f2a62040, Thread=1> - ThreadProc() Finished!

GPU0 <-> CPU:
  * Atomic Supported: no
Transpose Starting...

GPU Device 0: "Turing" with compute capability 7.5

> Device 0: "GeForce GTX 1650 SUPER"
> SM Capability 7.5 detected:
> [GeForce GTX 1650 SUPER] has 20 MP(s) x 64 (Cores/MP) = 1280 (Cores)
> Compute performance scaling factor = 1.00

Matrix size: 1024x1024 (64x64 tiles), tile size: 16x16, block size: 16x16

transpose simple copy       , Throughput = 145.2112 GB/s, Time = 0.05380 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose shared memory copy, Throughput = 146.3410 GB/s, Time = 0.05339 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose naive             , Throughput = 140.0724 GB/s, Time = 0.05577 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose coalesced         , Throughput = 144.1795 GB/s, Time = 0.05419 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose optimized         , Throughput = 143.1641 GB/s, Time = 0.05457 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose coarse-grained    , Throughput = 143.5876 GB/s, Time = 0.05441 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose fine-grained      , Throughput = 145.2457 GB/s, Time = 0.05379 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose diagonal          , Throughput = 124.3642 GB/s, Time = 0.06282 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
Test passed
[Vector addition of 50000 elements]
Copy input data from the host memory to the CUDA device
CUDA kernel launch with 196 blocks of 256 threads
Copy output data from the CUDA device to the host memory
Test PASSED
Done
Vector Addition (Driver API)
> Using CUDA Device [0]: GeForce GTX 1650 SUPER
> findModulePath found file at <./0_Simple/vectorAddDrv/data/vectorAdd_kernel64.fatbin>
> initCUDA loading module: <./0_Simple/vectorAddDrv/data/vectorAdd_kernel64.fatbin>
Result = PASS
Vector Addition (Driver API)
> Using CUDA Device [0]: GeForce GTX 1650 SUPER
Device 0 VIRTUAL ADDRESS MANAGEMENT SUPPORTED = 1.
> findModulePath found file at <./0_Simple/vectorAddMMAP/data/vectorAdd_kernel64.fatbin>
> initCUDA loading module: <./0_Simple/vectorAddMMAP/data/vectorAdd_kernel64.fatbin>
Result = PASS

error: unable to open GPU Device 0: "Turing" with compute capability 7.5

CPU max matches GPU max

Warp Aggregated Atomics PASSED 
NPP Library Version 11.3.2
CUDA Driver  Version: 11.2
CUDA Runtime Version: 11.2

Input file load succeeded.
Lena_Segments_8Way_512x512_8u succeeded.
Lena_CompressedSegmentLabels_8Way_512x512_32u succeeded.
Lena_SegmentBoundaries_8Way_512x512_8u succeeded.
Lena_SegmentsWithContrastingBoundaries_8Way_512x512_8u succeeded.
Input file load succeeded.
CT_Skull_Segments_8Way_512x512_8u succeeded.
CT_Skull_CompressedSegmentLabels_8Way_512x512_32u succeeded.
CT_Skull_SegmentBoundaries_8Way_512x512_8u succeeded.
CT_Skull_SegmentsWithContrastingBoundaries_8Way_512x512_8u succeeded.
Input file load succeeded.
Rocks_Segments_8Way_512x512_8u succeeded.
Rocks_CompressedSegmentLabels_8Way_512x512_32u succeeded.
Rocks_SegmentBoundaries_8Way_512x512_8u succeeded.
Rocks_SegmentsWithContrastingBoundaries_8Way_512x512_8u succeeded.
root@intel-x86-64:/usr/local/cuda-11.2/samples# 

```
### Issues
* There are errors in the outputs of few CUDA examples. We'll dig them further if needed.  

