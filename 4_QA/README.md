## 1. How about GPU performance comparisons between Wind River Linux and Ubuntu?
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

## 2. Can NVIDIA GPU run on any ARM based boards?

We tried to bring the NVIDIA Graphic Card in intel-socfpga-64 (ARM64) BSP target but failed.

The following were the steps.

* 1. Build kernel and rootfs image for intel-socfpga-64 BSP
```
$ /lpg-build/cdc/fast_prod/WRLINUX_MASTER_WR/MASTER_WR_GIT/wrlinux-10/setup.sh --machines=intel-socfpga-64 --templates=feature/xfce --dl-layers --accept-eula=yes
$ source environment-setup-x86_64-wrlinuxsdk-linux 
$ source oe-init-build-env
$ vi conf/local.conf

IMAGE_INSTALL_append = " libjpeg-turbo v4l-utils apt autoconf autoconf-archive automake binutils bison build-compare ccache chrpath cmake createrepo-c dejagnu desktop-file-utils diffstat distcc dmidecode dnf dosfstools dpkg dwarfsrcfiles e2fsprogs elfutils expect file flex gcc gdb git glide gnu-config go intltool json-c libcomps libdnf libedit libmodulemd librepo libtool m4 make makedevs meson mtools nasm ninja opkg opkg-utils orc patch patchelf perl prelink pseudo quilt rpm rsync ruby run-postinsts squashfs-tools strace subversion unifdef xmlto util-linux python3-pip python3-numpy python3-pkg-resources python3-setuptools libgcc make xz libcrypto libffi liblzma libssl libtirpc libmpc mpfr libunwind kernel-devsrc libmpc-dev gcc-plugins ncurses"


EXTRA_IMAGE_FEATURES ?= "debug-tweaks tools-sdk tools-debug"


$ vi ../layers/oe-core/meta/recipes-graphics/xorg-xserver/xserver-xorg.inc

OPENGL_PKGCONFIGS = "dri glx glamor dri3 xshmfence xinerama"
…
#  180.0k  libwfb.so
#  320.0k  libxaa.so
...
PACKAGES =+ "${PN}-sdl \
             ${PN}-fbdev \
...
             ${PN}-module-exa \
             ${PN}-module-wfb \
             ${PN}-module-xaa \
             ${PN}-module-libxf1bpp \
             ${PN}-module-libxf4bpp \
             xf86-video-modesetting"
...
FILES_${PN}-module-libcfb = "${libdir}/xorg/modules/libcfb.so"
FILES_${PN}-module-exa = "${libdir}/xorg/modules/libexa.so"
FILES_${PN}-module-wfb = "${libdir}/xorg/modules/libwfb.so"
FILES_${PN}-module-xaa = "${libdir}/xorg/modules/libxaa.so"
$ bitbake wrlinux-image-std

```
* 2. Download arm64 driver for NVIDIA's GPU card

```
wget https://download.nvidia.com/XFree86/Linux-aarch64/460.73.01/NVIDIA-Linux-aarch64-460.73.01.run
```
* 3. Deploy FPGA PCIE supported Firmware on the target of Stratix10 target

Issues met were as below.

