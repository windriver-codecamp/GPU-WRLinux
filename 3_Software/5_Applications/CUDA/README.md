## Demo Video:
> None

## Run CUDA Examples Steps
```
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
root@intel-x86-64:/usr/local/cuda-11.2/samples#
root@intel-x86-64:/usr/local/cuda-11.2/samples# sh -x /tmp/e 
+ ./0_Simple/UnifiedMemoryStreams/UnifiedMemoryStreams
GPU Device 0: "Turing" with compute capability 7.5

Executing tasks on host / device
Task [0], thread [0] executing on device (940)
Task [3], thread [2] executing on device (915)
Task [2], thread [3] executing on device (641)
Task [1], thread [1] executing on device (654)
Task [4], thread [2] executing on device (865)
Task [5], thread [0] executing on device (679)
Task [6], thread [3] executing on device (858)
Task [7], thread [1] executing on device (183)
Task [8], thread [1] executing on device (375)
Task [9], thread [0] executing on device (633)
Task [10], thread [2] executing on device (966)
Task [11], thread [3] executing on host (64)
Task [12], thread [3] executing on device (139)
Task [13], thread [1] executing on device (992)
Task [14], thread [0] executing on device (571)
Task [15], thread [3] executing on device (831)
Task [16], thread [1] executing on device (481)
Task [17], thread [0] executing on device (684)
Task [18], thread [2] executing on device (736)
Task [19], thread [1] executing on device (617)
Task [20], thread [0] executing on device (911)
Task [21], thread [3] executing on device (676)
Task [22], thread [1] executing on device (700)
Task [23], thread [3] executing on host (64)
Task [24], thread [1] executing on device (756)
Task [25], thread [2] executing on device (826)
Task [26], thread [0] executing on device (512)
Task [27], thread [3] executing on device (178)
Task [28], thread [2] executing on device (883)
Task [29], thread [0] executing on device (565)
Task [30], thread [1] executing on device (576)
Task [31], thread [3] executing on device (602)
Task [32], thread [2] executing on device (851)
Task [33], thread [0] executing on device (894)
Task [34], thread [3] executing on device (160)
Task [35], thread [0] executing on device (600)
Task [36], thread [1] executing on device (557)
Task [37], thread [2] executing on device (113)
Task [38], thread [1] executing on device (814)
Task [39], thread [0] executing on device (594)
All Done!
+ ./0_Simple/asyncAPI/asyncAPI
[./0_Simple/asyncAPI/asyncAPI] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER]
time spent executing by the GPU: 11.52
time spent by CPU in CUDA calls: 0.02
CPU executed 93514 iterations while waiting for GPU to finish
+ ./0_Simple/bf16TensorCoreGemm/bf16TensorCoreGemm
Initializing...
GPU Device 0: "Turing" with compute capability 7.5

bf16TensorCoreGemm requires requires SM 8.0 or higher to use Tensor Cores.  Exiting...
+ ./0_Simple/binaryPartitionCG/binaryPartitionCG
GPU Device 0: "Turing" with compute capability 7.5


Launching 100 blocks with 1024 threads...

Array size = 102400 Num of Odds = 50945 Sum of Odds = 1272565 Sum of Evens 1233938
...
```
## CUDA Examples Running Outputs

