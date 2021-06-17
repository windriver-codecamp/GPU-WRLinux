# How to build and deploy WR Linux Kernel and NVIDIA Driver?
## Setup steps
### Build Wind River Linux Kernel and Rootfs

```
$ /lpg-build/cdc/fast_prod/WRLINUX_MASTER_WR/MASTER_WR_GIT/wrlinux-10/setup.sh --machines=intel-x86-64 --distros=wrlinux-graphics --templates=feature/chromium,feature/xfce,feature/linux-yocto-dev,feature/userspace-next,feature/toolchain-next --layers=meta-browser --dl-layers --accept-eula=yes
$ source environment-setup-x86_64-wrlinuxsdk-linux 
$ source oe-init-build-env

$ vi conf/local.conf

IMAGE_INSTALL_append = " libjpeg-turbo v4l-utils apt autoconf autoconf-archive automake binutils bison build-compare ccache chrpath cmake createrepo-c dejagnu desktop-file-utils diffstat distcc dmidecode dnf dosfstools dpkg dwarfsrcfiles e2fsprogs elfutils expect file flex gcc gdb git glide gnu-config go intltool json-c libcomps libdnf libedit libmodulemd librepo libtool m4 make makedevs meson mtools nasm ninja opkg opkg-utils orc patch patchelf perl prelink pseudo quilt rpm rsync ruby run-postinsts squashfs-tools strace subversion unifdef xmlto util-linux python3-pip python3-numpy python3-pkg-resources python3-setuptools libgcc make xz libcrypto libffi liblzma libssl libtirpc libmpc mpfr libunwind kernel-devsrc libmpc-dev gcc-plugins ncurses"

EXTRA_IMAGE_FEATURES ?= "debug-tweaks tools-sdk tools-debug"

$ vi ../layers/oe-core/meta/recipes-graphics/xorg-xserver/xserver-xorg.inc

...

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


$ bitbake wrlinux-image-std-sato

```

## Deploy WR Linux kernel and rootfs to Intel-x86-64 host

### Deploy Kernel and rootfs to a SSD
```
$ dd if=wrlinux-image-std-sato-intel-x86-64.wic of=/dev/sdd
```
### Resize the partition on the SSD
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

### Install the SSD to the Intel-x86-64 host and boot it up 

## Download and compile NVIDIA Device Drivers on the Intel-x86-64 host

### Prepair kernel build environment
```
$ cd /usr/src/kernel

$ make scripts prepare

root@intel-x86-64:/usr/src/kernel# make scripts prepare
...
scripts/Makefile.build:421: warning: overriding recipe for target 'modules.order'
Makefile:1451: warning: ignoring old recipe for target 'modules.order'
warning: Cannot use CONFIG_STACK_VALIDATION=y, please install libelf-dev, libelf-devel or elfutils-libelf-devel
```
### Download NVIDIA Device Driver
```
root@intel-x86-64:/2021cc# wget https://us.download.nvidia.com/XFree86/Linux-x86_64/460.73.01/NVIDIA-Linux-x86_64-460.73.01.run
```
### Install NVIDIA Device Driver
```
$ systemctl stop lxdm

Disable default Nvidia driver used in kernel by running ./NVIDIA-Linux-x86_64-460.73.01.run firstly.


$ ./NVIDIA-Linux-x86_64-460.73.01.run --kernel-source-path /usr/src/kernel

ERROR: The Nouveau kernel driver is currently in use by your system.  This driver is incompatible with the NVIDIA driver, and must be disabled before proceeding.  Please consult the NVIDIA driver     
         README and your Linux distribution's documentation for details on how to correctly disable the Nouveau kernel driver.

  For some distributions, Nouveau can be disabled by adding a file in the modprobe configuration directory.  Would you like nvidia-installer to attempt to create this modprobe file for you?             

                                                                   Yes                                                                No   
Select “Yes” and “reboot”

 One or more modprobe configuration files to disable Nouveau have been written.  For some distributions, this may be sufficient to disable Nouveau; other distributions may require modification of the  
  initial ramdisk.  Please reboot your system and attempt NVIDIA driver installation again.  Note if you later wish to re-enable Nouveau, you will need to delete these files:
  /etc/modprobe.d/nvidia-installer-disable-nouveau.conf
  
Run the following commands again

$ systemctl stop lxdm


$ ./NVIDIA-Linux-x86_64-460.73.01.run --kernel-source-path /usr/src/kernel

Install NVIDIA's 32-bit compatibility libraries?
Select “No”

Would you like to run the nvidia-xconfig utility to automatically update your X configuration file so that the NVIDIA X driver will be used when you restart X?  Any pre-existing X configuration file
  will be backed up.  

Select “Yes”
```
## Issues

:bomb: At the first time of running "./NVIDIA-Linux-x86_64-460.73.01.run --kernel-source-path /usr/src/kernel", the following error will occured

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
### Solution
```
Run the following commands again

$ systemctl stop lxdm
$ ./NVIDIA-Linux-x86_64-460.73.01.run --kernel-source-path /usr/src/kernel
```