```
[    8.864335] nvidia 0000:01:00.0: enabling device (0000 -> 0002)
[    8.869277] nvidia 0000:01:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=none:owns=none
[    8.919669] NVRM: loading NVIDIA UNIX aarch64 Kernel Module  460.73.01  Thu Apr  1 21:51:06 UTC 2021
[   11.259484] socfpga-dwmac ff800000.ethernet eth0: PHY [stmmac-0:04] driver [Micrel KSZ9031 Gigabit PHY] (irq=POLL)
[   11.295497] socfpga-dwmac ff800000.ethernet eth0: No Safety Features support found
[   11.307540] socfpga-dwmac ff800000.ethernet eth0: IEEE 1588-2008 Advanced Timestamp supported
[   11.335577] socfpga-dwmac ff800000.ethernet eth0: registered PTP clock
[   11.351493] socfpga-dwmac ff800000.ethernet eth0: configuring for phy/rgmii link mode
[   11.979155] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:624)
[   11.995636] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   12.049030] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:624)
[   12.067657] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   13.413089] socfpga-dwmac ff800000.ethernet eth0: Link is Up - 100Mbps/Full - flow control rx/tx
[   13.420663] IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
[   17.380299] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:624)
[   17.386129] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   17.400816] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:624)
[   17.406630] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   22.903199] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:624)
[   22.909022] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   22.924024] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:624)
[   22.929843] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
root@intel-socfpga-64:/NVIDIA-Linux-aarch64-460.73.01#


kernel parameter pci=realloc or pci=nocrs workaround it?
pci=realloc

pcie_aspm=off rcutree.rcu_idle_gp_delay=1

quiet rcutree.rcu_idle_gp_delay=1 mem_encrypt=off



pci=nocrs,noearly mem_encrypt=off 

quiet splash pci=nocrs,noearly mem_encrypt=off vt.handoff=1


Using the latest driver
https://us.download.nvidia.com/XFree86/aarch64/465.31/NVIDIA-Linux-aarch64-465.31.run





/usr/share/doc/NVIDIA_GLX-1.0/README.txt


[    1.982788] pci 0000:00:00.0: BAR 15: no space for [mem size 0x18000000 64bit pref]
[    1.982806] pci 0000:00:00.0: BAR 15: failed to assign [mem size 0x18000000 64bit pref]
[    1.982824] pci 0000:00:00.0: BAR 14: assigned [mem 0x90000000-0x917fffff]
[    1.982839] pci 0000:00:00.0: BAR 13: no space for [io  size 0x1000]
[    1.982853] pci 0000:00:00.0: BAR 13: failed to assign [io  size 0x1000]
[    1.982879] pci 0000:01:00.0: BAR 1: no space for [mem size 0x10000000 64bit pref]
[    1.982895] pci 0000:01:00.0: BAR 1: failed to assign [mem size 0x10000000 64bit pref]
[    1.982914] pci 0000:01:00.0: BAR 3: no space for [mem size 0x02000000 64bit pref]
[    1.982929] pci 0000:01:00.0: BAR 3: failed to assign [mem size 0x02000000 64bit pref]
[    1.982947] pci 0000:01:00.0: BAR 0: assigned [mem 0x90000000-0x90ffffff]
[    1.982989] pci 0000:01:00.0: BAR 6: assigned [mem 0x91000000-0x9107ffff pref]
[    1.983007] pci 0000:01:00.2: BAR 0: assigned [mem 0x91080000-0x910bffff 64bit pref]
[    1.983106] pci 0000:01:00.2: BAR 3: assigned [mem 0x910c0000-0x910cffff 64bit pref]
[    1.983203] pci 0000:01:00.1: BAR 0: assigned [mem 0x910d0000-0x910d3fff]
[    1.983243] pci 0000:01:00.3: BAR 0: assigned [mem 0x910d4000-0x910d4fff]
[    1.983281] pci 0000:01:00.0: BAR 5: no space for [io  size 0x0080]
[    1.983295] pci 0000:01:00.0: BAR 5: failed to assign [io  size 0x0080]
[    1.983313] pci 0000:00:00.0: PCI bridge to [bus 01]
[    1.983332] pci 0000:00:00.0:   bridge window [mem 0x90000000-0x917fffff]
[    1.983463] pcieport 0000:00:00.0: enabling device (0000 -> 0002)
[    1.983725] pcieport 0000:00:00.0: PME: Signaling with IRQ 42
[    1.984218] pci 0000:01:00.1: D0 power state depends on 0000:01:00.0
[    1.984747] pci 0000:01:00.2: D0 power state depends on 0000:01:00.0
[    1.985156] pci 0000:01:00.2: enabling device (0000 -> 0002)
[    1.985408] pci 0000:01:00.3: D0 power state depends on 0000:01:00.0
[    3.116975] ehci-pci: EHCI PCI platform driver
root@intel-socfpga-64:~# 

root@intel-socfpga-64:/proc/device-tree/soc/bridge@80000000# lspci 
00:00.0 PCI bridge: Altera Corporation Device e000 (rev 01)
01:00.0 VGA compatible controller: NVIDIA Corporation TU116 [GeForce GTX 1650 SUPER] (rev a1)
01:00.1 Audio device: NVIDIA Corporation TU116 High Definition Audio Controller (rev a1)
01:00.2 USB controller: NVIDIA Corporation TU116 USB 3.1 Host Controller (rev a1)
01:00.3 Serial bus controller [0c80]: NVIDIA Corporation TU116 USB Type-C UCSI Controller (rev a1)



[    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
[    0.000000] Linux version 5.10.35-yocto-standard (oe-user@oe-host) (aarch64-wrs-linux-gcc (GCC) 10.2.0, GNU ld (GNU Binutils) 2.36.1.20210209) #1 SMP PREEMPT Wed May 12 08:49:49 UTC 2021
[    0.000000] Machine model: SoCFPGA Stratix 10 SoCDK
[    0.000000] earlycon: uart0 at MMIO32 0x00000000ffc02000 (options '115200n8')
[    0.000000] printk: bootconsole [uart0] enabled
[    0.000000] efi: UEFI not found.
[    0.000000] Reserved memory: created DMA memory pool at 0x0000000000000000, size 16 MiB
[    0.000000] OF: reserved mem: initialized node svcbuffer@0, compatible id shared-dma-pool
[    0.000000] cma: Reserved 16 MiB at 0x000000007e800000
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000000000-0x00000000ffffffff]
[    0.000000]   DMA32    empty
[    0.000000]   Normal   [mem 0x0000000100000000-0x00000001ffffffff]
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000000000-0x0000000000ffffff]
[    0.000000]   node   0: [mem 0x0000000001000000-0x000000007fffffff]
[    0.000000]   node   0: [mem 0x0000000180000000-0x00000001ffffffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000000000-0x00000001ffffffff]
[    0.000000] On node 0 totalpages: 1048576
[    0.000000]   DMA zone: 8192 pages used for memmap
[    0.000000]   DMA zone: 0 pages reserved
[    0.000000]   DMA zone: 524288 pages, LIFO batch:63
[    0.000000]   Normal zone: 8192 pages used for memmap
[    0.000000]   Normal zone: 524288 pages, LIFO batch:63
[    0.000000] psci: probing for conduit method from DT.
[    0.000000] psci: PSCIv65535.65535 detected in firmware.
[    0.000000] psci: Using standard PSCI v0.2 function IDs
[    0.000000] psci: MIGRATE_INFO_TYPE not supported.
[    0.000000] psci: SMC Calling Convention v1.0
[    0.000000] percpu: Embedded 30 pages/cpu s82008 r8192 d32680 u122880
[    0.000000] pcpu-alloc: s82008 r8192 d32680 u122880 alloc=30*4096
[    0.000000] pcpu-alloc: [0] 0 [0] 1 [0] 2 [0] 3 
[    0.000000] Detected VIPT I-cache on CPU0
[    0.000000] CPU features: detected: ARM erratum 845719
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 1032192
[    0.000000] Kernel command line: earlycon panic=-1 root=/dev/mmcblk0p2 rw rootwait
[    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
[    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
[    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
[    0.000000] software IO TLB: mapped [mem 0x000000007a800000-0x000000007e800000] (64MB)
[    0.000000] Memory: 3993020K/4194304K available (12416K kernel code, 1952K rwdata, 2936K rodata, 3968K init, 707K bss, 184900K reserved, 16384K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] ftrace: allocating 38327 entries in 150 pages
[    0.000000] ftrace: allocated 150 pages with 4 groups
[    0.000000] rcu: Preemptible hierarchical RCU implementation.
[    0.000000] rcu: 	RCU event tracing is enabled.
[    0.000000] 	Trampoline variant of Tasks RCU enabled.
[    0.000000] 	Rude variant of Tasks RCU enabled.
[    0.000000] 	Tracing variant of Tasks RCU enabled.
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
[    0.000000] GIC: Using split EOI/Deactivate mode
[    0.000000] random: get_random_bytes called from start_kernel+0x398/0x5a0 with crng_init=0
[    0.000000] arch_timer: cp15 timer(s) running at 400.00MHz (phys).
[    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x5c4093a7d1, max_idle_ns: 440795210635 ns
[    0.000005] sched_clock: 56 bits at 400MHz, resolution 2ns, wraps every 4398046511103ns
[    0.006873] Console: colour dummy device 80x25
[    0.010003] printk: console [tty0] enabled
[    0.012805] printk: bootconsole [uart0] disabled
[    0.016133] Calibrating delay loop (skipped), value calculated using timer frequency.. 800.00 BogoMIPS (lpj=1600000)
[    0.016158] pid_max: default: 32768 minimum: 301
[    0.016270] LSM: Security Framework initializing
[    0.016447] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.016482] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.018402] rcu: Hierarchical SRCU implementation.
[    0.018937] EFI services will not be available.
[    0.019176] smp: Bringing up secondary CPUs ...
[    0.019718] Detected VIPT I-cache on CPU1
[    0.019781] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
[    0.020386] Detected VIPT I-cache on CPU2
[    0.020419] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
[    0.021026] Detected VIPT I-cache on CPU3
[    0.021057] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
[    0.021167] smp: Brought up 1 node, 4 CPUs
[    0.021210] SMP: Total of 4 processors activated.
[    0.021222] CPU features: detected: 32-bit EL0 Support
[    0.021234] CPU features: detected: CRC32 instructions
[    0.021293] CPU: All CPU(s) started at EL2
[    0.021322] alternatives: patching kernel code
[    0.022073] devtmpfs: initialized
[    0.025870] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.025906] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
[    0.027054] DMI not present or invalid.
[    0.027522] NET: Registered protocol family 16
[    0.029220] DMA: preallocated 512 KiB GFP_KERNEL pool for atomic allocations
[    0.029405] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
[    0.029754] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
[    0.030428] cpuidle: using governor ladder
[    0.030522] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
[    0.030627] ASID allocator initialised with 65536 entries
[    0.117048] raid6: neonx8   gen()  1740 MB/s
[    0.185140] raid6: neonx8   xor()  1287 MB/s
[    0.253247] raid6: neonx4   gen()  1788 MB/s
[    0.321355] raid6: neonx4   xor()  1263 MB/s
[    0.389469] raid6: neonx2   gen()  1683 MB/s
[    0.457569] raid6: neonx2   xor()  1157 MB/s
[    0.525684] raid6: neonx1   gen()  1446 MB/s
[    0.593785] raid6: neonx1   xor()   990 MB/s
[    0.661889] raid6: int64x8  gen()  1198 MB/s
[    0.729991] raid6: int64x8  xor()   642 MB/s
[    0.798114] raid6: int64x4  gen()  1335 MB/s
[    0.866231] raid6: int64x4  xor()   682 MB/s
[    0.934319] raid6: int64x2  gen()  1166 MB/s
[    1.002378] raid6: int64x2  xor()   625 MB/s
[    1.070478] raid6: int64x1  gen()   862 MB/s
[    1.138554] raid6: int64x1  xor()   431 MB/s
[    1.138566] raid6: using algorithm neonx4 gen() 1788 MB/s
[    1.138577] raid6: .... xor() 1263 MB/s, rmw enabled
[    1.138589] raid6: using neon recovery algorithm
[    1.139639] iommu: Default domain type: Translated 
[    1.139837] vgaarb: loaded
[    1.140071] SCSI subsystem initialized
[    1.140297] usbcore: registered new interface driver usbfs
[    1.140351] usbcore: registered new interface driver hub
[    1.140396] usbcore: registered new device driver usb
[    1.140548] usb_phy_generic soc:usbphy@0: supply vcc not found, using dummy regulator
[    1.141027] pps_core: LinuxPPS API ver. 1 registered
[    1.141040] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    1.141068] PTP clock support registered
[    1.141260] EDAC MC: Ver: 3.0.0
[    1.142358] Intel Service Layer Driver Initialized
[    1.142505] FPGA manager framework
[    1.143552] clocksource: Switched to clocksource arch_sys_counter
[    1.899539] NET: Registered protocol family 2
[    1.900249] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes, linear)
[    1.900319] TCP established hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    1.900631] TCP bind hash table entries: 32768 (order: 7, 524288 bytes, linear)
[    1.901124] TCP: Hash tables configured (established 32768 bind 32768)
[    1.901265] UDP hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    1.901366] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    1.901622] NET: Registered protocol family 1
[    1.902087] RPC: Registered named UNIX socket transport module.
[    1.902101] RPC: Registered udp transport module.
[    1.902112] RPC: Registered tcp transport module.
[    1.902122] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    1.902144] PCI: CLS 0 bytes, default 64
[    1.903148] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
[    1.904652] workingset: timestamp_bits=46 max_order=20 bucket_order=0
[    1.912080] NFS: Registering the id_resolver key type
[    1.912122] Key type id_resolver registered
[    1.912133] Key type id_legacy registered
[    1.912804] Key type cifs.idmap registered
[    1.956650] xor: measuring software checksum speed
[    1.961693]    8regs           :  1968 MB/sec
[    1.965934]    32regs          :  2331 MB/sec
[    1.971666]    arm64_neon      :  1726 MB/sec
[    1.971678] xor: using function: 32regs (2331 MB/sec)
[    1.971695] async_tx: api initialized (async)
[    1.971743] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 248)
[    1.971761] io scheduler mq-deadline registered
[    1.971773] io scheduler kyber registered
[    1.972362] gpio-dwapb ffc03300.gpio: Cannot get reset descriptor
[    1.972788] altera-pcie a0000000.pcie: host bridge /soc/bridge@80000000/pcie@200000000 ranges:
[    1.972852] altera-pcie a0000000.pcie:      MEM 0x0090000000..0x0097ffffff -> 0x0000000000
[    1.973094] altera-pcie a0000000.pcie: PCI host bridge to bus 0000:00
[    1.973116] pci_bus 0000:00: root bus resource [bus 00-ff]
[    1.973134] pci_bus 0000:00: root bus resource [mem 0x90000000-0x97ffffff] (bus address [0x00000000-0x07ffffff])
[    1.973210] pci 0000:00:00.0: [1172:e000] type 01 class 0x060400
[    1.973284] pci 0000:00:00.0: enabling Extended Tags
[    1.974563] pci 0000:00:00.0: bridge configuration invalid ([bus 00-00]), reconfiguring
[    1.974979] pci 0000:01:00.0: [10de:2187] type 00 class 0x030000
[    1.975124] pci 0000:01:00.0: reg 0x10: [mem 0x90000000-0x90ffffff]
[    1.975243] pci 0000:01:00.0: reg 0x14: [mem 0x00000000-0x0fffffff 64bit pref]
[    1.975361] pci 0000:01:00.0: reg 0x1c: [mem 0x90000000-0x91ffffff 64bit pref]
[    1.975435] pci 0000:01:00.0: reg 0x24: [io  0x0000-0x007f]
[    1.975507] pci 0000:01:00.0: reg 0x30: [mem 0x90000000-0x9007ffff pref]
[    1.976305] pci 0000:01:00.0: PME# supported from D0 D3hot D3cold
[    1.976844] pci 0000:01:00.0: 63.008 Gb/s available PCIe bandwidth, limited by 8.0 GT/s PCIe x8 link at 0000:00:00.0 (capable of 126.016 Gb/s with 8.0 GT/s PCIe x16 link)
[    1.977013] pci 0000:01:00.0: vgaarb: VGA device added: decodes=io+mem,owns=none,locks=none
[    1.977225] pci 0000:01:00.1: [10de:1aeb] type 00 class 0x040300
[    1.977368] pci 0000:01:00.1: reg 0x10: [mem 0x90000000-0x90003fff]
[    1.978707] pci 0000:01:00.2: [10de:1aec] type 00 class 0x0c0330
[    1.978898] pci 0000:01:00.2: reg 0x10: [mem 0x90000000-0x9003ffff 64bit pref]
[    1.979074] pci 0000:01:00.2: reg 0x1c: [mem 0x90000000-0x9000ffff 64bit pref]
[    1.979742] pci 0000:01:00.2: PME# supported from D0 D3hot D3cold
[    1.980265] pci 0000:01:00.3: [10de:1aed] type 00 class 0x0c8000
[    1.980409] pci 0000:01:00.3: reg 0x10: [mem 0x90000000-0x90000fff]
[    1.981285] pci 0000:01:00.3: PME# supported from D0 D3hot D3cold
[    1.982738] pci_bus 0000:01: busn_res: [bus 01-ff] end is updated to 01
[    1.982788] pci 0000:00:00.0: BAR 15: no space for [mem size 0x18000000 64bit pref]
[    1.982806] pci 0000:00:00.0: BAR 15: failed to assign [mem size 0x18000000 64bit pref]
[    1.982824] pci 0000:00:00.0: BAR 14: assigned [mem 0x90000000-0x917fffff]
[    1.982839] pci 0000:00:00.0: BAR 13: no space for [io  size 0x1000]
[    1.982853] pci 0000:00:00.0: BAR 13: failed to assign [io  size 0x1000]
[    1.982879] pci 0000:01:00.0: BAR 1: no space for [mem size 0x10000000 64bit pref]
[    1.982895] pci 0000:01:00.0: BAR 1: failed to assign [mem size 0x10000000 64bit pref]
[    1.982914] pci 0000:01:00.0: BAR 3: no space for [mem size 0x02000000 64bit pref]
[    1.982929] pci 0000:01:00.0: BAR 3: failed to assign [mem size 0x02000000 64bit pref]
[    1.982947] pci 0000:01:00.0: BAR 0: assigned [mem 0x90000000-0x90ffffff]
[    1.982989] pci 0000:01:00.0: BAR 6: assigned [mem 0x91000000-0x9107ffff pref]
[    1.983007] pci 0000:01:00.2: BAR 0: assigned [mem 0x91080000-0x910bffff 64bit pref]
[    1.983106] pci 0000:01:00.2: BAR 3: assigned [mem 0x910c0000-0x910cffff 64bit pref]
[    1.983203] pci 0000:01:00.1: BAR 0: assigned [mem 0x910d0000-0x910d3fff]
[    1.983243] pci 0000:01:00.3: BAR 0: assigned [mem 0x910d4000-0x910d4fff]
[    1.983281] pci 0000:01:00.0: BAR 5: no space for [io  size 0x0080]
[    1.983295] pci 0000:01:00.0: BAR 5: failed to assign [io  size 0x0080]
[    1.983313] pci 0000:00:00.0: PCI bridge to [bus 01]
[    1.983332] pci 0000:00:00.0:   bridge window [mem 0x90000000-0x917fffff]
[    1.983463] pcieport 0000:00:00.0: enabling device (0000 -> 0002)
[    1.983725] pcieport 0000:00:00.0: PME: Signaling with IRQ 42
[    1.984218] pci 0000:01:00.1: D0 power state depends on 0000:01:00.0
[    1.984747] pci 0000:01:00.2: D0 power state depends on 0000:01:00.0
[    1.985156] pci 0000:01:00.2: enabling device (0000 -> 0002)
[    1.985408] pci 0000:01:00.3: D0 power state depends on 0000:01:00.0
[    1.986771] Serial: 8250/16550 driver, 4 ports, IRQ sharing enabled
[    1.988142] ffc02000.serial: ttyS0 at MMIO 0xffc02000 (irq = 33, base_baud = 6250000) is a 16550A
[    2.909901] printk: console [ttyS0] enabled
[    2.913920] cacheinfo: Unable to detect cache hierarchy for CPU 0
[    2.926228] brd: module loaded
[    2.936696] loop: module loaded
[    2.940109] spi-nor spi0.0: mt25qu02g (262144 Kbytes)
[    2.943909] 2 fixed-partitions partitions found on MTD device ff8d2000.spi.0
[    2.949646] Creating 2 MTD partitions on "ff8d2000.spi.0":
[    2.953827] 0x000000910000-0x000100010000 : "Boot and fpga data"
[    2.958526] mtd: partition "Boot and fpga data" extends beyond the end of device "ff8d2000.spi.0" -- size truncated to 0xf6f0000
[    2.980416] 0x000003fe0000-0x000010000000 : "Root Filesystem - JFFS2"
[    2.993400] libphy: Fixed MDIO Bus: probed
[    2.996664] socfpga-dwmac ff800000.ethernet: IRQ eth_wake_irq not found
[    3.001975] socfpga-dwmac ff800000.ethernet: IRQ eth_lpi not found
[    3.007232] socfpga-dwmac ff800000.ethernet: User ID: 0x11, Synopsys ID: 0x37
[    3.013069] socfpga-dwmac ff800000.ethernet: 	DWMAC1000
[    3.016993] socfpga-dwmac ff800000.ethernet: DMA HW capability register supported
[    3.023163] socfpga-dwmac ff800000.ethernet: RX Checksum Offload Engine supported
[    3.029331] socfpga-dwmac ff800000.ethernet: COE Type 2
[    3.033251] socfpga-dwmac ff800000.ethernet: TX Checksum insertion supported
[    3.038988] socfpga-dwmac ff800000.ethernet: Enhanced/Alternate descriptors
[    3.044638] socfpga-dwmac ff800000.ethernet: Enabled extended descriptors
[    3.050115] socfpga-dwmac ff800000.ethernet: Ring mode enabled
[    3.054646] socfpga-dwmac ff800000.ethernet: Enable RX Mitigation via HW Watchdog Timer
[    3.061342] socfpga-dwmac ff800000.ethernet: device MAC address 76:fe:28:b7:30:4e
[    3.068013] libphy: stmmac: probed
[    3.073035] dwc2 ffb00000.usb: supply vusb_d not found, using dummy regulator
[    3.078995] dwc2 ffb00000.usb: supply vusb_a not found, using dummy regulator
[    3.085125] dwc2 ffb00000.usb: EPs: 16, dedicated fifos, 8064 entries in SPRAM
[    3.091322] dwc2 ffb00000.usb: DWC OTG Controller
[    3.094767] dwc2 ffb00000.usb: new USB bus registered, assigned bus number 1
[    3.100531] dwc2 ffb00000.usb: irq 34, io mem 0xffb00000
[    3.105220] hub 1-0:1.0: USB hub found
[    3.107704] hub 1-0:1.0: 1 port detected
[    3.111722] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    3.116975] ehci-pci: EHCI PCI platform driver
[    3.120159] ehci-platform: EHCI generic platform driver
[    3.124847] xhci_hcd 0000:01:00.2: enabling device (0000 -> 0002)
[    3.129737] xhci_hcd 0000:01:00.2: xHCI Host Controller
[    3.133672] xhci_hcd 0000:01:00.2: new USB bus registered, assigned bus number 2
[    3.140450] xhci_hcd 0000:01:00.2: hcc params 0x0180ff05 hci version 0x110 quirks 0x0000000000000010
[    3.149435] hub 2-0:1.0: USB hub found
[    3.151924] hub 2-0:1.0: 2 ports detected
[    3.155096] xhci_hcd 0000:01:00.2: xHCI Host Controller
[    3.159030] xhci_hcd 0000:01:00.2: new USB bus registered, assigned bus number 3
[    3.165124] xhci_hcd 0000:01:00.2: Host supports USB 3.1 Enhanced SuperSpeed
[    3.170936] usb usb3: We don't know the algorithms for LPM for this host, disabling LPM.
[    3.178190] hub 3-0:1.0: USB hub found
[    3.180678] hub 3-0:1.0: 4 ports detected
[    3.184257] usbcore: registered new interface driver usb-storage
[    3.189871] i2c /dev entries driver
[    3.193258] device-mapper: ioctl: 4.43.0-ioctl (2020-10-01) initialised: dm-devel@redhat.com
[    3.201228] EDAC DEVICE0: Giving out device to module sdramedac controller Altera ECC Manager: DEV sdramedac (INTERRUPT)
[    3.211128] sdhci: Secure Digital Host Controller Interface driver
[    3.216112] sdhci: Copyright(c) Pierre Ossman
[    3.219158] Synopsys Designware Multimedia Card Interface Driver
[    3.224098] dw_mmc ff808000.dwmmc0: IDMAC supports 32-bit address mode.
[    3.227596] sdhci-pltfm: SDHCI platform and OF driver helper
[    3.229419] dw_mmc ff808000.dwmmc0: Using internal DMA controller.
[    3.238677] dw_mmc ff808000.dwmmc0: Version ID is 280a
[    3.242558] dw_mmc ff808000.dwmmc0: DW MMC controller at irq 19,32 bit host data width,1024 deep fifo
[    3.251787] mmc_host mmc0: card is polling.
[    3.257120] usbcore: registered new interface driver usbhid
[    3.261391] usbhid: USB HID core driver
[    3.264219] fpga_manager fpga0: Stratix10 SOC FPGA Manager registered
[    3.269367] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 400000Hz, actual 396825HZ div = 63)
[    3.271690] u32 classifier
[    3.278928]     input device check on
[    3.281307]     Actions configured
[    3.284049] NET: Registered protocol family 10
[    3.290130] Segment Routing with IPv6
[    3.292582] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
[    3.297733] NET: Registered protocol family 17
[    3.301003] Bridge firewalling registered
[    3.303820] Key type dns_resolver registered
[    3.306943] NET: Registered protocol family 40
[    3.310541] Key type ._fscrypt registered
[    3.313268] Key type .fscrypt registered
[    3.315902] Key type fscrypt-provisioning registered
[    3.320536] Btrfs loaded, crc32c=crc32c-generic
[    3.324712] Key type encrypted registered
[    3.330551] dma-pl330 ffda0000.pdma: Loaded driver for PL330 DMAC-341330
[    3.335952] dma-pl330 ffda0000.pdma: 	DBUFF-512x8bytes Num_Chans-8 Num_Peri-32 Num_Events-8
[    3.350994] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
[    3.352775] at24 0-0051: supply vcc not found, using dummy regulator
[    3.364521] mmc0: new high speed SDXC card at address 0001
[    3.365252] at24 0-0051: 4096 byte 24c32 EEPROM, writable, 32 bytes/write
[    3.374789] mmcblk0: mmc0:0001 SD64G 58.2 GiB 
[    3.377559] rtc-ds1307 0-0068: registered as rtc0
[    3.382233]  mmcblk0: p1 p2
[    3.383736] rtc-ds1307 0-0068: setting system clock to 2000-01-01T01:11:22 UTC (946689082)
[    3.391054] of-fpga-region soc:base_fpga_region: FPGA Region probed
[    3.397388] printk: console [netcon0] enabled
[    3.400466] netconsole: network logging started
[    3.403698] of_cfs_init
[    3.404933] of_cfs_init: OK
[    3.406826] dw-apb-uart ffc02000.serial: forbid DMA for kernel console
[    3.412144] md: Waiting for all devices to be available before autodetect
[    3.417641] md: If you don't use raid, use raid=noautodetect
[    3.422016] md: Autodetecting RAID arrays.
[    3.424835] md: autorun ...
[    3.426325] md: ... autorun DONE.
[    3.448891] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
[    3.455741] VFS: Mounted root (ext4 filesystem) on device 179:2.
[    3.461431] devtmpfs: mounted
[    3.467504] Freeing unused kernel memory: 3968K
[    3.470862] Run /sbin/init as init process
[    3.473659]   with arguments:
[    3.473663]     /sbin/init
[    3.473667]   with environment:
[    3.473671]     HOME=/
[    3.473676]     TERM=linux
[    3.559880] random: fast init done
[    3.857119] systemd[1]: System time before build time, advancing clock.
[    3.922285] systemd[1]: systemd 247.4+ running in system mode. (+PAM -AUDIT -SELINUX +IMA -APPARMOR -SMACK +SYSVINIT +UTMP -LIBCRYPTSETUP -GCRYPT -GNUTLS +ACL +XZ -LZ4 -ZSTD -SECCOMP +BLKID -ELFUTILS +KMOD -IDN2 -IDN -PCRE2 default-hierarchy=hybrid)
[    3.943571] systemd[1]: Detected architecture arm64.
[    3.955582] usb 1-1: new high-speed USB device number 2 using dwc2
[    3.988465] systemd[1]: Set hostname to <intel-socfpga-64>.
[    4.180625] usb-storage 1-1:1.0: USB Mass Storage device detected
[    4.185946] scsi host0: usb-storage 1-1:1.0
[    4.472783] systemd[1]: Queued start job for default target Graphical Interface.
[    4.480253] random: systemd: uninitialized urandom read (16 bytes read)
[    4.518567] systemd[1]: Created slice system-getty.slice.
[    4.531814] random: systemd: uninitialized urandom read (16 bytes read)
[    4.538774] systemd[1]: Created slice system-modprobe.slice.
[    4.551683] random: systemd: uninitialized urandom read (16 bytes read)
[    4.558548] systemd[1]: Created slice system-serial\x2dgetty.slice.
[    4.577249] systemd[1]: Created slice User and Session Slice.
[    4.592005] systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
[    4.607837] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[    4.624020] systemd[1]: Reached target Paths.
[    4.635704] systemd[1]: Reached target Remote File Systems.
[    4.651682] systemd[1]: Reached target Slices.
[    4.663705] systemd[1]: Reached target Swap.
[    4.692973] systemd[1]: Listening on RPCbind Server Activation Socket.
[    4.707819] systemd[1]: Reached target RPC Port Mapper.
[    4.725144] systemd[1]: Listening on Syslog Socket.
[    4.743944] systemd[1]: Listening on initctl Compatibility Named Pipe.
[    4.763186] systemd[1]: Condition check resulted in Journal Audit Socket being skipped.
[    4.770561] systemd[1]: Listening on Journal Socket (/dev/log).
[    4.784205] systemd[1]: Listening on Journal Socket.
[    4.800341] systemd[1]: Listening on Network Service Netlink Socket.
[    4.816267] systemd[1]: Listening on udev Control Socket.
[    4.832029] systemd[1]: Listening on udev Kernel Socket.
[    4.848025] systemd[1]: Listening on User Database Manager Socket.
[    4.864197] systemd[1]: Condition check resulted in Huge Pages File System being skipped.
[    4.874916] systemd[1]: Mounting POSIX Message Queue File System...
[    4.899882] systemd[1]: Mounting Kernel Debug File System...
[    4.919810] systemd[1]: Mounting Kernel Trace File System...
[    4.940589] systemd[1]: Mounting Temporary Directory (/tmp)...
[    4.960888] systemd[1]: Starting Create list of static device nodes for the current kernel...
[    4.983911] systemd[1]: Starting Load Kernel Module configfs...
[    5.003808] systemd[1]: Starting Load Kernel Module drm...
[    5.023863] systemd[1]: Starting Load Kernel Module fuse...
[    5.043280] fuse: init (API version 7.32)
[    5.044564] systemd[1]: Starting RPC Bind...
[    5.059943] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
[    5.074478] systemd[1]: Starting Journal Service...
[    5.106238] systemd[1]: Starting Load Kernel Modules...
[    5.124231] systemd[1]: Starting Remount Root and Kernel File Systems...
[    5.144907] systemd[1]: Starting Coldplug All udev Devices...
[    5.157281] EXT4-fs (mmcblk0p2): re-mounted. Opts: (null)
[    5.171763] systemd[1]: Started RPC Bind.
[    5.177398] openvswitch: Open vSwitch switching datapath
[    5.188530] systemd[1]: Mounted POSIX Message Queue File System.
[    5.204656] systemd[1]: Mounted Kernel Debug File System.
[    5.221242] scsi 0:0:0:0: Direct-Access     Generic- SD/MMC           1.00 PQ: 0 ANSI: 0 CCS
[    5.229268] systemd[1]: Mounted Kernel Trace File System.
[    5.244316] systemd[1]: Started Journal Service.
[    5.424686] systemd-journald[143]: Received client request to flush runtime journal.
[    5.855286] sd 0:0:0:0: [sda] 30244864 512-byte logical blocks: (15.5 GB/14.4 GiB)
[    5.862581] sd 0:0:0:0: [sda] Write Protect is off
[    5.872427] sd 0:0:0:0: [sda] Mode Sense: 03 00 00 00
[    5.872915] sd 0:0:0:0: [sda] No Caching mode page found
[    5.882816] sd 0:0:0:0: [sda] Assuming drive cache: write through
[    5.918708]  sda: sda1
[    5.927304] sd 0:0:0:0: [sda] Attached SCSI removable disk
[    5.995594] nvidia_drm: loading out-of-tree module taints kernel.
[    6.000634] nvidia_drm: module license 'MIT' taints kernel.
[    6.004973] Disabling lock debugging due to kernel taint
[    7.831597] random: crng init done
[    7.833728] random: 7 urandom warning(s) missed due to ratelimiting
[    8.227303] FAT-fs (mmcblk0p1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.
[    8.389846] nvidia-nvlink: Nvlink Core is being initialized, major device number 245

[    8.400353] nvidia 0000:01:00.0: enabling device (0000 -> 0002)
[    8.406398] nvidia 0000:01:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=none:owns=none
[    8.469193] NVRM: loading NVIDIA UNIX aarch64 Kernel Module  465.31  Thu May 13 22:39:49 UTC 2021
[   10.935596] socfpga-dwmac ff800000.ethernet eth0: PHY [stmmac-0:04] driver [Micrel KSZ9031 Gigabit PHY] (irq=POLL)
[   10.967589] socfpga-dwmac ff800000.ethernet eth0: No Safety Features support found
[   10.973912] socfpga-dwmac ff800000.ethernet eth0: IEEE 1588-2008 Advanced Timestamp supported
[   11.000311] socfpga-dwmac ff800000.ethernet eth0: registered PTP clock
[   11.019717] socfpga-dwmac ff800000.ethernet eth0: configuring for phy/rgmii link mode
[   11.619188] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   11.635842] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   11.695263] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   11.711834] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   13.093233] socfpga-dwmac ff800000.ethernet eth0: Link is Up - 100Mbps/Full - flow control rx/tx
[   13.100784] IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
[   16.942945] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   16.948800] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   16.964353] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   16.970209] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   22.300174] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   22.306004] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   22.321013] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   22.326830] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   27.802498] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   27.808327] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   27.823006] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   27.828837] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0




Without GPU card inserted
root@intel-socfpga-64:~# dmesg
[    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
[    0.000000] Linux version 5.10.35-yocto-standard (oe-user@oe-host) (aarch64-wrs-linux-gcc (GCC) 10.2.0, GNU ld (GNU Binutils) 2.36.1.20210209) #1 SMP PREEMPT Wed May 12 08:49:49 UTC 2021
[    0.000000] Machine model: SoCFPGA Stratix 10 SoCDK
[    0.000000] earlycon: uart0 at MMIO32 0x00000000ffc02000 (options '115200n8')
[    0.000000] printk: bootconsole [uart0] enabled
[    0.000000] efi: UEFI not found.
[    0.000000] Reserved memory: created DMA memory pool at 0x0000000000000000, size 16 MiB
[    0.000000] OF: reserved mem: initialized node svcbuffer@0, compatible id shared-dma-pool
[    0.000000] cma: Reserved 16 MiB at 0x000000007e800000
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000000000-0x00000000ffffffff]
[    0.000000]   DMA32    empty
[    0.000000]   Normal   [mem 0x0000000100000000-0x00000001ffffffff]
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000000000-0x0000000000ffffff]
[    0.000000]   node   0: [mem 0x0000000001000000-0x000000007fffffff]
[    0.000000]   node   0: [mem 0x0000000180000000-0x00000001ffffffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000000000-0x00000001ffffffff]
[    0.000000] On node 0 totalpages: 1048576
[    0.000000]   DMA zone: 8192 pages used for memmap
[    0.000000]   DMA zone: 0 pages reserved
[    0.000000]   DMA zone: 524288 pages, LIFO batch:63
[    0.000000]   Normal zone: 8192 pages used for memmap
[    0.000000]   Normal zone: 524288 pages, LIFO batch:63
[    0.000000] psci: probing for conduit method from DT.
[    0.000000] psci: PSCIv65535.65535 detected in firmware.
[    0.000000] psci: Using standard PSCI v0.2 function IDs
[    0.000000] psci: MIGRATE_INFO_TYPE not supported.
[    0.000000] psci: SMC Calling Convention v1.0
[    0.000000] percpu: Embedded 30 pages/cpu s82008 r8192 d32680 u122880
[    0.000000] pcpu-alloc: s82008 r8192 d32680 u122880 alloc=30*4096
[    0.000000] pcpu-alloc: [0] 0 [0] 1 [0] 2 [0] 3 
[    0.000000] Detected VIPT I-cache on CPU0
[    0.000000] CPU features: detected: ARM erratum 845719
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 1032192
[    0.000000] Kernel command line: earlycon panic=-1 root=/dev/mmcblk0p2 rw rootwait
[    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
[    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
[    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
[    0.000000] software IO TLB: mapped [mem 0x000000007a800000-0x000000007e800000] (64MB)
[    0.000000] Memory: 3993020K/4194304K available (12416K kernel code, 1952K rwdata, 2936K rodata, 3968K init, 707K bss, 184900K reserved, 16384K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] ftrace: allocating 38327 entries in 150 pages
[    0.000000] ftrace: allocated 150 pages with 4 groups
[    0.000000] rcu: Preemptible hierarchical RCU implementation.
[    0.000000] rcu: 	RCU event tracing is enabled.
[    0.000000] 	Trampoline variant of Tasks RCU enabled.
[    0.000000] 	Rude variant of Tasks RCU enabled.
[    0.000000] 	Tracing variant of Tasks RCU enabled.
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
[    0.000000] GIC: Using split EOI/Deactivate mode
[    0.000000] random: get_random_bytes called from start_kernel+0x398/0x5a0 with crng_init=0
[    0.000000] arch_timer: cp15 timer(s) running at 400.00MHz (phys).
[    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x5c4093a7d1, max_idle_ns: 440795210635 ns
[    0.000005] sched_clock: 56 bits at 400MHz, resolution 2ns, wraps every 4398046511103ns
[    0.006867] Console: colour dummy device 80x25
[    0.009997] printk: console [tty0] enabled
[    0.012790] printk: bootconsole [uart0] disabled
[    0.016119] Calibrating delay loop (skipped), value calculated using timer frequency.. 800.00 BogoMIPS (lpj=1600000)
[    0.016143] pid_max: default: 32768 minimum: 301
[    0.016255] LSM: Security Framework initializing
[    0.016431] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.016465] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.018380] rcu: Hierarchical SRCU implementation.
[    0.018916] EFI services will not be available.
[    0.019157] smp: Bringing up secondary CPUs ...
[    0.019696] Detected VIPT I-cache on CPU1
[    0.019759] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
[    0.020370] Detected VIPT I-cache on CPU2
[    0.020403] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
[    0.021011] Detected VIPT I-cache on CPU3
[    0.021042] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
[    0.021146] smp: Brought up 1 node, 4 CPUs
[    0.021190] SMP: Total of 4 processors activated.
[    0.021201] CPU features: detected: 32-bit EL0 Support
[    0.021214] CPU features: detected: CRC32 instructions
[    0.021274] CPU: All CPU(s) started at EL2
[    0.021303] alternatives: patching kernel code
[    0.022054] devtmpfs: initialized
[    0.025872] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.025907] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
[    0.027053] DMI not present or invalid.
[    0.027528] NET: Registered protocol family 16
[    0.029224] DMA: preallocated 512 KiB GFP_KERNEL pool for atomic allocations
[    0.029410] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
[    0.029759] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
[    0.030435] cpuidle: using governor ladder
[    0.030527] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
[    0.030630] ASID allocator initialised with 65536 entries
[    0.117031] raid6: neonx8   gen()  1739 MB/s
[    0.185120] raid6: neonx8   xor()  1287 MB/s
[    0.253233] raid6: neonx4   gen()  1787 MB/s
[    0.321337] raid6: neonx4   xor()  1263 MB/s
[    0.389451] raid6: neonx2   gen()  1683 MB/s
[    0.457558] raid6: neonx2   xor()  1165 MB/s
[    0.525669] raid6: neonx1   gen()  1446 MB/s
[    0.593781] raid6: neonx1   xor()   989 MB/s
[    0.661877] raid6: int64x8  gen()  1198 MB/s
[    0.729979] raid6: int64x8  xor()   642 MB/s
[    0.798095] raid6: int64x4  gen()  1335 MB/s
[    0.866220] raid6: int64x4  xor()   681 MB/s
[    0.934286] raid6: int64x2  gen()  1166 MB/s
[    1.002358] raid6: int64x2  xor()   624 MB/s
[    1.070463] raid6: int64x1  gen()   863 MB/s
[    1.138530] raid6: int64x1  xor()   431 MB/s
[    1.138541] raid6: using algorithm neonx4 gen() 1787 MB/s
[    1.138553] raid6: .... xor() 1263 MB/s, rmw enabled
[    1.138565] raid6: using neon recovery algorithm
[    1.139609] iommu: Default domain type: Translated 
[    1.139808] vgaarb: loaded
[    1.140042] SCSI subsystem initialized
[    1.140267] usbcore: registered new interface driver usbfs
[    1.140325] usbcore: registered new interface driver hub
[    1.140370] usbcore: registered new device driver usb
[    1.140518] usb_phy_generic soc:usbphy@0: supply vcc not found, using dummy regulator
[    1.140995] pps_core: LinuxPPS API ver. 1 registered
[    1.141009] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    1.141037] PTP clock support registered
[    1.141225] EDAC MC: Ver: 3.0.0
[    1.142283] Intel Service Layer Driver Initialized
[    1.142429] FPGA manager framework
[    1.143436] clocksource: Switched to clocksource arch_sys_counter
[    1.899192] NET: Registered protocol family 2
[    1.899899] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes, linear)
[    1.900027] TCP established hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    1.900287] TCP bind hash table entries: 32768 (order: 7, 524288 bytes, linear)
[    1.900779] TCP: Hash tables configured (established 32768 bind 32768)
[    1.900915] UDP hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    1.901016] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    1.901268] NET: Registered protocol family 1
[    1.901750] RPC: Registered named UNIX socket transport module.
[    1.901764] RPC: Registered udp transport module.
[    1.901774] RPC: Registered tcp transport module.
[    1.901785] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    1.901807] PCI: CLS 0 bytes, default 64
[    1.902812] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
[    1.904340] workingset: timestamp_bits=46 max_order=20 bucket_order=0
[    1.911748] NFS: Registering the id_resolver key type
[    1.911787] Key type id_resolver registered
[    1.911798] Key type id_legacy registered
[    1.912476] Key type cifs.idmap registered
[    1.957359] xor: measuring software checksum speed
[    1.962402]    8regs           :  1968 MB/sec
[    1.966642]    32regs          :  2331 MB/sec
[    1.972374]    arm64_neon      :  1726 MB/sec
[    1.972386] xor: using function: 32regs (2331 MB/sec)
[    1.972404] async_tx: api initialized (async)
[    1.972450] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 248)
[    1.972467] io scheduler mq-deadline registered
[    1.972479] io scheduler kyber registered
[    1.973065] gpio-dwapb ffc03300.gpio: Cannot get reset descriptor
[    1.973493] altera-pcie a0000000.pcie: host bridge /soc/bridge@80000000/pcie@200000000 ranges:
[    1.973556] altera-pcie a0000000.pcie:      MEM 0x0090000000..0x0097ffffff -> 0x0000000000
[    1.973813] altera-pcie a0000000.pcie: PCI host bridge to bus 0000:00
[    1.973835] pci_bus 0000:00: root bus resource [bus 00-ff]
[    1.973852] pci_bus 0000:00: root bus resource [mem 0x90000000-0x97ffffff] (bus address [0x00000000-0x07ffffff])
[    1.973932] pci 0000:00:00.0: [1172:e000] type 01 class 0x060400
[    1.974011] pci 0000:00:00.0: enabling Extended Tags
[    1.975288] pci 0000:00:00.0: bridge configuration invalid ([bus 00-00]), reconfiguring
[    1.976312] pci_bus 0000:01: busn_res: [bus 01-ff] end is updated to 01
[    1.976348] pci 0000:00:00.0: PCI bridge to [bus 01]
[    1.976714] pcieport 0000:00:00.0: PME: Signaling with IRQ 42
[    1.977925] Serial: 8250/16550 driver, 4 ports, IRQ sharing enabled
[    1.979252] ffc02000.serial: ttyS0 at MMIO 0xffc02000 (irq = 33, base_baud = 6250000) is a 16550A
[    2.669401] printk: console [ttyS0] enabled
[    2.673396] cacheinfo: Unable to detect cache hierarchy for CPU 0
[    2.685690] brd: module loaded
[    2.696149] loop: module loaded
[    2.711555] spi-nor spi0.0: mt25qu02g (262144 Kbytes)
[    2.715337] 2 fixed-partitions partitions found on MTD device ff8d2000.spi.0
[    2.721076] Creating 2 MTD partitions on "ff8d2000.spi.0":
[    2.725259] 0x000000910000-0x000100010000 : "Boot and fpga data"
[    2.729958] mtd: partition "Boot and fpga data" extends beyond the end of device "ff8d2000.spi.0" -- size truncated to 0xf6f0000
[    2.744388] 0x000003fe0000-0x000010000000 : "Root Filesystem - JFFS2"
[    2.757242] libphy: Fixed MDIO Bus: probed
[    2.760501] socfpga-dwmac ff800000.ethernet: IRQ eth_wake_irq not found
[    2.765810] socfpga-dwmac ff800000.ethernet: IRQ eth_lpi not found
[    2.771060] socfpga-dwmac ff800000.ethernet: User ID: 0x11, Synopsys ID: 0x37
[    2.776892] socfpga-dwmac ff800000.ethernet: 	DWMAC1000
[    2.780814] socfpga-dwmac ff800000.ethernet: DMA HW capability register supported
[    2.786981] socfpga-dwmac ff800000.ethernet: RX Checksum Offload Engine supported
[    2.793177] socfpga-dwmac ff800000.ethernet: COE Type 2
[    2.797097] socfpga-dwmac ff800000.ethernet: TX Checksum insertion supported
[    2.802832] socfpga-dwmac ff800000.ethernet: Enhanced/Alternate descriptors
[    2.808480] socfpga-dwmac ff800000.ethernet: Enabled extended descriptors
[    2.813955] socfpga-dwmac ff800000.ethernet: Ring mode enabled
[    2.818485] socfpga-dwmac ff800000.ethernet: Enable RX Mitigation via HW Watchdog Timer
[    2.825180] socfpga-dwmac ff800000.ethernet: device MAC address 2a:49:56:7b:2f:38
[    2.831832] libphy: stmmac: probed
[    2.836838] dwc2 ffb00000.usb: supply vusb_d not found, using dummy regulator
[    2.842803] dwc2 ffb00000.usb: supply vusb_a not found, using dummy regulator
[    2.848959] dwc2 ffb00000.usb: EPs: 16, dedicated fifos, 8064 entries in SPRAM
[    2.855152] dwc2 ffb00000.usb: DWC OTG Controller
[    2.858607] dwc2 ffb00000.usb: new USB bus registered, assigned bus number 1
[    2.864370] dwc2 ffb00000.usb: irq 34, io mem 0xffb00000
[    2.869051] hub 1-0:1.0: USB hub found
[    2.871540] hub 1-0:1.0: 1 port detected
[    2.875549] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    2.880798] ehci-pci: EHCI PCI platform driver
[    2.883981] ehci-platform: EHCI generic platform driver
[    2.888304] usbcore: registered new interface driver usb-storage
[    2.893896] i2c /dev entries driver
[    2.897191] device-mapper: ioctl: 4.43.0-ioctl (2020-10-01) initialised: dm-devel@redhat.com
[    2.905160] EDAC DEVICE0: Giving out device to module sdramedac controller Altera ECC Manager: DEV sdramedac (INTERRUPT)
[    2.915040] sdhci: Secure Digital Host Controller Interface driver
[    2.919917] sdhci: Copyright(c) Pierre Ossman
[    2.922962] Synopsys Designware Multimedia Card Interface Driver
[    2.927773] sdhci-pltfm: SDHCI platform and OF driver helper
[    2.927913] dw_mmc ff808000.dwmmc0: IDMAC supports 32-bit address mode.
[    2.935741] usbcore: registered new interface driver usbhid
[    2.937461] dw_mmc ff808000.dwmmc0: Using internal DMA controller.
[    2.941684] usbhid: USB HID core driver
[    2.946550] dw_mmc ff808000.dwmmc0: Version ID is 280a
[    2.949352] fpga_manager fpga0: Stratix10 SOC FPGA Manager registered
[    2.952945] dw_mmc ff808000.dwmmc0: DW MMC controller at irq 19,32 bit host data width,1024 deep fifo
[    2.958142] u32 classifier
[    2.966131] mmc_host mmc0: card is polling.
[    2.967318]     input device check on
[    2.972550]     Actions configured
[    2.975270] NET: Registered protocol family 10
[    2.979439] Segment Routing with IPv6
[    2.981853] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
[    2.982847] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 400000Hz, actual 396825HZ div = 63)
[    2.986989] NET: Registered protocol family 17
[    2.997811] Bridge firewalling registered
[    3.000627] Key type dns_resolver registered
[    3.003742] NET: Registered protocol family 40
[    3.007275] Key type ._fscrypt registered
[    3.009989] Key type .fscrypt registered
[    3.012610] Key type fscrypt-provisioning registered
[    3.017208] Btrfs loaded, crc32c=crc32c-generic
[    3.021352] Key type encrypted registered
[    3.027042] dma-pl330 ffda0000.pdma: Loaded driver for PL330 DMAC-341330
[    3.032444] dma-pl330 ffda0000.pdma: 	DBUFF-512x8bytes Num_Chans-8 Num_Peri-32 Num_Events-8
[    3.042681] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
[    3.049104] at24 0-0051: supply vcc not found, using dummy regulator
[    3.051174] mmc0: new high speed SDXC card at address 0001
[    3.056910] at24 0-0051: 4096 byte 24c32 EEPROM, writable, 32 bytes/write
[    3.060989] mmcblk0: mmc0:0001 SD64G 58.2 GiB 
[    3.067186] rtc-ds1307 0-0068: SET TIME!
[    3.072827]  mmcblk0: p1 p2
[    3.073796] rtc-ds1307 0-0068: registered as rtc0
[    3.078743] rtc-ds1307 0-0068: setting system clock to 2000-01-01T00:00:13 UTC (946684813)
[    3.086064] of-fpga-region soc:base_fpga_region: FPGA Region probed
[    3.092367] printk: console [netcon0] enabled
[    3.095413] netconsole: network logging started
[    3.098664] of_cfs_init
[    3.099924] of_cfs_init: OK
[    3.101826] dw-apb-uart ffc02000.serial: forbid DMA for kernel console
[    3.107104] md: Waiting for all devices to be available before autodetect
[    3.112614] md: If you don't use raid, use raid=noautodetect
[    3.116977] md: Autodetecting RAID arrays.
[    3.119775] md: autorun ...
[    3.121264] md: ... autorun DONE.
[    3.209635] random: fast init done
[    3.614677] EXT4-fs (mmcblk0p2): recovery complete
[    3.619389] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
[    3.626244] VFS: Mounted root (ext4 filesystem) on device 179:2.
[    3.631981] devtmpfs: mounted
[    3.637982] Freeing unused kernel memory: 3968K
[    3.641345] Run /sbin/init as init process
[    3.644145]   with arguments:
[    3.644149]     /sbin/init
[    3.644153]   with environment:
[    3.644157]     HOME=/
[    3.644161]     TERM=linux
[    3.719565] usb 1-1: new high-speed USB device number 2 using dwc2
[    3.944446] usb-storage 1-1:1.0: USB Mass Storage device detected
[    3.950073] scsi host0: usb-storage 1-1:1.0
[    4.014049] systemd[1]: System time before build time, advancing clock.
[    4.078405] systemd[1]: systemd 247.4+ running in system mode. (+PAM -AUDIT -SELINUX +IMA -APPARMOR -SMACK +SYSVINIT +UTMP -LIBCRYPTSETUP -GCRYPT -GNUTLS +ACL +XZ -LZ4 -ZSTD -SECCOMP +BLKID -ELFUTILS +KMOD -IDN2 -IDN -PCRE2 default-hierarchy=hybrid)
[    4.099755] systemd[1]: Detected architecture arm64.
[    4.144337] systemd[1]: Set hostname to <intel-socfpga-64>.
[    4.625123] systemd[1]: Queued start job for default target Graphical Interface.
[    4.632567] random: systemd: uninitialized urandom read (16 bytes read)
[    4.671423] systemd[1]: Created slice system-getty.slice.
[    4.687614] random: systemd: uninitialized urandom read (16 bytes read)
[    4.694574] systemd[1]: Created slice system-modprobe.slice.
[    4.707557] random: systemd: uninitialized urandom read (16 bytes read)
[    4.714344] systemd[1]: Created slice system-serial\x2dgetty.slice.
[    4.733094] systemd[1]: Created slice User and Session Slice.
[    4.747878] systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
[    4.763728] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[    4.779857] systemd[1]: Reached target Paths.
[    4.791571] systemd[1]: Reached target Remote File Systems.
[    4.807566] systemd[1]: Reached target Slices.
[    4.819596] systemd[1]: Reached target Swap.
[    4.849057] systemd[1]: Listening on RPCbind Server Activation Socket.
[    4.863697] systemd[1]: Reached target RPC Port Mapper.
[    4.881019] systemd[1]: Listening on Syslog Socket.
[    4.895840] systemd[1]: Listening on initctl Compatibility Named Pipe.
[    4.923018] systemd[1]: Condition check resulted in Journal Audit Socket being skipped.
[    4.930394] systemd[1]: Listening on Journal Socket (/dev/log).
[    4.952130] systemd[1]: Listening on Journal Socket.
[    4.964369] scsi 0:0:0:0: Direct-Access     Generic- SD/MMC           1.00 PQ: 0 ANSI: 0 CCS
[    4.976319] systemd[1]: Listening on Network Service Netlink Socket.
[    4.992172] systemd[1]: Listening on udev Control Socket.
[    5.007900] systemd[1]: Listening on udev Kernel Socket.
[    5.027875] systemd[1]: Listening on User Database Manager Socket.
[    5.048068] systemd[1]: Condition check resulted in Huge Pages File System being skipped.
[    5.058748] systemd[1]: Mounting POSIX Message Queue File System...
[    5.083711] systemd[1]: Mounting Kernel Debug File System...
[    5.107628] systemd[1]: Mounting Kernel Trace File System...
[    5.132468] systemd[1]: Mounting Temporary Directory (/tmp)...
[    5.152835] systemd[1]: Starting Create list of static device nodes for the current kernel...
[    5.175840] systemd[1]: Starting Load Kernel Module configfs...
[    5.195693] systemd[1]: Starting Load Kernel Module drm...
[    5.215643] systemd[1]: Starting Load Kernel Module fuse...
[    5.234835] fuse: init (API version 7.32)
[    5.236512] systemd[1]: Starting RPC Bind...
[    5.255772] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
[    5.270339] systemd[1]: Starting Journal Service...
[    5.298435] systemd[1]: Starting Load Kernel Modules...
[    5.315990] systemd[1]: Starting Remount Root and Kernel File Systems...
[    5.340723] systemd[1]: Starting Coldplug All udev Devices...
[    5.351668] EXT4-fs (mmcblk0p2): re-mounted. Opts: (null)
[    5.368671] systemd[1]: Started RPC Bind.
[    5.369053] openvswitch: Open vSwitch switching datapath
[    5.388399] systemd[1]: Started Journal Service.
[    5.596673] sd 0:0:0:0: [sda] 30244864 512-byte logical blocks: (15.5 GB/14.4 GiB)
[    5.607583] sd 0:0:0:0: [sda] Write Protect is off
[    5.609423] systemd-journald[143]: Received client request to flush runtime journal.
[    5.611097] sd 0:0:0:0: [sda] Mode Sense: 03 00 00 00
[    5.618231] sd 0:0:0:0: [sda] No Caching mode page found
[    5.627061] sd 0:0:0:0: [sda] Assuming drive cache: write through
[    5.669948]  sda: sda1
[    5.673733] sd 0:0:0:0: [sda] Attached SCSI removable disk
[    7.607500] random: crng init done
[    7.609629] random: 7 urandom warning(s) missed due to ratelimiting
[    9.327482] socfpga-dwmac ff800000.ethernet eth0: PHY [stmmac-0:04] driver [Micrel KSZ9031 Gigabit PHY] (irq=POLL)
[    9.359493] socfpga-dwmac ff800000.ethernet eth0: No Safety Features support found
[    9.365794] socfpga-dwmac ff800000.ethernet eth0: IEEE 1588-2008 Advanced Timestamp supported
[    9.384246] socfpga-dwmac ff800000.ethernet eth0: registered PTP clock
[    9.393088] socfpga-dwmac ff800000.ethernet eth0: configuring for phy/rgmii link mode
[   11.461151] socfpga-dwmac ff800000.ethernet eth0: Link is Up - 100Mbps/Full - flow control rx/tx
[   11.468698] IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready



https://rocketboards.org/foswiki/Projects/Stratix10PCIeRootPortWithMSI


$ cd ~
$ git clone https://github.com/altera-opensource/linux-socfpga
$ cd linux-socfpga
$ git checkout ACDS19.3_REL_GSRD_PR -b mybranch
$ git apply arm64_dts_add_stratix_10_PCIe_node.patch
$ make defconfig
$ make menuconfig


after change dtb

root@intel-socfpga-64:~# dmesg   
[    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
[    0.000000] Linux version 5.10.35-yocto-standard (oe-user@oe-host) (aarch64-wrs-linux-gcc (GCC) 10.2.0, GNU ld (GNU Binutils) 2.36.1.20210209) #1 SMP PREEMPT Wed May 12 08:49:49 UTC 2021
[    0.000000] Machine model: SoCFPGA Stratix 10 SoCDK
[    0.000000] earlycon: uart0 at MMIO32 0x00000000ffc02000 (options '115200n8')
[    0.000000] printk: bootconsole [uart0] enabled
[    0.000000] efi: UEFI not found.
[    0.000000] Reserved memory: created DMA memory pool at 0x0000000000000000, size 16 MiB
[    0.000000] OF: reserved mem: initialized node svcbuffer@0, compatible id shared-dma-pool
[    0.000000] cma: Reserved 16 MiB at 0x000000007e800000
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000000000-0x00000000ffffffff]
[    0.000000]   DMA32    empty
[    0.000000]   Normal   [mem 0x0000000100000000-0x00000001ffffffff]
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000000000-0x0000000000ffffff]
[    0.000000]   node   0: [mem 0x0000000001000000-0x000000007fffffff]
[    0.000000]   node   0: [mem 0x0000000180000000-0x00000001ffffffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000000000-0x00000001ffffffff]
[    0.000000] On node 0 totalpages: 1048576
[    0.000000]   DMA zone: 8192 pages used for memmap
[    0.000000]   DMA zone: 0 pages reserved
[    0.000000]   DMA zone: 524288 pages, LIFO batch:63
[    0.000000]   Normal zone: 8192 pages used for memmap
[    0.000000]   Normal zone: 524288 pages, LIFO batch:63
[    0.000000] psci: probing for conduit method from DT.
[    0.000000] psci: PSCIv65535.65535 detected in firmware.
[    0.000000] psci: Using standard PSCI v0.2 function IDs
[    0.000000] psci: MIGRATE_INFO_TYPE not supported.
[    0.000000] psci: SMC Calling Convention v1.0
[    0.000000] percpu: Embedded 30 pages/cpu s82008 r8192 d32680 u122880
[    0.000000] pcpu-alloc: s82008 r8192 d32680 u122880 alloc=30*4096
[    0.000000] pcpu-alloc: [0] 0 [0] 1 [0] 2 [0] 3 
[    0.000000] Detected VIPT I-cache on CPU0
[    0.000000] CPU features: detected: ARM erratum 845719
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 1032192
[    0.000000] Kernel command line: earlycon panic=-1 root=/dev/mmcblk0p2 rw rootwait
[    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
[    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
[    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
[    0.000000] software IO TLB: mapped [mem 0x000000007a800000-0x000000007e800000] (64MB)
[    0.000000] Memory: 3993020K/4194304K available (12416K kernel code, 1952K rwdata, 2936K rodata, 3968K init, 707K bss, 184900K reserved, 16384K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] ftrace: allocating 38327 entries in 150 pages
[    0.000000] ftrace: allocated 150 pages with 4 groups
[    0.000000] rcu: Preemptible hierarchical RCU implementation.
[    0.000000] rcu: 	RCU event tracing is enabled.
[    0.000000] 	Trampoline variant of Tasks RCU enabled.
[    0.000000] 	Rude variant of Tasks RCU enabled.
[    0.000000] 	Tracing variant of Tasks RCU enabled.
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
[    0.000000] GIC: Using split EOI/Deactivate mode
[    0.000000] random: get_random_bytes called from start_kernel+0x398/0x5a0 with crng_init=0
[    0.000000] arch_timer: cp15 timer(s) running at 400.00MHz (phys).
[    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x5c4093a7d1, max_idle_ns: 440795210635 ns
[    0.000005] sched_clock: 56 bits at 400MHz, resolution 2ns, wraps every 4398046511103ns
[    0.006867] Console: colour dummy device 80x25
[    0.009997] printk: console [tty0] enabled
[    0.012790] printk: bootconsole [uart0] disabled
[    0.016118] Calibrating delay loop (skipped), value calculated using timer frequency.. 800.00 BogoMIPS (lpj=1600000)
[    0.016143] pid_max: default: 32768 minimum: 301
[    0.016254] LSM: Security Framework initializing
[    0.016433] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.016467] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.018386] rcu: Hierarchical SRCU implementation.
[    0.018923] EFI services will not be available.
[    0.019165] smp: Bringing up secondary CPUs ...
[    0.019707] Detected VIPT I-cache on CPU1
[    0.019772] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
[    0.020383] Detected VIPT I-cache on CPU2
[    0.020418] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
[    0.021025] Detected VIPT I-cache on CPU3
[    0.021057] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
[    0.021167] smp: Brought up 1 node, 4 CPUs
[    0.021210] SMP: Total of 4 processors activated.
[    0.021222] CPU features: detected: 32-bit EL0 Support
[    0.021234] CPU features: detected: CRC32 instructions
[    0.021294] CPU: All CPU(s) started at EL2
[    0.021323] alternatives: patching kernel code
[    0.022074] devtmpfs: initialized
[    0.025873] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.025908] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
[    0.027053] DMI not present or invalid.
[    0.027522] NET: Registered protocol family 16
[    0.029222] DMA: preallocated 512 KiB GFP_KERNEL pool for atomic allocations
[    0.029409] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
[    0.029759] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
[    0.030433] cpuidle: using governor ladder
[    0.030528] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
[    0.030631] ASID allocator initialised with 65536 entries
[    0.117022] raid6: neonx8   gen()  1742 MB/s
[    0.185117] raid6: neonx8   xor()  1287 MB/s
[    0.253242] raid6: neonx4   gen()  1788 MB/s
[    0.321337] raid6: neonx4   xor()  1260 MB/s
[    0.389447] raid6: neonx2   gen()  1683 MB/s
[    0.457552] raid6: neonx2   xor()  1165 MB/s
[    0.525680] raid6: neonx1   gen()  1446 MB/s
[    0.593773] raid6: neonx1   xor()   990 MB/s
[    0.661876] raid6: int64x8  gen()  1198 MB/s
[    0.729978] raid6: int64x8  xor()   642 MB/s
[    0.798088] raid6: int64x4  gen()  1335 MB/s
[    0.866212] raid6: int64x4  xor()   679 MB/s
[    0.934287] raid6: int64x2  gen()  1165 MB/s
[    1.002373] raid6: int64x2  xor()   625 MB/s
[    1.070459] raid6: int64x1  gen()   863 MB/s
[    1.138531] raid6: int64x1  xor()   431 MB/s
[    1.138542] raid6: using algorithm neonx4 gen() 1788 MB/s
[    1.138554] raid6: .... xor() 1260 MB/s, rmw enabled
[    1.138565] raid6: using neon recovery algorithm
[    1.139609] iommu: Default domain type: Translated 
[    1.139807] vgaarb: loaded
[    1.140045] SCSI subsystem initialized
[    1.140270] usbcore: registered new interface driver usbfs
[    1.140327] usbcore: registered new interface driver hub
[    1.140374] usbcore: registered new device driver usb
[    1.140527] usb_phy_generic soc:usbphy@0: supply vcc not found, using dummy regulator
[    1.141005] pps_core: LinuxPPS API ver. 1 registered
[    1.141019] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    1.141046] PTP clock support registered
[    1.141237] EDAC MC: Ver: 3.0.0
[    1.142298] Intel Service Layer Driver Initialized
[    1.142443] FPGA manager framework
[    1.143443] clocksource: Switched to clocksource arch_sys_counter
[    1.899429] NET: Registered protocol family 2
[    1.900137] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes, linear)
[    1.900269] TCP established hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    1.900529] TCP bind hash table entries: 32768 (order: 7, 524288 bytes, linear)
[    1.901021] TCP: Hash tables configured (established 32768 bind 32768)
[    1.901161] UDP hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    1.901263] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    1.901513] NET: Registered protocol family 1
[    1.902001] RPC: Registered named UNIX socket transport module.
[    1.902016] RPC: Registered udp transport module.
[    1.902027] RPC: Registered tcp transport module.
[    1.902037] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    1.902059] PCI: CLS 0 bytes, default 64
[    1.903058] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
[    1.904578] workingset: timestamp_bits=46 max_order=20 bucket_order=0
[    1.911989] NFS: Registering the id_resolver key type
[    1.912028] Key type id_resolver registered
[    1.912039] Key type id_legacy registered
[    1.912714] Key type cifs.idmap registered
[    1.957067] xor: measuring software checksum speed
[    1.962111]    8regs           :  1968 MB/sec
[    1.966352]    32regs          :  2331 MB/sec
[    1.972083]    arm64_neon      :  1726 MB/sec
[    1.972095] xor: using function: 32regs (2331 MB/sec)
[    1.972112] async_tx: api initialized (async)
[    1.972159] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 248)
[    1.972176] io scheduler mq-deadline registered
[    1.972188] io scheduler kyber registered
[    1.972766] gpio-dwapb ffc03300.gpio: Cannot get reset descriptor
[    1.973197] altera-pcie a0000000.pcie: host bridge /soc/bridge@80000000/pcie@200000000 ranges:
[    1.973260] altera-pcie a0000000.pcie:      MEM 0x0090000000..0x0097ffffff -> 0x0000000000
[    1.973518] altera-pcie a0000000.pcie: PCI host bridge to bus 0000:00
[    1.973541] pci_bus 0000:00: root bus resource [bus 00-ff]
[    1.973558] pci_bus 0000:00: root bus resource [mem 0x90000000-0x97ffffff] (bus address [0x00000000-0x07ffffff])
[    1.973639] pci 0000:00:00.0: [1172:e000] type 01 class 0x060400
[    1.973717] pci 0000:00:00.0: enabling Extended Tags
[    1.974991] pci 0000:00:00.0: bridge configuration invalid ([bus 00-00]), reconfiguring
[    1.976016] pci_bus 0000:01: busn_res: [bus 01-ff] end is updated to 01
[    1.976052] pci 0000:00:00.0: PCI bridge to [bus 01]
[    1.976417] pcieport 0000:00:00.0: PME: Signaling with IRQ 42
[    1.977620] Serial: 8250/16550 driver, 4 ports, IRQ sharing enabled
[    1.978955] ffc02000.serial: ttyS0 at MMIO 0xffc02000 (irq = 33, base_baud = 6250000) is a 16550A
[    2.669089] printk: console [ttyS0] enabled
[    2.673079] cacheinfo: Unable to detect cache hierarchy for CPU 0
[    2.685375] brd: module loaded
[    2.695832] loop: module loaded
[    2.711562] spi-nor spi0.0: mt25qu02g (262144 Kbytes)
[    2.715342] 2 fixed-partitions partitions found on MTD device ff8d2000.spi.0
[    2.721082] Creating 2 MTD partitions on "ff8d2000.spi.0":
[    2.725264] 0x000000910000-0x000100010000 : "Boot and fpga data"
[    2.729963] mtd: partition "Boot and fpga data" extends beyond the end of device "ff8d2000.spi.0" -- size truncated to 0xf6f0000
[    2.744392] 0x000003fe0000-0x000010000000 : "Root Filesystem - JFFS2"
[    2.757256] libphy: Fixed MDIO Bus: probed
[    2.760513] socfpga-dwmac ff800000.ethernet: IRQ eth_wake_irq not found
[    2.765822] socfpga-dwmac ff800000.ethernet: IRQ eth_lpi not found
[    2.771073] socfpga-dwmac ff800000.ethernet: User ID: 0x11, Synopsys ID: 0x37
[    2.776905] socfpga-dwmac ff800000.ethernet: 	DWMAC1000
[    2.780827] socfpga-dwmac ff800000.ethernet: DMA HW capability register supported
[    2.786995] socfpga-dwmac ff800000.ethernet: RX Checksum Offload Engine supported
[    2.793190] socfpga-dwmac ff800000.ethernet: COE Type 2
[    2.797110] socfpga-dwmac ff800000.ethernet: TX Checksum insertion supported
[    2.802846] socfpga-dwmac ff800000.ethernet: Enhanced/Alternate descriptors
[    2.808494] socfpga-dwmac ff800000.ethernet: Enabled extended descriptors
[    2.813969] socfpga-dwmac ff800000.ethernet: Ring mode enabled
[    2.818500] socfpga-dwmac ff800000.ethernet: Enable RX Mitigation via HW Watchdog Timer
[    2.825195] socfpga-dwmac ff800000.ethernet: device MAC address 5e:4e:cb:b3:86:a7
[    2.831846] libphy: stmmac: probed
[    2.836868] dwc2 ffb00000.usb: supply vusb_d not found, using dummy regulator
[    2.842832] dwc2 ffb00000.usb: supply vusb_a not found, using dummy regulator
[    2.848988] dwc2 ffb00000.usb: EPs: 16, dedicated fifos, 8064 entries in SPRAM
[    2.855181] dwc2 ffb00000.usb: DWC OTG Controller
[    2.858635] dwc2 ffb00000.usb: new USB bus registered, assigned bus number 1
[    2.864399] dwc2 ffb00000.usb: irq 34, io mem 0xffb00000
[    2.869078] hub 1-0:1.0: USB hub found
[    2.871567] hub 1-0:1.0: 1 port detected
[    2.875575] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    2.880824] ehci-pci: EHCI PCI platform driver
[    2.884008] ehci-platform: EHCI generic platform driver
[    2.888330] usbcore: registered new interface driver usb-storage
[    2.893918] i2c /dev entries driver
[    2.897215] device-mapper: ioctl: 4.43.0-ioctl (2020-10-01) initialised: dm-devel@redhat.com
[    2.905187] EDAC DEVICE0: Giving out device to module sdramedac controller Altera ECC Manager: DEV sdramedac (INTERRUPT)
[    2.915069] sdhci: Secure Digital Host Controller Interface driver
[    2.919946] sdhci: Copyright(c) Pierre Ossman
[    2.922991] Synopsys Designware Multimedia Card Interface Driver
[    2.927802] sdhci-pltfm: SDHCI platform and OF driver helper
[    2.927953] dw_mmc ff808000.dwmmc0: IDMAC supports 32-bit address mode.
[    2.935780] usbcore: registered new interface driver usbhid
[    2.937490] dw_mmc ff808000.dwmmc0: Using internal DMA controller.
[    2.941712] usbhid: USB HID core driver
[    2.946578] dw_mmc ff808000.dwmmc0: Version ID is 280a
[    2.949380] fpga_manager fpga0: Stratix10 SOC FPGA Manager registered
[    2.952971] dw_mmc ff808000.dwmmc0: DW MMC controller at irq 19,32 bit host data width,1024 deep fifo
[    2.958170] u32 classifier
[    2.966157] mmc_host mmc0: card is polling.
[    2.967346]     input device check on
[    2.972579]     Actions configured
[    2.975306] NET: Registered protocol family 10
[    2.979474] Segment Routing with IPv6
[    2.981889] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
[    2.982876] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 400000Hz, actual 396825HZ div = 63)
[    2.987030] NET: Registered protocol family 17
[    2.997848] Bridge firewalling registered
[    3.000664] Key type dns_resolver registered
[    3.003784] NET: Registered protocol family 40
[    3.007310] Key type ._fscrypt registered
[    3.010024] Key type .fscrypt registered
[    3.012646] Key type fscrypt-provisioning registered
[    3.017243] Btrfs loaded, crc32c=crc32c-generic
[    3.021391] Key type encrypted registered
[    3.027077] dma-pl330 ffda0000.pdma: Loaded driver for PL330 DMAC-341330
[    3.032479] dma-pl330 ffda0000.pdma: 	DBUFF-512x8bytes Num_Chans-8 Num_Peri-32 Num_Events-8
[    3.042739] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
[    3.049122] at24 0-0051: supply vcc not found, using dummy regulator
[    3.051231] mmc0: new high speed SDXC card at address 0001
[    3.056970] at24 0-0051: 4096 byte 24c32 EEPROM, writable, 32 bytes/write
[    3.061046] mmcblk0: mmc0:0001 SD64G 58.2 GiB 
[    3.067232] rtc-ds1307 0-0068: SET TIME!
[    3.072884]  mmcblk0: p1 p2
[    3.073850] rtc-ds1307 0-0068: registered as rtc0
[    3.078814] rtc-ds1307 0-0068: setting system clock to 2000-01-01T00:00:14 UTC (946684814)
[    3.086148] of-fpga-region soc:base_fpga_region: FPGA Region probed
[    3.092473] printk: console [netcon0] enabled
[    3.095531] netconsole: network logging started
[    3.098751] of_cfs_init
[    3.100013] of_cfs_init: OK
[    3.101909] dw-apb-uart ffc02000.serial: forbid DMA for kernel console
[    3.107188] md: Waiting for all devices to be available before autodetect
[    3.112698] md: If you don't use raid, use raid=noautodetect
[    3.117060] md: Autodetecting RAID arrays.
[    3.119859] md: autorun ...
[    3.121348] md: ... autorun DONE.
[    3.215589] random: fast init done
[    3.376991] EXT4-fs (mmcblk0p2): recovery complete
[    3.384107] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
[    3.390959] VFS: Mounted root (ext4 filesystem) on device 179:2.
[    3.396625] devtmpfs: mounted
[    3.402627] Freeing unused kernel memory: 3968K
[    3.405984] Run /sbin/init as init process
[    3.408782]   with arguments:
[    3.408786]     /sbin/init
[    3.408790]   with environment:
[    3.408794]     HOME=/
[    3.408798]     TERM=linux
[    3.719491] usb 1-1: new high-speed USB device number 2 using dwc2
[    3.774181] systemd[1]: System time before build time, advancing clock.
[    3.837932] systemd[1]: systemd 247.4+ running in system mode. (+PAM -AUDIT -SELINUX +IMA -APPARMOR -SMACK +SYSVINIT +UTMP -LIBCRYPTSETUP -GCRYPT -GNUTLS +ACL +XZ -LZ4 -ZSTD -SECCOMP +BLKID -ELFUTILS +KMOD -IDN2 -IDN -PCRE2 default-hierarchy=hybrid)
[    3.859226] systemd[1]: Detected architecture arm64.
[    3.904265] systemd[1]: Set hostname to <intel-socfpga-64>.
[    3.945159] usb-storage 1-1:1.0: USB Mass Storage device detected
[    3.968155] scsi host0: usb-storage 1-1:1.0
[    4.375513] systemd[1]: Queued start job for default target Graphical Interface.
[    4.382969] random: systemd: uninitialized urandom read (16 bytes read)
[    4.422484] systemd[1]: Created slice system-getty.slice.
[    4.435635] random: systemd: uninitialized urandom read (16 bytes read)
[    4.442687] systemd[1]: Created slice system-modprobe.slice.
[    4.455572] random: systemd: uninitialized urandom read (16 bytes read)
[    4.462400] systemd[1]: Created slice system-serial\x2dgetty.slice.
[    4.481105] systemd[1]: Created slice User and Session Slice.
[    4.495902] systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
[    4.511737] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[    4.527898] systemd[1]: Reached target Paths.
[    4.539595] systemd[1]: Reached target Remote File Systems.
[    4.555577] systemd[1]: Reached target Slices.
[    4.567608] systemd[1]: Reached target Swap.
[    4.596721] systemd[1]: Listening on RPCbind Server Activation Socket.
[    4.611718] systemd[1]: Reached target RPC Port Mapper.
[    4.629034] systemd[1]: Listening on Syslog Socket.
[    4.643820] systemd[1]: Listening on initctl Compatibility Named Pipe.
[    4.663082] systemd[1]: Condition check resulted in Journal Audit Socket being skipped.
[    4.670474] systemd[1]: Listening on Journal Socket (/dev/log).
[    4.684090] systemd[1]: Listening on Journal Socket.
[    4.700209] systemd[1]: Listening on Network Service Netlink Socket.
[    4.716165] systemd[1]: Listening on udev Control Socket.
[    4.731913] systemd[1]: Listening on udev Kernel Socket.
[    4.747929] systemd[1]: Listening on User Database Manager Socket.
[    4.764128] systemd[1]: Condition check resulted in Huge Pages File System being skipped.
[    4.774825] systemd[1]: Mounting POSIX Message Queue File System...
[    4.795781] systemd[1]: Mounting Kernel Debug File System...
[    4.815684] systemd[1]: Mounting Kernel Trace File System...
[    4.840508] systemd[1]: Mounting Temporary Directory (/tmp)...
[    4.860851] systemd[1]: Starting Create list of static device nodes for the current kernel...
[    4.883833] systemd[1]: Starting Load Kernel Module configfs...
[    4.903837] systemd[1]: Starting Load Kernel Module drm...
[    4.923710] systemd[1]: Starting Load Kernel Module fuse...
[    4.944219] systemd[1]: Starting RPC Bind...
[    4.948607] fuse: init (API version 7.32)
[    4.963892] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
[    4.978368] systemd[1]: Starting Journal Service...
[    4.996456] scsi 0:0:0:0: Direct-Access     Generic- SD/MMC           1.00 PQ: 0 ANSI: 0 CCS
[    5.013764] systemd[1]: Starting Load Kernel Modules...
[    5.032304] systemd[1]: Starting Remount Root and Kernel File Systems...
[    5.052360] systemd[1]: Starting Coldplug All udev Devices...
[    5.068597] EXT4-fs (mmcblk0p2): re-mounted. Opts: (null)
[    5.082374] systemd[1]: Started RPC Bind.
[    5.100416] systemd[1]: Mounted POSIX Message Queue File System.
[    5.108164] openvswitch: Open vSwitch switching datapath
[    5.120249] systemd[1]: Started Journal Service.
[    5.360095] systemd-journald[144]: Received client request to flush runtime journal.
[    5.608032] sd 0:0:0:0: [sda] 30244864 512-byte logical blocks: (15.5 GB/14.4 GiB)
[    5.614598] sd 0:0:0:0: [sda] Write Protect is off
[    5.618113] sd 0:0:0:0: [sda] Mode Sense: 03 00 00 00
[    5.619472] sd 0:0:0:0: [sda] No Caching mode page found
[    5.623524] sd 0:0:0:0: [sda] Assuming drive cache: write through
[    5.658340]  sda: sda1
[    5.662450] sd 0:0:0:0: [sda] Attached SCSI removable disk
[    6.203113] FAT-fs (mmcblk0p1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.
[    6.763516] random: crng init done
[    6.765642] random: 7 urandom warning(s) missed due to ratelimiting
[    8.855512] socfpga-dwmac ff800000.ethernet eth0: PHY [stmmac-0:04] driver [Micrel KSZ9031 Gigabit PHY] (irq=POLL)
[    8.891470] socfpga-dwmac ff800000.ethernet eth0: No Safety Features support found
[    8.897854] socfpga-dwmac ff800000.ethernet eth0: IEEE 1588-2008 Advanced Timestamp supported
[    8.915821] socfpga-dwmac ff800000.ethernet eth0: registered PTP clock
[    8.932113] socfpga-dwmac ff800000.ethernet eth0: configuring for phy/rgmii link mode
[   11.013112] socfpga-dwmac ff800000.ethernet eth0: Link is Up - 100Mbps/Full - flow control rx/tx
[   11.020667] IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready


Failed to run NVIDIA's GPU on Intel Stratix10 Board with the following errors in kernel

wrsadmin@pek-lliu2-d1:~$ ssh root@128.224.162.185
The authenticity of host '128.224.162.185 (128.224.162.185)' can't be established.
ECDSA key fingerprint is SHA256:ijma70Q7obpZ+HQNV3q6K9d4oEeDQNzWFPgwtwcXuT0.
Are you sure you want to continue connecting (yes/no/[fingerprint])? YES
Warning: Permanently added '128.224.162.185' (ECDSA) to the list of known hosts.
root@intel-socfpga-64:~# dmesg
[    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
[    0.000000] Linux version 5.10.35-yocto-standard (oe-user@oe-host) (aarch64-wrs-linux-gcc (GCC) 10.2.0, GNU ld (GNU Binutils) 2.36.1.20210209) #1 SMP PREEMPT Wed May 12 08:49:49 UTC 2021
[    0.000000] Machine model: SoCFPGA Stratix 10 SoCDK
[    0.000000] earlycon: uart0 at MMIO32 0x00000000ffc02000 (options '115200n8')
[    0.000000] printk: bootconsole [uart0] enabled
[    0.000000] efi: UEFI not found.
[    0.000000] Reserved memory: created DMA memory pool at 0x0000000000000000, size 16 MiB
[    0.000000] OF: reserved mem: initialized node svcbuffer@0, compatible id shared-dma-pool
[    0.000000] cma: Reserved 16 MiB at 0x000000007e800000
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000000000-0x00000000ffffffff]
[    0.000000]   DMA32    empty
[    0.000000]   Normal   [mem 0x0000000100000000-0x00000001ffffffff]
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000000000-0x0000000000ffffff]
[    0.000000]   node   0: [mem 0x0000000001000000-0x000000007fffffff]
[    0.000000]   node   0: [mem 0x0000000180000000-0x00000001ffffffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000000000-0x00000001ffffffff]
[    0.000000] On node 0 totalpages: 1048576
[    0.000000]   DMA zone: 8192 pages used for memmap
[    0.000000]   DMA zone: 0 pages reserved
[    0.000000]   DMA zone: 524288 pages, LIFO batch:63
[    0.000000]   Normal zone: 8192 pages used for memmap
[    0.000000]   Normal zone: 524288 pages, LIFO batch:63
[    0.000000] psci: probing for conduit method from DT.
[    0.000000] psci: PSCIv65535.65535 detected in firmware.
[    0.000000] psci: Using standard PSCI v0.2 function IDs
[    0.000000] psci: MIGRATE_INFO_TYPE not supported.
[    0.000000] psci: SMC Calling Convention v1.0
[    0.000000] percpu: Embedded 30 pages/cpu s82008 r8192 d32680 u122880
[    0.000000] pcpu-alloc: s82008 r8192 d32680 u122880 alloc=30*4096
[    0.000000] pcpu-alloc: [0] 0 [0] 1 [0] 2 [0] 3 
[    0.000000] Detected VIPT I-cache on CPU0
[    0.000000] CPU features: detected: ARM erratum 845719
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 1032192
[    0.000000] Kernel command line: earlycon panic=-1 root=/dev/mmcblk0p2 rw rootwait
[    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
[    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
[    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
[    0.000000] software IO TLB: mapped [mem 0x000000007a800000-0x000000007e800000] (64MB)
[    0.000000] Memory: 3993020K/4194304K available (12416K kernel code, 1952K rwdata, 2936K rodata, 3968K init, 707K bss, 184900K reserved, 16384K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] ftrace: allocating 38327 entries in 150 pages
[    0.000000] ftrace: allocated 150 pages with 4 groups
[    0.000000] rcu: Preemptible hierarchical RCU implementation.
[    0.000000] rcu: 	RCU event tracing is enabled.
[    0.000000] 	Trampoline variant of Tasks RCU enabled.
[    0.000000] 	Rude variant of Tasks RCU enabled.
[    0.000000] 	Tracing variant of Tasks RCU enabled.
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
[    0.000000] GIC: Using split EOI/Deactivate mode
[    0.000000] random: get_random_bytes called from start_kernel+0x398/0x5a0 with crng_init=0
[    0.000000] arch_timer: cp15 timer(s) running at 400.00MHz (phys).
[    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x5c4093a7d1, max_idle_ns: 440795210635 ns
[    0.000005] sched_clock: 56 bits at 400MHz, resolution 2ns, wraps every 4398046511103ns
[    0.006872] Console: colour dummy device 80x25
[    0.010001] printk: console [tty0] enabled
[    0.012794] printk: bootconsole [uart0] disabled
[    0.016122] Calibrating delay loop (skipped), value calculated using timer frequency.. 800.00 BogoMIPS (lpj=1600000)
[    0.016147] pid_max: default: 32768 minimum: 301
[    0.016258] LSM: Security Framework initializing
[    0.016436] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.016471] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.018393] rcu: Hierarchical SRCU implementation.
[    0.018929] EFI services will not be available.
[    0.019172] smp: Bringing up secondary CPUs ...
[    0.019710] Detected VIPT I-cache on CPU1
[    0.019774] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
[    0.020383] Detected VIPT I-cache on CPU2
[    0.020416] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
[    0.021030] Detected VIPT I-cache on CPU3
[    0.021062] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
[    0.021166] smp: Brought up 1 node, 4 CPUs
[    0.021209] SMP: Total of 4 processors activated.
[    0.021221] CPU features: detected: 32-bit EL0 Support
[    0.021233] CPU features: detected: CRC32 instructions
[    0.021293] CPU: All CPU(s) started at EL2
[    0.021322] alternatives: patching kernel code
[    0.022074] devtmpfs: initialized
[    0.025876] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.025911] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
[    0.027046] DMI not present or invalid.
[    0.027512] NET: Registered protocol family 16
[    0.029212] DMA: preallocated 512 KiB GFP_KERNEL pool for atomic allocations
[    0.029400] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
[    0.029749] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
[    0.030423] cpuidle: using governor ladder
[    0.030516] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
[    0.030621] ASID allocator initialised with 65536 entries
[    0.117033] raid6: neonx8   gen()  1742 MB/s
[    0.185127] raid6: neonx8   xor()  1287 MB/s
[    0.253243] raid6: neonx4   gen()  1784 MB/s
[    0.321343] raid6: neonx4   xor()  1263 MB/s
[    0.389456] raid6: neonx2   gen()  1683 MB/s
[    0.457559] raid6: neonx2   xor()  1163 MB/s
[    0.525676] raid6: neonx1   gen()  1446 MB/s
[    0.593775] raid6: neonx1   xor()   990 MB/s
[    0.661878] raid6: int64x8  gen()  1198 MB/s
[    0.729979] raid6: int64x8  xor()   642 MB/s
[    0.798095] raid6: int64x4  gen()  1335 MB/s
[    0.866223] raid6: int64x4  xor()   681 MB/s
[    0.934294] raid6: int64x2  gen()  1165 MB/s
[    1.002394] raid6: int64x2  xor()   625 MB/s
[    1.070518] raid6: int64x1  gen()   863 MB/s
[    1.138611] raid6: int64x1  xor()   431 MB/s
[    1.138623] raid6: using algorithm neonx4 gen() 1784 MB/s
[    1.138634] raid6: .... xor() 1263 MB/s, rmw enabled
[    1.138646] raid6: using neon recovery algorithm
[    1.139641] iommu: Default domain type: Translated 
[    1.139830] vgaarb: loaded
[    1.140069] SCSI subsystem initialized
[    1.140308] usbcore: registered new interface driver usbfs
[    1.140359] usbcore: registered new interface driver hub
[    1.140405] usbcore: registered new device driver usb
[    1.140553] usb_phy_generic soc:usbphy@0: supply vcc not found, using dummy regulator
[    1.141035] pps_core: LinuxPPS API ver. 1 registered
[    1.141049] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    1.141077] PTP clock support registered
[    1.141273] EDAC MC: Ver: 3.0.0
[    1.142344] Intel Service Layer Driver Initialized
[    1.142492] FPGA manager framework
[    1.143552] clocksource: Switched to clocksource arch_sys_counter
[    1.899598] NET: Registered protocol family 2
[    1.900463] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes, linear)
[    1.900534] TCP established hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    1.900793] TCP bind hash table entries: 32768 (order: 7, 524288 bytes, linear)
[    1.901285] TCP: Hash tables configured (established 32768 bind 32768)
[    1.901424] UDP hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    1.901525] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    1.901780] NET: Registered protocol family 1
[    1.902256] RPC: Registered named UNIX socket transport module.
[    1.902271] RPC: Registered udp transport module.
[    1.902281] RPC: Registered tcp transport module.
[    1.902292] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    1.902313] PCI: CLS 0 bytes, default 64
[    1.903333] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
[    1.904847] workingset: timestamp_bits=46 max_order=20 bucket_order=0
[    1.912190] NFS: Registering the id_resolver key type
[    1.912237] Key type id_resolver registered
[    1.912249] Key type id_legacy registered
[    1.912929] Key type cifs.idmap registered
[    1.955777] xor: measuring software checksum speed
[    1.960802]    8regs           :  1968 MB/sec
[    1.965042]    32regs          :  2331 MB/sec
[    1.970758]    arm64_neon      :  1726 MB/sec
[    1.970770] xor: using function: 32regs (2331 MB/sec)
[    1.970787] async_tx: api initialized (async)
[    1.970832] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 248)
[    1.970849] io scheduler mq-deadline registered
[    1.970861] io scheduler kyber registered
[    1.971444] gpio-dwapb ffc03300.gpio: Cannot get reset descriptor
[    1.971907] altera-pcie a0000000.pcie: host bridge /soc/bridge@80000000/pcie@200000000 ranges:
[    1.971970] altera-pcie a0000000.pcie:      MEM 0x0090000000..0x0097ffffff -> 0x0000000000
[    1.972220] altera-pcie a0000000.pcie: PCI host bridge to bus 0000:00
[    1.972242] pci_bus 0000:00: root bus resource [bus 00-ff]
[    1.972259] pci_bus 0000:00: root bus resource [mem 0x90000000-0x97ffffff] (bus address [0x00000000-0x07ffffff])
[    1.972335] pci 0000:00:00.0: [1172:e000] type 01 class 0x060400
[    1.972410] pci 0000:00:00.0: enabling Extended Tags
[    1.973671] pci 0000:00:00.0: bridge configuration invalid ([bus 00-00]), reconfiguring
[    1.974083] pci 0000:01:00.0: [10de:2187] type 00 class 0x030000
[    1.974229] pci 0000:01:00.0: reg 0x10: [mem 0x90000000-0x90ffffff]
[    1.974348] pci 0000:01:00.0: reg 0x14: [mem 0x00000000-0x0fffffff 64bit pref]
[    1.974467] pci 0000:01:00.0: reg 0x1c: [mem 0x90000000-0x91ffffff 64bit pref]
[    1.974541] pci 0000:01:00.0: reg 0x24: [io  0x0000-0x007f]
[    1.974612] pci 0000:01:00.0: reg 0x30: [mem 0x90000000-0x9007ffff pref]
[    1.975398] pci 0000:01:00.0: PME# supported from D0 D3hot D3cold
[    1.975946] pci 0000:01:00.0: 63.008 Gb/s available PCIe bandwidth, limited by 8.0 GT/s PCIe x8 link at 0000:00:00.0 (capable of 126.016 Gb/s with 8.0 GT/s PCIe x16 link)
[    1.976116] pci 0000:01:00.0: vgaarb: VGA device added: decodes=io+mem,owns=none,locks=none
[    1.976328] pci 0000:01:00.1: [10de:1aeb] type 00 class 0x040300
[    1.976471] pci 0000:01:00.1: reg 0x10: [mem 0x90000000-0x90003fff]
[    1.977810] pci 0000:01:00.2: [10de:1aec] type 00 class 0x0c0330
[    1.977999] pci 0000:01:00.2: reg 0x10: [mem 0x90000000-0x9003ffff 64bit pref]
[    1.978176] pci 0000:01:00.2: reg 0x1c: [mem 0x90000000-0x9000ffff 64bit pref]
[    1.978825] pci 0000:01:00.2: PME# supported from D0 D3hot D3cold
[    1.979344] pci 0000:01:00.3: [10de:1aed] type 00 class 0x0c8000
[    1.979488] pci 0000:01:00.3: reg 0x10: [mem 0x90000000-0x90000fff]
[    1.980395] pci 0000:01:00.3: PME# supported from D0 D3hot D3cold
[    1.981854] pci_bus 0000:01: busn_res: [bus 01-ff] end is updated to 01
[    1.981904] pci 0000:00:00.0: BAR 15: no space for [mem size 0x18000000 64bit pref]
[    1.981922] pci 0000:00:00.0: BAR 15: failed to assign [mem size 0x18000000 64bit pref]
[    1.981940] pci 0000:00:00.0: BAR 14: assigned [mem 0x90000000-0x917fffff]
[    1.981956] pci 0000:00:00.0: BAR 13: no space for [io  size 0x1000]
[    1.981970] pci 0000:00:00.0: BAR 13: failed to assign [io  size 0x1000]
[    1.981995] pci 0000:01:00.0: BAR 1: no space for [mem size 0x10000000 64bit pref]
[    1.982011] pci 0000:01:00.0: BAR 1: failed to assign [mem size 0x10000000 64bit pref]
[    1.982030] pci 0000:01:00.0: BAR 3: no space for [mem size 0x02000000 64bit pref]
[    1.982046] pci 0000:01:00.0: BAR 3: failed to assign [mem size 0x02000000 64bit pref]
[    1.982063] pci 0000:01:00.0: BAR 0: assigned [mem 0x90000000-0x90ffffff]
[    1.982105] pci 0000:01:00.0: BAR 6: assigned [mem 0x91000000-0x9107ffff pref]
[    1.982124] pci 0000:01:00.2: BAR 0: assigned [mem 0x91080000-0x910bffff 64bit pref]
[    1.982223] pci 0000:01:00.2: BAR 3: assigned [mem 0x910c0000-0x910cffff 64bit pref]
[    1.982320] pci 0000:01:00.1: BAR 0: assigned [mem 0x910d0000-0x910d3fff]
[    1.982360] pci 0000:01:00.3: BAR 0: assigned [mem 0x910d4000-0x910d4fff]
[    1.982398] pci 0000:01:00.0: BAR 5: no space for [io  size 0x0080]
[    1.982413] pci 0000:01:00.0: BAR 5: failed to assign [io  size 0x0080]
[    1.982431] pci 0000:00:00.0: PCI bridge to [bus 01]
[    1.982451] pci 0000:00:00.0:   bridge window [mem 0x90000000-0x917fffff]
[    1.982580] pcieport 0000:00:00.0: enabling device (0000 -> 0002)
[    1.982829] pcieport 0000:00:00.0: PME: Signaling with IRQ 42
[    1.983333] pci 0000:01:00.1: D0 power state depends on 0000:01:00.0
[    1.983878] pci 0000:01:00.2: D0 power state depends on 0000:01:00.0
[    1.984287] pci 0000:01:00.2: enabling device (0000 -> 0002)
[    1.984536] pci 0000:01:00.3: D0 power state depends on 0000:01:00.0
[    1.985904] Serial: 8250/16550 driver, 4 ports, IRQ sharing enabled
[    1.987278] ffc02000.serial: ttyS0 at MMIO 0xffc02000 (irq = 33, base_baud = 6250000) is a 16550A
[    2.908995] printk: console [ttyS0] enabled
[    2.912999] cacheinfo: Unable to detect cache hierarchy for CPU 0
[    2.925292] brd: module loaded
[    2.935715] loop: module loaded
[    2.951673] spi-nor spi0.0: mt25qu02g (262144 Kbytes)
[    2.955453] 2 fixed-partitions partitions found on MTD device ff8d2000.spi.0
[    2.961192] Creating 2 MTD partitions on "ff8d2000.spi.0":
[    2.965375] 0x000000910000-0x000100010000 : "Boot and fpga data"
[    2.970075] mtd: partition "Boot and fpga data" extends beyond the end of device "ff8d2000.spi.0" -- size truncated to 0xf6f0000
[    2.984498] 0x000003fe0000-0x000010000000 : "Root Filesystem - JFFS2"
[    2.997390] libphy: Fixed MDIO Bus: probed
[    3.000649] socfpga-dwmac ff800000.ethernet: IRQ eth_wake_irq not found
[    3.005958] socfpga-dwmac ff800000.ethernet: IRQ eth_lpi not found
[    3.011217] socfpga-dwmac ff800000.ethernet: User ID: 0x11, Synopsys ID: 0x37
[    3.017049] socfpga-dwmac ff800000.ethernet: 	DWMAC1000
[    3.020971] socfpga-dwmac ff800000.ethernet: DMA HW capability register supported
[    3.027138] socfpga-dwmac ff800000.ethernet: RX Checksum Offload Engine supported
[    3.033305] socfpga-dwmac ff800000.ethernet: COE Type 2
[    3.037224] socfpga-dwmac ff800000.ethernet: TX Checksum insertion supported
[    3.042959] socfpga-dwmac ff800000.ethernet: Enhanced/Alternate descriptors
[    3.048606] socfpga-dwmac ff800000.ethernet: Enabled extended descriptors
[    3.054081] socfpga-dwmac ff800000.ethernet: Ring mode enabled
[    3.058612] socfpga-dwmac ff800000.ethernet: Enable RX Mitigation via HW Watchdog Timer
[    3.065308] socfpga-dwmac ff800000.ethernet: device MAC address 4a:31:78:3b:87:a2
[    3.071960] libphy: stmmac: probed
[    3.076970] dwc2 ffb00000.usb: supply vusb_d not found, using dummy regulator
[    3.082928] dwc2 ffb00000.usb: supply vusb_a not found, using dummy regulator
[    3.089047] dwc2 ffb00000.usb: EPs: 16, dedicated fifos, 8064 entries in SPRAM
[    3.095246] dwc2 ffb00000.usb: DWC OTG Controller
[    3.098698] dwc2 ffb00000.usb: new USB bus registered, assigned bus number 1
[    3.104465] dwc2 ffb00000.usb: irq 34, io mem 0xffb00000
[    3.109144] hub 1-0:1.0: USB hub found
[    3.111625] hub 1-0:1.0: 1 port detected
[    3.115664] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    3.120915] ehci-pci: EHCI PCI platform driver
[    3.124098] ehci-platform: EHCI generic platform driver
[    3.128789] xhci_hcd 0000:01:00.2: enabling device (0000 -> 0002)
[    3.133683] xhci_hcd 0000:01:00.2: xHCI Host Controller
[    3.137616] xhci_hcd 0000:01:00.2: new USB bus registered, assigned bus number 2
[    3.144390] xhci_hcd 0000:01:00.2: hcc params 0x0180ff05 hci version 0x110 quirks 0x0000000000000010
[    3.153379] hub 2-0:1.0: USB hub found
[    3.155866] hub 2-0:1.0: 2 ports detected
[    3.159042] xhci_hcd 0000:01:00.2: xHCI Host Controller
[    3.162974] xhci_hcd 0000:01:00.2: new USB bus registered, assigned bus number 3
[    3.169064] xhci_hcd 0000:01:00.2: Host supports USB 3.1 Enhanced SuperSpeed
[    3.174878] usb usb3: We don't know the algorithms for LPM for this host, disabling LPM.
[    3.182122] hub 3-0:1.0: USB hub found
[    3.184613] hub 3-0:1.0: 4 ports detected
[    3.188189] usbcore: registered new interface driver usb-storage
[    3.193822] i2c /dev entries driver
[    3.197214] device-mapper: ioctl: 4.43.0-ioctl (2020-10-01) initialised: dm-devel@redhat.com
[    3.205188] EDAC DEVICE0: Giving out device to module sdramedac controller Altera ECC Manager: DEV sdramedac (INTERRUPT)
[    3.215070] sdhci: Secure Digital Host Controller Interface driver
[    3.220058] sdhci: Copyright(c) Pierre Ossman
[    3.223104] Synopsys Designware Multimedia Card Interface Driver
[    3.228048] dw_mmc ff808000.dwmmc0: IDMAC supports 32-bit address mode.
[    3.231588] sdhci-pltfm: SDHCI platform and OF driver helper
[    3.233370] dw_mmc ff808000.dwmmc0: Using internal DMA controller.
[    3.241387] usbcore: registered new interface driver usbhid
[    3.242564] dw_mmc ff808000.dwmmc0: Version ID is 280a
[    3.246816] usbhid: USB HID core driver
[    3.250679] dw_mmc ff808000.dwmmc0: DW MMC controller at irq 19,32 bit host data width,1024 deep fifo
[    3.253470] fpga_manager fpga0: Stratix10 SOC FPGA Manager registered
[    3.261265] mmc_host mmc0: card is polling.
[    3.266322] u32 classifier
[    3.270485]     input device check on
[    3.272865]     Actions configured
[    3.275611] NET: Registered protocol family 10
[    3.279562] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 400000Hz, actual 396825HZ div = 63)
[    3.279658] Segment Routing with IPv6
[    3.290143] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
[    3.295285] NET: Registered protocol family 17
[    3.298485] Bridge firewalling registered
[    3.301376] Key type dns_resolver registered
[    3.304552] NET: Registered protocol family 40
[    3.308150] Key type ._fscrypt registered
[    3.310861] Key type .fscrypt registered
[    3.313506] Key type fscrypt-provisioning registered
[    3.318166] Btrfs loaded, crc32c=crc32c-generic
[    3.322372] Key type encrypted registered
[    3.328248] dma-pl330 ffda0000.pdma: Loaded driver for PL330 DMAC-341330
[    3.333688] dma-pl330 ffda0000.pdma: 	DBUFF-512x8bytes Num_Chans-8 Num_Peri-32 Num_Events-8
[    3.350531] at24 0-0051: supply vcc not found, using dummy regulator
[    3.356407] at24 0-0051: 4096 byte 24c32 EEPROM, writable, 32 bytes/write
[    3.363273] rtc-ds1307 0-0068: SET TIME!
[    3.368105] rtc-ds1307 0-0068: registered as rtc0
[    3.372506] rtc-ds1307 0-0068: setting system clock to 2000-01-01T00:00:14 UTC (946684814)
[    3.379827] of-fpga-region soc:base_fpga_region: FPGA Region probed
[    3.384813] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
[    3.393270] printk: console [netcon0] enabled
[    3.393299] mmc0: new high speed SDXC card at address 0001
[    3.396340] netconsole: network logging started
[    3.403838] of_cfs_init
[    3.404290] mmcblk0: mmc0:0001 SD64G 58.2 GiB 
[    3.405078] of_cfs_init: OK
[    3.410093] dw-apb-uart ffc02000.serial: forbid DMA for kernel console
[    3.415418]  mmcblk0: p1 p2
[    3.418059] md: Waiting for all devices to be available before autodetect
[    3.423585] md: If you don't use raid, use raid=noautodetect
[    3.427944] md: Autodetecting RAID arrays.
[    3.430730] md: autorun ...
[    3.432247] md: ... autorun DONE.
[    3.454536] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
[    3.461384] VFS: Mounted root (ext4 filesystem) on device 179:2.
[    3.467044] devtmpfs: mounted
[    3.473123] Freeing unused kernel memory: 3968K
[    3.476487] Run /sbin/init as init process
[    3.479274]   with arguments:
[    3.479278]     /sbin/init
[    3.479282]   with environment:
[    3.479286]     HOME=/
[    3.479290]     TERM=linux
[    3.572316] random: fast init done
[    3.861978] systemd[1]: System time before build time, advancing clock.
[    3.926619] systemd[1]: systemd 247.4+ running in system mode. (+PAM -AUDIT -SELINUX +IMA -APPARMOR -SMACK +SYSVINIT +UTMP -LIBCRYPTSETUP -GCRYPT -GNUTLS +ACL +XZ -LZ4 -ZSTD -SECCOMP +BLKID -ELFUTILS +KMOD -IDN2 -IDN -PCRE2 default-hierarchy=hybrid)
[    3.947934] systemd[1]: Detected architecture arm64.
[    3.959585] usb 1-1: new high-speed USB device number 2 using dwc2
[    3.996381] systemd[1]: Set hostname to <intel-socfpga-64>.
[    4.184593] usb-storage 1-1:1.0: USB Mass Storage device detected
[    4.189941] scsi host0: usb-storage 1-1:1.0
[    4.478021] systemd[1]: Queued start job for default target Graphical Interface.
[    4.485506] random: systemd: uninitialized urandom read (16 bytes read)
[    4.525003] systemd[1]: Created slice system-getty.slice.
[    4.539876] random: systemd: uninitialized urandom read (16 bytes read)
[    4.546813] systemd[1]: Created slice system-modprobe.slice.
[    4.559663] random: systemd: uninitialized urandom read (16 bytes read)
[    4.566462] systemd[1]: Created slice system-serial\x2dgetty.slice.
[    4.585197] systemd[1]: Created slice User and Session Slice.
[    4.600004] systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
[    4.615839] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[    4.631998] systemd[1]: Reached target Paths.
[    4.643740] systemd[1]: Reached target Remote File Systems.
[    4.659689] systemd[1]: Reached target Slices.
[    4.671690] systemd[1]: Reached target Swap.
[    4.701047] systemd[1]: Listening on RPCbind Server Activation Socket.
[    4.715860] systemd[1]: Reached target RPC Port Mapper.
[    4.733150] systemd[1]: Listening on Syslog Socket.
[    4.747913] systemd[1]: Listening on initctl Compatibility Named Pipe.
[    4.767185] systemd[1]: Condition check resulted in Journal Audit Socket being skipped.
[    4.774578] systemd[1]: Listening on Journal Socket (/dev/log).
[    4.788195] systemd[1]: Listening on Journal Socket.
[    4.804382] systemd[1]: Listening on Network Service Netlink Socket.
[    4.820296] systemd[1]: Listening on udev Control Socket.
[    4.836012] systemd[1]: Listening on udev Kernel Socket.
[    4.852024] systemd[1]: Listening on User Database Manager Socket.
[    4.868214] systemd[1]: Condition check resulted in Huge Pages File System being skipped.
[    4.878908] systemd[1]: Mounting POSIX Message Queue File System...
[    4.899914] systemd[1]: Mounting Kernel Debug File System...
[    4.919806] systemd[1]: Mounting Kernel Trace File System...
[    4.940638] systemd[1]: Mounting Temporary Directory (/tmp)...
[    4.960984] systemd[1]: Starting Create list of static device nodes for the current kernel...
[    4.987944] systemd[1]: Starting Load Kernel Module configfs...
[    5.007901] systemd[1]: Starting Load Kernel Module drm...
[    5.027845] systemd[1]: Starting Load Kernel Module fuse...
[    5.047184] fuse: init (API version 7.32)
[    5.048478] systemd[1]: Starting RPC Bind...
[    5.063901] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
[    5.078458] systemd[1]: Starting Journal Service...
[    5.110019] systemd[1]: Starting Load Kernel Modules...
[    5.124365] systemd[1]: Starting Remount Root and Kernel File Systems...
[    5.153280] systemd[1]: Starting Coldplug All udev Devices...
[    5.161088] EXT4-fs (mmcblk0p2): re-mounted. Opts: (null)
[    5.188757] systemd[1]: Started RPC Bind.
[    5.189448] openvswitch: Open vSwitch switching datapath
[    5.212715] systemd[1]: Mounted POSIX Message Queue File System.
[    5.220475] scsi 0:0:0:0: Direct-Access     Generic- SD/MMC           1.00 PQ: 0 ANSI: 0 CCS
[    5.232547] systemd[1]: Mounted Kernel Debug File System.
[    5.252636] systemd[1]: Started Journal Service.
[    5.483331] systemd-journald[146]: Received client request to flush runtime journal.
[    5.841456] sd 0:0:0:0: [sda] 30244864 512-byte logical blocks: (15.5 GB/14.4 GiB)
[    5.850469] sd 0:0:0:0: [sda] Write Protect is off
[    5.854040] sd 0:0:0:0: [sda] Mode Sense: 03 00 00 00
[    5.855507] sd 0:0:0:0: [sda] No Caching mode page found
[    5.859630] sd 0:0:0:0: [sda] Assuming drive cache: write through
[    5.906417]  sda: sda1
[    5.924027] sd 0:0:0:0: [sda] Attached SCSI removable disk
[    6.134331] nvidia_drm: loading out-of-tree module taints kernel.
[    6.141323] nvidia_drm: module license 'MIT' taints kernel.
[    6.148776] Disabling lock debugging due to kernel taint
[    7.891598] random: crng init done
[    7.893727] random: 7 urandom warning(s) missed due to ratelimiting
[    8.378131] FAT-fs (mmcblk0p1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.
[    8.550579] nvidia-nvlink: Nvlink Core is being initialized, major device number 245

[    8.562145] nvidia 0000:01:00.0: enabling device (0000 -> 0002)
[    8.567141] nvidia 0000:01:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=none:owns=none
[    8.620038] NVRM: loading NVIDIA UNIX aarch64 Kernel Module  465.31  Thu May 13 22:39:49 UTC 2021
[   11.091596] socfpga-dwmac ff800000.ethernet eth0: PHY [stmmac-0:04] driver [Micrel KSZ9031 Gigabit PHY] (irq=POLL)
[   11.119585] socfpga-dwmac ff800000.ethernet eth0: No Safety Features support found
[   11.125876] socfpga-dwmac ff800000.ethernet eth0: IEEE 1588-2008 Advanced Timestamp supported
[   11.147946] socfpga-dwmac ff800000.ethernet eth0: registered PTP clock
[   11.164934] socfpga-dwmac ff800000.ethernet eth0: configuring for phy/rgmii link mode
[   11.751189] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   11.767734] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   11.827296] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   11.843744] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   17.052200] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   17.058022] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   17.073149] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   17.078966] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   18.377166] socfpga-dwmac ff800000.ethernet eth0: Link is Up - 100Mbps/Full - flow control rx/tx
[   18.384695] IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
[   22.575147] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   22.580981] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   22.595913] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   22.601734] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   28.088060] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   28.093883] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   28.108765] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   28.114590] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   33.600859] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   33.606734] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   33.621572] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   33.627396] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   39.113858] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   39.119698] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   39.134759] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   39.140703] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   44.533827] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   44.539818] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   44.554490] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   44.560322] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   50.033771] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   50.039798] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   50.054480] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   50.060336] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   55.535407] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   55.541291] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   55.556401] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   55.562218] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   61.036573] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   61.042428] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   61.057614] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   61.063492] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   66.533860] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   66.540107] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   66.554964] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   66.560798] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   72.034047] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   72.039891] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   72.055097] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   72.060955] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   77.534047] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   77.539922] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   77.554772] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   77.560610] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   83.034396] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   83.040254] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   83.055261] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   83.061097] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   88.533365] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   88.539211] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   88.554156] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   88.560005] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   94.035385] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   94.041238] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   94.056338] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   94.062159] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
root@intel-socfpga-64:~# 

root@intel-socfpga-64:/NVIDIA-Linux-aarch64-465.31# grep -r "RmInitAdapter" ./
./html/commonproblems.html:NVRM: RmInitAdapter failed! (0x30:0xffffffff:858)
./README.txt:   NVRM: RmInitAdapter failed! (0x30:0xffffffff:858)
grep: ./kernel/nvidia/nv-kernel.o_binary: binary file matches
root@intel-socfpga-64:/NVIDIA-Linux-aarch64-465.31#

```

