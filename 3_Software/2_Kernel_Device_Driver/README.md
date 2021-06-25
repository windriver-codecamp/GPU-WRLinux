# Build and install NVIDIA driver on Wind River Linux
## Setup steps
### 1. Build Wind River Linux Kernel and Rootfs

```
$ /lpg-build/cdc/fast_prod/WRLINUX_MASTER_WR/MASTER_WR_GIT/wrlinux-10/setup.sh --machines=intel-x86-64 --distros=wrlinux-graphics --templates=feature/chromium,feature/xfce,feature/linux-yocto-dev,feature/userspace-next,feature/toolchain-next --layers=meta-browser --dl-layers --accept-eula=yes
```
```
$ source environment-setup-x86_64-wrlinuxsdk-linux 
$ source oe-init-build-env
```
```
$ vi conf/local.conf # append the following contents in the file
```
```
IMAGE_INSTALL_append = " libjpeg-turbo v4l-utils apt autoconf autoconf-archive automake binutils bison build-compare ccache chrpath cmake createrepo-c dejagnu desktop-file-utils diffstat distcc dmidecode dnf dosfstools dpkg dwarfsrcfiles e2fsprogs elfutils expect file flex gcc gdb git glide gnu-config go intltool json-c libcomps libdnf libedit libmodulemd librepo libtool m4 make makedevs meson mtools nasm ninja opkg opkg-utils orc patch patchelf perl prelink pseudo quilt rpm rsync ruby run-postinsts squashfs-tools strace subversion unifdef xmlto util-linux python3-pip python3-numpy python3-pkg-resources python3-setuptools libgcc make xz libcrypto libffi liblzma libssl libtirpc libmpc mpfr libunwind kernel-devsrc libmpc-dev gcc-plugins ncurses"
```
```
EXTRA_IMAGE_FEATURES ?= "debug-tweaks tools-sdk tools-debug"

```
```
$ vi ../layers/oe-core/meta/recipes-graphics/xorg-xserver/xserver-xorg.inc # append the following contents in the file

```
```
OPENGL_PKGCONFIGS = "dri glx glamor dri3 xshmfence xinerama"
PACKAGECONFIG ??= "dga dri2 udev ${XORG_CRYPTO} \
                   ${@bb.utils.contains('DISTRO_FEATURES', 'opengl', '${OPENGL_PKGCONFIGS}', '', d)} \
                   ${@bb.utils.contains('DISTRO_FEATURES', 'opengl wayland', 'xwayland', '', d)} \
                   ${@bb.utils.contains('DISTRO_FEATURES', 'systemd', 'systemd systemd-logind', '', d)} \
"

PACKAGECONFIG[udev] = "--enable-config-udev,--disable-config-udev,udev"
PACKAGECONFIG[dga] = "--enable-dga,--disable-dga"
PACKAGECONFIG[dri] = "--enable-dri,--disable-dri,virtual/mesa"
PACKAGECONFIG[dri2] = "--enable-dri2,--disable-dri2"
# DRI3 requires xshmfence to also be enabled
PACKAGECONFIG[dri3] = "--enable-dri3,--disable-dri3"
PACKAGECONFIG[glx] = "--enable-glx,--disable-glx,virtual/libgl virtual/libx11"
PACKAGECONFIG[glamor] = "--enable-glamor,--disable-glamor,libepoxy virtual/libgbm,libegl"
PACKAGECONFIG[unwind] = "--enable-libunwind,--disable-libunwind,libunwind"
PACKAGECONFIG[xshmfence] = "--enable-xshmfence,--disable-xshmfence,libxshmfence"
PACKAGECONFIG[xmlto] = "--with-xmlto, --without-xmlto, xmlto-native docbook-xml-dtd4-native docbook-xsl-stylesheets-native"
PACKAGECONFIG[systemd-logind] = "--enable-systemd-logind=yes,--enable-systemd-logind=no,dbus,"
PACKAGECONFIG[systemd] = "--with-systemd-daemon,--without-systemd-daemon,systemd"
PACKAGECONFIG[xinerama] = "--enable-xinerama,--disable-xinerama"
```

```
$ bitbake wrlinux-image-std-sato

```

### 2. Deploy Wind River Linux kernel and rootfs to Intel-x86-64 host (Dell PC)

