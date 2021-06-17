## A screen recorder application on Wind River Linux (kazam)
```
wget https://launchpadlibrarian.net/182631125/kazam-1.4.5.tar.gz
```
### Issue 
* Failed to install kazam
```
ModuleNotFoundError: No module named 'DistUtilsExtra'
```
#### Solution

```
[lliu2@pek-lpgtest7302 build]$ bitbake python3-distutils-extra
```
```
root@intel-x86-64:/mnt/sdd/lliu2# scp lliu2@128.224.153.48:/buildarea2/lliu2/2021cc/dell_pc/CDNext_20210508/build/tmp-glibc/work/corei7-64-wrs-linux/python3-distutils-extra/2.39-r0/deploy-rpms/corei7_64/python3-distutils-extra-2.39-r0.corei7_64.rpm .
lliu2@128.224.153.48's password: 
python3-distutils-extra-2.39-r0.corei7_64.rpm                                                                                                                            100%   31KB   1.5MB/s   00:00    
root@intel-x86-64:/mnt/sdd/lliu2# ls
NVIDIA-Linux-x86_64-460.73.01  NVIDIA-Linux-x86_64-460.73.01.run  NVIDIA_CUDA-11.2_Samples  kazam-1.4.5  kazam-1.4.5.tar.gz  python3-distutils-extra-2.39-r0.corei7_64.rpm
root@intel-x86-64:/mnt/sdd/lliu2# rpm -ivh python3-distutils-extra-2.39-r0.corei7_64.rpm 
```


* Failed to run kazam
```
root@intel-x86-64:/mnt/sdd/lliu2/kazam-1.4.5/bin# ./kazam 
/mnt/sdd/lliu2/kazam-1.4.5/bin/./kazam:32: PyGIWarning: Gtk was imported without specifying a version first. Use gi.require_version('Gtk', '3.0') before import to ensure that the right version gets loaded.
  from gi.repository import Gtk
WARNING Kazam - Running from local directory, AppIndicator icons could be missing.
WARNING Kazam - Failed to correctly detect operating system.
Traceback (most recent call last):
  File "/mnt/sdd/lliu2/kazam-1.4.5/bin/./kazam", line 146, in <module>
    from kazam.app import KazamApp
  File "../kazam/app.py", line 35, in <module>
    from kazam.backend.prefs import *
  File "../kazam/backend/prefs.py", line 26, in <module>
    from xdg.BaseDirectory import xdg_config_home
ModuleNotFoundError: No module named 'xdg'
```
#### Solution

```
bitbake xdg-utils
```
```
root@intel-x86-64:/mnt/sdd/lliu2# scp lliu2@128.224.153.48:/buildarea2/lliu2/2021cc/dell_pc/CDNext_20210508/build/tmp-glibc/work/corei7-64-wrs-linux/xdg-utils/1.1.3-r0/deploy-rpms/corei7_64/xdg-utils-1.1.3-r0.corei7_64.rpm .
lliu2@128.224.153.48's password: 
xdg-utils-1.1.3-r0.corei7_64.rpm                                                                                                                                         100%   33KB   2.3MB/s   00:00    
root@intel-x86-64:/mnt/sdd/lliu2# rpm -ivh xdg-utils-1.1.3-r0.corei7_64.rpm 
error: Failed dependencies:
	xprop is needed by xdg-utils-1.1.3-r0.corei7_64
root@intel-x86-64:/mnt/sdd/lliu2# scp lliu2@128.224.153.48:/buildarea2/lliu2/2021cc/dell_pc/CDNext_20210508/build/tmp-glibc/work/corei7-64-wrs-linux/xprop/1_1.2.5-r0/deploy-rpms/corei7_64/xprop-1.2.5-r0.corei7_64.rpm .
lliu2@128.224.153.48's password: 
xprop-1.2.5-r0.corei7_64.rpm                                                                                                                                             100%   23KB   2.3MB/s   00:00    
root@intel-x86-64:/mnt/sdd/lliu2# rpm -ivh xprop-1.2.5-r0.corei7_64.rpm
Verifying...                          ################################# [100%]
Preparing...                          ################################# [100%]
Updating / installing...
   1:xprop-1:1.2.5-r0                 ################################# [100%]
root@intel-x86-64:/mnt/sdd/lliu2# rpm -ivh xdg-utils-1.1.3-r0.corei7_64.rpm 
Verifying...                          ################################# [100%]
Preparing...                          ################################# [100%]
Updating / installing...
   1:xdg-utils-1.1.3-r0               ################################# [100%]
root@intel-x86-64:/mnt/sdd/lliu2#
```

## NVIDIA Nsight Graphics (TODO)
```
NVIDIA® Nsight™ Graphics is a standalone developer tool that enables you to debug, profile, and export frames built with Direct3D (11, 12, DXR), Vulkan (1.2, NV Vulkan Ray Tracing Extension), OpenGL, OpenVR, and the Oculus SDK.
```
### References:
* https://developer.nvidia.com/nsight-graphics

## Virtual Camera

Unreal Engine 4.26 Virtual Camera 2.0    https://www.youtube.com/watch?v=jDYLfCurgcI

Using an iPhone as a tracker for Virtual Production https://www.youtube.com/watch?v=zZQu9f6U8zw

https://docs.unrealengine.com/en-US/SharingAndReleasing/Mobile/iOS/UsingSlateRemotePlugin/index.html

https://docs.unrealengine.com/en-US/AnimatingObjects/VirtualCamera/index.html

How To Use Your iPad as a Virtual Camera in Unreal Engine 4
https://www.youtube.com/watch?v=PktWwOs5jek

Unreal Engine 4.26 Virtual Camera 2.0
https://www.youtube.com/watch?v=jDYLfCurgcI

## Metahuman

Metahuman Creator - Basic Introduction - Create Realistic Digital Humans
https://www.youtube.com/watch?v=gXuVqfasT90
https://www.unrealengine.com/en-US/metahuman-creator
https://www.youtube.com/watch?v=Whf6ExJCpxw
https://www.youtube.com/watch?v=R3c4WjSFXJg

iPhone Facial Capture with Unreal Engine | Unreal Fest Online 2020
https://www.youtube.com/watch?v=R3c4WjSFXJg

Unreal Engine MetaHuman Live Link Facial Mocap Setup & Change Character / iPhone or iPad
https://www.youtube.com/watch?v=bw7FEg4gedQ
https://www.unrealengine.com/marketplace/en-US/learn/metahumans

Unreal Engine MetaHuman ~ How to Animate MetaHuman with iClone Unreal Live Link
https://www.youtube.com/watch?v=2bbDrguOuUI

https://www.upwork.com/job/Build-video-with-Metahuman-using-Unreal-Engine-for-Linux_~01ab7c2f0ee0909b5a/

## VR and XR Samples
Your First VR App Using Unreal Engine (UE4)

* https://www.youtube.com/watch?v=QXNkGJl0ECg

How to Budget for Your VR Project
* https://www.youtube.com/watch?v=P5CW5-bIUhc

Face AR Sample (Live Link Broadcasting)
* https://docs.unrealengine.com/en-US/SharingAndReleasing/XRDevelopment/AR/HandheldAR/FaceARSample/index.html