```
 1.971752] gpio-dwapb ffc03300.gpio: Cannot get reset descriptor
[    1.972187] altera-pcie a0000000.pcie: host bridge /soc/bridge@80000000/pcie@200000000 ranges:
[    1.972251] altera-pcie a0000000.pcie:      MEM 0x00b0000000..0x00efffffff -> 0x0000000000
[    1.972284] altera-pcie a0000000.pcie: invalid resource
[    1.972298] altera-pcie a0000000.pcie: Parsing DT failed
[    1.972324] altera-pcie: probe of a0000000.pcie failed with error -22
[    1.973249] Serial: 8250/16550 driver, 4 ports, IRQ sharing enabled
[    1.974559] ffc02000.serial: ttyS0 at MMIO 0xffc02000 (irq = 33, base_baud = 6250000) is a 16550A
[    2.631227] printk: console [ttyS0] enabled
[    2.635205] cacheinfo: Unable to detect cache hierarchy for CPU 0
[    2.647487] brd: module loaded
[    2.657900] loop: module loaded
[    2.675628] spi-nor spi0.0: mt25qu02g (262144 Kbytes)
```

```
u-boot:
#ifdef CONFIG_PCIE1
#define CONFIG_SYS_PCIE1_MEM_VIRT       0x80000000
#define CONFIG_SYS_PCIE1_MEM_BUS        0xe0000000
#define CONFIG_SYS_PCIE1_MEM_PHYS       0xc00000000ull
#define CONFIG_SYS_PCIE1_MEM_SIZE       0x10000000      /* 256M */
#define CONFIG_SYS_PCIE1_IO_VIRT        0xf8000000
#define CONFIG_SYS_PCIE1_IO_BUS         0x00000000
#define CONFIG_SYS_PCIE1_IO_PHYS        0xff8000000ull
#define CONFIG_SYS_PCIE1_IO_SIZE        0x00010000      /* 64k */
#endif
In dts:
       pci0: pcie@ffe240000 {
                reg = <0xf 0xfe240000 0 0x10000>;
                ranges = <0x02000000 0 0xe0000000 0xc 0x0 0x0 0x10000000
                          0x01000000 0 0x0 0xf 0xf8000000 0x0 0x00010000>;
                pcie@0 {
                        ranges = <0x02000000 0 0xe0000000
                                  0x02000000 0 0xe0000000
                                  0 0x10000000

                                  0x01000000 0 0x00000000
                                  0x01000000 0 0x00000000
                                  0 0x00010000>;
                };
        };
```
```
able 1.PCI Express Data ThroughputThe following table shows the theoretical link bandwidth of a PCI Express link for Gen1, Gen2, and Gen3 for 1,2, 4, 8, and 16 lanes excluding overhead. This table provides bandwidths for a single transmit (TX) or receive(RX) channel. The numbers double for duplex operation. The protocol specifies 2.5 giga-transfers per second(GT/s) for Gen1, 5.0 GT/s for Gen2, and 8.0 GT/s for Gen3. Gen1 and Gen2 use 8B/10B encoding whichintroduces a 20% overhead. Gen3 uses 128b/130b encoding which an overhead of 1.54%. The following tableshows the actual usable data bandwidth in gigabytes per second (GBps). The encoding and decoding overheadhas been removed.Link Width×1×2×4×8×16PCI Express Gen1 (2.5 Gbps)2481632PCI Express Gen2 (5.0 Gbps)48163264PCI Express Gen3 (8.0 Gbps)7.8715.7531.563Not available incurrent release
```