#### a. Deploy Kernel and rootfs to a SSD
```
$ dd if=wrlinux-image-std-sato-intel-x86-64.wic of=/dev/sdd
```
#### b. Resize the partition on the SSD
```
$ parted /dev/sdd
GNU Parted 3.3
Using /dev/sdd
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) p                                                                
Warning: Not all of the space available to /dev/sdd appears to be used, you can fix the GPT to use all of the space (an extra 227735932 blocks) or continue with the current setting? 
Fix/Ignore? Fix                                                           
Model: TO Exter nal USB 3.0 (scsi)
Disk /dev/sdd: 120GB
Sector size (logical/physical): 512B/4096B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    File system  Name      Flags
 1      1049kB  29.6MB  28.6MB  fat16        msdos     legacy_boot, msftdata
 2      30.4MB  3433MB  3403MB  ext4         platform

(parted) resize
resize      resizepart  
(parted) resizepart 
align-check  disk_toggle  mklabel      mktable      print        rescue       resizepart   select       toggle       version      
disk_set     help         mkpart       name         quit         resize       rm           set          unit         
(parted) resizepart 2
End?  [3433MB]? 100%                                                      
(parted) p                                                                
Model: TO Exter nal USB 3.0 (scsi)
Disk /dev/sdd: 120GB
Sector size (logical/physical): 512B/4096B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    File system  Name      Flags
 1      1049kB  29.6MB  28.6MB  fat16        msdos     legacy_boot, msftdata
 2      30.4MB  120GB   120GB   ext4         platform

(parted) p
Model: TO Exter nal USB 3.0 (scsi)
Disk /dev/sdd: 120GB
Sector size (logical/physical): 512B/4096B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    File system  Name      Flags
 1      1049kB  29.6MB  28.6MB  fat16        msdos     legacy_boot, msftdata
 2      30.4MB  120GB   120GB   ext4         platform

(parted) q                                                                
Information: You may need to update /etc/fstab.

$ resize2fs /dev/sdd2
resize2fs 1.45.5 (07-Jan-2020)
Resizing the filesystem on /dev/sdd2 to 29297777 (4k) blocks.
The filesystem on /dev/sdd2 is now 29297777 (4k) blocks long.

```

#### c. Install the SSD to the Intel-x86-64 host (Dell PC) and boot it up 

### 3. Download and compile NVIDIA Device Drivers on the Intel-x86-64 host (Dell PC)

#### a. SSH to the Intel-x86-64 host (Dell PC) from a Terminal Console on another host

#### b. Prepair kernel build environment on the Intel-x86-64 host (Dell PC)

```
$ cd /usr/src/kernel
```
```
$ make scripts prepare
```
```
root@intel-x86-64:/usr/src/kernel# make scripts prepare
...
scripts/Makefile.build:421: warning: overriding recipe for target 'modules.order'
Makefile:1451: warning: ignoring old recipe for target 'modules.order'
warning: Cannot use CONFIG_STACK_VALIDATION=y, please install libelf-dev, libelf-devel or elfutils-libelf-devel
...
```
Note: It's fine to skip the WARNING above.

#### c. Download the NVIDIA device driver
```
root@intel-x86-64:/2021cc# wget https://us.download.nvidia.com/XFree86/Linux-x86_64/460.73.01/NVIDIA-Linux-x86_64-460.73.01.run
```
#### d. Install NVIDIA Device Driver
```
$ systemctl stop lxdm
```
Disable default Nvidia driver used in kernel by running ./NVIDIA-Linux-x86_64-460.73.01.run at the first time.

```
$ ./NVIDIA-Linux-x86_64-460.73.01.run --kernel-source-path /usr/src/kernel
...
ERROR: The Nouveau kernel driver is currently in use by your system.  This driver is incompatible with the NVIDIA driver, and must be disabled before proceeding.  Please consult the NVIDIA driver     
         README and your Linux distribution's documentation for details on how to correctly disable the Nouveau kernel driver.

  For some distributions, Nouveau can be disabled by adding a file in the modprobe configuration directory.  Would you like nvidia-installer to attempt to create this modprobe file for you?             

                                                                   Yes                                                                No   
Select “Yes” and “reboot”

 One or more modprobe configuration files to disable Nouveau have been written.  For some distributions, this may be sufficient to disable Nouveau; other distributions may require modification of the  
  initial ramdisk.  Please reboot your system and attempt NVIDIA driver installation again.  Note if you later wish to re-enable Nouveau, you will need to delete these files:
  /etc/modprobe.d/nvidia-installer-disable-nouveau.conf
```  
Run the following commands again
```
$ systemctl stop lxdm
```
```
$ ./NVIDIA-Linux-x86_64-460.73.01.run --kernel-source-path /usr/src/kernel

Install NVIDIA's 32-bit compatibility libraries?
Select “No”

Would you like to run the nvidia-xconfig utility to automatically update your X configuration file so that the NVIDIA X driver will be used when you restart X?  Any pre-existing X configuration file
  will be backed up.  

Select “Yes”
```

Now we complete the driver installation.



## Issues

### At the first time of running "./NVIDIA-Linux-x86_64-460.73.01.run --kernel-source-path /usr/src/kernel", the following error will occured

