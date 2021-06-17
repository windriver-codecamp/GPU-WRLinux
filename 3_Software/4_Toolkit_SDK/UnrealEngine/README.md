# Unreal Engine Installation

## Setup Steps

```
TODO
```

### Install Quixel Bridge
```
intel-x86-64:~$ ./Bridge.AppImage 
dlopen(): error loading libfuse.so.2

AppImages require FUSE to run. 
You might still be able to extract the contents of this AppImage 
if you run it with the --appimage-extract option. 
See https://github.com/AppImage/AppImageKit/wiki/FUSE 
for more information
intel-x86-64:~$ 


lliu2@pek-lpgtest7302 build]$ bitbake fuse


[lliu2@pek-lpgtest7302 corei7_64]$ scp libfuse2-2.9.9-r0.corei7_64.rpm fuse-utils-2.9.9-r0.corei7_64.rpm root@128.224.162.144:/
The authenticity of host '128.224.162.144 (128.224.162.144)' can't be established.
ECDSA key fingerprint is SHA256:vMWhEaKsgSUGgCpPD3Gj0/lY+8RgID401JSubIjUCU0.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '128.224.162.144' (ECDSA) to the list of known hosts.
libfuse2-2.9.9-r0.corei7_64.rpm                                                                                                                                          100%   73KB   9.5MB/s   00:00    
fuse-utils-2.9.9-r0.corei7_64.rpm                                                                                                                                        100%   25KB 697.2KB/s   00:00    
[lliu2@pek-lpgtest7302 corei7_64]$ 


intel-x86-64:/# rpm -ivh libfuse2-2.9.9-r0.corei7_64.rpm 
Verifying...                          ################################# [100%]
Preparing...                          ################################# [100%]
Updating / installing...
   1:libfuse2-2.9.9-r0                ################################# [100%]
%post(libfuse2-2.9.9-r0.corei7_64): scriptlet start
%post(libfuse2-2.9.9-r0.corei7_64): execv(/bin/sh) pid 1465
+ set -e
+ '[' x = x ']'
+ '[' -x /sbin/ldconfig ']'
+ /sbin/ldconfig
%post(libfuse2-2.9.9-r0.corei7_64): waitpid(1465) rc 1465 status 0
intel-x86-64:/# rpm -ivh lib
lib/                                  lib64/                                libfuse2-2.9.9-r0.corei7_64.rpm       libsdl-1.2-0-1.2.15-r3.corei7_64.rpm  
intel-x86-64:/# rpm -ivh fuse-utils-2.9.9-r0.corei7_64.rpm 
Verifying...                          ################################# [100%]
Preparing...                          ################################# [100%]
Updating / installing...
   1:fuse-utils-2.9.9-r0              ################################# [100%]
intel-x86-64:/# rpm -ivh libfuse2-2.9.9-r0.corei7_64.rpm 
Verifying...                          ################################# [100%]
Preparing...                          ################################# [100%]
	package libfuse2-2.9.9-r0.corei7_64 is already installed
intel-x86-64:/# 

intel-x86-64:~$ ./Bridge.AppImage 
/tmp/.mount_BridgeeWL7ef/megascans-bridge: error while loading shared libraries: libcups.so.2: cannot open shared object file: No such file or directory
[lliu2@pek-lpgtest7302 build]$ bitbake cups
…
[lliu2@pek-lpgtest7302 corei7_64]$ scp libcups2-2.3.3-r0.corei7_64.rpm root@128.224.162.144:/
libcups2-2.3.3-r0.corei7_64.rpm 
[lliu2@pek-lpgtest7302 corei7_64]$ scp cups-2.3.3-r0.corei7_64.rpm root@128.224.162.144:/
cups-2.3.3-r0.corei7_64.rpm  

intel-x86-64:/# rpm -ivh libcups2-2.3.3-r0.corei7_64.rpm 
Verifying...                          ################################# [100%]
Preparing...                          ################################# [100%]
Updating / installing...
   1:libcups2-2.3.3-r0                ################################# [100%]
%post(libcups2-2.3.3-r0.corei7_64): scriptlet start
%post(libcups2-2.3.3-r0.corei7_64): execv(/bin/sh) pid 1571
+ set -e
+ '[' x = x ']'
+ '[' -x /sbin/ldconfig ']'
+ /sbin/ldconfig
%post(libcups2-2.3.3-r0.corei7_64): waitpid(1571) rc 1571 status 0
intel-x86-64:/# rpm -ivh cups-2.3.3-r0.corei7_64.rpm 
Verifying...                          ################################# [100%]
Preparing...                          ################################# [100%]
%prein(cups-2.3.3-r0.corei7_64): scriptlet start
%prein(cups-2.3.3-r0.corei7_64): execv(/bin/sh) pid 1574
+ set -e
+ OPT=
+ SYSROOT=
+ test x '!=' x
+ test x = x
+ GROUPADD_PARAM='--system lpadmin'
+ USERADD_PARAM=
+ GROUPMEMS_PARAM=
++ echo --system lpadmin
++ tr -d '[:space:]'
+ test x--systemlpadmin '!=' x
+ echo 'Running groupadd commands...'
Running groupadd commands...
++ echo '--system lpadmin'
++ cut -d ';' -f 1
++ sed -e 's#[ \t]*$##'
+ opts='--system lpadmin'
++ echo '--system lpadmin'
++ cut -d ';' -f 2-
++ sed -e 's#[ \t]*$##'
+ remaining='--system lpadmin'
+ test 'x--system lpadmin' '!=' x
+ perform_groupadd '' ' --system lpadmin'
+ local rootdir=
+ local 'opts= --system lpadmin'
+ bbnote 'cups: Performing groupadd with [ --system lpadmin]'
+ echo 'NOTE: cups: Performing groupadd with [ --system lpadmin]'
NOTE: cups: Performing groupadd with [ --system lpadmin]
++ echo ' --system lpadmin'
++ awk '{ print $NF }'
+ local groupname=lpadmin
++ grep '^lpadmin:' /etc/group
++ true
+ local group_exists=
+ test x = x
+ eval flock -x /etc -c '"' groupadd '$opts"'
++ flock -x /etc -c ' groupadd  --system lpadmin'
++ grep '^lpadmin:' /etc/group
+ group_exists=lpadmin:x:977:
+ test xlpadmin:x:977: = x
+ test 'x--system lpadmin' = 'x--system lpadmin'
+ break
++ echo
++ tr -d '[:space:]'
+ test x '!=' x
++ echo
++ tr -d '[:space:]'
+ test x '!=' x
%prein(cups-2.3.3-r0.corei7_64): waitpid(1574) rc 1574 status 0
Updating / installing...
   1:cups-2.3.3-r0                    ################################# [100%]
%post(cups-2.3.3-r0.corei7_64): scriptlet start
%post(cups-2.3.3-r0.corei7_64): execv(/bin/sh) pid 1605
+ set -e
+ systemctl
+ OPTS=
+ '[' -n '' ']'
+ '[' enable = enable ']'
+ for service in org.cups.cupsd.socket org.cups.cupsd.path org.cups.cupsd.service org.cups.cups-lpd.socket
+ systemctl enable org.cups.cupsd.socket
Created symlink /etc/systemd/system/sockets.target.wants/org.cups.cupsd.socket → /lib/systemd/system/org.cups.cupsd.socket.
+ for service in org.cups.cupsd.socket org.cups.cupsd.path org.cups.cupsd.service org.cups.cups-lpd.socket
+ systemctl enable org.cups.cupsd.path
Created symlink /etc/systemd/system/multi-user.target.wants/org.cups.cupsd.path → /lib/systemd/system/org.cups.cupsd.path.
+ for service in org.cups.cupsd.socket org.cups.cupsd.path org.cups.cupsd.service org.cups.cups-lpd.socket
+ systemctl enable org.cups.cupsd.service
Created symlink /etc/systemd/system/printer.target.wants/org.cups.cupsd.service → /lib/systemd/system/org.cups.cupsd.service.
+ for service in org.cups.cupsd.socket org.cups.cupsd.path org.cups.cupsd.service org.cups.cups-lpd.socket
+ systemctl enable org.cups.cups-lpd.socket
Created symlink /etc/systemd/system/sockets.target.wants/org.cups.cups-lpd.socket → /lib/systemd/system/org.cups.cups-lpd.socket.
+ '[' -z '' ']'
+ systemctl daemon-reload
+ systemctl preset org.cups.cupsd.socket org.cups.cupsd.path org.cups.cupsd.service org.cups.cups-lpd.socket
+ '[' enable = enable ']'
+ systemctl --no-block restart org.cups.cupsd.socket org.cups.cupsd.path org.cups.cupsd.service org.cups.cups-lpd.socket
%post(cups-2.3.3-r0.corei7_64): waitpid(1605) rc 1605 status 0

intel-x86-64:/# su root
intel-x86-64:/# reboot

intel-x86-64:~$ ./Bridge.AppImage 
```