```
U-Boot SPL 2020.10-10892-gced41867be (Mar 05 2021 - 10:29:01 +0800)
Reset state: Cold
MPU         1000000 kHz
L3 main     400000 kHz
Main VCO    2000000 kHz
Per VCO     2000000 kHz
EOSC1       25000 kHz
HPS MMC     50000 kHz
UART        100000 kHz
DDR: 4096 MiB
SDRAM-ECC: Initialized success with 1105 ms
QSPI: Reference clock at 400000 kHz
WDT:   Started with servicing (30s timeout)
Trying to boot from MMC1


U-Boot 2020.10 (May 12 2021 - 10:09:46 +0000)socfpga_stratix10

CPU:   Intel FPGA SoCFPGA Platform (ARMv8 64bit Cortex-A53)
Model: SoCFPGA Stratix 10 SoCDK
DRAM:  4 GiB
WDT:   Started with servicing (30s timeout)
MMC:   dwmmc0@ff808000: 0
Loading Environment from MMC... OK
In:    serial0@ffc02000
Out:   serial0@ffc02000
Err:   serial0@ffc02000
Net:   
Warning: ethernet@ff800000 (eth0) using random MAC address - be:b7:9a:a2:58:74
eth0: ethernet@ff800000
Hit any key to stop autoboot:  0 
SOCFPGA_STRATIX10 # 
SOCFPGA_STRATIX10 # 
SOCFPGA_STRATIX10 # 
U-Boot SPL 2020.10-10892-gced41867be (Mar 05 2021 - 10:29:01 +0800)
Reset state: Cold
MPU         1000000 kHz
L3 main     400000 kHz
Main VCO    2000000 kHz
Per VCO     2000000 kHz
EOSC1       25000 kHz
HPS MMC     50000 kHz
UART        100000 kHz
DDR: 4096 MiB
SDRAM-ECC: Initialized success with 1105 ms
QSPI: Reference clock at 400000 kHz
WDT:   Started with servicing (30s timeout)
Trying to boot from MMC1


U-Boot 2020.10 (May 12 2021 - 10:09:46 +0000)socfpga_stratix10

CPU:   Intel FPGA SoCFPGA Platform (ARMv8 64bit Cortex-A53)
Model: SoCFPGA Stratix 10 SoCDK
DRAM:  4 GiB
WDT:   Started with servicing (30s timeout)
MMC:   dwmmc0@ff808000: 0
Loading Environment from MMC... OK
In:    serial0@ffc02000
Out:   serial0@ffc02000
Err:   serial0@ffc02000
Net:   
Warning: ethernet@ff800000 (eth0) using random MAC address - a6:6c:c9:86:4c:d5
eth0: ethernet@ff800000
Hit any key to stop autoboot:  0 
441 bytes read in 2 ms (214.8 KiB/s)
## Executing script at 02100000
6377472 bytes read in 296 ms (20.5 MiB/s)
.......FPGA reconfiguration OK!
21922304 bytes read in 986 ms (21.2 MiB/s)
18360 bytes read in 3 ms (5.8 MiB/s)
SF: Detected mt25qu02g with page size 256 Bytes, erase size 4 KiB, total 256 MiB
Enabling QSPI at Linux DTB...
RSU: Remote System Update Status
Current Image	: 0x01000000
Last Fail Image	: 0x00000000
State		: 0x00000000
Version		: 0x00000202
Error location	: 0x00000000
Error details	: 0x00000000
Retry counter	: 0x00000000
RSU: Sub-partition table 0 offset 0x00910000
RSU: Sub-partition table 1 offset 0x00918000
RSU: Sub-partition table content
       BOOT_INFO	Offset: 0x0000000000000000	Length: 0x00110000	Flag : 0x00000003
   FACTORY_IMAGE	Offset: 0x0000000000110000	Length: 0x00800000	Flag : 0x00000003
              P1	Offset: 0x0000000001000000	Length: 0x01000000	Flag : 0x00000000
            SPT0	Offset: 0x0000000000910000	Length: 0x00008000	Flag : 0x00000001
            SPT1	Offset: 0x0000000000918000	Length: 0x00008000	Flag : 0x00000001
            CPB0	Offset: 0x0000000000920000	Length: 0x00008000	Flag : 0x00000001
            CPB1	Offset: 0x0000000000928000	Length: 0x00008000	Flag : 0x00000001
              P2	Offset: 0x0000000002000000	Length: 0x01000000	Flag : 0x00000000
              P3	Offset: 0x0000000003000000	Length: 0x01000000	Flag : 0x00000000
RSU: CMF pointer block offset 0x00920000
RSU: CMF pointer block's image pointer list
Priority 1 Offset: 0x0000000001000000 nslot: 0
DTB: qspi_boot node at /soc/spi@ff8d2000/flash@0/partitions/partition@0
SPTs are GOOD!!!
CPBs are GOOD!!!
DCMF0 version = 20.4.0
DCMF1 version = 20.4.0
DCMF2 version = 20.4.0
DCMF3 version = 20.4.0
DCMF0: OK
DCMF1: OK
DCMF2: OK
DCMF3: OK
max_retry = 1
## Flattened Device Tree blob at 08000000
   Booting using the fdt blob at 0x8000000
   Loading Device Tree to 000000007fa33000, end 000000007fa3afff ... OK

Starting kernel ...

Deasserting all peripheral resets
Booting Linux on physical CPU 0x0000000000 [0x410fd034]
Linux version 5.10.35-yocto-standard (oe-user@oe-host) (aarch64-wrs-linux-gcc (GCC) 10.2.0, GNU ld (GNU Binutils) 2.36.1.20210209) #1 SMP PREEMPT Fri May 28 11:43:11 UTC 2021
Machine model: SoCFPGA Stratix 10 SoCDK
earlycon: uart0 at MMIO32 0x00000000ffc02000 (options '115200n8')
printk: bootconsole [uart0] enabled
efi: UEFI not found.
Reserved memory: created DMA memory pool at 0x0000000000000000, size 16 MiB
OF: reserved mem: initialized node svcbuffer@0, compatible id shared-dma-pool
cma: Reserved 16 MiB at 0x000000007e800000
Zone ranges:
  DMA      [mem 0x0000000000000000-0x00000000ffffffff]
  DMA32    empty
  Normal   [mem 0x0000000100000000-0x00000001ffffffff]
Movable zone start for each node
Early memory node ranges
  node   0: [mem 0x0000000000000000-0x0000000000ffffff]
  node   0: [mem 0x0000000001000000-0x000000007fffffff]
  node   0: [mem 0x0000000180000000-0x00000001ffffffff]
Initmem setup node 0 [mem 0x0000000000000000-0x00000001ffffffff]
psci: probing for conduit method from DT.
psci: PSCIv65535.65535 detected in firmware.
psci: Using standard PSCI v0.2 function IDs
psci: MIGRATE_INFO_TYPE not supported.
psci: SMC Calling Convention v1.0
percpu: Embedded 30 pages/cpu s82008 r8192 d32680 u122880
Detected VIPT I-cache on CPU0
CPU features: detected: ARM erratum 845719
Built 1 zonelists, mobility grouping on.  Total pages: 1032192
Kernel command line: earlycon panic=-1 root=/dev/mmcblk0p2 rw rootwait
Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
mem auto-init: stack:off, heap alloc:off, heap free:off
software IO TLB: mapped [mem 0x000000007a800000-0x000000007e800000] (64MB)
Memory: 3993020K/4194304K available (12416K kernel code, 1952K rwdata, 2936K rodata, 3968K init, 707K bss, 184900K reserved, 16384K cma-reserved)
SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
ftrace: allocating 38327 entries in 150 pages
ftrace: allocated 150 pages with 4 groups
rcu: Preemptible hierarchical RCU implementation.
rcu: 	RCU event tracing is enabled.
	Trampoline variant of Tasks RCU enabled.
	Rude variant of Tasks RCU enabled.
	Tracing variant of Tasks RCU enabled.
rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
GIC: Using split EOI/Deactivate mode
random: get_random_bytes called from start_kernel+0x398/0x5a0 with crng_init=0
arch_timer: cp15 timer(s) running at 400.00MHz (phys).
clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x5c4093a7d1, max_idle_ns: 440795210635 ns
sched_clock: 56 bits at 400MHz, resolution 2ns, wraps every 4398046511103ns
Console: colour dummy device 80x25
printk: console [tty0] enabled
printk: bootconsole [uart0] disabled
Booting Linux on physical CPU 0x0000000000 [0x410fd034]
Linux version 5.10.35-yocto-standard (oe-user@oe-host) (aarch64-wrs-linux-gcc (GCC) 10.2.0, GNU ld (GNU Binutils) 2.36.1.20210209) #1 SMP PREEMPT Fri May 28 11:43:11 UTC 2021
Machine model: SoCFPGA Stratix 10 SoCDK
earlycon: uart0 at MMIO32 0x00000000ffc02000 (options '115200n8')
printk: bootconsole [uart0] enabled
efi: UEFI not found.
Reserved memory: created DMA memory pool at 0x0000000000000000, size 16 MiB
OF: reserved mem: initialized node svcbuffer@0, compatible id shared-dma-pool
cma: Reserved 16 MiB at 0x000000007e800000
Zone ranges:
  DMA      [mem 0x0000000000000000-0x00000000ffffffff]
  DMA32    empty
  Normal   [mem 0x0000000100000000-0x00000001ffffffff]
Movable zone start for each node
Early memory node ranges
  node   0: [mem 0x0000000000000000-0x0000000000ffffff]
  node   0: [mem 0x0000000001000000-0x000000007fffffff]
  node   0: [mem 0x0000000180000000-0x00000001ffffffff]
Initmem setup node 0 [mem 0x0000000000000000-0x00000001ffffffff]
psci: probing for conduit method from DT.
psci: PSCIv65535.65535 detected in firmware.
psci: Using standard PSCI v0.2 function IDs
psci: MIGRATE_INFO_TYPE not supported.
psci: SMC Calling Convention v1.0
percpu: Embedded 30 pages/cpu s82008 r8192 d32680 u122880
Detected VIPT I-cache on CPU0
CPU features: detected: ARM erratum 845719
Built 1 zonelists, mobility grouping on.  Total pages: 1032192
Kernel command line: earlycon panic=-1 root=/dev/mmcblk0p2 rw rootwait
Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
mem auto-init: stack:off, heap alloc:off, heap free:off
software IO TLB: mapped [mem 0x000000007a800000-0x000000007e800000] (64MB)
Memory: 3993020K/4194304K available (12416K kernel code, 1952K rwdata, 2936K rodata, 3968K init, 707K bss, 184900K reserved, 16384K cma-reserved)
SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
ftrace: allocating 38327 entries in 150 pages
ftrace: allocated 150 pages with 4 groups
rcu: Preemptible hierarchical RCU implementation.
rcu: 	RCU event tracing is enabled.
	Trampoline variant of Tasks RCU enabled.
	Rude variant of Tasks RCU enabled.
	Tracing variant of Tasks RCU enabled.
rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
GIC: Using split EOI/Deactivate mode
random: get_random_bytes called from start_kernel+0x398/0x5a0 with crng_init=0
arch_timer: cp15 timer(s) running at 400.00MHz (phys).
clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x5c4093a7d1, max_idle_ns: 440795210635 ns
sched_clock: 56 bits at 400MHz, resolution 2ns, wraps every 4398046511103ns
Console: colour dummy device 80x25
printk: console [tty0] enabled
printk: bootconsole [uart0] disabled
Calibrating delay loop (skipped), value calculated using timer frequency.. 800.00 BogoMIPS (lpj=1600000)
pid_max: default: 32768 minimum: 301
LSM: Security Framework initializing
Mount-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
rcu: Hierarchical SRCU implementation.
EFI services will not be available.
smp: Bringing up secondary CPUs ...
Detected VIPT I-cache on CPU1
CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
Detected VIPT I-cache on CPU2
CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
Detected VIPT I-cache on CPU3
CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
smp: Brought up 1 node, 4 CPUs
SMP: Total of 4 processors activated.
CPU features: detected: 32-bit EL0 Support
CPU features: detected: CRC32 instructions
CPU: All CPU(s) started at EL2
alternatives: patching kernel code
devtmpfs: initialized
clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
DMI not present or invalid.
NET: Registered protocol family 16
DMA: preallocated 512 KiB GFP_KERNEL pool for atomic allocations
DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
cpuidle: using governor ladder
hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
ASID allocator initialised with 65536 entries
raid6: neonx8   gen()  1739 MB/s
raid6: neonx8   xor()  1286 MB/s
raid6: neonx4   gen()  1786 MB/s
raid6: neonx4   xor()  1257 MB/s
raid6: neonx2   gen()  1683 MB/s
raid6: neonx2   xor()  1165 MB/s
raid6: neonx1   gen()  1446 MB/s
raid6: neonx1   xor()   990 MB/s
raid6: int64x8  gen()  1198 MB/s
raid6: int64x8  xor()   642 MB/s
raid6: int64x4  gen()  1335 MB/s
raid6: int64x4  xor()   683 MB/s
raid6: int64x2  gen()  1165 MB/s
raid6: int64x2  xor()   625 MB/s
raid6: int64x1  gen()   862 MB/s
raid6: int64x1  xor()   431 MB/s
raid6: using algorithm neonx4 gen() 1786 MB/s
raid6: .... xor() 1257 MB/s, rmw enabled
raid6: using neon recovery algorithm
iommu: Default domain type: Translated 
vgaarb: loaded
SCSI subsystem initialized
usbcore: registered new interface driver usbfs
usbcore: registered new interface driver hub
usbcore: registered new device driver usb
usb_phy_generic soc:usbphy@0: supply vcc not found, using dummy regulator
pps_core: LinuxPPS API ver. 1 registered
pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
PTP clock support registered
EDAC MC: Ver: 3.0.0
Intel Service Layer Driver Initialized
FPGA manager framework
clocksource: Switched to clocksource arch_sys_counter
NET: Registered protocol family 2
tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes, linear)
TCP established hash table entries: 32768 (order: 6, 262144 bytes, linear)
TCP bind hash table entries: 32768 (order: 7, 524288 bytes, linear)
TCP: Hash tables configured (established 32768 bind 32768)
UDP hash table entries: 2048 (order: 4, 65536 bytes, linear)
UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes, linear)
NET: Registered protocol family 1
RPC: Registered named UNIX socket transport module.
RPC: Registered udp transport module.
RPC: Registered tcp transport module.
RPC: Registered tcp NFSv4.1 backchannel transport module.
PCI: CLS 0 bytes, default 64
hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
workingset: timestamp_bits=46 max_order=20 bucket_order=0
NFS: Registering the id_resolver key type
Key type id_resolver registered
Key type id_legacy registered
Key type cifs.idmap registered
xor: measuring software checksum speed
   8regs           :  1968 MB/sec
   32regs          :  2331 MB/sec
   arm64_neon      :  1726 MB/sec
xor: using function: 32regs (2331 MB/sec)
async_tx: api initialized (async)
Block layer SCSI generic (bsg) driver version 0.4 loaded (major 248)
io scheduler mq-deadline registered
io scheduler kyber registered
gpio-dwapb ffc03300.gpio: Cannot get reset descriptor
altera-pcie a0000000.pcie: host bridge /soc/bridge@80000000/pcie@200000000 ranges:
altera-pcie a0000000.pcie:      MEM 0x0090000000..0x0097ffffff -> 0x0000000000
altera-pcie a0000000.pcie: PCI host bridge to bus 0000:00
pci_bus 0000:00: root bus resource [bus 00-ff]
pci_bus 0000:00: root bus resource [mem 0x90000000-0x97ffffff] (bus address [0x00000000-0x07ffffff])
pci 0000:00:00.0: [1172:e000] type 01 class 0x060400
pci 0000:00:00.0: enabling Extended Tags
pci 0000:00:00.0: bridge configuration invalid ([bus 00-00]), reconfiguring
pci 0000:01:00.0: [10de:2187] type 00 class 0x030000
pci 0000:01:00.0: reg 0x10: [mem 0x90000000-0x90ffffff]
pci 0000:01:00.0: reg 0x14: [mem 0x00000000-0x0fffffff 64bit pref]
pci 0000:01:00.0: reg 0x1c: [mem 0x90000000-0x91ffffff 64bit pref]
pci 0000:01:00.0: reg 0x24: [io  0x0000-0x007f]
pci 0000:01:00.0: reg 0x30: [mem 0x90000000-0x9007ffff pref]
pci 0000:01:00.0: PME# supported from D0 D3hot D3cold
pci 0000:01:00.0: 63.008 Gb/s available PCIe bandwidth, limited by 8.0 GT/s PCIe x8 link at 0000:00:00.0 (capable of 126.016 Gb/s with 8.0 GT/s PCIe x16 link)
pci 0000:01:00.0: vgaarb: VGA device added: decodes=io+mem,owns=none,locks=none
pci 0000:01:00.1: [10de:1aeb] type 00 class 0x040300
pci 0000:01:00.1: reg 0x10: [mem 0x90000000-0x90003fff]
pci 0000:01:00.2: [10de:1aec] type 00 class 0x0c0330
pci 0000:01:00.2: reg 0x10: [mem 0x90000000-0x9003ffff 64bit pref]
pci 0000:01:00.2: reg 0x1c: [mem 0x90000000-0x9000ffff 64bit pref]
pci 0000:01:00.2: PME# supported from D0 D3hot D3cold
pci 0000:01:00.3: [10de:1aed] type 00 class 0x0c8000
pci 0000:01:00.3: reg 0x10: [mem 0x90000000-0x90000fff]
pci 0000:01:00.3: PME# supported from D0 D3hot D3cold
pci_bus 0000:01: busn_res: [bus 01-ff] end is updated to 01
pci 0000:00:00.0: BAR 15: no space for [mem size 0x18000000 64bit pref]
pci 0000:00:00.0: BAR 15: failed to assign [mem size 0x18000000 64bit pref]
pci 0000:00:00.0: BAR 14: assigned [mem 0x90000000-0x917fffff]
pci 0000:00:00.0: BAR 13: no space for [io  size 0x1000]
pci 0000:00:00.0: BAR 13: failed to assign [io  size 0x1000]
pci 0000:01:00.0: BAR 1: no space for [mem size 0x10000000 64bit pref]
pci 0000:01:00.0: BAR 1: failed to assign [mem size 0x10000000 64bit pref]
pci 0000:01:00.0: BAR 3: no space for [mem size 0x02000000 64bit pref]
pci 0000:01:00.0: BAR 3: failed to assign [mem size 0x02000000 64bit pref]
pci 0000:01:00.0: BAR 0: assigned [mem 0x90000000-0x90ffffff]
pci 0000:01:00.0: BAR 6: assigned [mem 0x91000000-0x9107ffff pref]
pci 0000:01:00.2: BAR 0: assigned [mem 0x91080000-0x910bffff 64bit pref]
pci 0000:01:00.2: BAR 3: assigned [mem 0x910c0000-0x910cffff 64bit pref]
pci 0000:01:00.1: BAR 0: assigned [mem 0x910d0000-0x910d3fff]
pci 0000:01:00.3: BAR 0: assigned [mem 0x910d4000-0x910d4fff]
pci 0000:01:00.0: BAR 5: no space for [io  size 0x0080]
pci 0000:01:00.0: BAR 5: failed to assign [io  size 0x0080]
pci 0000:00:00.0: PCI bridge to [bus 01]
pci 0000:00:00.0:   bridge window [mem 0x90000000-0x917fffff]
pcieport 0000:00:00.0: enabling device (0000 -> 0002)
pcieport 0000:00:00.0: PME: Signaling with IRQ 42
pci 0000:01:00.1: D0 power state depends on 0000:01:00.0
pci 0000:01:00.2: D0 power state depends on 0000:01:00.0
pci 0000:01:00.2: enabling device (0000 -> 0002)
pci 0000:01:00.3: D0 power state depends on 0000:01:00.0
Serial: 8250/16550 driver, 4 ports, IRQ sharing enabled
ffc02000.serial: ttyS0 at MMIO 0xffc02000 (irq = 33, base_baud = 6250000) is a 16550A
printk: console [ttyS0] enabled
cacheinfo: Unable to detect cache hierarchy for CPU 0
brd: module loaded
loop: module loaded
spi-nor spi0.0: mt25qu02g (262144 Kbytes)
2 fixed-partitions partitions found on MTD device ff8d2000.spi.0
Creating 2 MTD partitions on "ff8d2000.spi.0":
0x000000910000-0x000100010000 : "Boot and fpga data"
mtd: partition "Boot and fpga data" extends beyond the end of device "ff8d2000.spi.0" -- size truncated to 0xf6f0000
0x000003fe0000-0x000010000000 : "Root Filesystem - JFFS2"
libphy: Fixed MDIO Bus: probed
socfpga-dwmac ff800000.ethernet: IRQ eth_wake_irq not found
socfpga-dwmac ff800000.ethernet: IRQ eth_lpi not found
socfpga-dwmac ff800000.ethernet: User ID: 0x11, Synopsys ID: 0x37
socfpga-dwmac ff800000.ethernet: 	DWMAC1000
socfpga-dwmac ff800000.ethernet: DMA HW capability register supported
socfpga-dwmac ff800000.ethernet: RX Checksum Offload Engine supported
socfpga-dwmac ff800000.ethernet: COE Type 2
socfpga-dwmac ff800000.ethernet: TX Checksum insertion supported
socfpga-dwmac ff800000.ethernet: Enhanced/Alternate descriptors
socfpga-dwmac ff800000.ethernet: Enabled extended descriptors
socfpga-dwmac ff800000.ethernet: Ring mode enabled
socfpga-dwmac ff800000.ethernet: Enable RX Mitigation via HW Watchdog Timer
socfpga-dwmac ff800000.ethernet: device MAC address c6:d0:ef:ea:34:d5
libphy: stmmac: probed
dwc2 ffb00000.usb: supply vusb_d not found, using dummy regulator
dwc2 ffb00000.usb: supply vusb_a not found, using dummy regulator
dwc2 ffb00000.usb: EPs: 16, dedicated fifos, 8064 entries in SPRAM
dwc2 ffb00000.usb: DWC OTG Controller
dwc2 ffb00000.usb: new USB bus registered, assigned bus number 1
dwc2 ffb00000.usb: irq 34, io mem 0xffb00000
hub 1-0:1.0: USB hub found
hub 1-0:1.0: 1 port detected
ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
ehci-pci: EHCI PCI platform driver
ehci-platform: EHCI generic platform driver
xhci_hcd 0000:01:00.2: enabling device (0000 -> 0002)
xhci_hcd 0000:01:00.2: xHCI Host Controller
xhci_hcd 0000:01:00.2: new USB bus registered, assigned bus number 2
xhci_hcd 0000:01:00.2: hcc params 0x0180ff05 hci version 0x110 quirks 0x0000000000000010
hub 2-0:1.0: USB hub found
hub 2-0:1.0: 2 ports detected
xhci_hcd 0000:01:00.2: xHCI Host Controller
xhci_hcd 0000:01:00.2: new USB bus registered, assigned bus number 3
xhci_hcd 0000:01:00.2: Host supports USB 3.1 Enhanced SuperSpeed
usb usb3: We don't know the algorithms for LPM for this host, disabling LPM.
hub 3-0:1.0: USB hub found
hub 3-0:1.0: 4 ports detected
usbcore: registered new interface driver usb-storage
i2c /dev entries driver
device-mapper: ioctl: 4.43.0-ioctl (2020-10-01) initialised: dm-devel@redhat.com
EDAC DEVICE0: Giving out device to module sdramedac controller Altera ECC Manager: DEV sdramedac (INTERRUPT)
sdhci: Secure Digital Host Controller Interface driver
sdhci: Copyright(c) Pierre Ossman
Synopsys Designware Multimedia Card Interface Driver
dw_mmc ff808000.dwmmc0: IDMAC supports 32-bit address mode.
sdhci-pltfm: SDHCI platform and OF driver helper
dw_mmc ff808000.dwmmc0: Using internal DMA controller.
usbcore: registered new interface driver usbhid
dw_mmc ff808000.dwmmc0: Version ID is 280a
usbhid: USB HID core driver
dw_mmc ff808000.dwmmc0: DW MMC controller at irq 19,32 bit host data width,1024 deep fifo
fpga_manager fpga0: Stratix10 SOC FPGA Manager registered
mmc_host mmc0: card is polling.
u32 classifier
    input device check on
    Actions configured
NET: Registered protocol family 10
Segment Routing with IPv6
mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 400000Hz, actual 396825HZ div = 63)
sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
NET: Registered protocol family 17
Bridge firewalling registered
Key type dns_resolver registered
NET: Registered protocol family 40
Key type ._fscrypt registered
Key type .fscrypt registered
Key type fscrypt-provisioning registered
Btrfs loaded, crc32c=crc32c-generic
Key type encrypted registered
dma-pl330 ffda0000.pdma: Loaded driver for PL330 DMAC-341330
dma-pl330 ffda0000.pdma: 	DBUFF-512x8bytes Num_Chans-8 Num_Peri-32 Num_Events-8
at24 0-0051: supply vcc not found, using dummy regulator
at24 0-0051: 4096 byte 24c32 EEPROM, writable, 32 bytes/write
rtc-ds1307 0-0068: SET TIME!
rtc-ds1307 0-0068: registered as rtc0
rtc-ds1307 0-0068: setting system clock to 2000-01-01T00:00:14 UTC (946684814)
of-fpga-region soc:base_fpga_region: FPGA Region probed
mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
mmc0: new high speed SDXC card at address 0001
printk: console [netcon0] enabled
netconsole: network logging started
of_cfs_init
of_cfs_init: OK
dw-apb-uart ffc02000.serial: forbid DMA for kernel console
mmcblk0: mmc0:0001 SD64G 58.2 GiB 
 mmcblk0: p1 p2
md: Waiting for all devices to be available before autodetect
md: If you don't use raid, use raid=noautodetect
md: Autodetecting RAID arrays.
md: autorun ...
md: ... autorun DONE.
random: fast init done
EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
VFS: Mounted root (ext4 filesystem) on device 179:2.
devtmpfs: mounted
Freeing unused kernel memory: 3968K
Run /sbin/init as init process
systemd[1]: System time before build time, advancing clock.
systemd[1]: systemd 247.4+ running in system mode. (+PAM -AUDIT -SELINUX +IMA -APPARMOR -SMACK +SYSVINIT +UTMP -LIBCRYPTSETUP -GCRYPT -GNUTLS +ACL +XZ -LZ4 -ZSTD -SECCOMP +BLKID -ELFUTILS +KMOD -IDN2 -IDN -PCRE2 default-hierarchy=hybrid)
systemd[1]: Detected architecture arm64.

Welcome to Wind River Linux development 21.19!

systemd[1]: Set hostname to <intel-socfpga-64>.
systemd[1]: Queued start job for default target Graphical Interface.
random: systemd: uninitialized urandom read (16 bytes read)
systemd[1]: Created slice system-getty.slice.
[  OK  ] Created slice system-getty.slice.
random: systemd: uninitialized urandom read (16 bytes read)
systemd[1]: Created slice system-modprobe.slice.
[  OK  ] Created slice system-modprobe.slice.
random: systemd: uninitialized urandom read (16 bytes read)
systemd[1]: Created slice system-serial\x2dgetty.slice.
[  OK  ] Created slice system-serial\x2dgetty.slice.
systemd[1]: Created slice User and Session Slice.
[  OK  ] Created slice User and Session Slice.
systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
[  OK  ] Started Dispatch Password …ts to Console Directory Watch.
systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[  OK  ] Started Forward Password R…uests to Wall Directory Watch.
systemd[1]: Reached target Paths.
[  OK  ] Reached target Paths.
systemd[1]: Reached target Remote File Systems.
[  OK  ] Reached target Remote File Systems.
systemd[1]: Reached target Slices.
[  OK  ] Reached target Slices.
systemd[1]: Reached target Swap.
[  OK  ] Reached target Swap.
systemd[1]: Listening on RPCbind Server Activation Socket.
[  OK  ] Listening on RPCbind Server Activation Socket.
systemd[1]: Reached target RPC Port Mapper.
[  OK  ] Reached target RPC Port Mapper.
systemd[1]: Listening on Syslog Socket.
[  OK  ] Listening on Syslog Socket.
systemd[1]: Listening on initctl Compatibility Named Pipe.
[  OK  ] Listening on initctl Compatibility Named Pipe.
systemd[1]: Condition check resulted in Journal Audit Socket being skipped.
systemd[1]: Listening on Journal Socket (/dev/log).
[  OK  ] Listening on Journal Socket (/dev/log).
systemd[1]: Listening on Journal Socket.
[  OK  ] Listening on Journal Socket.
systemd[1]: Listening on Network Service Netlink Socket.
[  OK  ] Listening on Network Service Netlink Socket.
systemd[1]: Listening on udev Control Socket.
[  OK  ] Listening on udev Control Socket.
systemd[1]: Listening on udev Kernel Socket.
[  OK  ] Listening on udev Kernel Socket.
systemd[1]: Listening on User Database Manager Socket.
[  OK  ] Listening on User Database Manager Socket.
systemd[1]: Condition check resulted in Huge Pages File System being skipped.
systemd[1]: Mounting POSIX Message Queue File System...
         Mounting POSIX Message Queue File System...
systemd[1]: Mounting Kernel Debug File System...
         Mounting Kernel Debug File System...
systemd[1]: Mounting Kernel Trace File System...
         Mounting Kernel Trace File System...
systemd[1]: Mounting Temporary Directory (/tmp)...
         Mounting Temporary Directory (/tmp)...
systemd[1]: Starting Create list of static device nodes for the current kernel...
         Starting Create list of st…odes for the current kernel...
systemd[1]: Starting Load Kernel Module configfs...
         Starting Load Kernel Module configfs...
systemd[1]: Starting Load Kernel Module drm...
         Starting Load Kernel Module drm...
systemd[1]: Starting Load Kernel Module fuse...
         Starting Load Kernel Module fuse...
fuse: init (API version 7.32)
systemd[1]: Starting RPC Bind...
         Starting RPC Bind...
systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
systemd[1]: Starting Journal Service...
         Starting Journal Service...
systemd[1]: Starting Load Kernel Modules...
         Starting Load Kernel Modules...
systemd[1]: Starting Remount Root and Kernel File Systems...
         Starting Remount Root and Kernel File Systems...
systemd[1]: Starting Coldplug All udev Devices...
         Starting Coldplug All udev Devices...EXT4-fs (mmcblk0p2): re-mounted. Opts: (null)

openvswitch: Open vSwitch switching datapath
systemd[1]: Started RPC Bind.
[  OK  ] Started RPC Bind.
systemd[1]: Mounted POSIX Message Queue File System.
[  OK  ] Mounted POSIX Message Queue File System.
systemd[1]: Started Journal Service.
[  OK  ] Started Journal Service.
[  OK  ] Mounted Kernel Debug File System.
[  OK  ] Mounted Kernel Trace File System.
[  OK  ] Mounted Temporary Directory (/tmp).
[  OK  ] Finished Create list of st… nodes for the current kernel.
[  OK  ] Finished Load Kernel Module configfs.
[  OK  ] Finished Load Kernel Module drm.
[  OK  ] Finished Load Kernel Module fuse.
[  OK  ] Finished Load Kernel Modules.
[  OK  ] Finished Remount Root and Kernel File Systems.
         Mounting FUSE Control File System...
         Mounting Kernel Configuration File System...
         Starting Flush Journal to Persistent Storage...
systemd-journald[141]: Received client request to flush runtime journal.
         Starting Apply Kernel Variables...
         Starting Create Static Device Nodes in /dev...
[  OK  ] Mounted FUSE Control File System.
[  OK  ] Mounted Kernel Configuration File System.
[  OK  ] Finished Flush Journal to Persistent Storage.
[  OK  ] Finished Apply Kernel Variables.
[  OK  ] Finished Create Static Device Nodes in /dev.
[  OK  ] Reached target Local File Systems (Pre).
         Mounting /var/volatile...
         Starting Rule-based Manage…for Device Events and Files...
[  OK  ] Finished Coldplug All udev Devices.
[  OK  ] Mounted /var/volatile.
         Starting Load/Save Random Seed...
[  OK  ] Started Rule-based Manager for Device Events and Files.
nvidia_drm: loading out-of-tree module taints kernel.
nvidia_drm: module license 'MIT' taints kernel.
Disabling lock debugging due to kernel taint
[  OK  ] Found device /dev/mmcblk0p1.
[  OK  ] Reached target Hardware activated USB gadget.
[  OK  ] Listening on Load/Save RF …itch Status /dev/rfkill Watch.
         Mounting /boot...
random: crng init done
random: 7 urandom warning(s) missed due to ratelimiting
FAT-fs (mmcblk0p1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.
[  OK  ] Mounted /boot.
[  OK  ] Reached target Local File Systems.
         Starting Create Volatile Files and Directories...
[  OK  ] Finished Load/Save Random Seed.
[  OK  ] Finished Create Volatile Files and Directories.
[  OK  ] Started Hardware RNG Entropy Gatherer Daemon.
         Starting Network Time Synchronization...
         Starting Update UTMP about System Boot/Shutdown...
[  OK  ] Finished Update UTMP about System Boot/Shutdown.
nvidia-nvlink: Nvlink Core is being initialized, major device number 245

nvidia 0000:01:00.0: enabling device (0000 -> 0002)
nvidia 0000:01:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=none:owns=none
NVRM: loading NVIDIA UNIX aarch64 Kernel Module  465.31  Thu May 13 22:39:49 UTC 2021
[  OK  ] Started Network Time Synchronization.
[  OK  ] Reached target System Initialization.
[  OK  ] Started Daily Cleanup of Temporary Directories.
[  OK  ] Reached target System Time Set.
[  OK  ] Reached target System Time Synchronized.
[  OK  ] Started Daily rotation of log files.
[  OK  ] Reached target Timers.
[  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
[  OK  ] Listening on D-Bus System Message Bus Socket.
         Starting sshd.socket.
[  OK  ] Listening on sshd.socket.
[  OK  ] Reached target Sockets.
[  OK  ] Reached target Basic System.
[  OK  ] Started Job spooling tools.
[  OK  ] Started Periodic Command Scheduler.
[  OK  ] Started D-Bus System Message Bus.
         Starting IPv6 Packet Filtering Framework...
         Starting IPv4 Packet Filtering Framework...
         Starting Telephony service...
         Starting User Login Management...
         Starting OpenSSH Key Generation...
[  OK  ] Finished IPv6 Packet Filtering Framework.
[  OK  ] Finished IPv4 Packet Filtering Framework.
[  OK  ] Reached target Network (Pre).
         Starting Network Manager...
         Starting Network Service...
[  OK  ] Started Telephony service.
[  OK  ] Finished OpenSSH Key Generation.
[  OK  ] Started User Login Management.
[  OK  ] Started Network Service.
         Starting Wait for Network to be Configured...
         Starting Network Name Resolution...
[  OK  ] Started Network Manager.
         Starting Network Manager Wait Online...
         Starting Hostname Service...
[  OK  ] Started Network Name Resolution.
[  OK  ] Reached target Network.
         Starting Avahi mDNS/DNS-SD Stack...
         Starting Berkeley Internet Name Domain (DNS)...
[  OK  ] Started Respond to IPv6 Node Information Queries.
         Starting Postfix Mail Transport Agent...
         Starting /etc/rc.local Compatibility...
[  OK  ] Started Network Router Discovery Daemon.
         Starting Permit User Sessions...
[  OK  ] Started Xinetd A Powerful Replacement For Inetd.
[  OK  ] Started /etc/rc.local Compatibility.
[  OK  ] Finished Permit User Sessions.
[  OK  ] Started Avahi mDNS/DNS-SD Stack.
[  OK  ] Started LXDE Display Manager.
[  OK  ] Started Serial Getty on ttyS0.
[  OK  ] Reached target Login Prompts.
[  OK  ] Started Hostname Service.
         Starting Network Manager Script Dispatcher Service...
[  OK  ] Started Network Manager Script Dispatcher Service.
socfpga-dwmac ff800000.ethernet eth0: PHY [stmmac-0:04] driver [Micrel KSZ9031 Gigabit PHY] (irq=POLL)
socfpga-dwmac ff800000.ethernet eth0: No Safety Features support found
socfpga-dwmac ff800000.ethernet eth0: IEEE 1588-2008 Advanced Timestamp supported
socfpga-dwmac ff800000.ethernet eth0: registered PTP clock
socfpga-dwmac ff800000.ethernet eth0: configuring for phy/rgmii link mode
[  OK  ] Started Berkeley Internet Name Domain (DNS).
[  OK  ] Reached target Host and Network Name Lookups.
[  OK  ] Started NFS status monitor for NFSv2/3 locking..
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
socfpga-dwmac ff800000.ethernet eth0: Link is Up - 100Mbps/Full - flow control rx/tx
IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
[  OK  ] Started Postfix Mail Transport Agent.
[  OK  ] Finished Wait for Network to be Configured.
[  OK  ] Finished Network Manager Wait Online.
[  OK  ] Reached target Network is Online.
         Starting System Logging Service...
[  OK  ] Started System Logging Service.
[  OK  ] Reached target Multi-User System.
[  OK  ] Reached target Graphical Interface.
         Starting Update UTMP about System Runlevel Changes...
[  OK  ] Finished Update UTMP about System Runlevel Changes.

Wind River Linux development 21.19 intel-socfpga-64 ttyS0

intel-socfpga-64 login: root
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
root@intel-socfpga-64:~# lspci 
00:00.0 PCI bridge: Altera Corporation Device e000 (rev 01)
01:00.0 VGA compatible controller: NVIDIA Corporation TU116 [GeForce GTX 1650 SUPER] (rev a1)
01:00.1 Audio device: NVIDIA Corporation TU116 High Definition Audio Controller (rev a1)
01:00.2 USB controller: NVIDIA Corporation TU116 USB 3.1 Host Controller (rev a1)
01:00.3 Serial bus controller [0c80]: NVIDIA Corporation TU116 USB Type-C UCSI Controller (rev a1)
root@intel-socfpga-64:~# NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0

root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
dmesg
[    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
[    0.000000] Linux version 5.10.35-yocto-standard (oe-user@oe-host) (aarch64-wrs-linux-gcc (GCC) 10.2.0, GNU ld (GNU Binutils) 2.36.1.20210209) #1 SMP PREEMPT Fri May 28 11:43:11 UTC 2021
[    0.000000] Machine model: SoCFPGA Stratix 10 SoCDK
[    0.000000] earlycon: uart0 at MMIO32 0x00000000ffc02000 (options '115200n8')
[    0.000000] printk: bootconsole [uart0] enabled
[    0.000000] efi: UEFI not found.
[    0.000000] Reserved memory: created DMA memory pool at 0x0000000000000000, size 16 MiB
[    0.000000] OF: reserved mem: initialized node svcbuffer@0, compatible id shared-dma-pool
[    0.000000] cma: Reserved 16 MiB at 0x000000007e800000
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000000000-0x00000000ffffffff]
[    0.000000]   DMA32    empty
[    0.000000]   Normal   [mem 0x0000000100000000-0x00000001ffffffff]
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000000000-0x0000000000ffffff]
[    0.000000]   node   0: [mem 0x0000000001000000-0x000000007fffffff]
[    0.000000]   node   0: [mem 0x0000000180000000-0x00000001ffffffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000000000-0x00000001ffffffff]
[    0.000000] On node 0 totalpages: 1048576
[    0.000000]   DMA zone: 8192 pages used for memmap
[    0.000000]   DMA zone: 0 pages reserved
[    0.000000]   DMA zone: 524288 pages, LIFO batch:63
[    0.000000]   Normal zone: 8192 pages used for memmap
[    0.000000]   Normal zone: 524288 pages, LIFO batch:63
[    0.000000] psci: probing for conduit method from DT.
[    0.000000] psci: PSCIv65535.65535 detected in firmware.
[    0.000000] psci: Using standard PSCI v0.2 function IDs
[    0.000000] psci: MIGRATE_INFO_TYPE not supported.
[    0.000000] psci: SMC Calling Convention v1.0
[    0.000000] percpu: Embedded 30 pages/cpu s82008 r8192 d32680 u122880
[    0.000000] pcpu-alloc: s82008 r8192 d32680 u122880 alloc=30*4096
[    0.000000] pcpu-alloc: [0] 0 [0] 1 [0] 2 [0] 3 
[    0.000000] Detected VIPT I-cache on CPU0
[    0.000000] CPU features: detected: ARM erratum 845719
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 1032192
[    0.000000] Kernel command line: earlycon panic=-1 root=/dev/mmcblk0p2 rw rootwait
[    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
[    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
[    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
[    0.000000] software IO TLB: mapped [mem 0x000000007a800000-0x000000007e800000] (64MB)
[    0.000000] Memory: 3993020K/4194304K available (12416K kernel code, 1952K rwdata, 2936K rodata, 3968K init, 707K bss, 184900K reserved, 16384K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] ftrace: allocating 38327 entries in 150 pages
[    0.000000] ftrace: allocated 150 pages with 4 groups
[    0.000000] rcu: Preemptible hierarchical RCU implementation.
[    0.000000] rcu: 	RCU event tracing is enabled.
[    0.000000] 	Trampoline variant of Tasks RCU enabled.
[    0.000000] 	Rude variant of Tasks RCU enabled.
[    0.000000] 	Tracing variant of Tasks RCU enabled.
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
[    0.000000] GIC: Using split EOI/Deactivate mode
[    0.000000] random: get_random_bytes called from start_kernel+0x398/0x5a0 with crng_init=0
[    0.000000] arch_timer: cp15 timer(s) running at 400.00MHz (phys).
[    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x5c4093a7d1, max_idle_ns: 440795210635 ns
[    0.000005] sched_clock: 56 bits at 400MHz, resolution 2ns, wraps every 4398046511103ns
[    0.006868] Console: colour dummy device 80x25
[    0.009997] printk: console [tty0] enabled
[    0.012790] printk: bootconsole [uart0] disabled
[    0.016119] Calibrating delay loop (skipped), value calculated using timer frequency.. 800.00 BogoMIPS (lpj=1600000)
[    0.016143] pid_max: default: 32768 minimum: 301
[    0.016259] LSM: Security Framework initializing
[    0.016437] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.016472] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.018388] rcu: Hierarchical SRCU implementation.
[    0.018913] EFI services will not be available.
[    0.019155] smp: Bringing up secondary CPUs ...
[    0.019696] Detected VIPT I-cache on CPU1
[    0.019761] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
[    0.020366] Detected VIPT I-cache on CPU2
[    0.020400] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
[    0.021008] Detected VIPT I-cache on CPU3
[    0.021040] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
[    0.021144] smp: Brought up 1 node, 4 CPUs
[    0.021187] SMP: Total of 4 processors activated.
[    0.021199] CPU features: detected: 32-bit EL0 Support
[    0.021211] CPU features: detected: CRC32 instructions
[    0.021271] CPU: All CPU(s) started at EL2
[    0.021300] alternatives: patching kernel code
[    0.022048] devtmpfs: initialized
[    0.025848] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.025883] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
[    0.027026] DMI not present or invalid.
[    0.027496] NET: Registered protocol family 16
[    0.029190] DMA: preallocated 512 KiB GFP_KERNEL pool for atomic allocations
[    0.029378] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
[    0.029726] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
[    0.030397] cpuidle: using governor ladder
[    0.030489] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
[    0.030593] ASID allocator initialised with 65536 entries
[    0.117020] raid6: neonx8   gen()  1739 MB/s
[    0.185121] raid6: neonx8   xor()  1286 MB/s
[    0.253237] raid6: neonx4   gen()  1786 MB/s
[    0.321331] raid6: neonx4   xor()  1257 MB/s
[    0.389455] raid6: neonx2   gen()  1683 MB/s
[    0.457551] raid6: neonx2   xor()  1165 MB/s
[    0.525671] raid6: neonx1   gen()  1446 MB/s
[    0.593769] raid6: neonx1   xor()   990 MB/s
[    0.661882] raid6: int64x8  gen()  1198 MB/s
[    0.729975] raid6: int64x8  xor()   642 MB/s
[    0.798090] raid6: int64x4  gen()  1335 MB/s
[    0.866216] raid6: int64x4  xor()   683 MB/s
[    0.934278] raid6: int64x2  gen()  1165 MB/s
[    1.002371] raid6: int64x2  xor()   625 MB/s
[    1.070441] raid6: int64x1  gen()   862 MB/s
[    1.138527] raid6: int64x1  xor()   431 MB/s
[    1.138539] raid6: using algorithm neonx4 gen() 1786 MB/s
[    1.138550] raid6: .... xor() 1257 MB/s, rmw enabled
[    1.138562] raid6: using neon recovery algorithm
[    1.139601] iommu: Default domain type: Translated 
[    1.139798] vgaarb: loaded
[    1.140036] SCSI subsystem initialized
[    1.140261] usbcore: registered new interface driver usbfs
[    1.140318] usbcore: registered new interface driver hub
[    1.140363] usbcore: registered new device driver usb
[    1.140509] usb_phy_generic soc:usbphy@0: supply vcc not found, using dummy regulator
[    1.140983] pps_core: LinuxPPS API ver. 1 registered
[    1.140997] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    1.141025] PTP clock support registered
[    1.141215] EDAC MC: Ver: 3.0.0
[    1.142283] Intel Service Layer Driver Initialized
[    1.142430] FPGA manager framework
[    1.143428] clocksource: Switched to clocksource arch_sys_counter
[    1.899354] NET: Registered protocol family 2
[    1.900065] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes, linear)
[    1.900135] TCP established hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    1.900452] TCP bind hash table entries: 32768 (order: 7, 524288 bytes, linear)
[    1.900945] TCP: Hash tables configured (established 32768 bind 32768)
[    1.901083] UDP hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    1.901185] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    1.901437] NET: Registered protocol family 1
[    1.901907] RPC: Registered named UNIX socket transport module.
[    1.901921] RPC: Registered udp transport module.
[    1.901932] RPC: Registered tcp transport module.
[    1.901942] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    1.901965] PCI: CLS 0 bytes, default 64
[    1.902971] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
[    1.904470] workingset: timestamp_bits=46 max_order=20 bucket_order=0
[    1.911870] NFS: Registering the id_resolver key type
[    1.911909] Key type id_resolver registered
[    1.911920] Key type id_legacy registered
[    1.912593] Key type cifs.idmap registered
[    1.956794] xor: measuring software checksum speed
[    1.961838]    8regs           :  1968 MB/sec
[    1.966078]    32regs          :  2331 MB/sec
[    1.971810]    arm64_neon      :  1726 MB/sec
[    1.971822] xor: using function: 32regs (2331 MB/sec)
[    1.971839] async_tx: api initialized (async)
[    1.971885] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 248)
[    1.971902] io scheduler mq-deadline registered
[    1.971914] io scheduler kyber registered
[    1.972495] gpio-dwapb ffc03300.gpio: Cannot get reset descriptor
[    1.972911] altera-pcie a0000000.pcie: host bridge /soc/bridge@80000000/pcie@200000000 ranges:
[    1.972974] altera-pcie a0000000.pcie:      MEM 0x0090000000..0x0097ffffff -> 0x0000000000
[    1.973221] altera-pcie a0000000.pcie: PCI host bridge to bus 0000:00
[    1.973243] pci_bus 0000:00: root bus resource [bus 00-ff]
[    1.973261] pci_bus 0000:00: root bus resource [mem 0x90000000-0x97ffffff] (bus address [0x00000000-0x07ffffff])
[    1.973337] pci 0000:00:00.0: [1172:e000] type 01 class 0x060400
[    1.973411] pci 0000:00:00.0: enabling Extended Tags
[    1.974584] pci 0000:00:00.0: bridge configuration invalid ([bus 00-00]), reconfiguring
[    1.975001] pci 0000:01:00.0: [10de:2187] type 00 class 0x030000
[    1.975147] pci 0000:01:00.0: reg 0x10: [mem 0x90000000-0x90ffffff]
[    1.975266] pci 0000:01:00.0: reg 0x14: [mem 0x00000000-0x0fffffff 64bit pref]
[    1.975385] pci 0000:01:00.0: reg 0x1c: [mem 0x90000000-0x91ffffff 64bit pref]
[    1.975472] pci 0000:01:00.0: reg 0x24: [io  0x0000-0x007f]
[    1.975546] pci 0000:01:00.0: reg 0x30: [mem 0x90000000-0x9007ffff pref]
[    1.976331] pci 0000:01:00.0: PME# supported from D0 D3hot D3cold
[    1.976869] pci 0000:01:00.0: 63.008 Gb/s available PCIe bandwidth, limited by 8.0 GT/s PCIe x8 link at 0000:00:00.0 (capable of 126.016 Gb/s with 8.0 GT/s PCIe x16 link)
[    1.977037] pci 0000:01:00.0: vgaarb: VGA device added: decodes=io+mem,owns=none,locks=none
[    1.977248] pci 0000:01:00.1: [10de:1aeb] type 00 class 0x040300
[    1.977391] pci 0000:01:00.1: reg 0x10: [mem 0x90000000-0x90003fff]
[    1.978731] pci 0000:01:00.2: [10de:1aec] type 00 class 0x0c0330
[    1.978921] pci 0000:01:00.2: reg 0x10: [mem 0x90000000-0x9003ffff 64bit pref]
[    1.979098] pci 0000:01:00.2: reg 0x1c: [mem 0x90000000-0x9000ffff 64bit pref]
[    1.979760] pci 0000:01:00.2: PME# supported from D0 D3hot D3cold
[    1.980281] pci 0000:01:00.3: [10de:1aed] type 00 class 0x0c8000
[    1.980425] pci 0000:01:00.3: reg 0x10: [mem 0x90000000-0x90000fff]
[    1.981302] pci 0000:01:00.3: PME# supported from D0 D3hot D3cold
[    1.982660] pci_bus 0000:01: busn_res: [bus 01-ff] end is updated to 01
[    1.982711] pci 0000:00:00.0: BAR 15: no space for [mem size 0x18000000 64bit pref]
[    1.982729] pci 0000:00:00.0: BAR 15: failed to assign [mem size 0x18000000 64bit pref]
[    1.982747] pci 0000:00:00.0: BAR 14: assigned [mem 0x90000000-0x917fffff]
[    1.982762] pci 0000:00:00.0: BAR 13: no space for [io  size 0x1000]
[    1.982776] pci 0000:00:00.0: BAR 13: failed to assign [io  size 0x1000]
[    1.982801] pci 0000:01:00.0: BAR 1: no space for [mem size 0x10000000 64bit pref]
[    1.982817] pci 0000:01:00.0: BAR 1: failed to assign [mem size 0x10000000 64bit pref]
[    1.982836] pci 0000:01:00.0: BAR 3: no space for [mem size 0x02000000 64bit pref]
[    1.982852] pci 0000:01:00.0: BAR 3: failed to assign [mem size 0x02000000 64bit pref]
[    1.982869] pci 0000:01:00.0: BAR 0: assigned [mem 0x90000000-0x90ffffff]
[    1.982911] pci 0000:01:00.0: BAR 6: assigned [mem 0x91000000-0x9107ffff pref]
[    1.982929] pci 0000:01:00.2: BAR 0: assigned [mem 0x91080000-0x910bffff 64bit pref]
[    1.983028] pci 0000:01:00.2: BAR 3: assigned [mem 0x910c0000-0x910cffff 64bit pref]
[    1.983125] pci 0000:01:00.1: BAR 0: assigned [mem 0x910d0000-0x910d3fff]
[    1.983165] pci 0000:01:00.3: BAR 0: assigned [mem 0x910d4000-0x910d4fff]
[    1.983203] pci 0000:01:00.0: BAR 5: no space for [io  size 0x0080]
[    1.983218] pci 0000:01:00.0: BAR 5: failed to assign [io  size 0x0080]
[    1.983235] pci 0000:00:00.0: PCI bridge to [bus 01]
[    1.983255] pci 0000:00:00.0:   bridge window [mem 0x90000000-0x917fffff]
[    1.983385] pcieport 0000:00:00.0: enabling device (0000 -> 0002)
[    1.983645] pcieport 0000:00:00.0: PME: Signaling with IRQ 42
[    1.984139] pci 0000:01:00.1: D0 power state depends on 0000:01:00.0
[    1.984669] pci 0000:01:00.2: D0 power state depends on 0000:01:00.0
[    1.985078] pci 0000:01:00.2: enabling device (0000 -> 0002)
[    1.985328] pci 0000:01:00.3: D0 power state depends on 0000:01:00.0
[    1.986670] Serial: 8250/16550 driver, 4 ports, IRQ sharing enabled
[    1.988030] ffc02000.serial: ttyS0 at MMIO 0xffc02000 (irq = 33, base_baud = 6250000) is a 16550A
[    2.909775] printk: console [ttyS0] enabled
[    2.913752] cacheinfo: Unable to detect cache hierarchy for CPU 0
[    2.926067] brd: module loaded
[    2.936492] loop: module loaded
[    2.955546] spi-nor spi0.0: mt25qu02g (262144 Kbytes)
[    2.959326] 2 fixed-partitions partitions found on MTD device ff8d2000.spi.0
[    2.965066] Creating 2 MTD partitions on "ff8d2000.spi.0":
[    2.969248] 0x000000910000-0x000100010000 : "Boot and fpga data"
[    2.973948] mtd: partition "Boot and fpga data" extends beyond the end of device "ff8d2000.spi.0" -- size truncated to 0xf6f0000
[    2.992380] 0x000003fe0000-0x000010000000 : "Root Filesystem - JFFS2"
[    3.001244] libphy: Fixed MDIO Bus: probed
[    3.004507] socfpga-dwmac ff800000.ethernet: IRQ eth_wake_irq not found
[    3.009816] socfpga-dwmac ff800000.ethernet: IRQ eth_lpi not found
[    3.015072] socfpga-dwmac ff800000.ethernet: User ID: 0x11, Synopsys ID: 0x37
[    3.020904] socfpga-dwmac ff800000.ethernet: 	DWMAC1000
[    3.024826] socfpga-dwmac ff800000.ethernet: DMA HW capability register supported
[    3.030993] socfpga-dwmac ff800000.ethernet: RX Checksum Offload Engine supported
[    3.037160] socfpga-dwmac ff800000.ethernet: COE Type 2
[    3.041079] socfpga-dwmac ff800000.ethernet: TX Checksum insertion supported
[    3.046814] socfpga-dwmac ff800000.ethernet: Enhanced/Alternate descriptors
[    3.052461] socfpga-dwmac ff800000.ethernet: Enabled extended descriptors
[    3.057936] socfpga-dwmac ff800000.ethernet: Ring mode enabled
[    3.062467] socfpga-dwmac ff800000.ethernet: Enable RX Mitigation via HW Watchdog Timer
[    3.069161] socfpga-dwmac ff800000.ethernet: device MAC address c6:d0:ef:ea:34:d5
[    3.075811] libphy: stmmac: probed
[    3.080772] dwc2 ffb00000.usb: supply vusb_d not found, using dummy regulator
[    3.086729] dwc2 ffb00000.usb: supply vusb_a not found, using dummy regulator
[    3.092852] dwc2 ffb00000.usb: EPs: 16, dedicated fifos, 8064 entries in SPRAM
[    3.099052] dwc2 ffb00000.usb: DWC OTG Controller
[    3.102503] dwc2 ffb00000.usb: new USB bus registered, assigned bus number 1
[    3.108271] dwc2 ffb00000.usb: irq 34, io mem 0xffb00000
[    3.112923] hub 1-0:1.0: USB hub found
[    3.115395] hub 1-0:1.0: 1 port detected
[    3.119429] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    3.124679] ehci-pci: EHCI PCI platform driver
[    3.127861] ehci-platform: EHCI generic platform driver
[    3.132547] xhci_hcd 0000:01:00.2: enabling device (0000 -> 0002)
[    3.137440] xhci_hcd 0000:01:00.2: xHCI Host Controller
[    3.141373] xhci_hcd 0000:01:00.2: new USB bus registered, assigned bus number 2
[    3.148144] xhci_hcd 0000:01:00.2: hcc params 0x0180ff05 hci version 0x110 quirks 0x0000000000000010
[    3.157112] hub 2-0:1.0: USB hub found
[    3.159598] hub 2-0:1.0: 2 ports detected
[    3.162791] xhci_hcd 0000:01:00.2: xHCI Host Controller
[    3.166722] xhci_hcd 0000:01:00.2: new USB bus registered, assigned bus number 3
[    3.172815] xhci_hcd 0000:01:00.2: Host supports USB 3.1 Enhanced SuperSpeed
[    3.178627] usb usb3: We don't know the algorithms for LPM for this host, disabling LPM.
[    3.185877] hub 3-0:1.0: USB hub found
[    3.188362] hub 3-0:1.0: 4 ports detected
[    3.191919] usbcore: registered new interface driver usb-storage
[    3.197488] i2c /dev entries driver
[    3.200900] device-mapper: ioctl: 4.43.0-ioctl (2020-10-01) initialised: dm-devel@redhat.com
[    3.208873] EDAC DEVICE0: Giving out device to module sdramedac controller Altera ECC Manager: DEV sdramedac (INTERRUPT)
[    3.218765] sdhci: Secure Digital Host Controller Interface driver
[    3.223747] sdhci: Copyright(c) Pierre Ossman
[    3.226794] Synopsys Designware Multimedia Card Interface Driver
[    3.231735] dw_mmc ff808000.dwmmc0: IDMAC supports 32-bit address mode.
[    3.235462] sdhci-pltfm: SDHCI platform and OF driver helper
[    3.237055] dw_mmc ff808000.dwmmc0: Using internal DMA controller.
[    3.245085] usbcore: registered new interface driver usbhid
[    3.246267] dw_mmc ff808000.dwmmc0: Version ID is 280a
[    3.250503] usbhid: USB HID core driver
[    3.254386] dw_mmc ff808000.dwmmc0: DW MMC controller at irq 19,32 bit host data width,1024 deep fifo
[    3.257139] fpga_manager fpga0: Stratix10 SOC FPGA Manager registered
[    3.264951] mmc_host mmc0: card is polling.
[    3.270000] u32 classifier
[    3.274167]     input device check on
[    3.276530]     Actions configured
[    3.279252] NET: Registered protocol family 10
[    3.283432] Segment Routing with IPv6
[    3.283456] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 400000Hz, actual 396825HZ div = 63)
[    3.285845] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
[    3.299098] NET: Registered protocol family 17
[    3.302296] Bridge firewalling registered
[    3.305120] Key type dns_resolver registered
[    3.308316] NET: Registered protocol family 40
[    3.311934] Key type ._fscrypt registered
[    3.314655] Key type .fscrypt registered
[    3.317349] Key type fscrypt-provisioning registered
[    3.322000] Btrfs loaded, crc32c=crc32c-generic
[    3.326159] Key type encrypted registered
[    3.332085] dma-pl330 ffda0000.pdma: Loaded driver for PL330 DMAC-341330
[    3.337523] dma-pl330 ffda0000.pdma: 	DBUFF-512x8bytes Num_Chans-8 Num_Peri-32 Num_Events-8
[    3.354302] at24 0-0051: supply vcc not found, using dummy regulator
[    3.360179] at24 0-0051: 4096 byte 24c32 EEPROM, writable, 32 bytes/write
[    3.367052] rtc-ds1307 0-0068: SET TIME!
[    3.371878] rtc-ds1307 0-0068: registered as rtc0
[    3.376295] rtc-ds1307 0-0068: setting system clock to 2000-01-01T00:00:14 UTC (946684814)
[    3.383612] of-fpga-region soc:base_fpga_region: FPGA Region probed
[    3.388591] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
[    3.398319] mmc0: new high speed SDXC card at address 0001
[    3.402732] printk: console [netcon0] enabled
[    3.405793] netconsole: network logging started
[    3.409023] of_cfs_init
[    3.410263] of_cfs_init: OK
[    3.412202] dw-apb-uart ffc02000.serial: forbid DMA for kernel console
[    3.417913] mmcblk0: mmc0:0001 SD64G 58.2 GiB 
[    3.422982]  mmcblk0: p1 p2
[    3.425617] md: Waiting for all devices to be available before autodetect
[    3.431114] md: If you don't use raid, use raid=noautodetect
[    3.435489] md: Autodetecting RAID arrays.
[    3.438276] md: autorun ...
[    3.439774] md: ... autorun DONE.
[    3.457015] random: fast init done
[    3.469756] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
[    3.476590] VFS: Mounted root (ext4 filesystem) on device 179:2.
[    3.482239] devtmpfs: mounted
[    3.488293] Freeing unused kernel memory: 3968K
[    3.491647] Run /sbin/init as init process
[    3.494433]   with arguments:
[    3.494437]     /sbin/init
[    3.494442]   with environment:
[    3.494446]     HOME=/
[    3.494450]     TERM=linux
[    3.875484] systemd[1]: System time before build time, advancing clock.
[    3.940173] systemd[1]: systemd 247.4+ running in system mode. (+PAM -AUDIT -SELINUX +IMA -APPARMOR -SMACK +SYSVINIT +UTMP -LIBCRYPTSETUP -GCRYPT -GNUTLS +ACL +XZ -LZ4 -ZSTD -SECCOMP +BLKID -ELFUTILS +KMOD -IDN2 -IDN -PCRE2 default-hierarchy=hybrid)
[    3.961463] systemd[1]: Detected architecture arm64.
[    4.000246] systemd[1]: Set hostname to <intel-socfpga-64>.
[    4.470639] systemd[1]: Queued start job for default target Graphical Interface.
[    4.478131] random: systemd: uninitialized urandom read (16 bytes read)
[    4.515976] systemd[1]: Created slice system-getty.slice.
[    4.531629] random: systemd: uninitialized urandom read (16 bytes read)
[    4.538608] systemd[1]: Created slice system-modprobe.slice.
[    4.551550] random: systemd: uninitialized urandom read (16 bytes read)
[    4.558357] systemd[1]: Created slice system-serial\x2dgetty.slice.
[    4.577073] systemd[1]: Created slice User and Session Slice.
[    4.591875] systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
[    4.607714] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[    4.623848] systemd[1]: Reached target Paths.
[    4.635583] systemd[1]: Reached target Remote File Systems.
[    4.651559] systemd[1]: Reached target Slices.
[    4.663594] systemd[1]: Reached target Swap.
[    4.692782] systemd[1]: Listening on RPCbind Server Activation Socket.
[    4.707748] systemd[1]: Reached target RPC Port Mapper.
[    4.725014] systemd[1]: Listening on Syslog Socket.
[    4.739826] systemd[1]: Listening on initctl Compatibility Named Pipe.
[    4.759058] systemd[1]: Condition check resulted in Journal Audit Socket being skipped.
[    4.766453] systemd[1]: Listening on Journal Socket (/dev/log).
[    4.784072] systemd[1]: Listening on Journal Socket.
[    4.800205] systemd[1]: Listening on Network Service Netlink Socket.
[    4.816167] systemd[1]: Listening on udev Control Socket.
[    4.831909] systemd[1]: Listening on udev Kernel Socket.
[    4.847919] systemd[1]: Listening on User Database Manager Socket.
[    4.864067] systemd[1]: Condition check resulted in Huge Pages File System being skipped.
[    4.874719] systemd[1]: Mounting POSIX Message Queue File System...
[    4.899688] systemd[1]: Mounting Kernel Debug File System...
[    4.923626] systemd[1]: Mounting Kernel Trace File System...
[    4.948610] systemd[1]: Mounting Temporary Directory (/tmp)...
[    4.972836] systemd[1]: Starting Create list of static device nodes for the current kernel...
[    5.003768] systemd[1]: Starting Load Kernel Module configfs...
[    5.027714] systemd[1]: Starting Load Kernel Module drm...
[    5.051774] systemd[1]: Starting Load Kernel Module fuse...
[    5.070978] fuse: init (API version 7.32)
[    5.078660] systemd[1]: Starting RPC Bind...
[    5.095888] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
[    5.110662] systemd[1]: Starting Journal Service...
[    5.140559] systemd[1]: Starting Load Kernel Modules...
[    5.164417] systemd[1]: Starting Remount Root and Kernel File Systems...
[    5.193139] systemd[1]: Starting Coldplug All udev Devices...
[    5.201885] EXT4-fs (mmcblk0p2): re-mounted. Opts: (null)
[    5.219168] openvswitch: Open vSwitch switching datapath
[    5.225009] systemd[1]: Started RPC Bind.
[    5.244653] systemd[1]: Mounted POSIX Message Queue File System.
[    5.268262] systemd[1]: Started Journal Service.
[    5.471821] systemd-journald[141]: Received client request to flush runtime journal.
[    6.100732] nvidia_drm: loading out-of-tree module taints kernel.
[    6.110666] nvidia_drm: module license 'MIT' taints kernel.
[    6.118053] Disabling lock debugging due to kernel taint
[    8.083475] random: crng init done
[    8.085605] random: 7 urandom warning(s) missed due to ratelimiting
[    8.120246] FAT-fs (mmcblk0p1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.
[    8.486948] nvidia-nvlink: Nvlink Core is being initialized, major device number 245

[    8.495873] nvidia 0000:01:00.0: enabling device (0000 -> 0002)
[    8.501139] nvidia 0000:01:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=none:owns=none
[    8.563628] NVRM: loading NVIDIA UNIX aarch64 Kernel Module  465.31  Thu May 13 22:39:49 UTC 2021
[   10.799466] socfpga-dwmac ff800000.ethernet eth0: PHY [stmmac-0:04] driver [Micrel KSZ9031 Gigabit PHY] (irq=POLL)
[   10.827492] socfpga-dwmac ff800000.ethernet eth0: No Safety Features support found
[   10.833847] socfpga-dwmac ff800000.ethernet eth0: IEEE 1588-2008 Advanced Timestamp supported
[   10.871526] socfpga-dwmac ff800000.ethernet eth0: registered PTP clock
[   10.885652] socfpga-dwmac ff800000.ethernet eth0: configuring for phy/rgmii link mode
[   11.731107] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   11.747644] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   11.806853] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   11.813944] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   12.969140] socfpga-dwmac ff800000.ethernet eth0: Link is Up - 100Mbps/Full - flow control rx/tx
[   12.976676] IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
[   17.088170] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   17.094097] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   17.109509] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   17.115977] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   22.613549] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   22.619372] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   22.634186] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   22.640006] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   27.955914] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   27.961759] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
[   27.976567] NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
[   27.982440] NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
root@intel-socfpga-64:~# NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
c   
-sh: c: command not found
root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
cat /proc/iomem 
00000000-00ffffff : reserved
01000000-7fffffff : System RAM
  02000000-02f1ffff : Kernel code
  02f20000-032fffff : reserved
  03300000-0359ffff : Kernel data
  7a800000-7f7fffff : reserved
  7fa33000-7fa37fff : reserved
90000000-97ffffff : pcie@200000000
  90000000-917fffff : PCI Bus 0000:01
    90000000-90ffffff : 0000:01:00.0
      90000000-90ffffff : nvidia
    91000000-9107ffff : 0000:01:00.0
    91080000-910bffff : 0000:01:00.2
      91080000-910bffff : xhci-hcd
    910c0000-910cffff : 0000:01:00.2
    910d0000-910d3fff : 0000:01:00.1
    910d4000-910d4fff : 0000:01:00.3
a0000000-a01fffff : a0000000.pcie Hip
f8011100-f80111bf : soc:eccmgr sdr@f8011100
f9010000-f9017fff : a0000000.pcie Cra
f9018000-f901807f : f9018080.msi vector_slave
f9018080-f901808f : f9018080.msi csr
ff800000-ff801fff : ff800000.ethernet ethernet@ff800000
ff808000-ff808fff : ff808000.dwmmc0 dwmmc0@ff808000
ff8d2000-ff8d20ff : ff8d2000.spi spi@ff8d2000
ff900000-ff9fffff : ff8d2000.spi spi@ff8d2000
ffb00000-ffb3ffff : ffb00000.usb usb@ffb00000
ffc02000-ffc0201f : serial
ffc02900-ffc029ff : ffc02900.i2c i2c@ffc02900
ffc03300-ffc033ff : ffc03300.gpio gpio@ffc03300
ffd00200-ffd002ff : ffd00200.watchdog watchdog@ffd00200
ffd10000-ffd10fff : ffd10000.clock-controller clock-controller@ffd10000
ffd11000-ffd11fff : ffd11000.rstmgr rstmgr@ffd11000
ffda0000-ffda0fff : pdma@ffda0000
  ffda0000-ffda0fff : ffda0000.pdma pdma@ffda0000
ffe00000-ffefffff : ffe00000.sram sram@ffe00000
180000000-1ffffffff : System RAM
  1fb000000-1feffffff : reserved
  1ff10f000-1ff16efff : reserved
  1ff16f000-1ff76ffff : reserved
  1ff770000-1ff7e7fff : reserved
  1ff7ea000-1ff7ebfff : reserved
  1ff7ec000-1ff7ecfff : reserved
  1ff7ed000-1ff7effff : reserved
  1ff7f0000-1ffffffff : reserved
root@intel-socfpga-64:~# NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0

root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0

root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# 
root@intel-socfpga-64:~# NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
^C
root@intel-socfpga-64:~# ^C
root@intel-socfpga-64:~# NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
NVRM: GPU 0000:01:00.0: RmInitAdapter failed! (0x23:0xffff:643)
NVRM: GPU 0000:01:00.0: rm_init_adapter failed, device minor number 0
```

