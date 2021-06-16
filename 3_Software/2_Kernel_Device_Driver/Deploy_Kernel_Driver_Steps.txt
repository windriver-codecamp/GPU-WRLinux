## Setup steps

### Build Image

> # /lpg-build/cdc/fast_prod/WRLINUX_MASTER_WR/MASTER_WR_GIT/wrlinux-10/setup.sh --machines=intel-x86-64 --distros=wrlinux-graphics --templates=feature/chromium,feature/xfce,feature/linux-yocto-dev,feature/userspace-next,feature/toolchain-next --layers=meta-browser --dl-layers --accept-eula=yes
> 
> $ source environment-setup-x86_64-wrlinuxsdk-linux 
> $ source oe-init-build-env
> 
> $ vi conf/local.conf
> 
> IMAGE_INSTALL_append = " libjpeg-turbo v4l-utils apt autoconf autoconf-archive automake binutils bison build-compare ccache chrpath cmake createrepo-c dejagnu desktop-file-utils diffstat distcc dmidecode dnf dosfstools dpkg dwarfsrcfiles e2fsprogs elfutils expect file flex gcc gdb git glide gnu-config go intltool json-c libcomps libdnf libedit libmodulemd librepo libtool m4 make makedevs meson mtools nasm ninja opkg opkg-utils orc patch patchelf perl prelink pseudo quilt rpm rsync ruby run-postinsts squashfs-tools strace subversion unifdef xmlto util-linux python3-pip python3-numpy python3-pkg-resources python3-setuptools libgcc make xz libcrypto libffi liblzma libssl libtirpc libmpc mpfr libunwind kernel-devsrc libmpc-dev gcc-plugins ncurses"
> 
> 
> EXTRA_IMAGE_FEATURES ?= "debug-tweaks tools-sdk tools-debug"
> 
> 
> $ vi ../layers/oe-core/meta/recipes-graphics/xorg-xserver/xserver-xorg.inc
> 
> 
> ...
> 
> OPENGL_PKGCONFIGS = "dri glx glamor dri3 xshmfence xinerama"
> PACKAGECONFIG ??= "dga dri2 udev ${XORG_CRYPTO} \
>                    ${@bb.utils.contains('DISTRO_FEATURES', 'opengl', '${OPENGL_PKGCONFIGS}', '', d)} \
>                    ${@bb.utils.contains('DISTRO_FEATURES', 'opengl wayland', 'xwayland', '', d)} \
>                    ${@bb.utils.contains('DISTRO_FEATURES', 'systemd', 'systemd systemd-logind', '', d)} \
> "
> 
> PACKAGECONFIG[udev] = "--enable-config-udev,--disable-config-udev,udev"
> PACKAGECONFIG[dga] = "--enable-dga,--disable-dga"
> PACKAGECONFIG[dri] = "--enable-dri,--disable-dri,virtual/mesa"
> PACKAGECONFIG[dri2] = "--enable-dri2,--disable-dri2"
> # DRI3 requires xshmfence to also be enabled
> PACKAGECONFIG[dri3] = "--enable-dri3,--disable-dri3"
> PACKAGECONFIG[glx] = "--enable-glx,--disable-glx,virtual/libgl virtual/libx11"
> PACKAGECONFIG[glamor] = "--enable-glamor,--disable-glamor,libepoxy virtual/libgbm,libegl"
> PACKAGECONFIG[unwind] = "--enable-libunwind,--disable-libunwind,libunwind"
> PACKAGECONFIG[xshmfence] = "--enable-xshmfence,--disable-xshmfence,libxshmfence"
> PACKAGECONFIG[xmlto] = "--with-xmlto, --without-xmlto, xmlto-native docbook-xml-dtd4-native docbook-xsl-stylesheets-native"
> PACKAGECONFIG[systemd-logind] = "--enable-systemd-logind=yes,--enable-systemd-logind=no,dbus,"
> PACKAGECONFIG[systemd] = "--with-systemd-daemon,--without-systemd-daemon,systemd"
> PACKAGECONFIG[xinerama] = "--enable-xinerama,--disable-xinerama"
> 
> 
> $ bitbake wrlinux-image-std-sato

## Deploy Images to the target
> $ dd if=wrlinux-image-std-sato-intel-x86-64.wic of=/dev/sdd
> $ parted /dev/sdd
> GNU Parted 3.3
> Using /dev/sdd
> Welcome to GNU Parted! Type 'help' to view a list of commands.
> (parted) p                                                                
> Warning: Not all of the space available to /dev/sdd appears to be used, you can fix the GPT to use all of the space (an extra 227735932 blocks) or continue with the current setting? 
> Fix/Ignore? Fix                                                           
> Model: TO Exter nal USB 3.0 (scsi)
> Disk /dev/sdd: 120GB
> Sector size (logical/physical): 512B/4096B
> Partition Table: gpt
> Disk Flags: 
> 
> Number  Start   End     Size    File system  Name      Flags
>  1      1049kB  29.6MB  28.6MB  fat16        msdos     legacy_boot, msftdata
>  2      30.4MB  3433MB  3403MB  ext4         platform
> 
> (parted) resize
> resize      resizepart  
> (parted) resizepart 
> align-check  disk_toggle  mklabel      mktable      print        rescue       resizepart   select       toggle       version      
> disk_set     help         mkpart       name         quit         resize       rm           set          unit         
> (parted) resizepart 2
> End?  [3433MB]? 100%                                                      
> (parted) p                                                                
> Model: TO Exter nal USB 3.0 (scsi)
> Disk /dev/sdd: 120GB
> Sector size (logical/physical): 512B/4096B
> Partition Table: gpt
> Disk Flags: 
> 
> Number  Start   End     Size    File system  Name      Flags
>  1      1049kB  29.6MB  28.6MB  fat16        msdos     legacy_boot, msftdata
>  2      30.4MB  120GB   120GB   ext4         platform
> 
> (parted) p
> Model: TO Exter nal USB 3.0 (scsi)
> Disk /dev/sdd: 120GB
> Sector size (logical/physical): 512B/4096B
> Partition Table: gpt
> Disk Flags: 
> 
> Number  Start   End     Size    File system  Name      Flags
>  1      1049kB  29.6MB  28.6MB  fat16        msdos     legacy_boot, msftdata
>  2      30.4MB  120GB   120GB   ext4         platform
> 
> (parted) q                                                                
> Information: You may need to update /etc/fstab.
> 
> $ resize2fs /dev/sdd2
> resize2fs 1.45.5 (07-Jan-2020)
> Resizing the filesystem on /dev/sdd2 to 29297777 (4k) blocks.
> The filesystem on /dev/sdd2 is now 29297777 (4k) blocks long.

## Boot up target and run the following commands to prepare environment

### Compile Nvidia GPU drivers and deploy



