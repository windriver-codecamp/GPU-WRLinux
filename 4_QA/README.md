1. How about GPU performance comparisons between Wind River Linux and Ubuntu?
* On Ubuntu:
```
root@wind-OptiPlex-9020:/home/wind# nvidia-smi 
Tue May 11 01:43:03 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.73.01    Driver Version: 460.73.01    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce GTX 165...  Off  | 00000000:01:00.0  On |                  N/A |
| 33%   35C    P8     6W / 100W |    239MiB /  3878MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1300      G   /usr/lib/xorg/Xorg                110MiB |
|    0   N/A  N/A      1438      G   /usr/bin/gnome-shell              126MiB |
+-----------------------------------------------------------------------------+
root@wind-OptiPlex-9020:/home/wind# 


wind@wind-OptiPlex-9020:~/2021CodingCamp$ cat gpu.txt 
root@wind-OptiPlex-9020:/home/wind# glmark2 
=======================================================
    glmark2 2014.03+git20150611.fa71af2d
=======================================================
    OpenGL Information
    GL_VENDOR:     NVIDIA Corporation
    GL_RENDERER:   GeForce GTX 1650 SUPER/PCIe/SSE2
    GL_VERSION:    4.6.0 NVIDIA 460.39
=======================================================
[build] use-vbo=false: FPS: 7188 FrameTime: 0.139 ms
[build] use-vbo=true: FPS: 10026 FrameTime: 0.100 ms
[texture] texture-filter=nearest: FPS: 9587 FrameTime: 0.104 ms
[texture] texture-filter=linear: FPS: 9322 FrameTime: 0.107 ms
[texture] texture-filter=mipmap: FPS: 8777 FrameTime: 0.114 ms
[shading] shading=gouraud: FPS: 10257 FrameTime: 0.097 ms
[shading] shading=blinn-phong-inf: FPS: 9516 FrameTime: 0.105 ms
[shading] shading=phong: FPS: 8741 FrameTime: 0.114 ms
[shading] shading=cel: FPS: 9283 FrameTime: 0.108 ms
[bump] bump-render=high-poly: FPS: 8314 FrameTime: 0.120 ms
[bump] bump-render=normals: FPS: 10228 FrameTime: 0.098 ms
[bump] bump-render=height: FPS: 11145 FrameTime: 0.090 ms
[effect2d] kernel=0,1,0;1,-4,1;0,1,0;: FPS: 8106 FrameTime: 0.123 ms
[effect2d] kernel=1,1,1,1,1;1,1,1,1,1;1,1,1,1,1;: FPS: 6568 FrameTime: 0.152 ms
[pulsar] light=false:quads=5:texture=false: FPS: 11348 FrameTime: 0.088 ms
[desktop] blur-radius=5:effect=blur:passes=1:separable=true:windows=4: FPS: 4895 FrameTime: 0.204 ms
[desktop] effect=shadow:windows=4: FPS: 7283 FrameTime: 0.137 ms
[buffer] columns=200:interleave=false:update-dispersion=0.9:update-fraction=0.5:update-method=map: FPS: 1186 FrameTime: 0.843 ms
[buffer] columns=200:interleave=false:update-dispersion=0.9:update-fraction=0.5:update-method=subdata: FPS: 1616 FrameTime: 0.619 ms
[buffer] columns=200:interleave=true:update-dispersion=0.9:update-fraction=0.5:update-method=map: FPS: 1542 FrameTime: 0.649 ms
[ideas] speed=duration: FPS: 8893 FrameTime: 0.112 ms
[jellyfish] <default>: FPS: 8345 FrameTime: 0.120 ms
[terrain] <default>: FPS: 901 FrameTime: 1.110 ms
[shadow] <default>: FPS: 7905 FrameTime: 0.127 ms
[refract] <default>: FPS: 2437 FrameTime: 0.410 ms
[conditionals] fragment-steps=0:vertex-steps=0: FPS: 10224 FrameTime: 0.098 ms
[conditionals] fragment-steps=5:vertex-steps=0: FPS: 10906 FrameTime: 0.092 ms
[conditionals] fragment-steps=0:vertex-steps=5: FPS: 10089 FrameTime: 0.099 ms
[function] fragment-complexity=low:fragment-steps=5: FPS: 10574 FrameTime: 0.095 ms
[function] fragment-complexity=medium:fragment-steps=5: FPS: 10938 FrameTime: 0.091 ms
[loop] fragment-loop=false:fragment-steps=5:vertex-steps=5: FPS: 8734 FrameTime: 0.114 ms
[loop] fragment-steps=5:fragment-uniform=false:vertex-steps=5: FPS: 9849 FrameTime: 0.102 ms
[loop] fragment-steps=5:fragment-uniform=true:vertex-steps=5: FPS: 10503 FrameTime: 0.095 ms
=======================================================
                                  glmark2 Score: 8037 
=======================================================

bandwidthTest 



oot@wind-OptiPlex-9020:/usr/local/cuda-11.2/samples/bin/x86_64/linux/release# ./bandwidthTest 
[CUDA Bandwidth Test] - Starting...
Running on...

 Device 0: GeForce GTX 1650 SUPER
 Quick Mode

 Host to Device Bandwidth, 1 Device(s)
 PINNED Memory Transfers
   Transfer Size (Bytes)	Bandwidth(GB/s)
   32000000			12.6

 Device to Host Bandwidth, 1 Device(s)
 PINNED Memory Transfers
   Transfer Size (Bytes)	Bandwidth(GB/s)
   32000000			12.7

 Device to Device Bandwidth, 1 Device(s)
 PINNED Memory Transfers
   Transfer Size (Bytes)	Bandwidth(GB/s)
   32000000			144.8

Result = PASS

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
root@wind-OptiPlex-9020:/usr/local/cuda-11.2/samples/bin/x86_64/linux/release# 



deviceQuery:

root@wind-OptiPlex-9020:/usr/local/cuda-11.2/samples/bin/x86_64/linux/release# ./deviceQuery
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


root@wind-OptiPlex-9020:/usr/local/cuda-11.2/samples/bin/x86_64/linux/release# ./matrixMul
[Matrix Multiply Using CUDA] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

MatrixA(320,320), MatrixB(640,320)
Computing result using CUDA Kernel...
done
Performance= 430.11 GFlop/s, Time= 0.305 msec, Size= 131072000 Ops, WorkgroupSize= 1024 threads/block
Checking computed result for correctness: Result = PASS

NOTE: The CUDA Samples are not meant for performancemeasurements. Results may vary when GPU Boost is enabled.
root@wind-OptiPlex-9020:/usr/local/cuda-11.2/samples/bin/x86_64/linux/release# 
root@wind-OptiPlex-9020:/usr/local/cuda-11.2/samples/bin/x86_64/linux/release# ./matrixMulCUBLAS
[Matrix Multiply CUBLAS] - Starting...
GPU Device 0: "Turing" with compute capability 7.5

GPU Device 0: "GeForce GTX 1650 SUPER" with compute capability 7.5

MatrixA(640,480), MatrixB(480,320), MatrixC(640,320)
Computing result using CUBLAS...done.
Performance= 1701.12 GFlop/s, Time= 0.116 msec, Size= 196608000 Ops
Computing result using host CPU...done.
Comparing CUBLAS Matrix Multiply with CPU results: PASS


sudo /usr/local/cuda-X.Y/bin/uninstall_cuda_X.Y.pl
```

2. Can NVIDIA GPU run on any ARM based boards?
3. How to verify the GPU works well on Wind River Linux?
