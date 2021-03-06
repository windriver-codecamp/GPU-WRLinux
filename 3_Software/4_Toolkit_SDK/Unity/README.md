# Unity Installation

## Setup steps
 1. register an account on unity
	https://id.unity.com/en/conversations/aec46371-1052-4108-afdf-c7f8312edfb2018f?view=register

	2. Download Unity Editor

	http://beta.unity3d.com/download/fe82a0e88406/LinuxEditorInstaller/Unity.tar.xz
	tar xf Unity.tar.xz

	3. Download Unity Hub
	https://public-cdn.cloud.unity3d.com/hub/prod/UnityHub.AppImage?_gl=1*8s7rkd*_ga*OTMwMjEzMTk4LjE2MjIwODY0ODc.*_ga_1S78EFL1W5*MTYyMjUzODA2MC42LjEuMTYyMjUzODM5NS4w&_ga=2.51340841.1006021791.1622517514-930213198.1622086487

	4. Run Unity Hub and login
	./UnityHub.AppImage

	5. Active new license
	License Management --> Active new license

	6. Install Unity Editor
	Installs --> Locate, select Unity Editor (tar the Unity.tar.xz)

	7. Run projects
	Projects --> New --> 3D --> create  

### Issues
#### 1. Unity Editor cannot boot up without "libGLU.so"
#### Solution
> Run "bitbake libglu" and deploy "libglu1-9.0.1-0.corei7_64.rpm" to the host
#### 2. Failed to login on the "sign in".
#### Solution
> Manual Activation with file Unity_v2017.x.ulf

### References

* https://docs.unity3d.com/Manual/UnityManual.html
* https://blog.csdn.net/qq_30448401/article/details/104576125
* https://license.unity3d.com/manual
* https://home.aigei.com:8443/0-r12/GeiFileLocalStore/b80/pkg/code/zip/cf/cf17a9fda1b2435f95b379fcb789bfd0.zip?download/unity%E6%B1%BD%E8%BD%A6%E4%BB%BF%E7%9C%9F%E6%A8%A1%E6%8B%9FEdys+Vehicle+Physic_%E7%88%B1%E7%BB%99%E7%BD%91_aigei_com.zip&e=1624541760&token=P7S2Xpzfz11vAkASLTkfHN7Fw-oOZBecqeJaxypL:6gBopyAaXhrpDbJuzvvmGWhY6cc=