### Issues
* Failed to start UE4Editor for the reason of permission
```
sh-5.1$ ./UE4Editor
Increasing per-process limit of core file size to infinity.
sh: line 1: xdg-user-dir: command not found
LogInit: LLM is enabled
LogInit: LLM CsvWriter: off TraceWriter: off
LogInit: Display: Running engine without a game
LogPlatformFile: Not using cached read wrapper
LogTaskGraph: Started task graph with 5 named threads and 14 total threads with 3 sets of task threads.
LogStats: Stats thread started at 0.087217
LogICUInternationalization: ICU TimeZone Detection - Raw Offset: +0:00, Platform Override: ''
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_2.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_2.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_3.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_3.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_4.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_4.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_5.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_5.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_6.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_6.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_7.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_7.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_8.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_8.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_9.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_9.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_10.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_10.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_11.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_11.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_12.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_12.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_13.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_13.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_14.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_14.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_15.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_15.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_16.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_16.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_17.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_17.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_18.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_18.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_19.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_19.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_20.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_20.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_21.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_21.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_22.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_22.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_23.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_23.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_24.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_24.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_25.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_25.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_26.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_26.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_27.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_27.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_28.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_28.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_29.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_29.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_30.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_30.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_31.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Logs/UE4_31.log') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Config/CrashReportClient/UE4CC-Linux-4B56D113A06F482A86BC9063747D5E6D/CrashReportClient.ini') failed: errno=13 (Permission denied)
LogUnixPlatformFile: Warning: create dir('/UnrealEngine-release/Engine/Saved/Config/CrashReportClient/UE4CC-Linux-4B56D113A06F482A86BC9063747D5E6D/CrashReportClient.ini') failed: errno=13 (Permission denied)
LogPluginManager: Mounting plugin MeshPainting
LogPluginManager: Mounting plugin XGEController
LogPluginManager: Mounting plugin Paper2D
LogPluginManager: Mounting plugin LauncherChunkInstaller
LogPluginManager: Mounting plugin CameraShakePreviewer
LogPluginManager: Mounting plugin ScreenshotTools
LogPluginManager: Mounting plugin AISupport
LogPluginManager: Mounting plugin PlatformCrypto
LogPluginManager: Mounting plugin MotoSynth
LogPluginManager: Mounting plugin SkeletalReduction
LogPluginManager: Mounting plugin CharacterAI
LogPluginManager: Mounting plugin ProxyLODPlugin
LogPluginManager: Mounting plugin ChaosNiagara
LogPluginManager: Mounting plugin ChaosSolverPlugin
LogPluginManager: Mounting plugin ChaosCloth
LogPluginManager: Mounting plugin AutomationUtils
LogPluginManager: Mounting plugin PlanarCut
LogPluginManager: Mounting plugin AlembicImporter
LogPluginManager: Mounting plugin EnvironmentQueryEditor
LogPluginManager: Mounting plugin GeometryCollectionPlugin
LogPluginManager: Mounting plugin GeometryCache
LogPluginManager: Mounting plugin BackChannel
LogPluginManager: Mounting plugin ChaosClothEditor
LogPluginManager: Mounting plugin GeometryProcessing
LogPluginManager: Mounting plugin Niagara
LogPluginManager: Mounting plugin ChaosEditor
LogPluginManager: Mounting plugin DatasmithContent
LogPluginManager: Mounting plugin VariantManagerContent
LogPluginManager: Mounting plugin LevelSequenceEditor
LogPluginManager: Mounting plugin MatineeToLevelSequence
LogPluginManager: Mounting plugin ActorSequence
LogPluginManager: Mounting plugin TemplateSequence
LogPluginManager: Mounting plugin PostSplashScreen
LogPluginManager: Mounting plugin ChunkDownloader
LogPluginManager: Mounting plugin PhysXVehicles
LogPluginManager: Mounting plugin WebMMoviePlayer
LogPluginManager: Mounting plugin AssetTags
LogPluginManager: Mounting plugin SoundFields
LogPluginManager: Mounting plugin AppleImageUtils
LogPluginManager: Mounting plugin PropertyAccessEditor
LogPluginManager: Mounting plugin MLSDK
LogPluginManager: Mounting plugin MobilePatchingUtils
LogPluginManager: Mounting plugin SignificanceManager
LogPluginManager: Mounting plugin MagicLeapMedia
LogPluginManager: Mounting plugin MagicLeap
LogPluginManager: Mounting plugin WindowsMoviePlayer
LogPluginManager: Mounting plugin MagicLeapPassableWorld
LogPluginManager: Mounting plugin LuminPlatformFeatures
LogPluginManager: Mounting plugin EditableMesh
LogPluginManager: Mounting plugin MagicLeapLightEstimation
LogPluginManager: Mounting plugin CableComponent
LogPluginManager: Mounting plugin AssetManagerEditor
LogPluginManager: Mounting plugin MobileLauncherProfileWizard
LogPluginManager: Mounting plugin CryptoKeys
LogPluginManager: Mounting plugin PluginBrowser
LogPluginManager: Mounting plugin DataValidation
LogPluginManager: Mounting plugin FacialAnimation
LogPluginManager: Mounting plugin CustomMeshComponent
LogPluginManager: Mounting plugin GameplayTagsEditor
LogPluginManager: Mounting plugin MaterialAnalyzer
LogPluginManager: Mounting plugin AndroidDeviceProfileSelector
LogPluginManager: Mounting plugin MacGraphicsSwitching
LogPluginManager: Mounting plugin GeometryMode
LogPluginManager: Mounting plugin CurveEditorTools
LogPluginManager: Mounting plugin SpeedTreeImporter
LogPluginManager: Mounting plugin OnlineSubsystem
LogPluginManager: Mounting plugin GoogleCloudMessaging
LogPluginManager: Mounting plugin OnlineSubsystemUtils
LogPluginManager: Mounting plugin OnlineSubsystemNull
LogPluginManager: Mounting plugin ArchVisCharacter
LogPluginManager: Mounting plugin LinuxDeviceProfileSelector
LogPluginManager: Mounting plugin RuntimePhysXCooking
LogPluginManager: Mounting plugin AudioSynesthesia
LogPluginManager: Mounting plugin LocationServicesBPLibrary
LogPluginManager: Mounting plugin AudioCapture
LogPluginManager: Mounting plugin GooglePAD
LogPluginManager: Mounting plugin ActorLayerUtilities
LogPluginManager: Mounting plugin Synthesis
LogPluginManager: Mounting plugin IOSDeviceProfileSelector
LogPluginManager: Mounting plugin AppleMoviePlayer
LogPluginManager: Mounting plugin AndroidPermission
LogPluginManager: Mounting plugin ProceduralMeshComponent
LogPluginManager: Mounting plugin ExampleDeviceProfileSelector
LogPluginManager: Mounting plugin AndroidMoviePlayer
LogPluginManager: Mounting plugin CodeLiteSourceCodeAccess
LogPluginManager: Mounting plugin PropertyAccessNode
LogPluginManager: Mounting plugin GitSourceControl
LogPluginManager: Mounting plugin PerforceSourceControl
LogPluginManager: Mounting plugin RiderSourceCodeAccess
LogPluginManager: Mounting plugin VisualStudioSourceCodeAccess
LogPluginManager: Mounting plugin NullSourceCodeAccess
LogPluginManager: Mounting plugin CLionSourceCodeAccess
LogPluginManager: Mounting plugin AnimationSharing
LogPluginManager: Mounting plugin UObjectPlugin
LogPluginManager: Mounting plugin XCodeSourceCodeAccess
LogPluginManager: Mounting plugin KDevelopSourceCodeAccess
LogPluginManager: Mounting plugin SubversionSourceControl
LogPluginManager: Mounting plugin VisualStudioCodeSourceCodeAccess
LogPluginManager: Mounting plugin PluginUtils
LogPluginManager: Mounting plugin PlasticSourceControl
LogPluginManager: Mounting plugin TcpMessaging
LogPluginManager: Mounting plugin UdpMessaging
LogPluginManager: Mounting plugin LightPropagationVolume
LogPluginManager: Mounting plugin MediaCompositing
LogPluginManager: Mounting plugin WebMMedia
LogPluginManager: Mounting plugin MediaPlayerEditor
LogPluginManager: Mounting plugin AndroidMedia
LogPluginManager: Mounting plugin ImgMedia
LogPluginManager: Mounting plugin AvfMedia
LogPluginManager: Mounting plugin WmfMedia
LogPluginManager: Mounting plugin ContentBrowserAssetDataSource
LogPluginManager: Mounting plugin ContentBrowserClassDataSource
LogPluginManager: Mounting plugin OnlineSubsystemIOS
LogPluginManager: Mounting plugin OnlineSubsystemGooglePlay
LogPluginManager: Mounting plugin OculusVR
LogPluginManager: Mounting plugin SteamVR
LogInit: Using libcurl 7.65.3-DEV
LogInit:  - built for x86_64-unknown-linux-gnu
LogInit:  - supports SSL with OpenSSL/1.1.1c
LogInit:  - supports HTTP deflate (compression) using libz 1.2.8
LogInit:  - other features:
LogInit:      CURL_VERSION_SSL
LogInit:      CURL_VERSION_LIBZ
LogInit:      CURL_VERSION_IPV6
LogInit:      CURL_VERSION_ASYNCHDNS
LogInit:      CURL_VERSION_LARGEFILE
LogInit:      CURL_VERSION_TLSAUTH_SRP
LogInit:  CurlRequestOptions (configurable via config and command line):
LogInit:  - bVerifyPeer = true  - Libcurl will verify peer certificate
LogInit:  - bUseHttpProxy = false  - Libcurl will NOT use HTTP proxy
LogInit:  - bDontReuseConnections = false  - Libcurl will reuse connections
LogInit:  - MaxHostConnections = 16  - Libcurl will limit the number of connections to a host
LogInit:  - LocalHostAddr = Default
LogInit:  - BufferSize = 65536
LogOnline: OSS: Creating online subsystem instance for: NULL
LogOnline: OSS: TryLoadSubsystemAndSetDefault: Loaded subsystem for module [NULL]
LogInit: Build: ++UE4+Release-4.26-CL-0
LogInit: Engine Version: 4.26.2-0+++UE4+Release-4.26
LogInit: Compatible Engine Version: 4.26.0-0+++UE4+Release-4.26
LogInit: Net CL: 0
LogInit: OS: GenericOSVersionLabel (GenericOSSubVersionLabel), CPU: Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz, GPU: GenericGPUBrand
LogInit: Compiled (64-bit): May 18 2021 03:42:04
LogInit: Compiled with Clang: 10.0.1 
LogInit: Build Configuration: Development
LogInit: Branch Name: ++UE4+Release-4.26
LogInit: Command Line: 
LogInit: Base Directory: /UnrealEngine-release/Engine/Binaries/Linux/
LogInit: Allocator: binned2
LogInit: Installed Engine Build: 0
LogDevObjectVersion: Number of dev versions registered: 29
LogDevObjectVersion:   Dev-Blueprints (B0D832E4-1F89-4F0D-ACCF-7EB736FD4AA2): 10
LogDevObjectVersion:   Dev-Build (E1C64328-A22C-4D53-A36C-8E866417BD8C): 0
LogDevObjectVersion:   Dev-Core (375EC13C-06E4-48FB-B500-84F0262A717E): 4
LogDevObjectVersion:   Dev-Editor (E4B068ED-F494-42E9-A231-DA0B2E46BB41): 40
LogDevObjectVersion:   Dev-Framework (CFFC743F-43B0-4480-9391-14DF171D2073): 37
LogDevObjectVersion:   Dev-Mobile (B02B49B5-BB20-44E9-A304-32B752E40360): 3
LogDevObjectVersion:   Dev-Networking (A4E4105C-59A1-49B5-A7C5-40C4547EDFEE): 0
LogDevObjectVersion:   Dev-Online (39C831C9-5AE6-47DC-9A44-9C173E1C8E7C): 0
LogDevObjectVersion:   Dev-Physics (78F01B33-EBEA-4F98-B9B4-84EACCB95AA2): 4
LogDevObjectVersion:   Dev-Platform (6631380F-2D4D-43E0-8009-CF276956A95A): 0
LogDevObjectVersion:   Dev-Rendering (12F88B9F-8875-4AFC-A67C-D90C383ABD29): 44
LogDevObjectVersion:   Dev-Sequencer (7B5AE74C-D270-4C10-A958-57980B212A5A): 12
LogDevObjectVersion:   Dev-VR (D7296918-1DD6-4BDD-9DE2-64A83CC13884): 3
LogDevObjectVersion:   Dev-LoadTimes (C2A15278-BFE7-4AFE-6C17-90FF531DF755): 1
LogDevObjectVersion:   Private-Geometry (6EACA3D4-40EC-4CC1-B786-8BED09428FC5): 3
LogDevObjectVersion:   Dev-AnimPhys (29E575DD-E0A3-4627-9D10-D276232CDCEA): 17
LogDevObjectVersion:   Dev-Anim (AF43A65D-7FD3-4947-9873-3E8ED9C1BB05): 15
LogDevObjectVersion:   Dev-ReflectionCapture (6B266CEC-1EC7-4B8F-A30B-E4D90942FC07): 1
LogDevObjectVersion:   Dev-Automation (0DF73D61-A23F-47EA-B727-89E90C41499A): 1
LogDevObjectVersion:   FortniteMain (601D1886-AC64-4F84-AA16-D3DE0DEAC7D6): 43
LogDevObjectVersion:   FortniteRelease (E7086368-6B23-4C58-8439-1B7016265E91): 1
LogDevObjectVersion:   Dev-Enterprise (9DFFBCD6-494F-0158-E221-12823C92A888): 10
LogDevObjectVersion:   Dev-Niagara (F2AED0AC-9AFE-416F-8664-AA7FFA26D6FC): 1
LogDevObjectVersion:   Dev-Destruction (174F1F0B-B4C6-45A5-B13F-2EE8D0FB917D): 10
LogDevObjectVersion:   Dev-Physics-Ext (35F94A83-E258-406C-A318-09F59610247C): 40
LogDevObjectVersion:   Dev-PhysicsMaterial-Chaos (B68FC16E-8B1B-42E2-B453-215C058844FE): 1
LogDevObjectVersion:   Dev-CineCamera (B2E18506-4273-CFC2-A54E-F4BB758BBA07): 1
LogDevObjectVersion:   Dev-VirtualProduction (64F58936-FD1B-42BA-BA96-7289D5D0FA4E): 1
LogDevObjectVersion:   Dev-MediaFramework (6F0ED827-A609-4895-9C91-998D90180EA4): 2
LogInit: Presizing for max 25165824 objects, including 0 objects not considered by GC, pre-allocating 0 bytes for permanent pool.
LogConfig: Applying CVar settings from Section [/Script/Engine.StreamingSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
LogConfig: Setting CVar [[s.MinBulkDataSizeForAsyncLoading:131072]]
LogConfig: Setting CVar [[s.AsyncLoadingThreadEnabled:0]]
LogConfig: Setting CVar [[s.EventDrivenLoaderEnabled:1]]
LogConfig: Setting CVar [[s.WarnIfTimeLimitExceeded:0]]
LogConfig: Setting CVar [[s.TimeLimitExceededMultiplier:1.5]]
LogConfig: Setting CVar [[s.TimeLimitExceededMinTime:0.005]]
LogConfig: Setting CVar [[s.UseBackgroundLevelStreaming:1]]
LogConfig: Setting CVar [[s.PriorityAsyncLoadingExtraTime:15.0]]
LogConfig: Setting CVar [[s.LevelStreamingActorsUpdateTimeLimit:5.0]]
LogConfig: Setting CVar [[s.PriorityLevelStreamingActorsUpdateExtraTime:5.0]]
LogConfig: Setting CVar [[s.LevelStreamingComponentsRegistrationGranularity:10]]
LogConfig: Setting CVar [[s.UnregisterComponentsTimeLimit:1.0]]
LogConfig: Setting CVar [[s.LevelStreamingComponentsUnregistrationGranularity:5]]
LogConfig: Setting CVar [[s.FlushStreamingOnExit:1]]
LogInit: Object subsystem initialized
LogConfig: Setting CVar [[con.DebugEarlyDefault:1]]
LogConfig: Setting CVar [[r.setres:1280x720]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[r.VSync:0]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[r.RHICmdBypass:0]]
[2021.05.18-06.05.35:329][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.RendererSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[r.GPUCrashDebugging:0]]
[2021.05.18-06.05.35:329][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.RendererOverrideSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2021.05.18-06.05.35:329][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.StreamingSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[s.MinBulkDataSizeForAsyncLoading:131072]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[s.AsyncLoadingThreadEnabled:0]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[s.EventDrivenLoaderEnabled:1]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[s.WarnIfTimeLimitExceeded:0]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[s.TimeLimitExceededMultiplier:1.5]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[s.TimeLimitExceededMinTime:0.005]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[s.UseBackgroundLevelStreaming:1]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[s.PriorityAsyncLoadingExtraTime:15.0]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[s.LevelStreamingActorsUpdateTimeLimit:5.0]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[s.PriorityLevelStreamingActorsUpdateExtraTime:5.0]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[s.LevelStreamingComponentsRegistrationGranularity:10]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[s.UnregisterComponentsTimeLimit:1.0]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[s.LevelStreamingComponentsUnregistrationGranularity:5]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[s.FlushStreamingOnExit:1]]
[2021.05.18-06.05.35:329][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.GarbageCollectionSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[gc.MaxObjectsNotConsideredByGC:1]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[gc.SizeOfPermanentObjectPool:0]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[gc.FlushStreamingOnGC:0]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[gc.NumRetriesBeforeForcingGC:10]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[gc.AllowParallelGC:1]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[gc.TimeBetweenPurgingPendingKillObjects:61.1]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[gc.MaxObjectsInEditor:25165824]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[gc.IncrementalBeginDestroyEnabled:1]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[gc.CreateGCClusters:1]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[gc.MinGCClusterSize:5]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[gc.ActorClusteringEnabled:0]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[gc.BlueprintClusteringEnabled:0]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[gc.UseDisregardForGCOnDedicatedServers:0]]
[2021.05.18-06.05.35:329][  0]LogConfig: Setting CVar [[gc.MultithreadedDestructionEnabled:1]]
[2021.05.18-06.05.35:329][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.NetworkSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2021.05.18-06.05.35:329][  0]LogConfig: Applying CVar settings from Section [/Script/UnrealEd.CookerSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2021.05.18-06.05.35:329][  0]LogInit: Initializing SDL.
No protocol specified
[2021.05.18-06.05.35:336][  0]LogInit: Warning: Could not initialize SDL: No available video device
[2021.05.18-06.05.35:336][  0]LogInit: Warning: FDisplayMetrics::GetDisplayMetrics: InitSDL() failed, cannot get display metrics
[2021.05.18-06.05.35:336][  0]LogConfig: Applying CVar settings from Section [ViewDistanceQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.SkeletalMeshLODBias:0]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.ViewDistanceScale:1.0]]
[2021.05.18-06.05.35:336][  0]LogConfig: Applying CVar settings from Section [AntiAliasingQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.PostProcessAAQuality:4]]
[2021.05.18-06.05.35:336][  0]LogConfig: Applying CVar settings from Section [ShadowQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.LightFunctionQuality:1]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.ShadowQuality:5]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.Shadow.CSM.MaxCascades:10]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.Shadow.MaxResolution:2048]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.Shadow.MaxCSMResolution:2048]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.Shadow.RadiusThreshold:0.01]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.Shadow.DistanceScale:1.0]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.Shadow.CSM.TransitionScale:1.0]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.Shadow.PreShadowResolutionFactor:1.0]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.DistanceFieldShadowing:1]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.DistanceFieldAO:1]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.AOQuality:2]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.VolumetricFog:1]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.VolumetricFog.GridPixelSize:8]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.VolumetricFog.GridSizeZ:128]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.VolumetricFog.HistoryMissSupersampleCount:4]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.LightMaxDrawDistanceScale:1]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.CapsuleShadows:1]]
[2021.05.18-06.05.35:336][  0]LogConfig: Applying CVar settings from Section [PostProcessQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.MotionBlurQuality:4]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.AmbientOcclusionMipLevelFactor:0.4]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.AmbientOcclusionMaxQuality:100]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.AmbientOcclusionLevels:-1]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.AmbientOcclusionRadiusScale:1.0]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.DepthOfFieldQuality:2]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.RenderTargetPoolMin:400]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.LensFlareQuality:2]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.SceneColorFringeQuality:1]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.EyeAdaptationQuality:2]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.BloomQuality:5]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.FastBlurThreshold:100]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.Upscale.Quality:3]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.Tonemapper.GrainQuantization:1]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.LightShaftQuality:1]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.Filter.SizeScale:1]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.Tonemapper.Quality:5]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.DOF.Gather.AccumulatorQuality:1        ; higher gathering accumulator quality]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.DOF.Gather.PostfilterMethod:1          ; Median3x3 postfilering method]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.DOF.Gather.EnableBokehSettings:0       ; no bokeh simulation when gathering]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.DOF.Gather.RingCount:4                 ; medium number of samples when gathering]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.DOF.Scatter.ForegroundCompositing:1    ; additive foreground scattering]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.DOF.Scatter.BackgroundCompositing:2    ; additive background scattering]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.DOF.Scatter.EnableBokehSettings:1      ; bokeh simulation when scattering]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.DOF.Scatter.MaxSpriteRatio:0.1         ; only a maximum of 10% of scattered bokeh]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.DOF.Recombine.Quality:1                ; cheap slight out of focus]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.DOF.Recombine.EnableBokehSettings:0    ; no bokeh simulation on slight out of focus]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.DOF.TemporalAAQuality:1                ; more stable temporal accumulation]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.DOF.Kernel.MaxForegroundRadius:0.025]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.DOF.Kernel.MaxBackgroundRadius:0.025]]
[2021.05.18-06.05.35:336][  0]LogConfig: Applying CVar settings from Section [TextureQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.Streaming.MipBias:0]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.Streaming.AmortizeCPUToGPUCopy:0]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.Streaming.MaxNumTexturesToStreamPerFrame:0]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.Streaming.Boost:1]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.MaxAnisotropy:8]]
[2021.05.18-06.05.35:336][  0]LogConfig: Setting CVar [[r.VT.MaxAnisotropy:8]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Streaming.LimitPoolSizeToVRAM:0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Streaming.PoolSize:1000]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Streaming.MaxEffectiveScreenSize:0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Applying CVar settings from Section [EffectsQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.TranslucencyLightingVolumeDim:64]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.RefractionQuality:2]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SSR.Quality:3]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SSR.HalfResSceneColor:0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SceneColorFormat:4]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.DetailMode:2]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.TranslucencyVolumeBlur:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.MaterialQualityLevel:1 ; High quality]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.AnisotropicMaterials:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SSS.Scale:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SSS.SampleSet:2]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SSS.Quality:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SSS.HalfRes:0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SSGI.Quality:3]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.EmitterSpawnRateScale:1.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.ParticleLightQuality:2]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.FastApplyOnOpaque:1 ; Always have FastSkyLUT 1 in this case to avoid wrong sky]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.SampleCountMaxPerSlice:4]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.DepthResolution:16.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT.SampleCountMin:4.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT.SampleCountMax:128.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.SampleCountMin:4.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.SampleCountMax:128.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.TransmittanceLUT.UseSmallFormat:0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.TransmittanceLUT.SampleCount:10.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.MultiScatteringLUT.SampleCount:15.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Applying CVar settings from Section [FoliageQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[foliage.DensityScale:1.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[grass.DensityScale:1.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Applying CVar settings from Section [ShadingQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.HairStrands.SkyLighting.IntegrationType:2]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.HairStrands.SkyAO.SampleCount:4]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.HairStrands.Visibility.MSAA.SamplePerPixel:4]]
[2021.05.18-06.05.35:337][  0]LogLinux: Selected Device Profile: [Linux]
[2021.05.18-06.05.35:337][  0]LogInit: Applying CVar settings loaded from the selected device profile: [Linux]
[2021.05.18-06.05.35:337][  0]LogHAL: Display: Platform has ~ 4 GB [16724201472 / 4294967296 / 16], which maps to Smallest [LargestMinGB=32, LargerMinGB=12, DefaultMinGB=8, SmallerMinGB=6, SmallestMinGB=0)
[2021.05.18-06.05.35:337][  0]LogInit: Going up to parent DeviceProfile []
[2021.05.18-06.05.35:337][  0]LogConfig: Applying CVar settings from Section [ViewDistanceQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkeletalMeshLODBias:0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.ViewDistanceScale:1.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Applying CVar settings from Section [AntiAliasingQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.PostProcessAAQuality:4]]
[2021.05.18-06.05.35:337][  0]LogConfig: Applying CVar settings from Section [ShadowQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.LightFunctionQuality:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.ShadowQuality:5]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Shadow.CSM.MaxCascades:10]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Shadow.MaxResolution:2048]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Shadow.MaxCSMResolution:2048]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Shadow.RadiusThreshold:0.01]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Shadow.DistanceScale:1.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Shadow.CSM.TransitionScale:1.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Shadow.PreShadowResolutionFactor:1.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.DistanceFieldShadowing:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.DistanceFieldAO:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.AOQuality:2]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.VolumetricFog:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.VolumetricFog.GridPixelSize:8]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.VolumetricFog.GridSizeZ:128]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.VolumetricFog.HistoryMissSupersampleCount:4]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.LightMaxDrawDistanceScale:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.CapsuleShadows:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Applying CVar settings from Section [PostProcessQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.MotionBlurQuality:4]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.AmbientOcclusionMipLevelFactor:0.4]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.AmbientOcclusionMaxQuality:100]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.AmbientOcclusionLevels:-1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.AmbientOcclusionRadiusScale:1.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.DepthOfFieldQuality:2]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.RenderTargetPoolMin:400]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.LensFlareQuality:2]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SceneColorFringeQuality:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.EyeAdaptationQuality:2]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.BloomQuality:5]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.FastBlurThreshold:100]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Upscale.Quality:3]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Tonemapper.GrainQuantization:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.LightShaftQuality:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Filter.SizeScale:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Tonemapper.Quality:5]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.DOF.Gather.AccumulatorQuality:1        ; higher gathering accumulator quality]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.DOF.Gather.PostfilterMethod:1          ; Median3x3 postfilering method]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.DOF.Gather.EnableBokehSettings:0       ; no bokeh simulation when gathering]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.DOF.Gather.RingCount:4                 ; medium number of samples when gathering]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.DOF.Scatter.ForegroundCompositing:1    ; additive foreground scattering]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.DOF.Scatter.BackgroundCompositing:2    ; additive background scattering]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.DOF.Scatter.EnableBokehSettings:1      ; bokeh simulation when scattering]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.DOF.Scatter.MaxSpriteRatio:0.1         ; only a maximum of 10% of scattered bokeh]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.DOF.Recombine.Quality:1                ; cheap slight out of focus]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.DOF.Recombine.EnableBokehSettings:0    ; no bokeh simulation on slight out of focus]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.DOF.TemporalAAQuality:1                ; more stable temporal accumulation]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.DOF.Kernel.MaxForegroundRadius:0.025]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.DOF.Kernel.MaxBackgroundRadius:0.025]]
[2021.05.18-06.05.35:337][  0]LogConfig: Applying CVar settings from Section [TextureQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Streaming.MipBias:0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Streaming.AmortizeCPUToGPUCopy:0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Streaming.MaxNumTexturesToStreamPerFrame:0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Streaming.Boost:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.MaxAnisotropy:8]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.VT.MaxAnisotropy:8]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Streaming.LimitPoolSizeToVRAM:0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Streaming.PoolSize:1000]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.Streaming.MaxEffectiveScreenSize:0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Applying CVar settings from Section [EffectsQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.TranslucencyLightingVolumeDim:64]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.RefractionQuality:2]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SSR.Quality:3]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SSR.HalfResSceneColor:0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SceneColorFormat:4]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.DetailMode:2]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.TranslucencyVolumeBlur:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.MaterialQualityLevel:1 ; High quality]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.AnisotropicMaterials:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SSS.Scale:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SSS.SampleSet:2]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SSS.Quality:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SSS.HalfRes:0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SSGI.Quality:3]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.EmitterSpawnRateScale:1.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.ParticleLightQuality:2]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.FastApplyOnOpaque:1 ; Always have FastSkyLUT 1 in this case to avoid wrong sky]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.SampleCountMaxPerSlice:4]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.DepthResolution:16.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT:1]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT.SampleCountMin:4.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT.SampleCountMax:128.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.SampleCountMin:4.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.SampleCountMax:128.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.TransmittanceLUT.UseSmallFormat:0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.TransmittanceLUT.SampleCount:10.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.MultiScatteringLUT.SampleCount:15.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Applying CVar settings from Section [FoliageQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[foliage.DensityScale:1.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[grass.DensityScale:1.0]]
[2021.05.18-06.05.35:337][  0]LogConfig: Applying CVar settings from Section [ShadingQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.HairStrands.SkyLighting.IntegrationType:2]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.HairStrands.SkyAO.SampleCount:4]]
[2021.05.18-06.05.35:337][  0]LogConfig: Setting CVar [[r.HairStrands.Visibility.MSAA.SamplePerPixel:4]]
[2021.05.18-06.05.35:337][  0]LogConfig: Applying CVar settings from Section [Startup] File [../../../Engine/Config/ConsoleVariables.ini]
[2021.05.18-06.05.35:338][  0]LogConfig: Setting CVar [[net.UseAdaptiveNetUpdateFrequency:0]]
[2021.05.18-06.05.35:338][  0]LogConfig: Setting CVar [[p.chaos.AllowCreatePhysxBodies:1]]
[2021.05.18-06.05.35:338][  0]LogConfig: Setting CVar [[fx.SkipVectorVMBackendOptimizations:1]]
[2021.05.18-06.05.35:338][  0]LogConfig: Applying CVar settings from Section [ConsoleVariables] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2021.05.18-06.05.35:338][  0]LogConfig: Setting CVar [[g.TimeoutForBlockOnRenderFence:60000]]
[2021.05.18-06.05.35:338][  0]LogConfig: Applying CVar settings from Section [ConsoleVariables] File [../../../Engine/Saved/Config/Linux/Editor.ini]
[2021.05.18-06.05.35:338][  0]LogInit: Unix hardware info:
[2021.05.18-06.05.35:338][  0]LogInit:  - we are the first instance of this executable
[2021.05.18-06.05.35:338][  0]LogInit:  - this process' id (pid) is 29371, parent process' id (ppid) is 29303
[2021.05.18-06.05.35:338][  0]LogInit:  - we are not running under debugger
[2021.05.18-06.05.35:338][  0]LogInit:  - machine network name is 'intel-x86-64'
[2021.05.18-06.05.35:338][  0]LogInit:  - user name is 'test' (test)
[2021.05.18-06.05.35:338][  0]LogInit:  - we're logged in locally
[2021.05.18-06.05.35:338][  0]LogInit:  - we're running with rendering
[2021.05.18-06.05.35:338][  0]LogInit:  - CPU: GenuineIntel 'Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz' (signature: 0x306C3)
[2021.05.18-06.05.35:338][  0]LogInit:  - Number of physical cores available for the process: 4
[2021.05.18-06.05.35:338][  0]LogInit:  - Number of logical cores available for the process: 8
[2021.05.18-06.05.35:338][  0]LogInit:  - Cache line size: 64
[2021.05.18-06.05.35:338][  0]LogInit:  - Memory allocator used: binned2
[2021.05.18-06.05.35:338][  0]LogInit:  - This binary is optimized with LTO: no, PGO: no, instrumented for PGO data collection: no
[2021.05.18-06.05.35:338][  0]LogInit:  - This is an internal build.
[2021.05.18-06.05.35:338][  0]LogCore: Benchmarking clocks:
[2021.05.18-06.05.35:338][  0]LogCore:  - CLOCK_MONOTONIC (id=1) can sustain 70612387 (70612K, 71M) calls per second without zero deltas.
[2021.05.18-06.05.35:338][  0]LogCore:  - CLOCK_MONOTONIC_RAW (id=4) can sustain 69328550 (69329K, 69M) calls per second without zero deltas.
[2021.05.18-06.05.35:338][  0]LogCore:  - CLOCK_MONOTONIC_COARSE (id=6) can sustain 178704984 (178705K, 179M) calls per second with 99.999435% zero deltas.
[2021.05.18-06.05.35:338][  0]LogCore: Selected clock_id 1 (CLOCK_MONOTONIC) since it is the fastest support clock without zero deltas.
[2021.05.18-06.05.35:338][  0]LogInit: Unix-specific commandline switches:
[2021.05.18-06.05.35:338][  0]LogInit:  -ansimalloc - use malloc()/free() from libc (useful for tools like valgrind and electric fence)
[2021.05.18-06.05.35:338][  0]LogInit:  -jemalloc - use jemalloc for all memory allocation
[2021.05.18-06.05.35:338][  0]LogInit:  -binnedmalloc - use binned malloc  for all memory allocation
[2021.05.18-06.05.35:338][  0]LogInit:  -filemapcachesize=NUMBER - set the size for case-sensitive file mapping cache
[2021.05.18-06.05.35:338][  0]LogInit:  -useksm - uses kernel same-page mapping (KSM) for mapped memory (OFF)
[2021.05.18-06.05.35:338][  0]LogInit:  -ksmmergeall - marks all mmap'd memory pages suitable for KSM (OFF)
[2021.05.18-06.05.35:338][  0]LogInit:  -preloadmodulesymbols - Loads the main module symbols file into memory (OFF)
[2021.05.18-06.05.35:338][  0]LogInit:  -sigdfl=SIGNAL - Allows a specific signal to be set to its default handler rather then ignoring the signal
[2021.05.18-06.05.35:338][  0]LogInit:  -httpproxy=ADDRESS:PORT - redirects HTTP requests to a proxy (only supported if compiled with libcurl)
[2021.05.18-06.05.35:338][  0]LogInit:  -reuseconn - allow libcurl to reuse HTTP connections (only matters if compiled with libcurl)
[2021.05.18-06.05.35:338][  0]LogInit:  -virtmemkb=NUMBER - sets process virtual memory (address space) limit (overrides VirtualMemoryLimitInKB value from .ini)
[2021.05.18-06.05.35:338][  0]LogInit: Initializing SDL.
No protocol specified
[2021.05.18-06.05.35:343][  0]LogInit: Warning: Could not initialize SDL: No available video device
[2021.05.18-06.05.35:343][  0]LogInit:  - Physical RAM available (not considering process quota): 16 GB (15949 MB, 16332228 KB, 16724201472 bytes)
[2021.05.18-06.05.35:343][  0]LogInit:  - VirtualMemoryAllocator pools will grow at scale 1.4
[2021.05.18-06.05.35:343][  0]LogInit:  - MemoryRangeDecommit() will be a no-op (re-run with -vmapoolevict to change)
[2021.05.18-06.05.35:365][  0]LogInit: Physics initialised using underlying interface: PhysX
[2021.05.18-06.05.35:384][  0]LogInit: Using OS detected language (en-US-POSIX).
[2021.05.18-06.05.35:384][  0]LogInit: Using OS detected locale (en-US-POSIX).
[2021.05.18-06.05.35:385][  0]LogTextLocalizationManager: No specific localization for 'en-US-POSIX' exists, so the 'en' localization will be used.
[2021.05.18-06.05.35:521][  0]LogInit: Initializing SDL.
No protocol specified
[2021.05.18-06.05.35:527][  0]LogInit: Warning: Could not initialize SDL: No available video device
[2021.05.18-06.05.35:527][  0]LogInit: Warning: FLinuxSplashState::InitSplashResources() : InitSDL() failed, there will be no splash.
[2021.05.18-06.05.35:527][  0]LogInit: Initializing SDL.
No protocol specified
[2021.05.18-06.05.35:532][  0]LogInit: Warning: Could not initialize SDL: No available video device
[2021.05.18-06.05.35:532][  0]LogInit: Error: FLinuxApplication::CreateLinuxApplication() : InitSDL() failed, cannot create application instance.
[2021.05.18-06.05.35:532][  0]LogCore: FUnixPlatformMisc::RequestExit(bForce=true, ReturnCode=1)
[2021.05.18-06.05.35:532][  0]LogCore: FunixPlatformMisc::RequestExit(1)
```
#### Solution
Add none root user (test) and update the permission of the UE folder
```
$ useradd test
$ passwd test
$ reboot
$ Login by “test” user 
```
```
$ chmod -R 777 /UnrealEngine-release/
```
* Failed to start UE because of lacking libraries
```
root@intel-x86-64:/# cat /home/test/UE.txt1 
sh-5.1$ ./UE4Editor
Increasing per-process limit of core file size to infinity.
sh: line 1: xdg-user-dir: command not found
LogInit: LLM is enabled
LogInit: LLM CsvWriter: off TraceWriter: off
LogInit: Display: Running engine without a game
LogPlatformFile: Not using cached read wrapper
LogTaskGraph: Started task graph with 5 named threads and 14 total threads with 3 sets of task threads.
LogStats: Stats thread started at 0.086308
LogICUInternationalization: ICU TimeZone Detection - Raw Offset: +0:00, Platform Override: ''
LogPluginManager: Mounting plugin MeshPainting
LogPluginManager: Mounting plugin XGEController
LogPluginManager: Mounting plugin Paper2D
LogPluginManager: Mounting plugin LauncherChunkInstaller
LogPluginManager: Mounting plugin ScreenshotTools
LogPluginManager: Mounting plugin EnvironmentQueryEditor
LogPluginManager: Mounting plugin AISupport
LogPluginManager: Mounting plugin CameraShakePreviewer
LogPluginManager: Mounting plugin PlatformCrypto
LogPluginManager: Mounting plugin MotoSynth
LogPluginManager: Mounting plugin SkeletalReduction
LogPluginManager: Mounting plugin CharacterAI
LogPluginManager: Mounting plugin ProxyLODPlugin
LogPluginManager: Mounting plugin ChaosNiagara
LogPluginManager: Mounting plugin ChaosSolverPlugin
LogPluginManager: Mounting plugin ChaosCloth
LogPluginManager: Mounting plugin AutomationUtils
LogPluginManager: Mounting plugin PlanarCut
LogPluginManager: Mounting plugin DatasmithContent
LogPluginManager: Mounting plugin VariantManagerContent
LogPluginManager: Mounting plugin AlembicImporter
LogPluginManager: Mounting plugin GeometryCache
LogPluginManager: Mounting plugin GeometryCollectionPlugin
LogPluginManager: Mounting plugin BackChannel
LogPluginManager: Mounting plugin ChaosClothEditor
LogPluginManager: Mounting plugin GeometryProcessing
LogPluginManager: Mounting plugin ChaosEditor
LogPluginManager: Mounting plugin LevelSequenceEditor
LogPluginManager: Mounting plugin MLSDK
LogPluginManager: Mounting plugin MatineeToLevelSequence
LogPluginManager: Mounting plugin ActorSequence
LogPluginManager: Mounting plugin TemplateSequence
LogPluginManager: Mounting plugin MagicLeap
LogPluginManager: Mounting plugin MagicLeapMedia
LogPluginManager: Mounting plugin MagicLeapPassableWorld
LogPluginManager: Mounting plugin MagicLeapLightEstimation
LogPluginManager: Mounting plugin LuminPlatformFeatures
LogPluginManager: Mounting plugin Niagara
LogPluginManager: Mounting plugin PostSplashScreen
LogPluginManager: Mounting plugin ChunkDownloader
LogPluginManager: Mounting plugin PhysXVehicles
LogPluginManager: Mounting plugin OnlineSubsystem
LogPluginManager: Mounting plugin WebMMoviePlayer
LogPluginManager: Mounting plugin AssetTags
LogPluginManager: Mounting plugin SoundFields
LogPluginManager: Mounting plugin OnlineSubsystemUtils
LogPluginManager: Mounting plugin AppleImageUtils
LogPluginManager: Mounting plugin PropertyAccessEditor
LogPluginManager: Mounting plugin OnlineSubsystemNull
LogPluginManager: Mounting plugin MobilePatchingUtils
LogPluginManager: Mounting plugin SignificanceManager
LogPluginManager: Mounting plugin AssetManagerEditor
LogPluginManager: Mounting plugin WindowsMoviePlayer
LogPluginManager: Mounting plugin EditableMesh
LogPluginManager: Mounting plugin CableComponent
LogPluginManager: Mounting plugin MobileLauncherProfileWizard
LogPluginManager: Mounting plugin CryptoKeys
LogPluginManager: Mounting plugin PluginBrowser
LogPluginManager: Mounting plugin DataValidation
LogPluginManager: Mounting plugin CustomMeshComponent
LogPluginManager: Mounting plugin AndroidDeviceProfileSelector
LogPluginManager: Mounting plugin FacialAnimation
LogPluginManager: Mounting plugin GameplayTagsEditor
LogPluginManager: Mounting plugin MaterialAnalyzer
LogPluginManager: Mounting plugin MacGraphicsSwitching
LogPluginManager: Mounting plugin GeometryMode
LogPluginManager: Mounting plugin CurveEditorTools
LogPluginManager: Mounting plugin GoogleCloudMessaging
LogPluginManager: Mounting plugin SpeedTreeImporter
LogPluginManager: Mounting plugin ArchVisCharacter
LogPluginManager: Mounting plugin LinuxDeviceProfileSelector
LogPluginManager: Mounting plugin RuntimePhysXCooking
LogPluginManager: Mounting plugin AudioSynesthesia
LogPluginManager: Mounting plugin LocationServicesBPLibrary
LogPluginManager: Mounting plugin AudioCapture
LogPluginManager: Mounting plugin CodeLiteSourceCodeAccess
LogPluginManager: Mounting plugin GitSourceControl
LogPluginManager: Mounting plugin GooglePAD
LogPluginManager: Mounting plugin ActorLayerUtilities
LogPluginManager: Mounting plugin PropertyAccessNode
LogPluginManager: Mounting plugin Synthesis
LogPluginManager: Mounting plugin TcpMessaging
LogPluginManager: Mounting plugin PerforceSourceControl
LogPluginManager: Mounting plugin UdpMessaging
LogPluginManager: Mounting plugin RiderSourceCodeAccess
LogPluginManager: Mounting plugin VisualStudioSourceCodeAccess
LogPluginManager: Mounting plugin NullSourceCodeAccess
LogPluginManager: Mounting plugin CLionSourceCodeAccess
LogPluginManager: Mounting plugin UObjectPlugin
LogPluginManager: Mounting plugin IOSDeviceProfileSelector
LogPluginManager: Mounting plugin AppleMoviePlayer
LogPluginManager: Mounting plugin AnimationSharing
LogPluginManager: Mounting plugin XCodeSourceCodeAccess
LogPluginManager: Mounting plugin SubversionSourceControl
LogPluginManager: Mounting plugin ProceduralMeshComponent
LogPluginManager: Mounting plugin KDevelopSourceCodeAccess
LogPluginManager: Mounting plugin AndroidPermission
LogPluginManager: Mounting plugin ExampleDeviceProfileSelector
LogPluginManager: Mounting plugin VisualStudioCodeSourceCodeAccess
LogPluginManager: Mounting plugin PluginUtils
LogPluginManager: Mounting plugin LightPropagationVolume
LogPluginManager: Mounting plugin PlasticSourceControl
LogPluginManager: Mounting plugin AndroidMoviePlayer
LogPluginManager: Mounting plugin MediaCompositing
LogPluginManager: Mounting plugin WebMMedia
LogPluginManager: Mounting plugin AndroidMedia
LogPluginManager: Mounting plugin MediaPlayerEditor
LogPluginManager: Mounting plugin ImgMedia
LogPluginManager: Mounting plugin AvfMedia
LogPluginManager: Mounting plugin WmfMedia
LogPluginManager: Mounting plugin OnlineSubsystemIOS
LogPluginManager: Mounting plugin OnlineSubsystemGooglePlay
LogPluginManager: Mounting plugin ContentBrowserAssetDataSource
LogPluginManager: Mounting plugin ContentBrowserClassDataSource
LogPluginManager: Mounting plugin OculusVR
LogPluginManager: Mounting plugin SteamVR
LogInit: Using libcurl 7.65.3-DEV
LogInit:  - built for x86_64-unknown-linux-gnu
LogInit:  - supports SSL with OpenSSL/1.1.1c
LogInit:  - supports HTTP deflate (compression) using libz 1.2.8
LogInit:  - other features:
LogInit:      CURL_VERSION_SSL
LogInit:      CURL_VERSION_LIBZ
LogInit:      CURL_VERSION_IPV6
LogInit:      CURL_VERSION_ASYNCHDNS
LogInit:      CURL_VERSION_LARGEFILE
LogInit:      CURL_VERSION_TLSAUTH_SRP
LogInit:  CurlRequestOptions (configurable via config and command line):
LogInit:  - bVerifyPeer = true  - Libcurl will verify peer certificate
LogInit:  - bUseHttpProxy = false  - Libcurl will NOT use HTTP proxy
LogInit:  - bDontReuseConnections = false  - Libcurl will reuse connections
LogInit:  - MaxHostConnections = 16  - Libcurl will limit the number of connections to a host
LogInit:  - LocalHostAddr = Default
LogInit:  - BufferSize = 65536
LogOnline: OSS: Creating online subsystem instance for: NULL
LogOnline: OSS: TryLoadSubsystemAndSetDefault: Loaded subsystem for module [NULL]
LogInit: Build: ++UE4+Release-4.26-CL-0
LogInit: Engine Version: 4.26.2-0+++UE4+Release-4.26
LogInit: Compatible Engine Version: 4.26.0-0+++UE4+Release-4.26
LogInit: Net CL: 0
LogInit: OS: GenericOSVersionLabel (GenericOSSubVersionLabel), CPU: Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz, GPU: GenericGPUBrand
LogInit: Compiled (64-bit): May 18 2021 03:42:04
LogInit: Compiled with Clang: 10.0.1 
LogInit: Build Configuration: Development
LogInit: Branch Name: ++UE4+Release-4.26
LogInit: Command Line: 
LogInit: Base Directory: /UnrealEngine-release/Engine/Binaries/Linux/
LogInit: Allocator: binned2
LogInit: Installed Engine Build: 0
LogDevObjectVersion: Number of dev versions registered: 29
LogDevObjectVersion:   Dev-Blueprints (B0D832E4-1F89-4F0D-ACCF-7EB736FD4AA2): 10
LogDevObjectVersion:   Dev-Build (E1C64328-A22C-4D53-A36C-8E866417BD8C): 0
LogDevObjectVersion:   Dev-Core (375EC13C-06E4-48FB-B500-84F0262A717E): 4
LogDevObjectVersion:   Dev-Editor (E4B068ED-F494-42E9-A231-DA0B2E46BB41): 40
LogDevObjectVersion:   Dev-Framework (CFFC743F-43B0-4480-9391-14DF171D2073): 37
LogDevObjectVersion:   Dev-Mobile (B02B49B5-BB20-44E9-A304-32B752E40360): 3
LogDevObjectVersion:   Dev-Networking (A4E4105C-59A1-49B5-A7C5-40C4547EDFEE): 0
LogDevObjectVersion:   Dev-Online (39C831C9-5AE6-47DC-9A44-9C173E1C8E7C): 0
LogDevObjectVersion:   Dev-Physics (78F01B33-EBEA-4F98-B9B4-84EACCB95AA2): 4
LogDevObjectVersion:   Dev-Platform (6631380F-2D4D-43E0-8009-CF276956A95A): 0
LogDevObjectVersion:   Dev-Rendering (12F88B9F-8875-4AFC-A67C-D90C383ABD29): 44
LogDevObjectVersion:   Dev-Sequencer (7B5AE74C-D270-4C10-A958-57980B212A5A): 12
LogDevObjectVersion:   Dev-VR (D7296918-1DD6-4BDD-9DE2-64A83CC13884): 3
LogDevObjectVersion:   Dev-LoadTimes (C2A15278-BFE7-4AFE-6C17-90FF531DF755): 1
LogDevObjectVersion:   Private-Geometry (6EACA3D4-40EC-4CC1-B786-8BED09428FC5): 3
LogDevObjectVersion:   Dev-AnimPhys (29E575DD-E0A3-4627-9D10-D276232CDCEA): 17
LogDevObjectVersion:   Dev-Anim (AF43A65D-7FD3-4947-9873-3E8ED9C1BB05): 15
LogDevObjectVersion:   Dev-ReflectionCapture (6B266CEC-1EC7-4B8F-A30B-E4D90942FC07): 1
LogDevObjectVersion:   Dev-Automation (0DF73D61-A23F-47EA-B727-89E90C41499A): 1
LogDevObjectVersion:   FortniteMain (601D1886-AC64-4F84-AA16-D3DE0DEAC7D6): 43
LogDevObjectVersion:   FortniteRelease (E7086368-6B23-4C58-8439-1B7016265E91): 1
LogDevObjectVersion:   Dev-Enterprise (9DFFBCD6-494F-0158-E221-12823C92A888): 10
LogDevObjectVersion:   Dev-Niagara (F2AED0AC-9AFE-416F-8664-AA7FFA26D6FC): 1
LogDevObjectVersion:   Dev-Destruction (174F1F0B-B4C6-45A5-B13F-2EE8D0FB917D): 10
LogDevObjectVersion:   Dev-Physics-Ext (35F94A83-E258-406C-A318-09F59610247C): 40
LogDevObjectVersion:   Dev-PhysicsMaterial-Chaos (B68FC16E-8B1B-42E2-B453-215C058844FE): 1
LogDevObjectVersion:   Dev-CineCamera (B2E18506-4273-CFC2-A54E-F4BB758BBA07): 1
LogDevObjectVersion:   Dev-VirtualProduction (64F58936-FD1B-42BA-BA96-7289D5D0FA4E): 1
LogDevObjectVersion:   Dev-MediaFramework (6F0ED827-A609-4895-9C91-998D90180EA4): 2
LogInit: Presizing for max 25165824 objects, including 0 objects not considered by GC, pre-allocating 0 bytes for permanent pool.
LogConfig: Applying CVar settings from Section [/Script/Engine.StreamingSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
LogConfig: Setting CVar [[s.MinBulkDataSizeForAsyncLoading:131072]]
LogConfig: Setting CVar [[s.AsyncLoadingThreadEnabled:0]]
LogConfig: Setting CVar [[s.EventDrivenLoaderEnabled:1]]
LogConfig: Setting CVar [[s.WarnIfTimeLimitExceeded:0]]
LogConfig: Setting CVar [[s.TimeLimitExceededMultiplier:1.5]]
LogConfig: Setting CVar [[s.TimeLimitExceededMinTime:0.005]]
LogConfig: Setting CVar [[s.UseBackgroundLevelStreaming:1]]
LogConfig: Setting CVar [[s.PriorityAsyncLoadingExtraTime:15.0]]
LogConfig: Setting CVar [[s.LevelStreamingActorsUpdateTimeLimit:5.0]]
LogConfig: Setting CVar [[s.PriorityLevelStreamingActorsUpdateExtraTime:5.0]]
LogConfig: Setting CVar [[s.LevelStreamingComponentsRegistrationGranularity:10]]
LogConfig: Setting CVar [[s.UnregisterComponentsTimeLimit:1.0]]
LogConfig: Setting CVar [[s.LevelStreamingComponentsUnregistrationGranularity:5]]
LogConfig: Setting CVar [[s.FlushStreamingOnExit:1]]
LogInit: Object subsystem initialized
LogConfig: Setting CVar [[con.DebugEarlyDefault:1]]
LogConfig: Setting CVar [[r.setres:1280x720]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[r.VSync:0]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[r.RHICmdBypass:0]]
[2021.05.18-06.16.21:184][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.RendererSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[r.GPUCrashDebugging:0]]
[2021.05.18-06.16.21:184][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.RendererOverrideSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2021.05.18-06.16.21:184][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.StreamingSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[s.MinBulkDataSizeForAsyncLoading:131072]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[s.AsyncLoadingThreadEnabled:0]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[s.EventDrivenLoaderEnabled:1]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[s.WarnIfTimeLimitExceeded:0]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[s.TimeLimitExceededMultiplier:1.5]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[s.TimeLimitExceededMinTime:0.005]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[s.UseBackgroundLevelStreaming:1]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[s.PriorityAsyncLoadingExtraTime:15.0]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[s.LevelStreamingActorsUpdateTimeLimit:5.0]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[s.PriorityLevelStreamingActorsUpdateExtraTime:5.0]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[s.LevelStreamingComponentsRegistrationGranularity:10]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[s.UnregisterComponentsTimeLimit:1.0]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[s.LevelStreamingComponentsUnregistrationGranularity:5]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[s.FlushStreamingOnExit:1]]
[2021.05.18-06.16.21:184][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.GarbageCollectionSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[gc.MaxObjectsNotConsideredByGC:1]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[gc.SizeOfPermanentObjectPool:0]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[gc.FlushStreamingOnGC:0]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[gc.NumRetriesBeforeForcingGC:10]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[gc.AllowParallelGC:1]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[gc.TimeBetweenPurgingPendingKillObjects:61.1]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[gc.MaxObjectsInEditor:25165824]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[gc.IncrementalBeginDestroyEnabled:1]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[gc.CreateGCClusters:1]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[gc.MinGCClusterSize:5]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[gc.ActorClusteringEnabled:0]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[gc.BlueprintClusteringEnabled:0]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[gc.UseDisregardForGCOnDedicatedServers:0]]
[2021.05.18-06.16.21:184][  0]LogConfig: Setting CVar [[gc.MultithreadedDestructionEnabled:1]]
[2021.05.18-06.16.21:184][  0]LogConfig: Applying CVar settings from Section [/Script/Engine.NetworkSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2021.05.18-06.16.21:184][  0]LogConfig: Applying CVar settings from Section [/Script/UnrealEd.CookerSettings] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2021.05.18-06.16.21:184][  0]LogInit: Initializing SDL.
No protocol specified
[2021.05.18-06.16.21:191][  0]LogInit: Warning: Could not initialize SDL: No available video device
[2021.05.18-06.16.21:191][  0]LogInit: Warning: FDisplayMetrics::GetDisplayMetrics: InitSDL() failed, cannot get display metrics
[2021.05.18-06.16.21:191][  0]LogConfig: Applying CVar settings from Section [ViewDistanceQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.SkeletalMeshLODBias:0]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.ViewDistanceScale:1.0]]
[2021.05.18-06.16.21:191][  0]LogConfig: Applying CVar settings from Section [AntiAliasingQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.PostProcessAAQuality:4]]
[2021.05.18-06.16.21:191][  0]LogConfig: Applying CVar settings from Section [ShadowQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.LightFunctionQuality:1]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.ShadowQuality:5]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.Shadow.CSM.MaxCascades:10]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.Shadow.MaxResolution:2048]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.Shadow.MaxCSMResolution:2048]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.Shadow.RadiusThreshold:0.01]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.Shadow.DistanceScale:1.0]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.Shadow.CSM.TransitionScale:1.0]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.Shadow.PreShadowResolutionFactor:1.0]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.DistanceFieldShadowing:1]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.DistanceFieldAO:1]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.AOQuality:2]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.VolumetricFog:1]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.VolumetricFog.GridPixelSize:8]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.VolumetricFog.GridSizeZ:128]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.VolumetricFog.HistoryMissSupersampleCount:4]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.LightMaxDrawDistanceScale:1]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.CapsuleShadows:1]]
[2021.05.18-06.16.21:191][  0]LogConfig: Applying CVar settings from Section [PostProcessQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.MotionBlurQuality:4]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.AmbientOcclusionMipLevelFactor:0.4]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.AmbientOcclusionMaxQuality:100]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.AmbientOcclusionLevels:-1]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.AmbientOcclusionRadiusScale:1.0]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.DepthOfFieldQuality:2]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.RenderTargetPoolMin:400]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.LensFlareQuality:2]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.SceneColorFringeQuality:1]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.EyeAdaptationQuality:2]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.BloomQuality:5]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.FastBlurThreshold:100]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.Upscale.Quality:3]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.Tonemapper.GrainQuantization:1]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.LightShaftQuality:1]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.Filter.SizeScale:1]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.Tonemapper.Quality:5]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.DOF.Gather.AccumulatorQuality:1        ; higher gathering accumulator quality]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.DOF.Gather.PostfilterMethod:1          ; Median3x3 postfilering method]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.DOF.Gather.EnableBokehSettings:0       ; no bokeh simulation when gathering]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.DOF.Gather.RingCount:4                 ; medium number of samples when gathering]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.DOF.Scatter.ForegroundCompositing:1    ; additive foreground scattering]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.DOF.Scatter.BackgroundCompositing:2    ; additive background scattering]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.DOF.Scatter.EnableBokehSettings:1      ; bokeh simulation when scattering]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.DOF.Scatter.MaxSpriteRatio:0.1         ; only a maximum of 10% of scattered bokeh]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.DOF.Recombine.Quality:1                ; cheap slight out of focus]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.DOF.Recombine.EnableBokehSettings:0    ; no bokeh simulation on slight out of focus]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.DOF.TemporalAAQuality:1                ; more stable temporal accumulation]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.DOF.Kernel.MaxForegroundRadius:0.025]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.DOF.Kernel.MaxBackgroundRadius:0.025]]
[2021.05.18-06.16.21:191][  0]LogConfig: Applying CVar settings from Section [TextureQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.Streaming.MipBias:0]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.Streaming.AmortizeCPUToGPUCopy:0]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.Streaming.MaxNumTexturesToStreamPerFrame:0]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.Streaming.Boost:1]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.MaxAnisotropy:8]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.VT.MaxAnisotropy:8]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.Streaming.LimitPoolSizeToVRAM:0]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.Streaming.PoolSize:1000]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.Streaming.MaxEffectiveScreenSize:0]]
[2021.05.18-06.16.21:191][  0]LogConfig: Applying CVar settings from Section [EffectsQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.TranslucencyLightingVolumeDim:64]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.RefractionQuality:2]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.SSR.Quality:3]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.SSR.HalfResSceneColor:0]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.SceneColorFormat:4]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.DetailMode:2]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.TranslucencyVolumeBlur:1]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.MaterialQualityLevel:1 ; High quality]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.AnisotropicMaterials:1]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.SSS.Scale:1]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.SSS.SampleSet:2]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.SSS.Quality:1]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.SSS.HalfRes:0]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.SSGI.Quality:3]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.EmitterSpawnRateScale:1.0]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.ParticleLightQuality:2]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.FastApplyOnOpaque:1 ; Always have FastSkyLUT 1 in this case to avoid wrong sky]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.SampleCountMaxPerSlice:4]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.DepthResolution:16.0]]
[2021.05.18-06.16.21:191][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT:1]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT.SampleCountMin:4.0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT.SampleCountMax:128.0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.SampleCountMin:4.0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.SampleCountMax:128.0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.TransmittanceLUT.UseSmallFormat:0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.TransmittanceLUT.SampleCount:10.0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.MultiScatteringLUT.SampleCount:15.0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Applying CVar settings from Section [FoliageQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[foliage.DensityScale:1.0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[grass.DensityScale:1.0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Applying CVar settings from Section [ShadingQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.HairStrands.SkyLighting.IntegrationType:2]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.HairStrands.SkyAO.SampleCount:4]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.HairStrands.Visibility.MSAA.SamplePerPixel:4]]
[2021.05.18-06.16.21:192][  0]LogLinux: Selected Device Profile: [Linux]
[2021.05.18-06.16.21:192][  0]LogInit: Applying CVar settings loaded from the selected device profile: [Linux]
[2021.05.18-06.16.21:192][  0]LogHAL: Display: Platform has ~ 4 GB [16724201472 / 4294967296 / 16], which maps to Smallest [LargestMinGB=32, LargerMinGB=12, DefaultMinGB=8, SmallerMinGB=6, SmallestMinGB=0)
[2021.05.18-06.16.21:192][  0]LogInit: Going up to parent DeviceProfile []
[2021.05.18-06.16.21:192][  0]LogConfig: Applying CVar settings from Section [ViewDistanceQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.SkeletalMeshLODBias:0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.ViewDistanceScale:1.0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Applying CVar settings from Section [AntiAliasingQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.PostProcessAAQuality:4]]
[2021.05.18-06.16.21:192][  0]LogConfig: Applying CVar settings from Section [ShadowQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.LightFunctionQuality:1]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.ShadowQuality:5]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.Shadow.CSM.MaxCascades:10]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.Shadow.MaxResolution:2048]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.Shadow.MaxCSMResolution:2048]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.Shadow.RadiusThreshold:0.01]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.Shadow.DistanceScale:1.0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.Shadow.CSM.TransitionScale:1.0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.Shadow.PreShadowResolutionFactor:1.0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.DistanceFieldShadowing:1]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.DistanceFieldAO:1]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.AOQuality:2]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.VolumetricFog:1]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.VolumetricFog.GridPixelSize:8]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.VolumetricFog.GridSizeZ:128]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.VolumetricFog.HistoryMissSupersampleCount:4]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.LightMaxDrawDistanceScale:1]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.CapsuleShadows:1]]
[2021.05.18-06.16.21:192][  0]LogConfig: Applying CVar settings from Section [PostProcessQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.MotionBlurQuality:4]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.AmbientOcclusionMipLevelFactor:0.4]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.AmbientOcclusionMaxQuality:100]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.AmbientOcclusionLevels:-1]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.AmbientOcclusionRadiusScale:1.0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.DepthOfFieldQuality:2]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.RenderTargetPoolMin:400]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.LensFlareQuality:2]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.SceneColorFringeQuality:1]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.EyeAdaptationQuality:2]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.BloomQuality:5]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.FastBlurThreshold:100]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.Upscale.Quality:3]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.Tonemapper.GrainQuantization:1]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.LightShaftQuality:1]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.Filter.SizeScale:1]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.Tonemapper.Quality:5]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.DOF.Gather.AccumulatorQuality:1        ; higher gathering accumulator quality]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.DOF.Gather.PostfilterMethod:1          ; Median3x3 postfilering method]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.DOF.Gather.EnableBokehSettings:0       ; no bokeh simulation when gathering]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.DOF.Gather.RingCount:4                 ; medium number of samples when gathering]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.DOF.Scatter.ForegroundCompositing:1    ; additive foreground scattering]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.DOF.Scatter.BackgroundCompositing:2    ; additive background scattering]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.DOF.Scatter.EnableBokehSettings:1      ; bokeh simulation when scattering]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.DOF.Scatter.MaxSpriteRatio:0.1         ; only a maximum of 10% of scattered bokeh]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.DOF.Recombine.Quality:1                ; cheap slight out of focus]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.DOF.Recombine.EnableBokehSettings:0    ; no bokeh simulation on slight out of focus]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.DOF.TemporalAAQuality:1                ; more stable temporal accumulation]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.DOF.Kernel.MaxForegroundRadius:0.025]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.DOF.Kernel.MaxBackgroundRadius:0.025]]
[2021.05.18-06.16.21:192][  0]LogConfig: Applying CVar settings from Section [TextureQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.Streaming.MipBias:0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.Streaming.AmortizeCPUToGPUCopy:0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.Streaming.MaxNumTexturesToStreamPerFrame:0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.Streaming.Boost:1]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.MaxAnisotropy:8]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.VT.MaxAnisotropy:8]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.Streaming.LimitPoolSizeToVRAM:0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.Streaming.PoolSize:1000]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.Streaming.MaxEffectiveScreenSize:0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Applying CVar settings from Section [EffectsQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.TranslucencyLightingVolumeDim:64]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.RefractionQuality:2]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.SSR.Quality:3]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.SSR.HalfResSceneColor:0]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.SceneColorFormat:4]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.DetailMode:2]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.TranslucencyVolumeBlur:1]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.MaterialQualityLevel:1 ; High quality]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.AnisotropicMaterials:1]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.SSS.Scale:1]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.SSS.SampleSet:2]]
[2021.05.18-06.16.21:192][  0]LogConfig: Setting CVar [[r.SSS.Quality:1]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[r.SSS.HalfRes:0]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[r.SSGI.Quality:3]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[r.EmitterSpawnRateScale:1.0]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[r.ParticleLightQuality:2]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.FastApplyOnOpaque:1 ; Always have FastSkyLUT 1 in this case to avoid wrong sky]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.SampleCountMaxPerSlice:4]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.AerialPerspectiveLUT.DepthResolution:16.0]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT:1]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT.SampleCountMin:4.0]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.FastSkyLUT.SampleCountMax:128.0]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.SampleCountMin:4.0]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.SampleCountMax:128.0]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.TransmittanceLUT.UseSmallFormat:0]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.TransmittanceLUT.SampleCount:10.0]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[r.SkyAtmosphere.MultiScatteringLUT.SampleCount:15.0]]
[2021.05.18-06.16.21:193][  0]LogConfig: Applying CVar settings from Section [FoliageQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[foliage.DensityScale:1.0]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[grass.DensityScale:1.0]]
[2021.05.18-06.16.21:193][  0]LogConfig: Applying CVar settings from Section [ShadingQuality@3] File [../../../Engine/Saved/Config/Linux/Scalability.ini]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[r.HairStrands.SkyLighting.IntegrationType:2]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[r.HairStrands.SkyAO.SampleCount:4]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[r.HairStrands.Visibility.MSAA.SamplePerPixel:4]]
[2021.05.18-06.16.21:193][  0]LogConfig: Applying CVar settings from Section [Startup] File [../../../Engine/Config/ConsoleVariables.ini]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[net.UseAdaptiveNetUpdateFrequency:0]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[p.chaos.AllowCreatePhysxBodies:1]]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[fx.SkipVectorVMBackendOptimizations:1]]
[2021.05.18-06.16.21:193][  0]LogConfig: Applying CVar settings from Section [ConsoleVariables] File [../../../Engine/Saved/Config/Linux/Engine.ini]
[2021.05.18-06.16.21:193][  0]LogConfig: Setting CVar [[g.TimeoutForBlockOnRenderFence:60000]]
[2021.05.18-06.16.21:193][  0]LogConfig: Applying CVar settings from Section [ConsoleVariables] File [../../../Engine/Saved/Config/Linux/Editor.ini]
[2021.05.18-06.16.21:193][  0]LogInit: Unix hardware info:
[2021.05.18-06.16.21:193][  0]LogInit:  - we are the first instance of this executable
[2021.05.18-06.16.21:193][  0]LogInit:  - this process' id (pid) is 29470, parent process' id (ppid) is 29303
[2021.05.18-06.16.21:193][  0]LogInit:  - we are not running under debugger
[2021.05.18-06.16.21:193][  0]LogInit:  - machine network name is 'intel-x86-64'
[2021.05.18-06.16.21:193][  0]LogInit:  - user name is 'test' (test)
[2021.05.18-06.16.21:193][  0]LogInit:  - we're logged in locally
[2021.05.18-06.16.21:193][  0]LogInit:  - we're running with rendering
[2021.05.18-06.16.21:193][  0]LogInit:  - CPU: GenuineIntel 'Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz' (signature: 0x306C3)
[2021.05.18-06.16.21:193][  0]LogInit:  - Number of physical cores available for the process: 4
[2021.05.18-06.16.21:193][  0]LogInit:  - Number of logical cores available for the process: 8
[2021.05.18-06.16.21:193][  0]LogInit:  - Cache line size: 64
[2021.05.18-06.16.21:193][  0]LogInit:  - Memory allocator used: binned2
[2021.05.18-06.16.21:193][  0]LogInit:  - This binary is optimized with LTO: no, PGO: no, instrumented for PGO data collection: no
[2021.05.18-06.16.21:193][  0]LogInit:  - This is an internal build.
[2021.05.18-06.16.21:193][  0]LogCore: Benchmarking clocks:
[2021.05.18-06.16.21:193][  0]LogCore:  - CLOCK_MONOTONIC (id=1) can sustain 70213180 (70213K, 70M) calls per second without zero deltas.
[2021.05.18-06.16.21:193][  0]LogCore:  - CLOCK_MONOTONIC_RAW (id=4) can sustain 69905720 (69906K, 70M) calls per second without zero deltas.
[2021.05.18-06.16.21:193][  0]LogCore:  - CLOCK_MONOTONIC_COARSE (id=6) can sustain 178627141 (178627K, 179M) calls per second with 99.999435% zero deltas.
[2021.05.18-06.16.21:193][  0]LogCore: Selected clock_id 1 (CLOCK_MONOTONIC) since it is the fastest support clock without zero deltas.
[2021.05.18-06.16.21:193][  0]LogInit: Unix-specific commandline switches:
[2021.05.18-06.16.21:193][  0]LogInit:  -ansimalloc - use malloc()/free() from libc (useful for tools like valgrind and electric fence)
[2021.05.18-06.16.21:193][  0]LogInit:  -jemalloc - use jemalloc for all memory allocation
[2021.05.18-06.16.21:193][  0]LogInit:  -binnedmalloc - use binned malloc  for all memory allocation
[2021.05.18-06.16.21:193][  0]LogInit:  -filemapcachesize=NUMBER - set the size for case-sensitive file mapping cache
[2021.05.18-06.16.21:193][  0]LogInit:  -useksm - uses kernel same-page mapping (KSM) for mapped memory (OFF)
[2021.05.18-06.16.21:193][  0]LogInit:  -ksmmergeall - marks all mmap'd memory pages suitable for KSM (OFF)
[2021.05.18-06.16.21:193][  0]LogInit:  -preloadmodulesymbols - Loads the main module symbols file into memory (OFF)
[2021.05.18-06.16.21:193][  0]LogInit:  -sigdfl=SIGNAL - Allows a specific signal to be set to its default handler rather then ignoring the signal
[2021.05.18-06.16.21:193][  0]LogInit:  -httpproxy=ADDRESS:PORT - redirects HTTP requests to a proxy (only supported if compiled with libcurl)
[2021.05.18-06.16.21:193][  0]LogInit:  -reuseconn - allow libcurl to reuse HTTP connections (only matters if compiled with libcurl)
[2021.05.18-06.16.21:193][  0]LogInit:  -virtmemkb=NUMBER - sets process virtual memory (address space) limit (overrides VirtualMemoryLimitInKB value from .ini)
[2021.05.18-06.16.21:193][  0]LogInit: Initializing SDL.
No protocol specified
[2021.05.18-06.16.21:198][  0]LogInit: Warning: Could not initialize SDL: No available video device
[2021.05.18-06.16.21:198][  0]LogInit:  - Physical RAM available (not considering process quota): 16 GB (15949 MB, 16332228 KB, 16724201472 bytes)
[2021.05.18-06.16.21:198][  0]LogInit:  - VirtualMemoryAllocator pools will grow at scale 1.4
[2021.05.18-06.16.21:198][  0]LogInit:  - MemoryRangeDecommit() will be a no-op (re-run with -vmapoolevict to change)
[2021.05.18-06.16.21:219][  0]LogInit: Physics initialised using underlying interface: PhysX
[2021.05.18-06.16.21:239][  0]LogInit: Using OS detected language (en-US-POSIX).
[2021.05.18-06.16.21:239][  0]LogInit: Using OS detected locale (en-US-POSIX).
[2021.05.18-06.16.21:240][  0]LogTextLocalizationManager: No specific localization for 'en-US-POSIX' exists, so the 'en' localization will be used.
[2021.05.18-06.16.21:376][  0]LogInit: Initializing SDL.
No protocol specified
[2021.05.18-06.16.21:382][  0]LogInit: Warning: Could not initialize SDL: No available video device
[2021.05.18-06.16.21:382][  0]LogInit: Warning: FLinuxSplashState::InitSplashResources() : InitSDL() failed, there will be no splash.
[2021.05.18-06.16.21:382][  0]LogInit: Initializing SDL.
No protocol specified
[2021.05.18-06.16.21:387][  0]LogInit: Warning: Could not initialize SDL: No available video device
[2021.05.18-06.16.21:387][  0]LogInit: Error: FLinuxApplication::CreateLinuxApplication() : InitSDL() failed, cannot create application instance.
[2021.05.18-06.16.21:387][  0]LogCore: FUnixPlatformMisc::RequestExit(bForce=true, ReturnCode=1)
[2021.05.18-06.16.21:387][  0]LogCore: FUnixPlatformMisc::RequestExit(1)
sh-5.1$ 
```