```
ERROR: The Nouveau kernel driver is currently in use by your system.  This driver is incompatible with the NVIDIA driver, and must be disabled before proceeding.  Please consult the NVIDIA driver     
         README and your Linux distribution's documentation for details on how to correctly disable the Nouveau kernel driver.

  For some distributions, Nouveau can be disabled by adding a file in the modprobe configuration directory.  Would you like nvidia-installer to attempt to create this modprobe file for you?             

                                                                   Yes                                                                No   
Select “Yes” and “reboot”

 One or more modprobe configuration files to disable Nouveau have been written.  For some distributions, this may be sufficient to disable Nouveau; other distributions may require modification of the  
  initial ramdisk.  Please reboot your system and attempt NVIDIA driver installation again.  Note if you later wish to re-enable Nouveau, you will need to delete these files:
  /etc/modprobe.d/nvidia-installer-disable-nouveau.conf
  
```
#### Solution
Run the following commands again
```
$ systemctl stop lxdm
$ ./NVIDIA-Linux-x86_64-460.73.01.run --kernel-source-path /usr/src/kernel
```

### There are extra packages required to build NVIDIA driver
There will be various build errors if missing them.

#### Solution
Add the packages to the file of "conf/local.conf" during Wind River Linux project is building.

## FAQ
* What does the NVIDIA GPU related dmesg look like?
```
[    0.000000] Linux version 5.12.0-rc8-yoctodev-standard (oe-user@oe-host) (x86_64-wrs-linux-gcc (GCC) 10.2.0, GNU ld (GNU Binutils) 2.36.1.20210209) #1 SMP PREEMPT Sun Apr 25 06:53:32 UTC 2021
[    0.000000] Command line: BOOT_IMAGE=/bzImage root=PARTUUID=a092d5df-5b0c-4100-bc2b-ac93acc2003f rootwait rootfstype=ext4 console=ttyS0,115200 console=tty0
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000]   Hygon HygonGenuine
[    0.000000]   Centaur CentaurHauls
[    0.000000]   zhaoxin   Shanghai  
[    0.000000] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
...
[    2.012418] pci 0000:01:00.0: 32.000 Gb/s available PCIe bandwidth, limited by 2.5 GT/s PCIe x16 link at 0000:00:01.0 (capable of 126.016 Gb/s with 8.0 GT/s PCIe x16 link)
..
[    2.071440] pci 0000:00:01.0: PCI bridge to [bus 01]
[    2.075390] pci 0000:00:01.0:   bridge window [io  0xe000-0xefff]
[    2.080390] pci 0000:00:01.0:   bridge window [mem 0xf6000000-0xf70fffff]
[    2.085390] pci 0000:00:01.0:   bridge window [mem 0xe0000000-0xf20fffff 64bit pref]
...
[    2.176400] pci 0000:01:00.0: vgaarb: setting as boot VGA device
[    2.177388] pci 0000:01:00.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
[    2.188390] pci 0000:01:00.0: vgaarb: bridge control possible
[    2.192389] vgaarb: loaded
...
[    2.487916] pci 0000:00:01.0: PCI bridge to [bus 01]
[    2.491551] pci 0000:00:01.0:   bridge window [io  0xe000-0xefff]
[    2.496311] pci 0000:00:01.0:   bridge window [mem 0xf6000000-0xf70fffff]
[    2.501756] pci 0000:00:01.0:   bridge window [mem 0xe0000000-0xf20fffff 64bit pref]
...
[    2.617452] pci 0000:00:1a.0: quirk_usb_early_handoff+0x0/0x6d0 took 15836 usecs
[    2.640450] pci 0000:00:1d.0: quirk_usb_early_handoff+0x0/0x6d0 took 16535 usecs
[    2.646524] pci 0000:01:00.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
[    2.653542] pci 0000:01:00.1: D0 power state depends on 0000:01:00.0
[    2.658596] pci 0000:01:00.2: D0 power state depends on 0000:01:00.0
[    2.663677] pci 0000:01:00.2: enabling device (0000 -> 0002)
[    2.668078] pci 0000:01:00.3: D0 power state depends on 0000:01:00.0
...
[    4.661341] nvidia: loading out-of-tree module taints kernel.
[    4.667589] nvidia: module license 'NVIDIA' taints kernel.
...
[    4.726690] nvidia-nvlink: Nvlink Core is being initialized, major device number 244

[    4.726971] nvidia 0000:01:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=none:owns=io+mem
[    4.749233] random: rngd: uninitialized urandom read (16 bytes read)
[    4.772468] NVRM: loading NVIDIA UNIX x86_64 Kernel Module  460.73.01  Thu Apr  1 21:40:36 UTC 2021
[    4.809156] input: HDA NVidia HDMI/DP,pcm=3 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input5
[    4.821148] input: HDA NVidia HDMI/DP,pcm=7 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input6
[    4.821190] input: HDA NVidia HDMI/DP,pcm=8 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input7
[    4.821230] input: HDA NVidia HDMI/DP,pcm=9 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input8
[    4.821274] input: HDA NVidia HDMI/DP,pcm=10 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input9
[    4.821317] input: HDA NVidia HDMI/DP,pcm=11 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input10
[    4.895974] nvidia-modeset: Loading NVIDIA Kernel Mode Setting Driver for UNIX platforms  460.73.01  Thu Apr  1 21:32:31 UTC 2021
...
[    4.935155] [drm] [nvidia-drm] [GPU ID 0x00000100] Loading driver
[    4.983090] [drm] Initialized nvidia-drm 0.0.0 20160202 for 0000:01:00.0 on minor 0
...
[  325.546958] [drm] [nvidia-drm] [GPU ID 0x00000100] Unloading driver
[  325.563929] nvidia-modeset: Unloading
[  325.574106] nvidia-nvlink: Unregistered the Nvlink Core, major device number 244

```
* What's the DRM inside?