```
./0_Simple/UnifiedMemoryStreams/UnifiedMemoryStreams: error while loading shared libraries: libcublas.so.11: cannot open shared object file: No such file or directory
[./0_Simple/asyncAPI/asyncAPI] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER]
time spent executing by the GPU: 11.65
time spent by CPU in CUDA calls: 0.02
CPU executed 88856 iterations while waiting for GPU to finish
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
|  BLOCK 7 launched by thread 1 of block 1
|  BLOCK 6 launched by thread 1 of block 1
|  BLOCK 8 launched by thread 1 of block 0
|  BLOCK 9 launched by thread 1 of block 0
GPU Device 0: "Turing" with compute capability 7.5

Initializing data:
Running quicksort on 128 elements
Launching kernel on the GPU
Validating results: OK
CUDA Clock sample
GPU Device 0: "Turing" with compute capability 7.5

Average clocks/block = 2584.109375
./0_Simple/clock_nvrtc/clock_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
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
Time: 182.599228 ms
TFLOPS: 0.75
Initializing...
GPU Device 0: "Turing" with compute capability 7.5

dmmaTensorCoreGemm requires SM 8.0 or higher.  Exiting...
GPU Device 0: "Turing" with compute capability 7.5

Result native operators	: 665574.000000 
Result intrinsics	: 665574.000000 
&&&& fp16ScalarProduct PASSED
[globalToShmemAsyncCopy] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

MatrixA(1280,1280), MatrixB(1280,1280)
Running kernel = 0 - AsyncCopyMultiStageLargeChunk
Computing result using CUDA Kernel...
done
Performance= 202.49 GFlop/s, Time= 20.714 msec, Size= 4194304000 Ops, WorkgroupSize= 256 threads/block
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
Time: 71.960960 ms
TOPS: 1.91
CUDA inline PTX assembler sample
GPU Device 0: "Turing" with compute capability 7.5

Test Successful.
./0_Simple/inlinePTX_nvrtc/inlinePTX_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
[Matrix Multiply Using CUDA] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

MatrixA(320,320), MatrixB(640,320)
Computing result using CUDA Kernel...
done
Performance= 617.13 GFlop/s, Time= 0.212 msec, Size= 131072000 Ops, WorkgroupSize= 1024 threads/block
Checking computed result for correctness: Result = PASS

NOTE: The CUDA Samples are not meant for performancemeasurements. Results may vary when GPU Boost is enabled.
./0_Simple/matrixMulCUBLAS/matrixMulCUBLAS: error while loading shared libraries: libcublas.so.11: cannot open shared object file: No such file or directory
[ matrixMulDrv (Driver API) ]
> Using CUDA Device [0]: GeForce GTX 1650 SUPER
> GPU Device has SM 7.5 compute capability
  Total amount of global memory:     4066574336 bytes
> findModulePath found file at <./0_Simple/matrixMulDrv/data/matrixMul_kernel64.fatbin>
> initCUDA loading module: <./0_Simple/matrixMulDrv/data/matrixMul_kernel64.fatbin>
Processing time: 0.078000 (ms)
Checking computed result for correctness: Result = PASS

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
./0_Simple/matrixMul_nvrtc/matrixMul_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
> findModulePath found file at <./0_Simple/memMapIPCDrv/data/memMapIpc_kernel64.fatbin>
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
./0_Simple/simpleAssert_nvrtc/simpleAssert_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
simpleAtomicIntrinsics starting...
GPU Device 0: "Turing" with compute capability 7.5

Processing time: 60.381001 (ms)
simpleAtomicIntrinsics completed, returned OK
./0_Simple/simpleAtomicIntrinsics_nvrtc/simpleAtomicIntrinsics_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
./0_Simple/simpleAttributes/simpleAttributes Starting...

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
Processing time: 0.007 msec
3510.86 Mtexlookups/sec
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
Processing time: 0.082 msec
15984.39 Mtexlookups/sec
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
 Memcpy host to device	: 1.349152 ms (12.435379 GB/s)
 Memcpy device to host	: 1.371840 ms (12.229718 GB/s)
 Kernel			: 0.246272 ms (681.247408 GB/s)

Theoretical limits for speedup gained from overlapped data transfers:
No overlap at all (transfer-kernel-transfer): 2.967264 ms 
Compute can overlap with one transfer: 2.720992 ms
Compute can overlap with both data transfers: 1.371840 ms

Average measured timings over 10 repetitions:
 Avg. time when execution fully serialized	: 2.923894 ms
 Avg. time when overlapped using 4 streams	: 1.691261 ms
 Avg. speedup gained (serialized - overlapped)	: 1.232634 ms

Measured throughput:
 Fully serialized execution		: 11.475939 GB/s
 Overlapped using 4 streams		: 19.839893 GB/s
Starting simpleMultiGPU
CUDA-capable device count: 1
Generating input data...

Computing with 1 GPUs...
  GPU Processing time: 12.420000 (ms)

Computing with Host CPU...

Comparing GPU and Host CPU results...
  GPU sum: 16777296.000000
  CPU sum: 16777294.395033
  Relative difference: 9.566307E-08 

starting Simple Occupancy

[ Manual configuration with 32 threads per block ]
Potential occupancy: 50%
Elapsed time: 0.100448ms

[ Automatic, occupancy-based configuration ]
Suggested block size: 1024
Minimum grid size for maximum occupancy: 20
Potential occupancy: 100%
Elapsed time: 0.057024ms

Test PASSED

[./0_Simple/simpleP2P/simpleP2P] - Starting...
Checking for multiple GPUs...
CUDA-capable device count: 1
Two or more GPUs with Peer-to-Peer access capability are required for ./0_Simple/simpleP2P/simpleP2P.
Waiving test.
simplePitchLinearTexture starting...

GPU Device 0: "Turing" with compute capability 7.5


Bandwidth (GB/s) for pitch linear: 1.51e+02; for array: 1.57e+02

Texture fetch rate (Mpix/s) for pitch linear: 1.88e+04; for array: 1.96e+04

simplePitchLinearTexture completed, returned OK
GPU Device 0: "Turing" with compute capability 7.5

Device 0: "GeForce GTX 1650 SUPER" with Compute 7.5 capability
printf() is called. Output:

[1, 0]:		Value is:10
[1, 1]:		Value is:10
[1, 2]:		Value is:10
[1, 3]:		Value is:10
[1, 4]:		Value is:10
[1, 5]:		Value is:10
[1, 6]:		Value is:10
[1, 7]:		Value is:10
[0, 0]:		Value is:10
[0, 1]:		Value is:10
[0, 2]:		Value is:10
[0, 3]:		Value is:10
[0, 4]:		Value is:10
[0, 5]:		Value is:10
[0, 6]:		Value is:10
[0, 7]:		Value is:10
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
memcopy:	5.32
kernel:		0.92
non-streamed:	6.13
4 streams:	5.65
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
Processing time: 59.866001 (ms)
Compare OK

> runTest<int,64>
GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER] has 20 Multi-Processors
Processing time: 0.113000 (ms)
Compare OK


[simpleTemplates] -> Test Results: 0 Failures
./0_Simple/simpleTemplates_nvrtc/simpleTemplates_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
simpleTexture starting...
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
./0_Simple/simpleVoteIntrinsics_nvrtc/simpleVoteIntrinsics_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
  Device 0: <          Turing >, Compute SM 7.5 detected
> Using CUDA Host Allocated (cudaHostAlloc)
> vectorAddGPU kernel will add vectors using mapped CPU memory...
> Checking the results from vectorAddGPU() ...
> Releasing CPU memory...
GPU Device 0: "Turing" with compute capability 7.5

Starting basicStreamOrderedAllocation()
> Checking the results from vectorAddGPU() ...
basicStreamOrderedAllocation PASSED
Starting streamOrderedAllocationPostSync()
Total elapsed time = 36.543232 ms over 20 iterations
> Checking the results from vectorAddGPU() ...
streamOrderedAllocationPostSync PASSED
No Two or more GPUs with same architecture capable of cuda Memory Pools found.
Waiving the sample
GPU Device 0: "Turing" with compute capability 7.5

CANNOT access pageable memory
systemWideAtomics completed, returned OK 
./0_Simple/template/template Starting...

GPU Device 0: "Turing" with compute capability 7.5

Processing time: 59.638000 (ms)
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
./0_Simple/vectorAdd_nvrtc/vectorAdd_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
GPU Device 0: "Turing" with compute capability 7.5

Running ........................................................

Overall Time For matrixMultiplyPerf 

Printing Average of 20 measurements in (ms)
Size_KB	 UMhint	UMhntAs	 UMeasy	  0Copy	MemCopy	CpAsync	CpHpglk	CpPglAs
4	  0.227	  0.247	  0.285	  0.013	  0.026	  0.021	  0.030	  0.029
16	  0.239	  0.246	  0.372	  0.030	  0.047	  0.036	  0.046	  0.046
64	  0.382	  0.292	  0.690	  0.090	  0.111	  0.102	  0.112	  0.103
256	  0.817	  0.761	  1.221	  0.443	  0.407	  0.389	  0.363	  0.350
1024	  2.375	  2.319	  3.001	  2.515	  1.762	  1.707	  1.423	  1.412
4096	  9.634	  9.312	 12.554	 17.826	  8.549	  8.598	  7.576	  7.535
16384	 49.889	 47.024	 60.957	131.519	 49.658	 46.848	 43.200	 43.163

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
   32000000			159.8

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
     0 145.87 
Unidirectional P2P=Enabled Bandwidth (P2P Writes) Matrix (GB/s)
   D\D     0 
     0 138.93 
Bidirectional P2P=Disabled Bandwidth Matrix (GB/s)
   D\D     0 
     0 149.45 
Bidirectional P2P=Enabled Bandwidth Matrix (GB/s)
   D\D     0 
     0 147.52 
P2P=Disabled Latency Matrix (us)
   GPU     0 
     0   1.44 

   CPU     0 
     0   1.75 
P2P=Enabled Latency (P2P Writes) Matrix (us)
   GPU     0 
     0   1.21 

   CPU     0 
     0   1.69 

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
  CUDA resize nv12(1920x1080 --> 640x480), batch: 24, average time: 0.307 ms ==> 0.013 ms/frame
  CUDA convert nv12(640x480) to bgr(640x480), batch: 24, average time: 0.670 ms ==> 0.028 ms/frame

TEST#2:
  CUDA convert nv12(1920x1080) to bgr(1920x1080), batch: 24, average time: 4.571 ms ==> 0.190 ms/frame
  CUDA resize bgr(1920x1080 --> 640x480), batch: 24, average time: 3.384 ms ==> 0.141 ms/frame
./3_Imaging/convolutionFFT2D/convolutionFFT2D: error while loading shared libraries: libcufft.so.10: cannot open shared object file: No such file or directory
[./3_Imaging/convolutionSeparable/convolutionSeparable] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

Image Width x Height = 3072 x 3072

Allocating and initializing host arrays...
Allocating and initializing CUDA arrays...
Running GPU convolution (16 identical iterations)...

convolutionSeparable, Throughput = 8150.4346 MPixels/sec, Time = 0.00116 s, Size = 9437184 Pixels, NumDevsUsed = 1, Workgroup = 0

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
Average convolutionRowsGPU() time: 0.636600 msecs; //7412.176987 Mpix/s
Copying convolutionRowGPU() output back to the texture...
cudaMemcpyToArray() time: 0.258000 msecs; //18289.117242 Mpix/s
Running GPU columns convolution (10 iterations)
Average convolutionColumnsGPU() time: 0.600600 msecs; //7856.463482 Mpix/s
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
Running CUDA 2 (GPU) version... 18029.161075 MPix/s //0.014540 ms
Success
Running CUDA short (GPU) version... Success
Dumping result to barbara_gold1.bmp... Success
Dumping result to barbara_gold2.bmp... Success
Dumping result to barbara_cuda1.bmp... Success
Dumping result to barbara_cuda2.bmp... Success
Dumping result to barbara_cuda_short.bmp... Success
Processing time (CUDA 1)    : 0.071300 ms 
Processing time (CUDA 2)    : 0.014540 ms 
Processing time (CUDA short): 0.062000 ms 
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

dxtc, Throughput = 91.9481 MPixels/s, Time = 0.00285 s, Size = 262144 Pixels, NumDevsUsed = 1, Workgroup = 64

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

histogram64() time (average) : 0.00073 sec, 92372.8373 MB/sec

histogram64, Throughput = 92372.8373 MB/s, Time = 0.00073 s, Size = 67108864 Bytes, NumDevsUsed = 1, Workgroup = 64

Validating GPU results...
 ...reading back GPU results
 ...histogram64CPU()
 ...comparing the results...
 ...64-bin histograms match

Shutting down 64-bin histogram...


Initializing 256-bin histogram...
Running 256-bin GPU histogram for 67108864 bytes (16 runs)...

histogram256() time (average) : 0.00060 sec, 111941.3911 MB/sec

histogram256, Throughput = 111941.3911 MB/s, Time = 0.00060 s, Size = 67108864 Bytes, NumDevsUsed = 1, Workgroup = 192

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
GPU processing time : 1.0710 (ms)
Pixel throughput    : 318.504 Mpixels/sec
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
BlackScholesGPU() time    : 0.490234 msec
Effective memory bandwidth: 163.187251 GB/s
Gigaoptions per second    : 16.318725     

BlackScholes, Throughput = 16.3187 GOptions/s, Time = 0.00049 s, Size = 8000000 options, NumDevsUsed = 1, Workgroup = 128

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
./4_Finance/BlackScholes_nvrtc/BlackScholes_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
./4_Finance/MonteCarloMultiGPU/MonteCarloMultiGPU: error while loading shared libraries: libcurand.so.10: cannot open shared object file: No such file or directory
Sobol Quasi-Random Number Generator Starting...

> number of vectors = 100000
> number of dimensions = 100
GPU Device 0: "Turing" with compute capability 7.5

Allocating CPU memory...
Allocating GPU memory...
Initializing direction numbers...
Copying direction numbers to device...
Executing QRNG on GPU...
Gsamples/s: 25.2525
Reading results from GPU...

Executing QRNG on CPU...
Gsamples/s: 0.254563
Checking results...
L1-Error: 0
Shutting down...
[./4_Finance/binomialOptions/binomialOptions] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

Generating input data...
Running GPU binomial tree...
Options count            : 1024     
Time steps               : 2048     
binomialOptionsGPU() time: 3.120000 msec
Options per second       : 328205.140244     
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
./4_Finance/binomialOptions_nvrtc/binomialOptions_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
./4_Finance/quasirandomGenerator/quasirandomGenerator Starting...

Allocating GPU memory...
Allocating CPU memory...
Initializing QRNG tables...

Testing QRNG...

quasirandomGenerator, Throughput = 14.0340 GNumbers/s, Time = 0.00022 s, Size = 3145728 Numbers, NumDevsUsed = 1, Workgroup = 384

Reading GPU results...
Comparing to the CPU results...

L1 norm: 7.275964E-12

Testing inverseCNDgpu()...

quasirandomGenerator-inverse, Throughput = 30.6900 GNumbers/s, Time = 0.00010 s, Size = 3145728 Numbers, NumDevsUsed = 1, Workgroup = 128
Reading GPU results...

Comparing to the CPU results...
L1 norm: 9.439909E-08

Shutting down...
./4_Finance/quasirandomGenerator_nvrtc/quasirandomGenerator_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
./6_Advanced/FDTD3d/FDTD3d Starting...

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
elapsed time of kernels launched to LOW priority stream: 6.810 ms
elapsed time of kernels launched to HI  priority stream: 3.569 ms
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
Avg. time: 1.307188 ms / Copy throughput: 35.623051 GB/s.
	TEST OK
uint16...
Avg. time: 0.913219 ms / Copy throughput: 50.991080 GB/s.
	TEST OK
RGBA8_misaligned...
Avg. time: 0.764938 ms / Copy throughput: 60.875573 GB/s.
	TEST OK
LA32_misaligned...
Avg. time: 0.633313 ms / Copy throughput: 73.527694 GB/s.
	TEST OK
RGB32_misaligned...
Avg. time: 0.710844 ms / Copy throughput: 65.508081 GB/s.
	TEST OK
RGBA32_misaligned...
Avg. time: 0.666062 ms / Copy throughput: 69.912375 GB/s.
	TEST OK
Testing aligned types...
RGBA8...
Avg. time: 0.706688 ms / Copy throughput: 65.893353 GB/s.
	TEST OK
I32...
Avg. time: 0.705719 ms / Copy throughput: 65.983806 GB/s.
	TEST OK
LA32...
Avg. time: 0.633969 ms / Copy throughput: 73.451583 GB/s.
	TEST OK
RGB32...
Avg. time: 0.631750 ms / Copy throughput: 73.709554 GB/s.
	TEST OK
RGBA32...
Avg. time: 0.631125 ms / Copy throughput: 73.782549 GB/s.
	TEST OK
RGBA32_2...
Avg. time: 0.670406 ms / Copy throughput: 69.459393 GB/s.
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
Sorted 5000 elems in 0.785 ms (6.366 Melems/sec)
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

GPU Final, residual = 1.600115e-06, kernel execution time = 13.285216 ms
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
Average time step 1: 1.715950 ms
Average time step 2, one intervals: 1.962183 ms
Average time step 2, mult intervals: 4.445660 ms
Average time TOTAL: 8.136761 ms
Test Succeeded!
./6_Advanced/fastWalshTransform/fastWalshTransform Starting...

GPU Device 0: "Turing" with compute capability 7.5

Initializing data...
...allocating CPU memory
...allocating GPU memory
...generating data
Data length: 8388608; kernel length: 128
Running GPU dyadic convolution using Fast Walsh Transform...
GPU time: 9.598000 ms; GOP/s: 30.152843
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
Time per equation: 21.1140632629395 us

Check against Host computation...

GPU Device 0: "Turing" with compute capability 7.5

CPU iterations : 2954
CPU error : 4.988e-03
CPU Processing time: 1789.118042 (ms)
GPU iterations : 2954
GPU error : 4.988e-03
GPU Processing time: 157.561005 (ms)
&&&& jacobiCudaGraphs PASSED
[./6_Advanced/lineOfSight/lineOfSight] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

Line of sight
Average time: 0.018160 ms

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
Time: 10.225000 ms
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
ptxas info    : 0 bytes gmem
ptxas info    : Compiling entry function 'myKernel' for 'sm_75'
ptxas info    : Function properties for myKernel
ptxas         .     0 bytes stack frame, 0 bytes spill stores, 0 bytes spill loads
ptxas info    : Used 8 registers, 360 bytes cmem[0]
info    : 0 bytes gmem
info    : Function properties for 'myKernel':
info    : used 8 registers, 0 stack, 0 bytes smem, 360 bytes cmem[0], 0 bytes lmem
CUDA kernel launched
./6_Advanced/radixSortThrust/radixSortThrust Starting...

GPU Device 0: "Turing" with compute capability 7.5


Sorting 1048576 32-bit unsigned int keys and values

radixSortThrust, Throughput = 880.2755 MElements/s, Time = 0.00119 s, Size = 1048576 elements
Test passed
./6_Advanced/reduction/reduction Starting...

GPU Device 0: "Turing" with compute capability 7.5

Using Device 0: GeForce GTX 1650 SUPER

Reducing array of type int

16777216 elements
256 threads (max)
64 blocks

Reduction, Throughput = 171.3315 GB/s, Time = 0.00039 s, Size = 16777216 Elements, NumDevsUsed = 1, Workgroup = 256

GPU result = 2139353471
CPU result = 2139353471

Test passed
reductionMultiBlockCG Starting...

GPU Device 0: "Turing" with compute capability 7.5

33554432 elements
numThreads: 1024
numBlocks: 20

Launching SinglePass Multi Block Cooperative Groups kernel
Average time: 1.002170 ms
Bandwidth:    133.927142 GB/s

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
GPU time: 0.073000 msecs.
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


scan, Throughput = 378.4599 MElements/s, Time = 0.00069 s, Size = 262144 Elements, NumDevsUsed = 1, Workgroup = 256

Shutting down...
./6_Advanced/segmentationTreeThrust/segmentationTreeThrust Starting...

GPU Device 0: "Turing" with compute capability 7.5

* Building segmentation tree... done in 63.264 (ms)
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
Time (ms): 0.030720
65536 elements scanned in 0.030720 ms -> 2133.333496 MegaElements/s
CPU verify result diff (GPUvsCPU) = 0
CPU sum (naive) took 0.027180 ms

Computing Integral Image Test on size 1920 x 1080 synthetic data
---------------------------------------------------
Method: Fast  Time (GPU Timer): 0.069600 ms Diff = 0
Method: Vertical Scan  Time (GPU Timer): 0.126656 ms 
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
Average time: 0.405000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 128 (8192 arrays per batch)...
Average time: 0.495000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 256 (4096 arrays per batch)...
Average time: 0.676000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 512 (2048 arrays per batch)...
Average time: 0.728000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 1024 (1024 arrays per batch)...
Average time: 0.855000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 2048 (512 arrays per batch)...
Average time: 1.015000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 4096 (256 arrays per batch)...
Average time: 1.358000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 8192 (128 arrays per batch)...
Average time: 1.861000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 16384 (64 arrays per batch)...
Average time: 2.389000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 32768 (32 arrays per batch)...
Average time: 3.017000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 65536 (16 arrays per batch)...
Average time: 3.833000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 131072 (8 arrays per batch)...
Average time: 4.636000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 262144 (4 arrays per batch)...
Average time: 5.635000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 524288 (2 arrays per batch)...
Average time: 6.780000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 1048576 (1 arrays per batch)...
Average time: 7.818000 ms

sortingNetworks-bitonic, Throughput = 134.1233 MElements/s, Time = 0.00782 s, Size = 1048576 elements, NumDevsUsed = 1, Workgroup = 512

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
Bandwidth:    123.253191 GB/s

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
<CUDA Device=0, Context=0x55ae769fb040, Thread=0> - ThreadProc() Launched...
<CUDA Device=0, Context=0x55ae769fb040, Thread=1> - ThreadProc() Launched...
<CUDA Device=0, Context=0x55ae769fb040, Thread=0> - ThreadProc() Finished!

<CUDA Device=0, Context=0x55ae769fb040, Thread=1> - ThreadProc() Finished!

Transpose Starting...

GPU Device 0: "Turing" with compute capability 7.5

> Device 0: "GeForce GTX 1650 SUPER"
> SM Capability 7.5 detected:
> [GeForce GTX 1650 SUPER] has 20 MP(s) x 64 (Cores/MP) = 1280 (Cores)
> Compute performance scaling factor = 1.00

Matrix size: 1024x1024 (64x64 tiles), tile size: 16x16, block size: 16x16

transpose simple copy       , Throughput = 146.9992 GB/s, Time = 0.05315 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose shared memory copy, Throughput = 145.4326 GB/s, Time = 0.05372 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose naive             , Throughput = 117.3646 GB/s, Time = 0.06657 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose coalesced         , Throughput = 137.7240 GB/s, Time = 0.05673 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose optimized         , Throughput = 146.9708 GB/s, Time = 0.05316 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose coarse-grained    , Throughput = 147.9649 GB/s, Time = 0.05280 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose fine-grained      , Throughput = 145.7643 GB/s, Time = 0.05360 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose diagonal          , Throughput = 123.4299 GB/s, Time = 0.06330 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
Test passed
GPU Device 0: "Turing" with compute capability 7.5

CPU max matches GPU max

Warp Aggregated Atomics PASSED 
./7_CUDALibraries/MC_EstimatePiInlineP/MC_EstimatePiInlineP: error while loading shared libraries: libcurand.so.10: cannot open shared object file: No such file or directory
./7_CUDALibraries/MC_EstimatePiInlineQ/MC_EstimatePiInlineQ: error while loading shared libraries: libcurand.so.10: cannot open shared object file: No such file or directory
./7_CUDALibraries/MC_EstimatePiP/MC_EstimatePiP: error while loading shared libraries: libcurand.so.10: cannot open shared object file: No such file or directory
./7_CUDALibraries/MC_EstimatePiQ/MC_EstimatePiQ: error while loading shared libraries: libcurand.so.10: cannot open shared object file: No such file or directory
./7_CUDALibraries/MC_SingleAsianOptionP/MC_SingleAsianOptionP: error while loading shared libraries: libcurand.so.10: cannot open shared object file: No such file or directory
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

MersenneTwisterGP11213, Throughput = 17.4672 GNumbers/s, Time = 0.00014 s, Size = 2400000 Numbers
Shutting down...
./7_CUDALibraries/batchCUBLAS/batchCUBLAS: error while loading shared libraries: libcublas.so.11: cannot open shared object file: No such file or directory
NPP Library Version 11.3.2
CUDA Driver  Version: 11.2
CUDA Runtime Version: 11.2

Input file load succeeded.
Lena_CompressedMarkerLabelsUF_8Way_512x512_32u succeeded, compressed label count is 553.
Input file load succeeded.
CT_Skull_CompressedMarkerLabelsUF_8Way_512x512_32u succeeded, compressed label count is 414.
Input file load succeeded.
PCB_METAL_CompressedMarkerLabelsUF_8Way_509x335_32u succeeded, compressed label count is 3731.
Input file load succeeded.
PCB2_CompressedMarkerLabelsUF_8Way_1024x683_32u succeeded, compressed label count is 1223.
Input file load succeeded.
PCB_CompressedMarkerLabelsUF_8Way_1280x720_32u succeeded, compressed label count is 1441.


Lena_CompressedMarkerLabelsUFBatch_8Way_512x512_32u succeeded, compressed label count is 553.
CT_Skull_CompressedMarkerLabelsUFBatch_8Way_512x512_32u succeeded, compressed label count is 416.
PCB_METAL_CompressedMarkerLabelsUFBatch_8Way_509x335_32u succeeded, compressed label count is 3731.
PCB2_CompressedMarkerLabelsUFBatch_8Way_1024x683_32u succeeded, compressed label count is 1222.
PCB_CompressedMarkerLabelsUFBatch_8Way_1280x720_32u succeeded, compressed label count is 1440.
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
./7_CUDALibraries/conjugateGradientPrecond/conjugateGradientPrecond: error while loading shared libraries: libcublas.so.11: cannot open shared object file: No such file or directory
./7_CUDALibraries/conjugateGradientUM/conjugateGradientUM: error while loading shared libraries: libcublas.so.11: cannot open shared object file: No such file or directory
Error: Condition (allocation_cb == 1) failed at cuHook.cpp:115
cuHook sample failed (Didn't receive the allocation callback)
/tmp/e: line 132:  3645 Segmentation fault      ./7_CUDALibraries/cuHook/libcuhook.so.1
./7_CUDALibraries/cuSolverDn_LinearSolver/cuSolverDn_LinearSolver: error while loading shared libraries: libcusolver.so.11: cannot open shared object file: No such file or directory
./7_CUDALibraries/cuSolverRf/cuSolverRf: error while loading shared libraries: libcusolver.so.11: cannot open shared object file: No such file or directory
./7_CUDALibraries/cuSolverSp_LinearSolver/cuSolverSp_LinearSolver: error while loading shared libraries: libcusolver.so.11: cannot open shared object file: No such file or directory
./7_CUDALibraries/cuSolverSp_LowlevelCholesky/cuSolverSp_LowlevelCholesky: error while loading shared libraries: libcusolver.so.11: cannot open shared object file: No such file or directory
./7_CUDALibraries/cuSolverSp_LowlevelQR/cuSolverSp_LowlevelQR: error while loading shared libraries: libcusolver.so.11: cannot open shared object file: No such file or directory
./7_CUDALibraries/nvJPEG/nvJPEG: error while loading shared libraries: libnvjpeg.so.11: cannot open shared object file: No such file or directory
./7_CUDALibraries/nvJPEG_encoder/nvJPEG_encoder: error while loading shared libraries: libnvjpeg.so.11: cannot open shared object file: No such file or directory
./7_CUDALibraries/simpleCUBLAS/simpleCUBLAS: error while loading shared libraries: libcublas.so.11: cannot open shared object file: No such file or directory
./7_CUDALibraries/simpleCUBLASXT/simpleCUBLASXT: error while loading shared libraries: libcublas.so.11: cannot open shared object file: No such file or directory
./7_CUDALibraries/simpleCUFFT/simpleCUFFT: error while loading shared libraries: libcufft.so.10: cannot open shared object file: No such file or directory
./7_CUDALibraries/simpleCUFFT_2d_MGPU/simpleCUFFT_2d_MGPU: error while loading shared libraries: libcufft.so.10: cannot open shared object file: No such file or directory
./7_CUDALibraries/simpleCUFFT_MGPU/simpleCUFFT_MGPU: error while loading shared libraries: libcufft.so.10: cannot open shared object file: No such file or directory
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
BlackScholesGPU() time    : 0.491572 msec
Effective memory bandwidth: 162.743113 GB/s
Gigaoptions per second    : 16.274311     

BlackScholes, Throughput = 16.2743 GOptions/s, Time = 0.00049 s, Size = 8000000 options, NumDevsUsed = 1, Workgroup = 128

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
./bin/x86_64/linux/release/BlackScholes_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
./bin/x86_64/linux/release/FDTD3d Starting...

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
./bin/x86_64/linux/release/MC_EstimatePiInlineP: error while loading shared libraries: libcurand.so.10: cannot open shared object file: No such file or directory
./bin/x86_64/linux/release/MC_EstimatePiInlineQ: error while loading shared libraries: libcurand.so.10: cannot open shared object file: No such file or directory
./bin/x86_64/linux/release/MC_EstimatePiP: error while loading shared libraries: libcurand.so.10: cannot open shared object file: No such file or directory
./bin/x86_64/linux/release/MC_EstimatePiQ: error while loading shared libraries: libcurand.so.10: cannot open shared object file: No such file or directory
./bin/x86_64/linux/release/MC_SingleAsianOptionP: error while loading shared libraries: libcurand.so.10: cannot open shared object file: No such file or directory
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

MersenneTwisterGP11213, Throughput = 20.8514 GNumbers/s, Time = 0.00012 s, Size = 2400000 Numbers
Shutting down...
./bin/x86_64/linux/release/MonteCarloMultiGPU: error while loading shared libraries: libcurand.so.10: cannot open shared object file: No such file or directory
GPU Device 0: "Turing" with compute capability 7.5


TEST#1:
  CUDA resize nv12(1920x1080 --> 640x480), batch: 24, average time: 0.294 ms ==> 0.012 ms/frame
  CUDA convert nv12(640x480) to bgr(640x480), batch: 24, average time: 0.687 ms ==> 0.029 ms/frame

TEST#2:
  CUDA convert nv12(1920x1080) to bgr(1920x1080), batch: 24, average time: 4.691 ms ==> 0.195 ms/frame
  CUDA resize bgr(1920x1080 --> 640x480), batch: 24, average time: 3.386 ms ==> 0.141 ms/frame
Sobol Quasi-Random Number Generator Starting...

> number of vectors = 100000
> number of dimensions = 100
GPU Device 0: "Turing" with compute capability 7.5

Allocating CPU memory...
Allocating GPU memory...
Initializing direction numbers...
Copying direction numbers to device...
Executing QRNG on GPU...
Gsamples/s: 22.4215
Reading results from GPU...

Executing QRNG on CPU...
Gsamples/s: 0.253678
Checking results...
L1-Error: 0
Shutting down...
Starting [./bin/x86_64/linux/release/StreamPriorities]...
GPU Device 0: "Turing" with compute capability 7.5

CUDA stream priority range: LOW: 0 to HIGH: -2
elapsed time of kernels launched to LOW priority stream: 7.022 ms
elapsed time of kernels launched to HI  priority stream: 3.679 ms
GPU Device 0: "Turing" with compute capability 7.5

Running ........................................................

Overall Time For matrixMultiplyPerf 

Printing Average of 20 measurements in (ms)
Size_KB	 UMhint	UMhntAs	 UMeasy	  0Copy	MemCopy	CpAsync	CpHpglk	CpPglAs
4	  0.215	  0.220	  0.308	  0.013	  0.026	  0.021	  0.030	  0.029
16	  0.276	  0.249	  0.412	  0.028	  0.045	  0.039	  0.047	  0.055
64	  0.353	  0.296	  0.717	  0.090	  0.108	  0.103	  0.110	  0.101
256	  0.820	  0.729	  1.157	  0.451	  0.420	  0.421	  0.368	  0.358
1024	  2.327	  2.322	  2.872	  2.524	  1.768	  1.746	  1.443	  1.482
4096	  9.996	  9.543	 12.092	 17.788	  8.598	  8.557	  7.591	  7.584
16384	 48.974	 46.990	 60.553	129.174	 46.661	 46.575	 43.293	 43.280

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
./bin/x86_64/linux/release/UnifiedMemoryStreams: error while loading shared libraries: libcublas.so.11: cannot open shared object file: No such file or directory
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
Avg. time: 1.229000 ms / Copy throughput: 37.889350 GB/s.
	TEST OK
uint16...
Avg. time: 0.917313 ms / Copy throughput: 50.763518 GB/s.
	TEST OK
RGBA8_misaligned...
Avg. time: 0.777750 ms / Copy throughput: 59.872721 GB/s.
	TEST OK
LA32_misaligned...
Avg. time: 0.639687 ms / Copy throughput: 72.794937 GB/s.
	TEST OK
RGB32_misaligned...
Avg. time: 0.716625 ms / Copy throughput: 64.979607 GB/s.
	TEST OK
RGBA32_misaligned...
Avg. time: 0.666531 ms / Copy throughput: 69.863204 GB/s.
	TEST OK
Testing aligned types...
RGBA8...
Avg. time: 0.718219 ms / Copy throughput: 64.835414 GB/s.
	TEST OK
I32...
Avg. time: 0.718031 ms / Copy throughput: 64.852346 GB/s.
	TEST OK
LA32...
Avg. time: 0.640188 ms / Copy throughput: 72.738080 GB/s.
	TEST OK
RGB32...
Avg. time: 0.639031 ms / Copy throughput: 72.869693 GB/s.
	TEST OK
RGBA32...
Avg. time: 0.641219 ms / Copy throughput: 72.621101 GB/s.
	TEST OK
RGBA32_2...
Avg. time: 0.670250 ms / Copy throughput: 69.475583 GB/s.
	TEST OK

[alignedTypes] -> Test Results: 0 Failures
Shutting down...
Test passed
[./bin/x86_64/linux/release/asyncAPI] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER]
time spent executing by the GPU: 11.65
time spent by CPU in CUDA calls: 0.02
CPU executed 90984 iterations while waiting for GPU to finish
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
./bin/x86_64/linux/release/batchCUBLAS: error while loading shared libraries: libcublas.so.11: cannot open shared object file: No such file or directory
NPP Library Version 11.3.2
CUDA Driver  Version: 11.2
CUDA Runtime Version: 11.2

Input file load succeeded.
Lena_CompressedMarkerLabelsUF_8Way_512x512_32u succeeded, compressed label count is 553.
Input file load succeeded.
CT_Skull_CompressedMarkerLabelsUF_8Way_512x512_32u succeeded, compressed label count is 415.
Input file load succeeded.
PCB_METAL_CompressedMarkerLabelsUF_8Way_509x335_32u succeeded, compressed label count is 3731.
Input file load succeeded.
PCB2_CompressedMarkerLabelsUF_8Way_1024x683_32u succeeded, compressed label count is 1223.
Input file load succeeded.
PCB_CompressedMarkerLabelsUF_8Way_1280x720_32u succeeded, compressed label count is 1441.


Lena_CompressedMarkerLabelsUFBatch_8Way_512x512_32u succeeded, compressed label count is 554.
CT_Skull_CompressedMarkerLabelsUFBatch_8Way_512x512_32u succeeded, compressed label count is 416.
PCB_METAL_CompressedMarkerLabelsUFBatch_8Way_509x335_32u succeeded, compressed label count is 3731.
PCB2_CompressedMarkerLabelsUFBatch_8Way_1024x683_32u succeeded, compressed label count is 1223.
PCB_CompressedMarkerLabelsUFBatch_8Way_1280x720_32u succeeded, compressed label count is 1440.
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
binomialOptionsGPU() time: 3.104000 msec
Options per second       : 329896.897486     
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
./bin/x86_64/linux/release/binomialOptions_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
GPU Device 0: "Turing" with compute capability 7.5

Cannot find the input text file
. Exiting..
GPU Device 0: "Turing" with compute capability 7.5

GPU device GeForce GTX 1650 SUPER has compute capabilities (SM 7.5)
Running qsort on 5000 elements with seed 100, on GeForce GTX 1650 SUPER
    cdpAdvancedQuicksort PASSED
Sorted 5000 elems in 0.694 ms (7.200 Melems/sec)
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

Average clocks/block = 2584.718750
./bin/x86_64/linux/release/clock_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
[./bin/x86_64/linux/release/concurrentKernels] - Starting...
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

GPU Final, residual = 1.600115e-06, kernel execution time = 13.244544 ms
Test Summary:  Error amount = 0.000000 
&&&& conjugateGradientMultiBlockCG PASSED
Starting [conjugateGradientMultiDeviceCG]...
GPU Device 0: "GeForce GTX 1650 SUPER" with compute capability 7.5
No Two or more GPUs with same architecture capable of cooperativeMultiDeviceLaunch & concurrentManagedAccess found. 
Waiving the sample
./bin/x86_64/linux/release/conjugateGradientPrecond: error while loading shared libraries: libcublas.so.11: cannot open shared object file: No such file or directory
./bin/x86_64/linux/release/conjugateGradientUM: error while loading shared libraries: libcublas.so.11: cannot open shared object file: No such file or directory
./bin/x86_64/linux/release/convolutionFFT2D: error while loading shared libraries: libcufft.so.10: cannot open shared object file: No such file or directory
[./bin/x86_64/linux/release/convolutionSeparable] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

Image Width x Height = 3072 x 3072

Allocating and initializing host arrays...
Allocating and initializing CUDA arrays...
Running GPU convolution (16 identical iterations)...

convolutionSeparable, Throughput = 6941.9773 MPixels/sec, Time = 0.00136 s, Size = 9437184 Pixels, NumDevsUsed = 1, Workgroup = 0

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
Average convolutionRowsGPU() time: 0.740500 msecs; //6372.169872 Mpix/s
Copying convolutionRowGPU() output back to the texture...
cudaMemcpyToArray() time: 0.255000 msecs; //18504.282699 Mpix/s
Running GPU columns convolution (10 iterations)
Average convolutionColumnsGPU() time: 0.715300 msecs; //6596.661873 Mpix/s
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
./bin/x86_64/linux/release/cuSolverDn_LinearSolver: error while loading shared libraries: libcusolver.so.11: cannot open shared object file: No such file or directory
./bin/x86_64/linux/release/cuSolverRf: error while loading shared libraries: libcusolver.so.11: cannot open shared object file: No such file or directory
./bin/x86_64/linux/release/cuSolverSp_LinearSolver: error while loading shared libraries: libcusolver.so.11: cannot open shared object file: No such file or directory
./bin/x86_64/linux/release/cuSolverSp_LowlevelCholesky: error while loading shared libraries: libcusolver.so.11: cannot open shared object file: No such file or directory
./bin/x86_64/linux/release/cuSolverSp_LowlevelQR: error while loading shared libraries: libcusolver.so.11: cannot open shared object file: No such file or directory
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
Time: 188.803207 ms
TFLOPS: 0.73
./bin/x86_64/linux/release/dct8x8 Starting...

GPU Device 0: "Turing" with compute capability 7.5

CUDA sample DCT/IDCT implementation
===================================
Loading test image: barbara.bmp... [512 x 512]... Success
Running Gold 1 (CPU) version... Success
Running Gold 2 (CPU) version... Success
Running CUDA 1 (GPU) version... Success
Running CUDA 2 (GPU) version... 17593.557242 MPix/s //0.014900 ms
Success
Running CUDA short (GPU) version... Success
Dumping result to barbara_gold1.bmp... Success
Dumping result to barbara_gold2.bmp... Success
Dumping result to barbara_cuda1.bmp... Success
Dumping result to barbara_cuda2.bmp... Success
Dumping result to barbara_cuda_short.bmp... Success
Processing time (CUDA 1)    : 0.057900 ms 
Processing time (CUDA 2)    : 0.014900 ms 
Processing time (CUDA short): 0.059000 ms 
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

dxtc, Throughput = 118.0297 MPixels/s, Time = 0.00222 s, Size = 262144 Pixels, NumDevsUsed = 1, Workgroup = 64

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
Average time step 1: 1.651281 ms
Average time step 2, one intervals: 1.892401 ms
Average time step 2, mult intervals: 4.287807 ms
Average time TOTAL: 7.844680 ms
Test Succeeded!
./bin/x86_64/linux/release/fastWalshTransform Starting...

GPU Device 0: "Turing" with compute capability 7.5

Initializing data...
...allocating CPU memory
...allocating GPU memory
...generating data
Data length: 8388608; kernel length: 128
Running GPU dyadic convolution using Fast Walsh Transform...
GPU time: 9.622000 ms; GOP/s: 30.077633
Reading back GPU results...
Running straightforward CPU dyadic convolution...
Comparing the results...
Shutting down...
L2 norm: 1.021579E-07
Test passed
GPU Device 0: "Turing" with compute capability 7.5

Result native operators	: 662539.000000 
Result intrinsics	: 662539.000000 
&&&& fp16ScalarProduct PASSED
[globalToShmemAsyncCopy] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

MatrixA(1280,1280), MatrixB(1280,1280)
Running kernel = 0 - AsyncCopyMultiStageLargeChunk
Computing result using CUDA Kernel...
done
Performance= 201.62 GFlop/s, Time= 20.803 msec, Size= 4194304000 Ops, WorkgroupSize= 256 threads/block
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

histogram64() time (average) : 0.00057 sec, 118724.2219 MB/sec

histogram64, Throughput = 118724.2219 MB/s, Time = 0.00057 s, Size = 67108864 Bytes, NumDevsUsed = 1, Workgroup = 64

Validating GPU results...
 ...reading back GPU results
 ...histogram64CPU()
 ...comparing the results...
 ...64-bin histograms match

Shutting down 64-bin histogram...


Initializing 256-bin histogram...
Running 256-bin GPU histogram for 67108864 bytes (16 runs)...

histogram256() time (average) : 0.00054 sec, 124275.6691 MB/sec

histogram256, Throughput = 124275.6691 MB/s, Time = 0.00054 s, Size = 67108864 Bytes, NumDevsUsed = 1, Workgroup = 192

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
Time: 89.565277 ms
TOPS: 1.53
CUDA inline PTX assembler sample
GPU Device 0: "Turing" with compute capability 7.5

Test Successful.
./bin/x86_64/linux/release/inlinePTX_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
[Interval Computing]  starting ...

GPU Device 0: "Turing" with compute capability 7.5

> GPU Device has Compute Capabilities SM 7.5

GPU naive implementation
Searching for roots in [0.01, 4]...
Found 2 intervals that may contain the root(s)
 i[0] = [0.999655515093009, 1.00011722206639]
 i[1] = [1.00011907576551, 1.00044661086269]
Number of equations solved: 65536
Time per equation: 16.5699520111084 us

Check against Host computation...

GPU Device 0: "Turing" with compute capability 7.5

CPU iterations : 2954
CPU error : 4.988e-03
CPU Processing time: 1792.833984 (ms)
GPU iterations : 2954
GPU error : 4.988e-03
GPU Processing time: 158.572998 (ms)
&&&& jacobiCudaGraphs PASSED
/tmp/e: line 217:  3988 Segmentation fault      ./bin/x86_64/linux/release/libcuhook.so.1
[./bin/x86_64/linux/release/lineOfSight] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

Line of sight
Average time: 0.017660 ms

Test passed
[Matrix Multiply Using CUDA] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

MatrixA(320,320), MatrixB(640,320)
Computing result using CUDA Kernel...
done
Performance= 518.71 GFlop/s, Time= 0.253 msec, Size= 131072000 Ops, WorkgroupSize= 1024 threads/block
Checking computed result for correctness: Result = PASS

NOTE: The CUDA Samples are not meant for performancemeasurements. Results may vary when GPU Boost is enabled.
./bin/x86_64/linux/release/matrixMulCUBLAS: error while loading shared libraries: libcublas.so.11: cannot open shared object file: No such file or directory
[ matrixMulDrv (Driver API) ]
> Using CUDA Device [0]: GeForce GTX 1650 SUPER
> GPU Device has SM 7.5 compute capability
  Total amount of global memory:     4066574336 bytes
> findModulePath found file at <./0_Simple/matrixMulDrv/data/matrixMul_kernel64.fatbin>
> initCUDA loading module: <./0_Simple/matrixMulDrv/data/matrixMul_kernel64.fatbin>
Processing time: 0.088000 (ms)
Checking computed result for correctness: Result = PASS

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
[ matrixMulDynlinkJIT (CUDA dynamic linking) ]
> Device 0: "GeForce GTX 1650 SUPER" with Compute 7.5 capability
> Compiling CUDA module
> PTX JIT log:

Test run success!
./bin/x86_64/linux/release/matrixMul_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
> findModulePath found file at <./0_Simple/memMapIPCDrv/data/memMapIpc_kernel64.fatbin>
> initCUDA loading module: <./0_Simple/memMapIPCDrv/data/memMapIpc_kernel64.fatbin>
Step 0 done
Process 0: verifying...
./bin/x86_64/linux/release/mergeSort Starting...

GPU Device 0: "Turing" with compute capability 7.5

Allocating and initializing host arrays...

Allocating and initializing CUDA arrays...

Initializing GPU merge sort...
Running GPU merge sort...
Time: 9.185000 ms
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
./bin/x86_64/linux/release/nvJPEG: error while loading shared libraries: libnvjpeg.so.11: cannot open shared object file: No such file or directory
./bin/x86_64/linux/release/nvJPEG_encoder: error while loading shared libraries: libnvjpeg.so.11: cannot open shared object file: No such file or directory
[P2P (Peer-to-Peer) GPU Bandwidth Latency Test]
Device: 0, GeForce GTX 1650 SUPER, pciBusID: 1, pciDeviceID: 0, pciDomainID:0

***NOTE: In case a device doesn't have P2P access to other one, it falls back to normal memcopy procedure.
So you can see lesser Bandwidth (GB/s) and unstable Latency (us) in those cases.

P2P Connectivity Matrix
     D\D     0
     0	     1
Unidirectional P2P=Disabled Bandwidth Matrix (GB/s)
   D\D     0 
     0 146.69 
Unidirectional P2P=Enabled Bandwidth (P2P Writes) Matrix (GB/s)
   D\D     0 
     0 137.67 
Bidirectional P2P=Disabled Bandwidth Matrix (GB/s)
   D\D     0 
     0 148.37 
Bidirectional P2P=Enabled Bandwidth Matrix (GB/s)
   D\D     0 
     0 147.38 
P2P=Disabled Latency Matrix (us)
   GPU     0 
     0   1.59 

   CPU     0 
     0   1.73 
P2P=Enabled Latency (P2P Writes) Matrix (us)
   GPU     0 
     0   1.33 

   CPU     0 
     0   1.67 

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

quasirandomGenerator, Throughput = 17.9962 GNumbers/s, Time = 0.00017 s, Size = 3145728 Numbers, NumDevsUsed = 1, Workgroup = 384

Reading GPU results...
Comparing to the CPU results...

L1 norm: 7.275964E-12

Testing inverseCNDgpu()...

quasirandomGenerator-inverse, Throughput = 30.8556 GNumbers/s, Time = 0.00010 s, Size = 3145728 Numbers, NumDevsUsed = 1, Workgroup = 128
Reading GPU results...

Comparing to the CPU results...
L1 norm: 9.439909E-08

Shutting down...
./bin/x86_64/linux/release/quasirandomGenerator_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
./bin/x86_64/linux/release/radixSortThrust Starting...

GPU Device 0: "Turing" with compute capability 7.5


Sorting 1048576 32-bit unsigned int keys and values

radixSortThrust, Throughput = 914.5952 MElements/s, Time = 0.00115 s, Size = 1048576 elements
Test passed
./bin/x86_64/linux/release/reduction Starting...

GPU Device 0: "Turing" with compute capability 7.5

Using Device 0: GeForce GTX 1650 SUPER

Reducing array of type int

16777216 elements
256 threads (max)
64 blocks

Reduction, Throughput = 171.2704 GB/s, Time = 0.00039 s, Size = 16777216 Elements, NumDevsUsed = 1, Workgroup = 256

GPU result = 2139353471
CPU result = 2139353471

Test passed
reductionMultiBlockCG Starting...

GPU Device 0: "Turing" with compute capability 7.5

33554432 elements
numThreads: 1024
numBlocks: 20

Launching SinglePass Multi Block Cooperative Groups kernel
Average time: 1.001910 ms
Bandwidth:    133.961897 GB/s

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
GPU time: 0.068000 msecs.
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


scan, Throughput = 3.0046 MElements/s, Time = 0.00034 s, Size = 1024 Elements, NumDevsUsed = 1, Workgroup = 256

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


scan, Throughput = 378.3124 MElements/s, Time = 0.00069 s, Size = 262144 Elements, NumDevsUsed = 1, Workgroup = 256

Shutting down...
./bin/x86_64/linux/release/segmentationTreeThrust Starting...

GPU Device 0: "Turing" with compute capability 7.5

* Building segmentation tree... done in 62.9334 (ms)
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
Time (ms): 0.028512
65536 elements scanned in 0.028512 ms -> 2298.541016 MegaElements/s
CPU verify result diff (GPUvsCPU) = 0
CPU sum (naive) took 0.024600 ms

Computing Integral Image Test on size 1920 x 1080 synthetic data
---------------------------------------------------
Method: Fast  Time (GPU Timer): 0.069120 ms Diff = 0
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
./bin/x86_64/linux/release/simpleAssert_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
simpleAtomicIntrinsics starting...
GPU Device 0: "Turing" with compute capability 7.5

Processing time: 68.351997 (ms)
simpleAtomicIntrinsics completed, returned OK
./bin/x86_64/linux/release/simpleAtomicIntrinsics_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
./bin/x86_64/linux/release/simpleAttributes Starting...

GPU Device 0: "Turing" with compute capability 7.5

Waiving execution as device 0 does not support persisting L2 Caching
./bin/x86_64/linux/release/simpleCUBLAS: error while loading shared libraries: libcublas.so.11: cannot open shared object file: No such file or directory
./bin/x86_64/linux/release/simpleCUBLASXT: error while loading shared libraries: libcublas.so.11: cannot open shared object file: No such file or directory
./bin/x86_64/linux/release/simpleCUFFT: error while loading shared libraries: libcufft.so.10: cannot open shared object file: No such file or directory
./bin/x86_64/linux/release/simpleCUFFT_2d_MGPU: error while loading shared libraries: libcufft.so.10: cannot open shared object file: No such file or directory
./bin/x86_64/linux/release/simpleCUFFT_MGPU: error while loading shared libraries: libcufft.so.10: cannot open shared object file: No such file or directory
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
Processing time: 0.083 msec
15791.81 Mtexlookups/sec
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
 Memcpy host to device	: 1.358272 ms (12.351883 GB/s)
 Memcpy device to host	: 1.320288 ms (12.707240 GB/s)
 Kernel			: 0.235040 ms (713.802605 GB/s)

Theoretical limits for speedup gained from overlapped data transfers:
No overlap at all (transfer-kernel-transfer): 2.913600 ms 
Compute can overlap with one transfer: 2.678560 ms
Compute can overlap with both data transfers: 1.358272 ms

Average measured timings over 10 repetitions:
 Avg. time when execution fully serialized	: 2.911482 ms
 Avg. time when overlapped using 4 streams	: 1.681818 ms
 Avg. speedup gained (serialized - overlapped)	: 1.229664 ms

Measured throughput:
 Fully serialized execution		: 11.524865 GB/s
 Overlapped using 4 streams		: 19.951290 GB/s
Starting simpleMultiGPU
CUDA-capable device count: 1
Generating input data...

Computing with 1 GPUs...
  GPU Processing time: 12.343000 (ms)

Computing with Host CPU...

Comparing GPU and Host CPU results...
  GPU sum: 16777296.000000
  CPU sum: 16777294.395033
  Relative difference: 9.566307E-08 

starting Simple Occupancy

[ Manual configuration with 32 threads per block ]
Potential occupancy: 50%
Elapsed time: 0.102368ms

[ Automatic, occupancy-based configuration ]
Suggested block size: 1024
Minimum grid size for maximum occupancy: 20
Potential occupancy: 100%
Elapsed time: 0.057568ms

Test PASSED

[./bin/x86_64/linux/release/simpleP2P] - Starting...
Checking for multiple GPUs...
CUDA-capable device count: 1
Two or more GPUs with Peer-to-Peer access capability are required for ./bin/x86_64/linux/release/simpleP2P.
Waiving test.
simplePitchLinearTexture starting...

GPU Device 0: "Turing" with compute capability 7.5


Bandwidth (GB/s) for pitch linear: 1.51e+02; for array: 1.56e+02

Texture fetch rate (Mpix/s) for pitch linear: 1.89e+04; for array: 1.95e+04

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
kernel:		0.93
non-streamed:	6.13
4 streams:	5.65
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
Processing time: 61.213001 (ms)
Compare OK

> runTest<int,64>
GPU Device 0: "Turing" with compute capability 7.5

CUDA device [GeForce GTX 1650 SUPER] has 20 Multi-Processors
Processing time: 0.116000 (ms)
Compare OK


[simpleTemplates] -> Test Results: 0 Failures
./bin/x86_64/linux/release/simpleTemplates_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
simpleTexture starting...
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
./bin/x86_64/linux/release/simpleVoteIntrinsics_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
  Device 0: <          Turing >, Compute SM 7.5 detected
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
Average time: 0.311000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 128 (8192 arrays per batch)...
Average time: 0.563000 ms


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
Average time: 0.724000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 1024 (1024 arrays per batch)...
Average time: 0.852000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 2048 (512 arrays per batch)...
Average time: 1.014000 ms


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
Average time: 1.803000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 16384 (64 arrays per batch)...
Average time: 2.432000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 32768 (32 arrays per batch)...
Average time: 3.029000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 65536 (16 arrays per batch)...
Average time: 3.848000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 131072 (8 arrays per batch)...
Average time: 4.665000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 262144 (4 arrays per batch)...
Average time: 5.666000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 524288 (2 arrays per batch)...
Average time: 6.637000 ms


Validating the results...
...reading back GPU results
...inspecting keys array: OK
...inspecting keys and values array: OK
...stability property: NOT stable

Testing array length 1048576 (1 arrays per batch)...
Average time: 7.883000 ms

sortingNetworks-bitonic, Throughput = 133.0174 MElements/s, Time = 0.00788 s, Size = 1048576 elements, NumDevsUsed = 1, Workgroup = 512

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
GPU processing time : 1.0711 (ms)
Pixel throughput    : 318.475 Mpixels/sec
GPU Checksum = 4293895789, GPU image: <output_GPU.pgm>
Computing CPU reference...
CPU Checksum = 4293895789, CPU image: <output_CPU.pgm>
GPU Device 0: "Turing" with compute capability 7.5

Starting basicStreamOrderedAllocation()
> Checking the results from vectorAddGPU() ...
basicStreamOrderedAllocation PASSED
Starting streamOrderedAllocationPostSync()
Total elapsed time = 33.968704 ms over 20 iterations
> Checking the results from vectorAddGPU() ...
streamOrderedAllocationPostSync PASSED
No Two or more GPUs with same architecture capable of cuda Memory Pools found.
Waiving the sample
GPU Device 0: "Turing" with compute capability 7.5

CANNOT access pageable memory
systemWideAtomics completed, returned OK 
./bin/x86_64/linux/release/template Starting...

GPU Device 0: "Turing" with compute capability 7.5

Processing time: 60.344002 (ms)
Initializing...
GPU Device 0: "Turing" with compute capability 7.5

tf32TensorCoreGemm requires requires SM 8.0 or higher to use Tensor Cores.  Exiting...
threadFenceReduction Starting...

GPU Device 0: "Turing" with compute capability 7.5

GPU Device supports SM 7.5 compute capability

1048576 elements
128 threads (max)
64 blocks
Average time: 0.031760 ms
Bandwidth:    132.062485 GB/s

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
<CUDA Device=0, Context=0x5602f9608040, Thread=0> - ThreadProc() Launched...
<CUDA Device=0, Context=0x5602f9608040, Thread=1> - ThreadProc() Launched...
<CUDA Device=0, Context=0x5602f9608040, Thread=0> - ThreadProc() Finished!

<CUDA Device=0, Context=0x5602f9608040, Thread=1> - ThreadProc() Finished!

GPU0 <-> CPU:
  * Atomic Supported: no
Transpose Starting...

GPU Device 0: "Turing" with compute capability 7.5

> Device 0: "GeForce GTX 1650 SUPER"
> SM Capability 7.5 detected:
> [GeForce GTX 1650 SUPER] has 20 MP(s) x 64 (Cores/MP) = 1280 (Cores)
> Compute performance scaling factor = 1.00

Matrix size: 1024x1024 (64x64 tiles), tile size: 16x16, block size: 16x16

transpose simple copy       , Throughput = 145.0938 GB/s, Time = 0.05384 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose shared memory copy, Throughput = 144.4149 GB/s, Time = 0.05410 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose naive             , Throughput = 137.8671 GB/s, Time = 0.05667 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose coalesced         , Throughput = 146.7932 GB/s, Time = 0.05322 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose optimized         , Throughput = 146.6134 GB/s, Time = 0.05329 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose coarse-grained    , Throughput = 143.6265 GB/s, Time = 0.05439 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose fine-grained      , Throughput = 144.7703 GB/s, Time = 0.05396 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
transpose diagonal          , Throughput = 122.8962 GB/s, Time = 0.06357 ms, Size = 1048576 fp32 elements, NumDevsUsed = 1, Workgroup = 256
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
./bin/x86_64/linux/release/vectorAdd_nvrtc: error while loading shared libraries: libnvrtc.so.11.2: cannot open shared object file: No such file or directory
GPU Device 0: "Turing" with compute capability 7.5

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