#### Solution

Buid and deploy extra packages (dg-user-dirs and libsdl)

```
[lliu2@pek-lpgtest7302 build]$ bitbake xdg-user-dirs
WARNING: Host distribution "rhel-8.3" has not been validated with this version of the build system; you may possibly experience unexpected failures. It is recommended that you use a tested distribution.
Loading cache: 100% |#######################################################################################################################################################################| Time: 0:00:01
Loaded 8378 entries from dependency cache.
Parsing recipes: 100% |#####################################################################################################################################################################| Time: 0:00:04
Parsing of 3353 .bb files complete (3350 cached, 3 parsed). 8381 targets, 5428 skipped, 0 masked, 0 errors.
WARNING: xdg-user-dirs is not whitelisted, figuring out PNWHITELIST...
ERROR: Nothing PROVIDES 'xdg-user-dirs'
xdg-user-dirs was skipped: Not supported in this configuration by Wind River. To override, add to your local.conf:
PNWHITELIST_openembedded-layer += 'xdg-user-dirs'

You may also have to add: BB_NO_NETWORK = '0'


[lliu2@pek-lpgtest7302 corei7_64]$ scp xdg-user-dirs-0.17-r0.corei7_64.rpm root@128.224.162.134:/
xdg-user-dirs-0.17-r0.corei7_64.rpm                                                                                                                                      100%   16KB   6.1MB/s   00:00    
[lliu2@pek-lpgtest7302 corei7_64]$ 

[lliu2@pek-lpgtest7302 build]$ bitbake libsdl
WARNING: Host distribution "rhel-8.3" has not been validated with this version of the build system; you may possibly experience unexpected failures. It is recommended that you use a tested distribution.
Loading cache: 100% |#######################################################################################################################################################################| Time: 0:00:08
Loaded 8378 entries from dependency cache.
Parsing recipes: 100% |#####################################################################################################################################################################| Time: 0:00:07
Parsing of 3353 .bb files complete (3350 cached, 3 parsed). 8381 targets, 5426 skipped, 0 masked, 0 errors.
WARNING: libsdl is not whitelisted, figuring out PNWHITELIST...
ERROR: Nothing PROVIDES 'libsdl'
libsdl was skipped: Not supported in this configuration by Wind River. To override, add to your local.conf:
PNWHITELIST_openembedded-layer += 'libsdl'

You may also have to add: BB_NO_NETWORK = '0'

Summary: There were 2 WARNING messages shown.
Summary: There was 1 ERROR message shown, returning a non-zero exit code.
[lliu2@pek-lpgtest7302 build]$ vi conf/local.conf 
[lliu2@pek-lpgtest7302 build]$ bitbake libsdl
```


### References

* https://docs.unrealengine.com/en-US/SharingAndReleasing/Linux/BeginnerLinuxDeveloper/SettingUpAnUnrealWorkflow/index.html
* 