```
First scenario : you run a graphic application written with OpenInventor, without using to the X Window System, and you don't have a graphic card. The program flow would be quite similar to : 
Your application
  ↓ (uses functions of)
OpenInventor
  ↓ (calls functions declared by)
OpenGL
  ↓ (redirects function calls to implementation defined by)
Mesa
  ↓ (implemented OpenGL functions to be run on the CPU)
[Probably] Operating System rendering API
  ↓
3D Images on your screen
What happens here is called "software rendering" : the graphics command are not handled by any graphic hardware, but instead by your usual CPU, the processor that generally runs software. 
Second scenario : now imagine that with the same conditions as above, you have a graphic card. The flow would look more like this : 
Your application
  ↓ (uses functions of)
OpenInventor
  ↓ (calls functions declared by)
OpenGL
  ↓ (redirects function calls to implementation defined by)
Proprietary Drivers
  ↓ (converts OpenGL commands to GPU commands)
Graphic Card
  ↓
3D Images on your screen
What happens now is called "hardware acceleration", usually faster than the first scenario.
Third scenario : now let's introduce the X Window System flow, or at least how I think it is, based on the few Wikipedia lines I read.
Let's forget about the graphic hardware and API for a while. The flow should look like :
Your application (X Window System sees it as an "X Client")
  ↓ (sends requests defined by the X Window System Core Protocol)
X Server
  ↓ (convert your request to graphic commands)
[Probably] Operating System rendering API
  ↓
Windows or 2D images on your screen
Note that when using the X Window System, your screen and the computer from which you run your application may not be "directly" connected, but could be connected through a network.
Fourth scenario : suppose you want to add fancy 3D graphic renderings to your X Client application from the previous example. It seems to me that the X Window System is not originally able to do this, or at least it would necessitate much convoluted code to perform the equivalent of an OpenGL API function.
Luckily you can use GLX to add support for OpenGL commands to the system. You now have :
Your application
  ↓ (sends graphic requests defined by the "GLX extension to the X Protocol")
X Server with the GLX extension
  ↓ (convert your request to OpenGL commands)
OpenGL
  ↓ (redirects function calls to implementation defined by)
 ...
Now you can reconnect that last arrow to the one after "OpenGL" in the first scenario : you can get 3D images on your screen !
Finally about what I think understand of the DRI :
It seems to allow Mesa to have access to the GPU, so that would modify the flow of our first scenario into :
...
  ↓
Mesa
  ↓ (forwards OpenGL commands)
DRI
  ↓ (converts OpenGL commands to GPU commands)
Graphic Card
  ↓
3D Images on your screen
And it also seems to short-circuit the flow when using GLX, given the condition that its server and client are on the same computer, and that you have a GPU. In that case the graph of our fourth scenario would simply become :
Your application
  ↓ (sends graphic requests defined by the "GLX extension to the X Protocol")
DRI
  ↓ ("catches" OpenGL commands and converts them to GPU commands)
Graphic Card
  ↓
3D Images on your screen
That's it !
Now keep in mind that I'm not an expert in Unix environments, so my best advice is to study the documentation of each of those APIs to know precisely what they can do.
Combining the previous chart into a single one might make things easier to understand. I let this as an exercice to you!
```

## References

* https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#runfile-nouveau
* https://www.daimajiaoliu.com/daima/4794f5557100418
* https://softwareengineering.stackexchange.com/questions/164997/what-is-the-relationship-between-opengl-glx-dri-and-mesa3d
* https://en.wikipedia.org/wiki/X.Org_Server#/media/File:Schema_of_the_layers_of_the_graphical_user_interface.svg
* https://en.wikipedia.org/wiki/Direct_Rendering_Manager#/media/File:DRM_architecture.svg
* https://en.wikipedia.org/wiki/Direct_Rendering_Manager
* https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/inside-linux-graphics-paper.pdf