## FAQ
* What's the dmesg log?
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
[    0.000000] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
[    0.000000] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
[    0.000000] x86/fpu: Enabled xstate features 0x7, context size is 832 bytes, using 'standard' format.
[    0.000000] BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x0000000000057fff] usable
[    0.000000] BIOS-e820: [mem 0x0000000000058000-0x0000000000058fff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000059000-0x000000000009cfff] usable
[    0.000000] BIOS-e820: [mem 0x000000000009d000-0x000000000009efff] reserved
[    0.000000] BIOS-e820: [mem 0x000000000009f000-0x000000000009ffff] usable
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x00000000d20e3fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000d20e4000-0x00000000d20eafff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000d20eb000-0x00000000d2520fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000d2521000-0x00000000d29b3fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000d29b4000-0x00000000daee9fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000daeea000-0x00000000daffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000db000000-0x00000000db75efff] usable
[    0.000000] BIOS-e820: [mem 0x00000000db75f000-0x00000000db7fffff] type 20
[    0.000000] BIOS-e820: [mem 0x00000000db800000-0x00000000dbfadfff] usable
[    0.000000] BIOS-e820: [mem 0x00000000dbfae000-0x00000000dbffffff] ACPI data
[    0.000000] BIOS-e820: [mem 0x00000000dc000000-0x00000000dd71bfff] usable
[    0.000000] BIOS-e820: [mem 0x00000000dd71c000-0x00000000dd7fffff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000dd800000-0x00000000deb9bfff] usable
[    0.000000] BIOS-e820: [mem 0x00000000deb9c000-0x00000000deffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000f8000000-0x00000000fbffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fec00000-0x00000000fec00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed00000-0x00000000fed03fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed1c000-0x00000000fed1ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000ff000000-0x00000000ffffffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000100000000-0x000000041dffffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] efi: EFI v2.31 by American Megatrends
[    0.000000] efi: ACPI=0xdbfee000 ACPI 2.0=0xdbfee000 SMBIOS=0xf0000 
[    0.000000] SMBIOS 2.7 present.
[    0.000000] DMI: Dell Inc. OptiPlex 9020/03CPWF, BIOS A12 05/06/2015
[    0.000000] tsc: Fast TSC calibration using PIT
[    0.000000] tsc: Detected 3591.842 MHz processor
[    0.000034] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.000036] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.000042] last_pfn = 0x41e000 max_arch_pfn = 0x400000000
[    0.000124] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT  
[    0.000741] e820: update [mem 0xe0000000-0xffffffff] usable ==> reserved
[    0.000746] last_pfn = 0xdeb9c max_arch_pfn = 0x400000000
[    0.005887] check: Scanning 1 areas for low memory corruption
[    0.005892] Using GB pages for direct mapping
[    0.006688] Secure boot disabled
[    0.006689] ACPI: Early table checksum verification disabled
[    0.006691] ACPI: RSDP 0x00000000DBFEE000 000024 (v02 DELL  )
[    0.006694] ACPI: XSDT 0x00000000DBFEE090 00009C (v01 DELL   CBX3     01072009 AMI  00010013)
[    0.006698] ACPI: FACP 0x00000000DBFF9478 00010C (v05 DELL   CBX3     01072009 AMI  00010013)
[    0.006702] ACPI: DSDT 0x00000000DBFEE1B8 00B2B9 (v02 DELL   CBX3     00000014 INTL 20091112)
[    0.006704] ACPI: FACS 0x00000000DD7FE080 000040
[    0.006706] ACPI: APIC 0x00000000DBFF9588 000092 (v03 DELL   CBX3     01072009 AMI  00010013)
[    0.006708] ACPI: FPDT 0x00000000DBFF9620 000044 (v01 DELL   CBX3     01072009 AMI  00010013)
[    0.006710] ACPI: SLIC 0x00000000DBFF9668 000176 (v03 DELL   CBX3     01072009 MSFT 00010013)
[    0.006713] ACPI: LPIT 0x00000000DBFF97E0 00005C (v01 DELL   CBX3     00000000 AMI. 00000005)
[    0.006715] ACPI: SSDT 0x00000000DBFF9840 000539 (v01 PmRef  Cpu0Ist  00003000 INTL 20120711)
[    0.006717] ACPI: SSDT 0x00000000DBFF9D80 000AD8 (v01 PmRef  CpuPm    00003000 INTL 20120711)
[    0.006719] ACPI: SSDT 0x00000000DBFFA858 0001C7 (v01 PmRef  LakeTiny 00003000 INTL 20120711)
[    0.006722] ACPI: HPET 0x00000000DBFFAA20 000038 (v01 DELL   CBX3     01072009 AMI. 00000005)
[    0.006724] ACPI: SSDT 0x00000000DBFFAA58 00036D (v01 SataRe SataTabl 00001000 INTL 20120711)
[    0.006726] ACPI: MCFG 0x00000000DBFFADC8 00003C (v01 DELL   CBX3     01072009 MSFT 00000097)
[    0.006728] ACPI: SSDT 0x00000000DBFFAE08 0034D6 (v01 SaSsdt SaSsdt   00003000 INTL 20091112)
[    0.006730] ACPI: ASF! 0x00000000DBFFE2E0 0000A5 (v32 INTEL   HCG     00000001 TFSM 000F4240)
[    0.006733] ACPI: BGRT 0x00000000DBFFE388 000038 (v00 H\xb8?d??          01072009 AMI  00010013)
[    0.006735] ACPI: DMAR 0x00000000DBFFE3C0 000080 (v01 INTEL  HSW      00000001 INTL 00000001)
[    0.006737] ACPI: Reserving FACP table memory at [mem 0xdbff9478-0xdbff9583]
[    0.006738] ACPI: Reserving DSDT table memory at [mem 0xdbfee1b8-0xdbff9470]
[    0.006739] ACPI: Reserving FACS table memory at [mem 0xdd7fe080-0xdd7fe0bf]
[    0.006740] ACPI: Reserving APIC table memory at [mem 0xdbff9588-0xdbff9619]
[    0.006741] ACPI: Reserving FPDT table memory at [mem 0xdbff9620-0xdbff9663]
[    0.006741] ACPI: Reserving SLIC table memory at [mem 0xdbff9668-0xdbff97dd]
[    0.006742] ACPI: Reserving LPIT table memory at [mem 0xdbff97e0-0xdbff983b]
[    0.006743] ACPI: Reserving SSDT table memory at [mem 0xdbff9840-0xdbff9d78]
[    0.006744] ACPI: Reserving SSDT table memory at [mem 0xdbff9d80-0xdbffa857]
[    0.006745] ACPI: Reserving SSDT table memory at [mem 0xdbffa858-0xdbffaa1e]
[    0.006746] ACPI: Reserving HPET table memory at [mem 0xdbffaa20-0xdbffaa57]
[    0.006746] ACPI: Reserving SSDT table memory at [mem 0xdbffaa58-0xdbffadc4]
[    0.006747] ACPI: Reserving MCFG table memory at [mem 0xdbffadc8-0xdbffae03]
[    0.006748] ACPI: Reserving SSDT table memory at [mem 0xdbffae08-0xdbffe2dd]
[    0.006749] ACPI: Reserving ASF! table memory at [mem 0xdbffe2e0-0xdbffe384]
[    0.006750] ACPI: Reserving BGRT table memory at [mem 0xdbffe388-0xdbffe3bf]
[    0.006751] ACPI: Reserving DMAR table memory at [mem 0xdbffe3c0-0xdbffe43f]
[    0.006757] ACPI: Local APIC address 0xfee00000
[    0.006792] No NUMA configuration found
[    0.006793] Faking a node at [mem 0x0000000000000000-0x000000041dffffff]
[    0.006796] NODE_DATA(0) allocated [mem 0x41dffc000-0x41dffffff]
[    0.006815] Zone ranges:
[    0.006816]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
[    0.006817]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
[    0.006818]   Normal   [mem 0x0000000100000000-0x000000041dffffff]
[    0.006820] Movable zone start for each node
[    0.006820] Early memory node ranges
[    0.006821]   node   0: [mem 0x0000000000001000-0x0000000000057fff]
[    0.006822]   node   0: [mem 0x0000000000059000-0x000000000009cfff]
[    0.006823]   node   0: [mem 0x000000000009f000-0x000000000009ffff]
[    0.006824]   node   0: [mem 0x0000000000100000-0x00000000d20e3fff]
[    0.006825]   node   0: [mem 0x00000000d20eb000-0x00000000d2520fff]
[    0.006825]   node   0: [mem 0x00000000d29b4000-0x00000000daee9fff]
[    0.006826]   node   0: [mem 0x00000000db000000-0x00000000db75efff]
[    0.006827]   node   0: [mem 0x00000000db800000-0x00000000dbfadfff]
[    0.006827]   node   0: [mem 0x00000000dc000000-0x00000000dd71bfff]
[    0.006828]   node   0: [mem 0x00000000dd800000-0x00000000deb9bfff]
[    0.006829]   node   0: [mem 0x0000000100000000-0x000000041dffffff]
[    0.006830] Initmem setup node 0 [mem 0x0000000000001000-0x000000041dffffff]
[    0.006832] On node 0 totalpages: 4178865
[    0.006833]   DMA zone: 64 pages used for memmap
[    0.006834]   DMA zone: 23 pages reserved
[    0.006834]   DMA zone: 3996 pages, LIFO batch:0
[    0.007038]   DMA zone: 28772 pages in unavailable ranges
[    0.007039]   DMA32 zone: 14161 pages used for memmap
[    0.007040]   DMA32 zone: 906261 pages, LIFO batch:63
[    0.012457]   DMA32 zone: 7147 pages in unavailable ranges
[    0.012461]   Normal zone: 51072 pages used for memmap
[    0.012461]   Normal zone: 3268608 pages, LIFO batch:63
[    0.032260]   Normal zone: 8192 pages in unavailable ranges
[    0.032449] ACPI: PM-Timer IO Port: 0x1808
[    0.032451] ACPI: Local APIC address 0xfee00000
[    0.032455] ACPI: LAPIC_NMI (acpi_id[0xff] high edge lint[0x1])
[    0.032464] IOAPIC[0]: apic_id 8, version 32, address 0xfec00000, GSI 0-23
[    0.032466] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    0.032468] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 high level)
[    0.032469] ACPI: IRQ0 used by override.
[    0.032470] ACPI: IRQ9 used by override.
[    0.032471] Using ACPI (MADT) for SMP configuration information
[    0.032472] ACPI: HPET id: 0x8086a701 base: 0xfed00000
[    0.032479] e820: update [mem 0xd45c4000-0xd47ebfff] usable ==> reserved
[    0.032488] [Firmware Bug]: TSC_DEADLINE disabled due to Errata; please update microcode to version: 0x22 (or later)
[    0.032490] smpboot: Allowing 8 CPUs, 0 hotplug CPUs
[    0.032509] PM: hibernation: Registered nosave memory: [mem 0x00000000-0x00000fff]
[    0.032510] PM: hibernation: Registered nosave memory: [mem 0x00058000-0x00058fff]
[    0.032512] PM: hibernation: Registered nosave memory: [mem 0x0009d000-0x0009efff]
[    0.032514] PM: hibernation: Registered nosave memory: [mem 0x000a0000-0x000fffff]
[    0.032515] PM: hibernation: Registered nosave memory: [mem 0xd20e4000-0xd20eafff]
[    0.032517] PM: hibernation: Registered nosave memory: [mem 0xd2521000-0xd29b3fff]
[    0.032518] PM: hibernation: Registered nosave memory: [mem 0xd45c4000-0xd47ebfff]
[    0.032520] PM: hibernation: Registered nosave memory: [mem 0xdaeea000-0xdaffffff]
[    0.032521] PM: hibernation: Registered nosave memory: [mem 0xdb75f000-0xdb7fffff]
[    0.032523] PM: hibernation: Registered nosave memory: [mem 0xdbfae000-0xdbffffff]
[    0.032524] PM: hibernation: Registered nosave memory: [mem 0xdd71c000-0xdd7fffff]
[    0.032526] PM: hibernation: Registered nosave memory: [mem 0xdeb9c000-0xdeffffff]
[    0.032526] PM: hibernation: Registered nosave memory: [mem 0xdf000000-0xf7ffffff]
[    0.032527] PM: hibernation: Registered nosave memory: [mem 0xf8000000-0xfbffffff]
[    0.032528] PM: hibernation: Registered nosave memory: [mem 0xfc000000-0xfebfffff]
[    0.032528] PM: hibernation: Registered nosave memory: [mem 0xfec00000-0xfec00fff]
[    0.032529] PM: hibernation: Registered nosave memory: [mem 0xfec01000-0xfecfffff]
[    0.032530] PM: hibernation: Registered nosave memory: [mem 0xfed00000-0xfed03fff]
[    0.032530] PM: hibernation: Registered nosave memory: [mem 0xfed04000-0xfed1bfff]
[    0.032531] PM: hibernation: Registered nosave memory: [mem 0xfed1c000-0xfed1ffff]
[    0.032532] PM: hibernation: Registered nosave memory: [mem 0xfed20000-0xfedfffff]
[    0.032532] PM: hibernation: Registered nosave memory: [mem 0xfee00000-0xfee00fff]
[    0.032533] PM: hibernation: Registered nosave memory: [mem 0xfee01000-0xfeffffff]
[    0.032534] PM: hibernation: Registered nosave memory: [mem 0xff000000-0xffffffff]
[    0.032535] [mem 0xdf000000-0xf7ffffff] available for PCI devices
[    0.032537] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 1910969940391419 ns
[    0.032542] setup_percpu: NR_CPUS:256 nr_cpumask_bits:256 nr_cpu_ids:8 nr_node_ids:1
[    0.032699] percpu: Embedded 53 pages/cpu s178648 r8192 d30248 u262144
[    0.032704] pcpu-alloc: s178648 r8192 d30248 u262144 alloc=1*2097152
[    0.032706] pcpu-alloc: [0] 0 1 2 3 4 5 6 7 
[    0.032724] Built 1 zonelists, mobility grouping on.  Total pages: 4113545
[    0.032726] Policy zone: Normal
[    0.032727] Kernel command line: BOOT_IMAGE=/bzImage root=PARTUUID=a092d5df-5b0c-4100-bc2b-ac93acc2003f rootwait rootfstype=ext4 console=ttyS0,115200 console=tty0
[    0.033423] Dentry cache hash table entries: 2097152 (order: 12, 16777216 bytes, linear)
[    0.033759] Inode-cache hash table entries: 1048576 (order: 11, 8388608 bytes, linear)
[    0.033812] mem auto-init: stack:off, heap alloc:off, heap free:off
[    0.068921] Memory: 16213044K/16715460K available (16397K kernel code, 2317K rwdata, 5304K rodata, 1664K init, 1992K bss, 502156K reserved, 0K cma-reserved)
[    0.068956] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=8, Nodes=1
[    0.068963] Kernel/User page tables isolation: enabled
[    0.068975] ftrace: allocating 49923 entries in 196 pages
[    0.081299] ftrace: allocated 196 pages with 3 groups
[    0.081355] rcu: Preemptible hierarchical RCU implementation.
[    0.081356] rcu: 	RCU event tracing is enabled.
[    0.081356] rcu: 	RCU restricting CPUs from NR_CPUS=256 to nr_cpu_ids=8.
[    0.081358] 	Trampoline variant of Tasks RCU enabled.
[    0.081358] 	Rude variant of Tasks RCU enabled.
[    0.081359] 	Tracing variant of Tasks RCU enabled.
[    0.081359] rcu: RCU calculated value of scheduler-enlistment delay is 100 jiffies.
[    0.081360] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=8
[    0.083973] NR_IRQS: 16640, nr_irqs: 488, preallocated irqs: 16
[    0.084168] random: get_random_bytes called from start_kernel+0x392/0x55d with crng_init=0
[    0.084187] Console: colour dummy device 80x25
[    0.084354] printk: console [tty0] enabled
[    1.024915] printk: console [ttyS0] enabled
[    1.027780] ACPI: Core revision 20210105
[    1.030447] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 133484882848 ns
[    1.038234] APIC: Switch to symmetric I/O mode setup
[    1.041886] spurious 8259A interrupt: IRQ7.
[    1.041891] DMAR: Host address width 39
[    1.044420] DMAR: DRHD base: 0x000000fed90000 flags: 0x1
[    1.048417] DMAR: dmar0: reg_base_addr fed90000 ver 1:0 cap d2008c20660462 ecap f010da
[    1.054997] DMAR: RMRR base: 0x000000ded06000 end: 0x000000ded13fff
[    1.059940] DMAR-IR: IOAPIC id 8 under DRHD base  0xfed90000 IOMMU 0
[    1.064969] DMAR-IR: HPET id 0 under DRHD base 0xfed90000
[    1.069048] DMAR-IR: Queued invalidation will be enabled to support x2apic and Intr-remapping.
[    1.076528] DMAR-IR: Enabled IRQ remapping in x2apic mode
[    1.080593] x2apic enabled
[    1.081994] Switched APIC routing to cluster x2apic.
[    1.086019] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    1.095231] clocksource: tsc-early: mask: 0xffffffffffffffff max_cycles: 0x33c63887049, max_idle_ns: 440795303383 ns
[    1.104389] Calibrating delay loop (skipped), value calculated using timer frequency.. 7183.68 BogoMIPS (lpj=3591842)
[    1.105389] pid_max: default: 32768 minimum: 301
[    1.109400] LSM: Security Framework initializing
[    1.110435] Mount-cache hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    1.111413] Mountpoint-cache hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    1.112532] CPU0: Thermal monitoring enabled (TM1)
[    1.113407] process: using mwait in idle threads
[    1.114390] Last level iTLB entries: 4KB 1024, 2MB 1024, 4MB 1024
[    1.115389] Last level dTLB entries: 4KB 1024, 2MB 1024, 4MB 1024, 1GB 4
[    1.116389] Spectre V1 : Mitigation: usercopy/swapgs barriers and __user pointer sanitization
[    1.117389] Spectre V2 : Mitigation: Full generic retpoline
[    1.118389] Spectre V2 : Spectre v2 / SpectreRSB mitigation: Filling RSB on context switch
[    1.119389] Speculative Store Bypass: Vulnerable
[    1.120389] SRBDS: Vulnerable: No microcode
[    1.121389] MDS: Vulnerable: Clear CPU buffers attempted, no microcode
[    1.122534] Freeing SMP alternatives memory: 52K
[    1.123517] smpboot: Estimated ratio of average max frequency by base frequency (times 1024): 1080
[    1.226711] smpboot: CPU0: Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz (family: 0x6, model: 0x3c, stepping: 0x3)
[    1.227466] Performance Events: PEBS fmt2+, Haswell events, 16-deep LBR, full-width counters, Intel PMU driver.
[    1.228389] ... version:                3
[    1.229389] ... bit width:              48
[    1.230389] ... generic registers:      4
[    1.231390] ... value mask:             0000ffffffffffff
[    1.232389] ... max period:             00007fffffffffff
[    1.233389] ... fixed-purpose events:   3
[    1.234389] ... event mask:             000000070000000f
[    1.235473] rcu: Hierarchical SRCU implementation.
[    1.236573] smp: Bringing up secondary CPUs ...
[    1.238435] x86: Booting SMP configuration:
[    1.239389] .... node  #0, CPUs:      #1 #2 #3 #4
[    1.241835] MDS CPU bug present and SMT on, data leak possible. See https://www.kernel.org/doc/html/latest/admin-guide/hw-vuln/mds.html for more details.
[    1.243459]  #5 #6 #7
[    1.244755] smp: Brought up 1 node, 8 CPUs
[    1.246390] smpboot: Max logical packages: 1
[    1.247389] smpboot: Total of 8 processors activated (57469.47 BogoMIPS)
[    1.249798] devtmpfs: initialized
[    1.250473] PM: Registering ACPI NVS region [mem 0xd20e4000-0xd20eafff] (28672 bytes)
[    1.251391] PM: Registering ACPI NVS region [mem 0xdd71c000-0xdd7fffff] (933888 bytes)
[    1.252424] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 1911260446275000 ns
[    1.253391] futex hash table entries: 2048 (order: 5, 131072 bytes, linear)
[    1.254425] pinctrl core: initialized pinctrl subsystem
[    1.255485] NET: Registered protocol family 16
[    1.256485] thermal_sys: Registered thermal governor 'step_wise'
[    1.256486] thermal_sys: Registered thermal governor 'user_space'
[    1.257398] cpuidle: using governor menu
[    1.265412] ACPI FADT declares the system doesn't support PCIe ASPM, so disable it
[    1.271389] ACPI: bus type PCI registered
[    1.274389] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    1.279426] dca service started, version 1.12.1
[    1.282398] PCI: MMCONFIG for domain 0000 [bus 00-3f] at [mem 0xf8000000-0xfbffffff] (base 0xf8000000)
[    1.290390] PCI: MMCONFIG at [mem 0xf8000000-0xfbffffff] reserved in E820
[    1.295393] pmd_set_huge: Cannot satisfy [mem 0xf8000000-0xf8200000] with a huge-page mapping due to MTRR override.
[    1.304417] PCI: Using configuration type 1 for base access
[    1.309405] core: PMU erratum BJ122, BV98, HSD29 worked around, HT is on
[    1.314506] ENERGY_PERF_BIAS: Set to 'normal', was 'performance'
[    1.316538] Kprobes globally optimized
[    1.318405] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
[    1.324391] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    1.346744] raid6: avx2x4   gen() 37445 MB/s
[    1.365745] raid6: avx2x4   xor() 13341 MB/s
[    1.384744] raid6: avx2x2   gen() 36682 MB/s
[    1.403744] raid6: avx2x2   xor() 21382 MB/s
[    1.422744] raid6: avx2x1   gen() 32833 MB/s
[    1.441745] raid6: avx2x1   xor() 18341 MB/s
[    1.460744] raid6: sse2x4   gen() 20034 MB/s
[    1.479744] raid6: sse2x4   xor() 11440 MB/s
[    1.498745] raid6: sse2x2   gen() 19393 MB/s
[    1.517745] raid6: sse2x2   xor() 12339 MB/s
[    1.536745] raid6: sse2x1   gen() 15489 MB/s
[    1.555745] raid6: sse2x1   xor()  9976 MB/s
[    1.558390] raid6: using algorithm avx2x4 gen() 37445 MB/s
[    1.563389] raid6: .... xor() 13341 MB/s, rmw enabled
[    1.566389] raid6: using avx2x2 recovery algorithm
[    1.570423] ACPI: Added _OSI(Module Device)
[    1.573389] ACPI: Added _OSI(Processor Device)
[    1.576389] ACPI: Added _OSI(3.0 _SCP Extensions)
[    1.579389] ACPI: Added _OSI(Processor Aggregator Device)
[    1.583389] ACPI: Added _OSI(Linux-Dell-Video)
[    1.586389] ACPI: Added _OSI(Linux-Lenovo-NV-HDMI-Audio)
[    1.590389] ACPI: Added _OSI(Linux-HPI-Hybrid-Graphics)
[    1.599576] ACPI: 6 ACPI AML tables successfully acquired and loaded
[    1.605107] ACPI: [Firmware Bug]: BIOS _OSI(Linux) query ignored
[    1.610719] ACPI: Dynamic OEM Table Load:
[    1.613392] ACPI: SSDT 0xFFFF942880D19400 0003D3 (v01 PmRef  Cpu0Cst  00003001 INTL 20120711)
[    1.620654] ACPI: Dynamic OEM Table Load:
[    1.623393] ACPI: SSDT 0xFFFF942880D42800 0005AA (v01 PmRef  ApIst    00003000 INTL 20120711)
[    1.630873] ACPI: Dynamic OEM Table Load:
[    1.633392] ACPI: SSDT 0xFFFF942880D12000 000119 (v01 PmRef  ApCst    00003000 INTL 20120711)
[    1.642037] ACPI: Interpreter enabled
[    1.644408] ACPI: (supports S0 S3 S4 S5)
[    1.647394] ACPI: Using IOAPIC for interrupt routing
[    1.650407] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    1.658517] ACPI: Enabled 8 GPEs in block 00 to 3F
[    1.667724] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-3e])
[    1.672392] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI HPX-Type3]
[    1.680644] acpi PNP0A08:00: _OSC: OS now controls [PCIeHotplug PME PCIeCapability LTR]
[    1.687397] acpi PNP0A08:00: FADT indicates ASPM is unsupported, using BIOS configuration
[    1.694607] PCI host bridge to bus 0000:00
[    1.697391] pci_bus 0000:00: root bus resource [io  0x0000-0x0cf7 window]
[    1.702389] pci_bus 0000:00: root bus resource [io  0x0d00-0xffff window]
[    1.708389] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
[    1.714389] pci_bus 0000:00: root bus resource [mem 0x000c0000-0x000c3fff window]
[    1.720389] pci_bus 0000:00: root bus resource [mem 0x000c4000-0x000c7fff window]
[    1.726389] pci_bus 0000:00: root bus resource [mem 0x000c8000-0x000cbfff window]
[    1.732389] pci_bus 0000:00: root bus resource [mem 0x000cc000-0x000cffff window]
[    1.738389] pci_bus 0000:00: root bus resource [mem 0x000d0000-0x000d3fff window]
[    1.745389] pci_bus 0000:00: root bus resource [mem 0x000d4000-0x000d7fff window]
[    1.751389] pci_bus 0000:00: root bus resource [mem 0x000d8000-0x000dbfff window]
[    1.757389] pci_bus 0000:00: root bus resource [mem 0x000dc000-0x000dffff window]
[    1.763389] pci_bus 0000:00: root bus resource [mem 0xe0000000-0xfeafffff window]
[    1.769389] pci_bus 0000:00: root bus resource [bus 00-3e]
[    1.773397] pci 0000:00:00.0: [8086:0c00] type 00 class 0x060000
[    1.778448] pci 0000:00:01.0: [8086:0c01] type 01 class 0x060400
[    1.783417] pci 0000:00:01.0: PME# supported from D0 D3hot D3cold
[    1.788499] pci 0000:00:14.0: [8086:8c31] type 00 class 0x0c0330
[    1.792406] pci 0000:00:14.0: reg 0x10: [mem 0xf7120000-0xf712ffff 64bit]
[    1.798442] pci 0000:00:14.0: PME# supported from D3hot D3cold
[    1.802456] pci 0000:00:16.0: [8086:8c3a] type 00 class 0x078000
[    1.807403] pci 0000:00:16.0: reg 0x10: [mem 0xf713c000-0xf713c00f 64bit]
[    1.813442] pci 0000:00:16.0: PME# supported from D0 D3hot D3cold
[    1.817441] pci 0000:00:16.3: [8086:8c3d] type 00 class 0x070002
[    1.822399] pci 0000:00:16.3: reg 0x10: [io  0xf0a0-0xf0a7]
[    1.826394] pci 0000:00:16.3: reg 0x14: [mem 0xf713a000-0xf713afff]
[    1.831484] pci 0000:00:19.0: [8086:153a] type 00 class 0x020000
[    1.836400] pci 0000:00:19.0: reg 0x10: [mem 0xf7100000-0xf711ffff]
[    1.841395] pci 0000:00:19.0: reg 0x14: [mem 0xf7139000-0xf7139fff]
[    1.846395] pci 0000:00:19.0: reg 0x18: [io  0xf040-0xf05f]
[    1.850415] pci 0000:00:19.0: PME# supported from D0 D3hot D3cold
[    1.855450] pci 0000:00:1a.0: [8086:8c2d] type 00 class 0x0c0320
[    1.860401] pci 0000:00:1a.0: reg 0x10: [mem 0xf7138000-0xf71383ff]
[    1.865461] pci 0000:00:1a.0: PME# supported from D0 D3hot D3cold
[    1.869452] pci 0000:00:1b.0: [8086:8c20] type 00 class 0x040300
[    1.874402] pci 0000:00:1b.0: reg 0x10: [mem 0xf7130000-0xf7133fff 64bit]
[    1.880450] pci 0000:00:1b.0: PME# supported from D0 D3hot D3cold
[    1.884448] pci 0000:00:1c.0: [8086:8c10] type 01 class 0x060400
[    1.889453] pci 0000:00:1c.0: PME# supported from D0 D3hot D3cold
[    1.894483] pci 0000:00:1c.1: [8086:8c12] type 01 class 0x060400
[    1.899454] pci 0000:00:1c.1: PME# supported from D0 D3hot D3cold
[    1.904487] pci 0000:00:1d.0: [8086:8c26] type 00 class 0x0c0320
[    1.908402] pci 0000:00:1d.0: reg 0x10: [mem 0xf7137000-0xf71373ff]
[    1.913461] pci 0000:00:1d.0: PME# supported from D0 D3hot D3cold
[    1.918450] pci 0000:00:1f.0: [8086:8c4e] type 00 class 0x060100
[    1.923532] pci 0000:00:1f.2: [8086:8c02] type 00 class 0x010601
[    1.928398] pci 0000:00:1f.2: reg 0x10: [io  0xf090-0xf097]
[    1.932394] pci 0000:00:1f.2: reg 0x14: [io  0xf080-0xf083]
[    1.936394] pci 0000:00:1f.2: reg 0x18: [io  0xf070-0xf077]
[    1.940394] pci 0000:00:1f.2: reg 0x1c: [io  0xf060-0xf063]
[    1.945394] pci 0000:00:1f.2: reg 0x20: [io  0xf020-0xf03f]
[    1.949394] pci 0000:00:1f.2: reg 0x24: [mem 0xf7136000-0xf71367ff]
[    1.954419] pci 0000:00:1f.2: PME# supported from D3hot
[    1.958443] pci 0000:00:1f.3: [8086:8c22] type 00 class 0x0c0500
[    1.962402] pci 0000:00:1f.3: reg 0x10: [mem 0xf7135000-0xf71350ff 64bit]
[    1.968405] pci 0000:00:1f.3: reg 0x20: [io  0xf000-0xf01f]
[    1.972482] pci 0000:01:00.0: [10de:2187] type 00 class 0x030000
[    1.977399] pci 0000:01:00.0: reg 0x10: [mem 0xf6000000-0xf6ffffff]
[    1.982397] pci 0000:01:00.0: reg 0x14: [mem 0xe0000000-0xefffffff 64bit pref]
[    1.988396] pci 0000:01:00.0: reg 0x1c: [mem 0xf0000000-0xf1ffffff 64bit pref]
[    1.994394] pci 0000:01:00.0: reg 0x24: [io  0xe000-0xe07f]
[    1.998394] pci 0000:01:00.0: reg 0x30: [mem 0xf7000000-0xf707ffff pref]
[    2.003403] pci 0000:01:00.0: BAR 1: assigned to efifb
[    2.007409] pci 0000:01:00.0: PME# supported from D0 D3hot D3cold
[    2.012418] pci 0000:01:00.0: 32.000 Gb/s available PCIe bandwidth, limited by 2.5 GT/s PCIe x16 link at 0000:00:01.0 (capable of 126.016 Gb/s with 8.0 GT/s PCIe x16 link)
[    2.026427] pci 0000:01:00.1: [10de:1aeb] type 00 class 0x040300
[    2.031398] pci 0000:01:00.1: reg 0x10: [mem 0xf7080000-0xf7083fff]
[    2.035477] pci 0000:01:00.2: [10de:1aec] type 00 class 0x0c0330
[    2.040400] pci 0000:01:00.2: reg 0x10: [mem 0xf2000000-0xf203ffff 64bit pref]
[    2.046399] pci 0000:01:00.2: reg 0x1c: [mem 0xf2040000-0xf204ffff 64bit pref]
[    2.052428] pci 0000:01:00.2: PME# supported from D0 D3hot D3cold
[    2.057426] pci 0000:01:00.3: [10de:1aed] type 00 class 0x0c8000
[    2.062397] pci 0000:01:00.3: reg 0x10: [mem 0xf7084000-0xf7084fff]
[    2.066442] pci 0000:01:00.3: PME# supported from D0 D3hot D3cold
[    2.071440] pci 0000:00:01.0: PCI bridge to [bus 01]
[    2.075390] pci 0000:00:01.0:   bridge window [io  0xe000-0xefff]
[    2.080390] pci 0000:00:01.0:   bridge window [mem 0xf6000000-0xf70fffff]
[    2.085390] pci 0000:00:01.0:   bridge window [mem 0xe0000000-0xf20fffff 64bit pref]
[    2.092430] acpiphp: Slot [1] registered
[    2.094393] pci 0000:00:1c.0: PCI bridge to [bus 02]
[    2.098457] pci 0000:03:00.0: [104c:8240] type 01 class 0x060400
[    2.103530] pci 0000:03:00.0: supports D1 D2
[    2.106467] pci 0000:00:1c.1: PCI bridge to [bus 03-04]
[    2.110444] pci_bus 0000:04: extended config space not accessible
[    2.114468] pci 0000:03:00.0: PCI bridge to [bus 04]
[    2.118870] ACPI: PCI Interrupt Link [LNKA] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
[    2.125420] ACPI: PCI Interrupt Link [LNKB] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
[    2.132418] ACPI: PCI Interrupt Link [LNKC] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
[    2.139418] ACPI: PCI Interrupt Link [LNKD] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
[    2.145420] ACPI: PCI Interrupt Link [LNKE] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
[    2.152418] ACPI: PCI Interrupt Link [LNKF] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
[    2.159419] ACPI: PCI Interrupt Link [LNKG] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
[    2.165418] ACPI: PCI Interrupt Link [LNKH] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
[    2.172521] iommu: Default domain type: Translated 
[    2.176400] pci 0000:01:00.0: vgaarb: setting as boot VGA device
[    2.177388] pci 0000:01:00.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
[    2.188390] pci 0000:01:00.0: vgaarb: bridge control possible
[    2.192389] vgaarb: loaded
[    2.194420] SCSI subsystem initialized
[    2.196394] libata version 3.00 loaded.
[    2.196408] ACPI: bus type USB registered
[    2.199397] usbcore: registered new interface driver usbfs
[    2.203393] usbcore: registered new interface driver hub
[    2.207392] usbcore: registered new device driver usb
[    2.211402] pps_core: LinuxPPS API ver. 1 registered
[    2.214389] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    2.222391] PTP clock support registered
[    2.225398] EDAC MC: Ver: 3.0.0
[    2.226440] EDAC DEBUG: edac_mc_sysfs_init: device mc created
[    2.226444] Registered efivars operations
[    2.229409] Advanced Linux Sound Architecture Driver Initialized.
[    2.234473] Bluetooth: Core ver 2.22
[    2.236392] NET: Registered protocol family 31
[    2.239389] Bluetooth: HCI device and connection manager initialized
[    2.244389] Bluetooth: HCI socket layer initialized
[    2.248389] Bluetooth: L2CAP socket layer initialized
[    2.252390] Bluetooth: SCO socket layer initialized
[    2.255400] PCI: Using ACPI for IRQ routing
[    2.259572] PCI: pci_cache_line_size set to 64 bytes
[    2.259620] e820: reserve RAM buffer [mem 0x00058000-0x0005ffff]
[    2.259621] e820: reserve RAM buffer [mem 0x0009d000-0x0009ffff]
[    2.259622] e820: reserve RAM buffer [mem 0xd20e4000-0xd3ffffff]
[    2.259623] e820: reserve RAM buffer [mem 0xd2521000-0xd3ffffff]
[    2.259624] e820: reserve RAM buffer [mem 0xd45c4000-0xd7ffffff]
[    2.259624] e820: reserve RAM buffer [mem 0xdaeea000-0xdbffffff]
[    2.259625] e820: reserve RAM buffer [mem 0xdb75f000-0xdbffffff]
[    2.259626] e820: reserve RAM buffer [mem 0xdbfae000-0xdbffffff]
[    2.259627] e820: reserve RAM buffer [mem 0xdd71c000-0xdfffffff]
[    2.259627] e820: reserve RAM buffer [mem 0xdeb9c000-0xdfffffff]
[    2.259628] e820: reserve RAM buffer [mem 0x41e000000-0x41fffffff]
[    2.259639] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0, 0, 0, 0, 0, 0
[    2.264389] hpet0: 8 comparators, 64-bit 14.318180 MHz counter
[    2.271405] clocksource: Switched to clocksource tsc-early
[    2.282752] pnp: PnP ACPI init
[    2.284546] system 00:00: [mem 0xfed40000-0xfed44fff] has been reserved
[    2.289827] system 00:00: Plug and Play ACPI device, IDs PNP0c01 (active)
[    2.289930] system 00:01: [io  0x0680-0x069f] has been reserved
[    2.294518] system 00:01: [io  0xffff] has been reserved
[    2.298498] system 00:01: [io  0xffff] has been reserved
[    2.302481] system 00:01: [io  0xffff] has been reserved
[    2.306460] system 00:01: [io  0x1c00-0x1cfe] has been reserved
[    2.311044] system 00:01: [io  0x1d00-0x1dfe] has been reserved
[    2.315628] system 00:01: [io  0x1e00-0x1efe] has been reserved
[    2.320213] system 00:01: [io  0x1f00-0x1ffe] has been reserved
[    2.324798] system 00:01: [io  0x1800-0x18fe] has been reserved
[    2.329384] system 00:01: [io  0x164e-0x164f] has been reserved
[    2.333971] system 00:01: Plug and Play ACPI device, IDs PNP0c02 (active)
[    2.333986] pnp 00:02: Plug and Play ACPI device, IDs PNP0b00 (active)
[    2.334015] system 00:03: [io  0x1854-0x1857] has been reserved
[    2.338603] system 00:03: Plug and Play ACPI device, IDs INT3f0d PNP0c02 (active)
[    2.338662] system 00:04: [io  0x0a00-0x0a0f] has been reserved
[    2.343249] system 00:04: Plug and Play ACPI device, IDs PNP0c02 (active)
[    2.343279] system 00:05: [io  0x04d0-0x04d1] has been reserved
[    2.347868] system 00:05: Plug and Play ACPI device, IDs PNP0c02 (active)
[    2.348193] pnp 00:06: [dma 0 disabled]
[    2.348218] pnp 00:06: Plug and Play ACPI device, IDs PNP0501 (active)
[    2.348466] system 00:07: [mem 0xfed1c000-0xfed1ffff] has been reserved
[    2.353741] system 00:07: [mem 0xfed10000-0xfed17fff] has been reserved
[    2.359014] system 00:07: [mem 0xfed18000-0xfed18fff] has been reserved
[    2.364288] system 00:07: [mem 0xfed19000-0xfed19fff] has been reserved
[    2.369561] system 00:07: [mem 0xf8000000-0xfbffffff] has been reserved
[    2.374836] system 00:07: [mem 0xfed20000-0xfed3ffff] has been reserved
[    2.380109] system 00:07: [mem 0xfed90000-0xfed93fff] could not be reserved
[    2.385729] system 00:07: [mem 0xfed45000-0xfed8ffff] has been reserved
[    2.391004] system 00:07: [mem 0xff000000-0xffffffff] has been reserved
[    2.396278] system 00:07: [mem 0xfee00000-0xfeefffff] could not be reserved
[    2.401896] system 00:07: [mem 0xf7fee000-0xf7feefff] has been reserved
[    2.407168] system 00:07: [mem 0xf7fd0000-0xf7fdffff] has been reserved
[    2.412448] system 00:07: Plug and Play ACPI device, IDs PNP0c02 (active)
[    2.412576] pnp: PnP ACPI: found 8 devices
[    2.420691] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[    2.428240] NET: Registered protocol family 2
[    2.431365] tcp_listen_portaddr_hash hash table entries: 8192 (order: 5, 131072 bytes, linear)
[    2.438644] TCP established hash table entries: 131072 (order: 8, 1048576 bytes, linear)
[    2.445481] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes, linear)
[    2.451629] TCP: Hash tables configured (established 131072 bind 65536)
[    2.456922] UDP hash table entries: 8192 (order: 6, 262144 bytes, linear)
[    2.462397] UDP-Lite hash table entries: 8192 (order: 6, 262144 bytes, linear)
[    2.468379] NET: Registered protocol family 1
[    2.471470] RPC: Registered named UNIX socket transport module.
[    2.476056] RPC: Registered udp transport module.
[    2.479434] RPC: Registered tcp transport module.
[    2.482809] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    2.487916] pci 0000:00:01.0: PCI bridge to [bus 01]
[    2.491551] pci 0000:00:01.0:   bridge window [io  0xe000-0xefff]
[    2.496311] pci 0000:00:01.0:   bridge window [mem 0xf6000000-0xf70fffff]
[    2.501756] pci 0000:00:01.0:   bridge window [mem 0xe0000000-0xf20fffff 64bit pref]
[    2.508153] pci 0000:00:1c.0: PCI bridge to [bus 02]
[    2.511797] pci 0000:03:00.0: PCI bridge to [bus 04]
[    2.515449] pci 0000:00:1c.1: PCI bridge to [bus 03-04]
[    2.519350] pci_bus 0000:00: resource 4 [io  0x0000-0x0cf7 window]
[    2.524195] pci_bus 0000:00: resource 5 [io  0x0d00-0xffff window]
[    2.529037] pci_bus 0000:00: resource 6 [mem 0x000a0000-0x000bffff window]
[    2.534571] pci_bus 0000:00: resource 7 [mem 0x000c0000-0x000c3fff window]
[    2.540104] pci_bus 0000:00: resource 8 [mem 0x000c4000-0x000c7fff window]
[    2.545637] pci_bus 0000:00: resource 9 [mem 0x000c8000-0x000cbfff window]
[    2.551169] pci_bus 0000:00: resource 10 [mem 0x000cc000-0x000cffff window]
[    2.556785] pci_bus 0000:00: resource 11 [mem 0x000d0000-0x000d3fff window]
[    2.562406] pci_bus 0000:00: resource 12 [mem 0x000d4000-0x000d7fff window]
[    2.568023] pci_bus 0000:00: resource 13 [mem 0x000d8000-0x000dbfff window]
[    2.573642] pci_bus 0000:00: resource 14 [mem 0x000dc000-0x000dffff window]
[    2.579261] pci_bus 0000:00: resource 15 [mem 0xe0000000-0xfeafffff window]
[    2.584882] pci_bus 0000:01: resource 0 [io  0xe000-0xefff]
[    2.589120] pci_bus 0000:01: resource 1 [mem 0xf6000000-0xf70fffff]
[    2.594049] pci_bus 0000:01: resource 2 [mem 0xe0000000-0xf20fffff 64bit pref]
[    2.617452] pci 0000:00:1a.0: quirk_usb_early_handoff+0x0/0x6d0 took 15836 usecs
[    2.640450] pci 0000:00:1d.0: quirk_usb_early_handoff+0x0/0x6d0 took 16535 usecs
[    2.646524] pci 0000:01:00.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
[    2.653542] pci 0000:01:00.1: D0 power state depends on 0000:01:00.0
[    2.658596] pci 0000:01:00.2: D0 power state depends on 0000:01:00.0
[    2.663677] pci 0000:01:00.2: enabling device (0000 -> 0002)
[    2.668078] pci 0000:01:00.3: D0 power state depends on 0000:01:00.0
[    2.673126] PCI: CLS 64 bytes, default 64
[    2.675844] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
[    2.680946] software IO TLB: mapped [mem 0x00000000cc13c000-0x00000000d013c000] (64MB)
[    2.687568] RAPL PMU: API unit is 2^-32 Joules, 3 fixed counters, 655360 ms ovfl timer
[    2.694140] RAPL PMU: hw unit of domain pp0-core 2^-14 Joules
[    2.698552] RAPL PMU: hw unit of domain package 2^-14 Joules
[    2.702876] RAPL PMU: hw unit of domain dram 2^-14 Joules
[    2.707368] check: Scanning for low memory corruption every 60 seconds
[    2.712823] Initialise system trusted keyrings
[    2.715965] workingset: timestamp_bits=40 max_order=22 bucket_order=0
[    2.722029] NFS: Registering the id_resolver key type
[    2.725754] Key type id_resolver registered
[    2.728615] Key type id_legacy registered
[    2.731384] Key type cifs.idmap registered
[    2.741715] xor: automatically using best checksumming function   avx       
[    2.747427] async_tx: api initialized (async)
[    2.750459] Key type asymmetric registered
[    2.753234] Asymmetric key parser 'x509' registered
[    2.756785] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 249)
[    2.762838] io scheduler mq-deadline registered
[    2.766041] io scheduler kyber registered
[    2.768834] pcieport 0000:00:01.0: PME: Signaling with IRQ 25
[    2.773357] pcieport 0000:00:1c.0: PME: Signaling with IRQ 26
[    2.777886] pcieport 0000:00:1c.1: PME: Signaling with IRQ 27
[    2.782368] efifb: probing for efifb
[    2.784644] efifb: framebuffer at 0xe0000000, using 34560k, total 34560k
[    2.790006] efifb: mode is 3840x2160x32, linelength=16384, pages=1
[    2.794850] efifb: scrolling: redraw
[    2.797106] efifb: Truecolor: size=8:8:8:8, shift=24:16:8:0
[    2.813174] Console: switching to colour frame buffer device 480x135
[    2.829987] fb0: EFI VGA frame buffer device
[    2.833241] input: Power Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0C:00/input/input0
[    2.841423] ACPI: button: Power Button [PWRB]
[    2.844493] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input1
[    2.850648] ACPI: button: Power Button [PWRF]
[    2.853887] ioatdma: Intel(R) QuickData Technology Driver 5.00
[    2.858514] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
[    2.863605] 00:06: ttyS0 at I/O 0x3f8 (irq = 4, base_baud = 115200) is a 16550A
[    2.870055] serial 0000:00:16.3: enabling device (0000 -> 0003)
[    2.874847] 0000:00:16.3: ttyS1 at I/O 0xf0a0 (irq = 19, base_baud = 115200) is a 16550A
[    2.881852] Linux agpgart interface v0.103
[    2.885973] brd: module loaded
[    2.888795] loop: module loaded
[    2.890659] isci: Intel(R) C600 SAS Controller Driver - version 1.2.0
[    2.895781] mpt3sas version 37.100.00.00 loaded
[    2.899191] ahci 0000:00:1f.2: version 3.0
[    2.899289] ahci 0000:00:1f.2: AHCI 0001.0300 32 slots 6 ports 6 Gbps 0x1 impl SATA mode
[    2.906050] ahci 0000:00:1f.2: flags: 64bit ncq pm led clo pio slum part ems apst 
[    2.912681] scsi host0: ahci
[    2.914363] scsi host1: ahci
[    2.916027] scsi host2: ahci
[    2.917677] scsi host3: ahci
[    2.919324] scsi host4: ahci
[    2.920972] scsi host5: ahci
[    2.922575] ata1: SATA max UDMA/133 abar m2048@0xf7136000 port 0xf7136100 irq 28
[    2.928643] ata2: DUMMY
[    2.929782] ata3: DUMMY
[    2.930919] ata4: DUMMY
[    2.932056] ata5: DUMMY
[    2.933191] ata6: DUMMY
[    2.934370] e100: Intel(R) PRO/100 Network Driver
[    2.937753] e100: Copyright(c) 1999-2006 Intel Corporation
[    2.941922] e1000: Intel(R) PRO/1000 Network Driver
[    2.945479] e1000: Copyright (c) 1999-2006 Intel Corporation.
[    2.949909] e1000e: Intel(R) PRO/1000 Network Driver
[    2.953551] e1000e: Copyright(c) 1999 - 2015 Intel Corporation.
[    2.958221] e1000e 0000:00:19.0: Interrupt Throttling Rate (ints/sec) set to dynamic conservative mode
[    3.040947] e1000e 0000:00:19.0 0000:00:19.0 (uninitialized): registered PHC clock
[    3.115910] e1000e 0000:00:19.0 eth0: (PCI Express:2.5GT/s:Width x1) 64:00:6a:66:41:bc
[    3.122509] e1000e 0000:00:19.0 eth0: Intel(R) PRO/1000 Network Connection
[    3.128102] e1000e 0000:00:19.0 eth0: MAC: 11, PHY: 12, PBA No: FFFFFF-0FF
[    3.133669] igb: Intel(R) Gigabit Ethernet Network Driver
[    3.137743] igb: Copyright (c) 2007-2014 Intel Corporation.
[    3.142003] ixgbe: Intel(R) 10 Gigabit PCI Express Network Driver
[    3.146772] ixgbe: Copyright (c) 1999-2016 Intel Corporation.
[    3.151355] ixgb: Intel(R) PRO/10GbE Network Driver
[    3.154918] ixgb: Copyright (c) 1999-2008 Intel Corporation.
[    3.159263] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    3.164461] ehci-pci: EHCI PCI platform driver
[    3.167688] ehci-pci 0000:00:1a.0: EHCI Host Controller
[    3.171595] ehci-pci 0000:00:1a.0: new USB bus registered, assigned bus number 1
[    3.177670] ehci-pci 0000:00:1a.0: debug port 2
[    3.184782] ehci-pci 0000:00:1a.0: irq 16, io mem 0xf7138000
[    3.195460] ehci-pci 0000:00:1a.0: USB 2.0 started, EHCI 1.00
[    3.200101] hub 1-0:1.0: USB hub found
[    3.202542] hub 1-0:1.0: 3 ports detected
[    3.205440] ehci-pci 0000:00:1d.0: EHCI Host Controller
[    3.209348] ehci-pci 0000:00:1d.0: new USB bus registered, assigned bus number 2
[    3.215420] ehci-pci 0000:00:1d.0: debug port 2
[    3.222529] ehci-pci 0000:00:1d.0: irq 23, io mem 0xf7137000
[    3.233460] ehci-pci 0000:00:1d.0: USB 2.0 started, EHCI 1.00
[    3.238091] hub 2-0:1.0: USB hub found
[    3.240531] hub 2-0:1.0: 3 ports detected
[    3.243349] uhci_hcd: USB Universal Host Controller Interface driver
[    3.244897] ata1: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[    3.248494] xhci_hcd 0000:00:14.0: xHCI Host Controller
[    3.253439] ata1.00: ATA-11: KINGSTON SA400S37120G, SBFKB1D1, max UDMA/133
[    3.257152] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 3
[    3.262699] ata1.00: 234441648 sectors, multi 16: LBA48 NCQ (depth 32), AA
[    3.269846] xhci_hcd 0000:00:14.0: hcc params 0x200077c1 hci version 0x100 quirks 0x0000000000009810
[    3.274456] ata1.00: configured for UDMA/133
[    3.282386] hub 3-0:1.0: USB hub found
[    3.285122] scsi 0:0:0:0: Direct-Access     ATA      KINGSTON SA400S3 B1D1 PQ: 0 ANSI: 5
[    3.287567] hub 3-0:1.0: 15 ports detected
[    3.294525] sd 0:0:0:0: [sda] 234441648 512-byte logical blocks: (120 GB/112 GiB)
[    3.298888] xhci_hcd 0000:00:14.0: xHCI Host Controller
[    3.303245] sd 0:0:0:0: [sda] Write Protect is off
[    3.307144] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 4
[    3.310615] sd 0:0:0:0: [sda] Mode Sense: 00 3a 00 00
[    3.316685] xhci_hcd 0000:00:14.0: Host supports USB 3.0 SuperSpeed
[    3.316691] sd 0:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    3.321773] hub 4-0:1.0: USB hub found
[    3.331803] hub 4-0:1.0: 6 ports detected
[    3.334067]  sda: sda1 sda2
[    3.335026] xhci_hcd 0000:01:00.2: enabling device (0000 -> 0002)
[    3.336316] sd 0:0:0:0: [sda] Attached SCSI disk
[    3.340850] xhci_hcd 0000:01:00.2: xHCI Host Controller
[    3.348049] xhci_hcd 0000:01:00.2: new USB bus registered, assigned bus number 5
[    3.354726] xhci_hcd 0000:01:00.2: hcc params 0x0180ff05 hci version 0x110 quirks 0x0000000000000010
[    3.362733] hub 5-0:1.0: USB hub found
[    3.365172] hub 5-0:1.0: 2 ports detected
[    3.367936] xhci_hcd 0000:01:00.2: xHCI Host Controller
[    3.371841] xhci_hcd 0000:01:00.2: new USB bus registered, assigned bus number 6
[    3.377907] xhci_hcd 0000:01:00.2: Host supports USB 3.1 Enhanced SuperSpeed
[    3.383642] usb usb6: We don't know the algorithms for LPM for this host, disabling LPM.
[    3.390472] hub 6-0:1.0: USB hub found
[    3.392922] hub 6-0:1.0: 4 ports detected
[    3.395720] usbcore: registered new interface driver usb-storage
[    3.400497] usbcore: registered new interface driver usbserial_generic
[    3.405706] usbserial: USB Serial support registered for generic
[    3.410400] i8042: PNP: No PS/2 controller found.
[    3.413920] input: PC Speaker as /devices/platform/pcspkr/input/input2
[    3.419162] rtc_cmos 00:02: RTC can wake from S4
[    3.422652] rtc_cmos 00:02: registered as rtc0
[    3.425841] rtc_cmos 00:02: setting system clock to 2021-04-29T10:08:30 UTC (1619690910)
[    3.432613] rtc_cmos 00:02: alarms up to one month, y3k, 242 bytes nvram, hpet irqs
[    3.439195] device-mapper: ioctl: 4.44.0-ioctl (2021-02-01) initialised: dm-devel@redhat.com
[    3.446370] intel_pstate: Intel P-state driver initializing
[    3.450897] sdhci: Secure Digital Host Controller Interface driver
[    3.455750] sdhci: Copyright(c) Pierre Ossman
[    3.458799] sdhci-pltfm: SDHCI platform and OF driver helper
[    3.466012] pstore: Registered efi as persistent store backend
[    3.471859] usbcore: registered new interface driver usbhid
[    3.477399] usbhid: USB HID core driver
[    3.481226] u32 classifier
[    3.483905]     input device check on
[    3.487532]     Actions configured
[    3.491039] NET: Registered protocol family 10
[    3.495610] Segment Routing with IPv6
[    3.499241] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
[    3.505188] NET: Registered protocol family 17
[    3.509601] Bridge firewalling registered
[    3.513575] lib80211: common routines for IEEE802.11 drivers
[    3.519188] lib80211_crypt: registered algorithm 'NULL'
[    3.519189] lib80211_crypt: registered algorithm 'WEP'
[    3.519190] lib80211_crypt: registered algorithm 'CCMP'
[    3.519190] lib80211_crypt: registered algorithm 'TKIP'
[    3.519196] Key type dns_resolver registered
[    3.523619] NET: Registered protocol family 40
[    3.528426] microcode: sig=0x306c3, pf=0x2, revision=0x1c
[    3.534010] microcode: Microcode Update Driver: v2.2.
[    3.534021] IPI shorthand broadcast: enabled
[    3.539409] usb 1-1: new high-speed USB device number 2 using ehci-pci
[    3.543261] sched_clock: Marking stable (2538999757, 1004243304)->(3708505559, -165262498)
[    3.558060] registered taskstats version 1
[    3.562140] Loading compiled-in X.509 certificates
[    3.566910] Key type ._fscrypt registered
[    3.570407] usb 2-1: new high-speed USB device number 2 using ehci-pci
[    3.570896] Key type .fscrypt registered
[    3.581324] Key type fscrypt-provisioning registered
[    3.586373] Btrfs loaded, crc32c=crc32c-generic, zoned=no
[    3.591817] pstore: Using crash dump compression: deflate
[    3.597597] Key type encrypted registered
[    3.601913] printk: console [netcon0] enabled
[    3.606250] netconsole: network logging started
[    3.610832] ALSA device list:
[    3.613776]   No soundcards found.
[    3.617170] md: Waiting for all devices to be available before autodetect
[    3.623931] md: If you don't use raid, use raid=noautodetect
[    3.629542] md: Autodetecting RAID arrays.
[    3.633601] md: autorun ...
[    3.636354] md: ... autorun DONE.
[    3.645104] EXT4-fs (sda2): mounted filesystem with ordered data mode. Opts: (null). Quota mode: disabled.
[    3.654709] VFS: Mounted root (ext4 filesystem) readonly on device 8:2.
[    3.661458] devtmpfs: mounted
[    3.665093] Freeing unused kernel image (initmem) memory: 1664K
[    3.670976] Write protecting the kernel read-only data: 24576k
[    3.677178] Freeing unused kernel image (text/rodata gap) memory: 2032K
[    3.683868] Freeing unused kernel image (rodata/data gap) memory: 840K
[    3.686079] hub 1-1:1.0: USB hub found
[    3.694112] Run /sbin/init as init process
[    3.694288] hub 1-1:1.0: 6 ports detected
[    3.698182]   with arguments:
[    3.698182]     /sbin/init
[    3.698183]   with environment:
[    3.698183]     HOME=/
[    3.698183]     TERM=linux
[    3.698184]     BOOT_IMAGE=/bzImage
[    3.715918] hub 2-1:1.0: USB hub found
[    3.719923] hub 2-1:1.0: 8 ports detected
[    3.739156] random: fast init done
[    3.743438] tsc: Refined TSC clocksource calibration: 3591.683 MHz
[    3.750459] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x33c5a2aaf01, max_idle_ns: 440795238424 ns
[    3.761346] clocksource: Switched to clocksource tsc
[    3.782316] systemd[1]: systemd 247.4+ running in system mode. (+PAM -AUDIT -SELINUX +IMA -APPARMOR -SMACK +SYSVINIT +UTMP -LIBCRYPTSETUP -GCRYPT -GNUTLS +ACL +XZ -LZ4 -ZSTD -SECCOMP +BLKID -ELFUTILS +KMOD -IDN2 -IDN -PCRE2 default-hierarchy=hybrid)
[    3.816536] systemd[1]: Detected architecture x86-64.
[    3.835363] systemd[1]: Set hostname to <intel-x86-64>.
[    3.911967] systemd[1]: Queued start job for default target Graphical Interface.
[    3.923959] systemd[1]: Created slice system-getty.slice.
[    3.931058] systemd[1]: Created slice system-modprobe.slice.
[    3.938469] systemd[1]: Created slice system-serial\x2dgetty.slice.
[    3.946410] systemd[1]: Created slice User and Session Slice.
[    3.953885] systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
[    3.963334] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[    3.972492] systemd[1]: Reached target Paths.
[    3.975409] usb 1-1.1: new low-speed USB device number 3 using ehci-pci
[    3.985318] systemd[1]: Reached target Remote File Systems.
[    3.992494] systemd[1]: Reached target Slices.
[    3.998533] systemd[1]: Reached target Swap.
[    4.004409] usb 2-1.5: new low-speed USB device number 3 using ehci-pci
[    4.013535] systemd[1]: Listening on RPCbind Server Activation Socket.
[    4.021873] systemd[1]: Reached target RPC Port Mapper.
[    4.029029] systemd[1]: Listening on Syslog Socket.
[    4.035720] systemd[1]: Listening on initctl Compatibility Named Pipe.
[    4.044682] systemd[1]: Condition check resulted in Journal Audit Socket being skipped.
[    4.052989] systemd[1]: Listening on Journal Socket (/dev/log).
[    4.060773] systemd[1]: Listening on Journal Socket.
[    4.067648] systemd[1]: Listening on Network Service Netlink Socket.
[    4.068656] input: Logitech USB Optical Mouse as /devices/pci0000:00/0000:00:1a.0/usb1/1-1/1-1.1/1-1.1:1.0/0003:046D:C077.0001/input/input3
[    4.086908] hid-generic 0003:046D:C077.0001: input: USB HID v1.11 Mouse [Logitech USB Optical Mouse] on usb-0000:00:1a.0-1.1/input0
[    4.100480] systemd[1]: Listening on udev Control Socket.
[    4.107650] systemd[1]: Listening on udev Kernel Socket.
[    4.114726] systemd[1]: Listening on User Database Manager Socket.
[    4.123043] systemd[1]: Mounting Huge Pages File System...
[    4.128850] input: DELL Dell USB Entry Keyboard as /devices/pci0000:00/0000:00:1d.0/usb2/2-1/2-1.5/2-1.5:1.0/0003:413C:2107.0002/input/input4
[    4.143523] systemd[1]: Mounting POSIX Message Queue File System...
[    4.152012] systemd[1]: Mounting Kernel Debug File System...
[    4.160010] systemd[1]: Mounting Kernel Trace File System...
[    4.168055] systemd[1]: Mounting Temporary Directory (/tmp)...
[    4.176162] systemd[1]: Starting Create list of static device nodes for the current kernel...
[    4.180509] hid-generic 0003:413C:2107.0002: input: USB HID v1.10 Keyboard [DELL Dell USB Entry Keyboard] on usb-0000:00:1d.0-1.5/input0
[    4.199611] systemd[1]: Starting Load Kernel Module configfs...
[    4.208006] systemd[1]: Starting Load Kernel Module drm...
[    4.215840] systemd[1]: Starting Load Kernel Module fuse...
[    4.222213] fuse: init (API version 7.33)
[    4.228292] systemd[1]: Starting RPC Bind...
[    4.234895] systemd[1]: Starting File System Check on Root Device...
[    4.244090] systemd[1]: Starting Journal Service...
[    4.252927] systemd[1]: Starting Load Kernel Modules...
[    4.261210] systemd[1]: Starting Coldplug All udev Devices...
[    4.271817] systemd[1]: Started RPC Bind.
[    4.276870] openvswitch: Open vSwitch switching datapath
[    4.284323] systemd[1]: Started Journal Service.
[    4.321343] EXT4-fs (sda2): re-mounted. Opts: (null). Quota mode: disabled.
[    4.341010] systemd-journald[190]: Received client request to flush runtime journal.
[    4.434946] ACPI: \_TZ_.TZ00: Invalid active0 threshold
[    4.441934] thermal LNXTHERM:00: registered as thermal_zone0
[    4.449288] ACPI: thermal: Thermal Zone [TZ00] (28 C)
[    4.456191] ACPI Warning: SystemIO range 0x0000000000001828-0x000000000000182F conflicts with OpRegion 0x0000000000001800-0x000000000000187F (\PMIO) (20210105/utaddress-204)
[    4.473217] cryptd: max_cpu_qlen set to 1000
[    4.473635] ACPI: OSL: Resource conflict; ACPI support missing from driver?
[    4.473824] thermal LNXTHERM:01: registered as thermal_zone1
[    4.473826] ACPI: thermal: Thermal Zone [TZ01] (30 C)
[    4.500025] ACPI Warning: SystemIO range 0x0000000000001C40-0x0000000000001C4F conflicts with OpRegion 0x0000000000001C00-0x0000000000001FFF (\GPR) (20210105/utaddress-204)
[    4.516431] ACPI: OSL: Resource conflict; ACPI support missing from driver?
[    4.523794] ACPI Warning: SystemIO range 0x0000000000001C30-0x0000000000001C3F conflicts with OpRegion 0x0000000000001C00-0x0000000000001C3F (\GPRL) (20210105/utaddress-204)
[    4.523798] ACPI Warning: SystemIO range 0x0000000000001C30-0x0000000000001C3F conflicts with OpRegion 0x0000000000001C00-0x0000000000001FFF (\GPR) (20210105/utaddress-204)
[    4.523800] ACPI: OSL: Resource conflict; ACPI support missing from driver?
[    4.523801] ACPI Warning: SystemIO range 0x0000000000001C00-0x0000000000001C2F conflicts with OpRegion 0x0000000000001C00-0x0000000000001C3F (\GPRL) (20210105/utaddress-204)
[    4.523802] ACPI Warning: SystemIO range 0x0000000000001C00-0x0000000000001C2F conflicts with OpRegion 0x0000000000001C00-0x0000000000001FFF (\GPR) (20210105/utaddress-204)
[    4.523804] ACPI: OSL: Resource conflict; ACPI support missing from driver?
[    4.523804] lpc_ich: Resource conflict(s) found affecting gpio_ich
[    4.610056] i801_smbus 0000:00:1f.3: SPD Write Disable is set
[    4.610094] i801_smbus 0000:00:1f.3: SMBus using PCI interrupt
[    4.611731] i2c i2c-0: 2/4 memory slots populated (from DMI)
[    4.630486] i2c i2c-0: Successfully instantiated SPD at 0x51
[    4.637131] i2c i2c-0: Successfully instantiated SPD at 0x53
[    4.661341] nvidia: loading out-of-tree module taints kernel.
[    4.667589] nvidia: module license 'NVIDIA' taints kernel.
[    4.667591] Disabling lock debugging due to kernel taint
[    4.680615] iTCO_vendor_support: vendor-support=0
[    4.693764] AVX2 version of gcm_enc/dec engaged.
[    4.699884] AES CTR mode by8 optimization enabled
[    4.705880] iTCO_wdt iTCO_wdt.1.auto: Found a Lynx Point TCO device (Version=2, TCOBASE=0x1860)
[    4.705963] iTCO_wdt iTCO_wdt.1.auto: initialized. heartbeat=30 sec (nowayout=0)
[    4.725720] snd_hda_intel 0000:01:00.1: enabling device (0000 -> 0002)
[    4.725747] snd_hda_intel 0000:01:00.1: Disabling MSI
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
[    4.896493] snd_hda_codec_realtek hdaudioC0D0: autoconfig for ALC3220: line_outs=1 (0x1b/0x0/0x0/0x0/0x0) type:line
[    4.896497] snd_hda_codec_realtek hdaudioC0D0:    speaker_outs=1 (0x14/0x0/0x0/0x0/0x0)
[    4.896500] snd_hda_codec_realtek hdaudioC0D0:    hp_outs=1 (0x15/0x0/0x0/0x0/0x0)
[    4.896501] snd_hda_codec_realtek hdaudioC0D0:    mono: mono_out=0x0
[    4.896503] snd_hda_codec_realtek hdaudioC0D0:    inputs:
[    4.896504] snd_hda_codec_realtek hdaudioC0D0:      Front Mic=0x1a
[    4.896505] snd_hda_codec_realtek hdaudioC0D0:      Rear Mic=0x18
[    4.935155] [drm] [nvidia-drm] [GPU ID 0x00000100] Loading driver
[    4.983090] [drm] Initialized nvidia-drm 0.0.0 20160202 for 0000:01:00.0 on minor 0
[    4.997833] input: HDA Intel PCH Front Mic as /devices/pci0000:00/0000:00:1b.0/sound/card0/input11
[    4.997878] input: HDA Intel PCH Rear Mic as /devices/pci0000:00/0000:00:1b.0/sound/card0/input12
[    4.997920] input: HDA Intel PCH Line Out as /devices/pci0000:00/0000:00:1b.0/sound/card0/input13
[    4.997960] input: HDA Intel PCH Front Headphone as /devices/pci0000:00/0000:00:1b.0/sound/card0/input14
[    5.053918] intel_rapl_common: Found RAPL domain package
[    5.053920] intel_rapl_common: Found RAPL domain core
[    5.053922] intel_rapl_common: Found RAPL domain dram
[    5.053926] intel_rapl_common: RAPL package-0 domain package locked by BIOS
[    5.053930] intel_rapl_common: RAPL package-0 domain dram locked by BIOS
[    5.135041] random: dbus-daemon: uninitialized urandom read (12 bytes read)
[    5.145085] random: dbus-daemon: uninitialized urandom read (12 bytes read)
[    5.370456] random: crng init done
[    5.370459] random: 3 urandom warning(s) missed due to ratelimiting
[    7.125430] e1000e 0000:00:19.0 eth0: NIC Link is Up 100 Mbps Full Duplex, Flow Control: Rx/Tx
[    7.132730] e1000e 0000:00:19.0 eth0: 10/100 speed: disabling TSO
[    7.137559] IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
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




