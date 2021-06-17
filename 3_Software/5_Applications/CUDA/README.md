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