```
[lliu2@pek-lpgtest7302 CDStandard_20210512]$ cat /buildarea2/lliu2/2021cc/intel-socfpga-64/CDStandard_20210512/build/tmp-glibc/work-shared/intel-socfpga-64/kernel-source/arch/arm64/boot/dts/altera/socfpga_stratix10_socdk_pcie.dts 
// SPDX-License-Identifier: GPL-2.0-only
/*
 * Copyright Altera Corporation (C) 2019. All rights reserved.
 */

#include "socfpga_stratix10_socdk.dts"

/ {
	soc {
		bridge@80000000 {
		compatible = "simple-bus";
		reg = <0x80000000 0x20200000 0xf9000000 0x100000>;
		reg-names = "axi_h2f", "axi_h2f_lw";
		#address-cells = <0x2>;
		#size-cells = <0x1>;
		ranges = <0x0 0x0 0x80000000 0x40000 0x0 0x10000000 0x90000000 0x10000000 0x0 0x20000000 0xa0000000 0x200000 0x1 0x10000 0xf9010000 0x8000 0x1 0x18000 0xf9018000 0x80 0x1 0x18080 0xf9018080 0x10>;

			pcie_0_pcie_s10: pcie@200000000 {
				compatible = "altr,pcie-root-port-2.0";
				reg = <0x0 0x20000000 0x200000 0x0 0x10000000 0x10000000 0x1 0x10000 0x8000>;
				reg-names = "Hip", "Txs", "Cra";
				interrupt-parent = <&intc>;
				interrupts = <0x0 0x14 0x4>;
				interrupt-controller;
				#interrupt-cells = <0x1>;
				device_type = "pci";
				bus-range = <0x0 0xff>;
				ranges = <0x82000000 0x0 0x0 0x0 0x10000000 0x0 0x8000000>;
				msi-parent = <&pcie_0_msi_irq>;
				#address-cells = <0x3>;
				#size-cells = <0x2>;
				dma-coherent;
				interrupt-map-mask = <0x0 0x0 0x0 0x7>;
				interrupt-map = <0x0 0x0 0x0 0x1 &pcie_0_pcie_s10 0x1 0x0 0x0 0x0 0x2 &pcie_0_pcie_s10 0x2 0x0 0x0 0x0 0x3 &pcie_0_pcie_s10 0x3 0x0 0x0 0x0 0x4 &pcie_0_pcie_s10 0x4>;
				linux,phandle = <0x36>;
				phandle = <0x36>;
			};

			pcie_0_msi_irq: msi@10008080 {
				compatible = "altr,msi-1.0";
				reg = <0x1 0x18080 0x10 0x1 0x18000 0x80>;
				reg-names = "csr", "vector_slave";
				interrupt-parent = <&intc>;
				interrupts = <0x0 0x13 0x4>;
				msi-controller = <0x1>;
				num-vectors = <0x20>;
				linux,phandle = <0x35>;
				phandle = <0x35>;
			};
		};
	};
};
[lliu2@pek-lpgtest7302 CDStandard_20210512]$ 

[lliu2@pek-lpgtest7302 CDStandard_20210512]$ cat ~/socfpga_stratix10_socdk_pcie.dts_bk01 
// SPDX-License-Identifier: GPL-2.0-only
/*
 * Copyright Altera Corporation (C) 2019. All rights reserved.
 */

#include "socfpga_stratix10_socdk.dts"

/ {
	soc {
		s10_hps_bridges: bridge@80000000 {
			compatible = "simple-bus";
			reg = <0x80000000 0x20200000>,
				<0xf9000000 0x00100000>;
			reg-names = "axi_h2f", "axi_h2f_lw";
			#address-cells = <2>;
			#size-cells = <1>;
			ranges = <0x00000000 0x00000000 0x80000000 0x00040000>,
				<0x00000000 0x10000000 0x90000000 0x20000000>,
				<0x00000000 0x30000000 0xa0000000 0x00200000>,
				<0x00000001 0x00010000 0xf9010000 0x00008000>,
				<0x00000001 0x00018000 0xf9018000 0x00000080>,
				<0x00000001 0x00018080 0xf9018080 0x00000010>;

			pcie_0_pcie_s10: pcie@200000000 {
				compatible = "altr,pcie-root-port-2.0";
				reg = 	<0x00000000 0x30000000 0x00200000>,
					<0x00000000 0x10000000 0x20000000>,
					<0x00000001 0x00010000 0x00008000>;
				reg-names = "Hip", "Txs", "Cra";
				interrupt-parent = <&intc>;
				interrupts = <0 20 4>;
				interrupt-controller;
				#interrupt-cells = <1>;
				device_type = "pci";    /* embeddedsw.dts.params.device_type type STRING */
				bus-range = <0x00000000 0x000000ff>;
				ranges = <0x82000000 0x00000000 0x00000000 0x00000000 0x10000000 0x00000000 0x20000000>;
				msi-parent = <&pcie_0_msi_irq>;
				#address-cells = <3>;
				#size-cells = <2>;
				dma-coherent;
				interrupt-map-mask = <0 0 0 7>;
				interrupt-map = <0 0 0 1 &pcie_0_pcie_s10 1>,
						<0 0 0 2 &pcie_0_pcie_s10 2>,
						<0 0 0 3 &pcie_0_pcie_s10 3>,
						<0 0 0 4 &pcie_0_pcie_s10 4>;
			}; //end pcie@0x010000000 (pcie_0_pcie_s10)

			pcie_0_msi_irq: msi@10008080 {
				compatible = "altr,msi-1.0";
				reg = <0x00000001 0x00018080 0x00000010>,
					<0x00000001 0x00018000 0x00000080>;
				reg-names = "csr", "vector_slave";
				interrupt-parent = <&intc>;
				interrupts = <0 19 4>;
				msi-controller = <1>;   /* embeddedsw.dts.params.msi-controller type NUMBER */
				num-vectors = <32>;     /* embeddedsw.dts.params.num-vectors type NUMBER */
			}; //end msi@0x100008000 (pcie_0_msi_irq)
		};
	};
};
```



### References
* https://rocketboards.org/foswiki/pub/Projects/Stratix10PCIeRootPortWithMSI/S10_%20PCIe_RP_devcie_tree_descriptions.pdf
* https://rocketboards.org/foswiki/Projects/Stratix10PCIeRootPortWithMSI#AXI_454_to_ACE_45lite_Accelerator_Coherency_Port_Bridge
* https://rocketboards.org/foswiki/Projects/Stratix10PCIeRootPortWithMSI
* https://www.intel.com/content/www/us/en/programmable/products/stratix-series/s10/support/documentation.html
* https://elinux.org/Device_Tree_Usage
* https://community.nxp.com/t5/T-Series/ERROR-PCI-memory-allocation-BAR-Registers-on-T1042D4RDB-64B/m-p/1037715
* https://rocketboards.org/foswiki/Projects/Stratix10PCIeRootPortWithMSI
* https://releases.rocketboards.org/release/2021.04/pcie/s10_pcie/socfpga_stratix10_pcie.dtsi
* https://www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/ug/ug_s10_pcie_avmm.pdf
* https://www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/ug/ug_s10_pcie_avmm.pdf

### 3. How to verify the GPU works well on Wind River Linux?
