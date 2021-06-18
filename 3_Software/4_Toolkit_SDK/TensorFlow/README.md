# How to install Tensorflow-gpu?   GPU!!!!!
    step1: pip3 install tensorflow-gpu
    setp2: (check whether run by gpu?)
            python3
            import tensorflow as tf
            tf.__version__   
            tf.test.is_gpu_available()   ---->  physical GPU (device: 0, name: GeForce GTX 1650 SUPER, pci bus id: 0000:01:00.0, compute capability: 7.5) True 
            
            
    intel-x86-64:~$ uname -a
    Linux intel-x86-64 5.12.0-yoctodev-standard #1 SMP PREEMPT Sat May 8 03:46:47 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
    intel-x86-64:~$ 
    intel-x86-64:~$ pip3 install tensorflow-gpu
    Defaulting to user installation because normal site-packages is not writeable
    Requirement already satisfied: tensorflow-gpu in /usr/lib64/python3.9/site-packages (2.5.0)
    Requirement already satisfied: termcolor~=1.1.0 in /usr/lib/python3.9/site-packages (from tensorflow-gpu) (1.1.0)
    Collecting h5py~=3.1.0
      Downloading h5py-3.1.0-cp39-cp39-manylinux1_x86_64.whl (4.4 MB)
     |████████████████████████████████| 4.4 MB 1.5 MB/s 
    Requirement already satisfied: wrapt~=1.12.1 in ./.local/lib/python3.9/site-packages (from tensorflow-gpu) (1.12.1)
    Requirement already satisfied: six~=1.15.0 in /usr/lib64/python3.9/site-packages (from tensorflow-gpu) (1.15.0)
    Requirement already satisfied: google-pasta~=0.2 in /usr/lib/python3.9/site-packages (from tensorflow-gpu) (0.2.0)
    Requirement already satisfied: keras-preprocessing~=1.1.2 in /usr/lib/python3.9/site-packages (from tensorflow-gpu) (1.1.2)
    Requirement already satisfied: keras-nightly~=2.5.0.dev in /usr/lib/python3.9/site-packages (from tensorflow-gpu) (2.5.0.dev2021032900)
    Requirement already satisfied: flatbuffers~=1.12.0 in /usr/lib/python3.9/site-packages (from tensorflow-gpu) (1.12)
    Requirement already satisfied: absl-py~=0.10 in ./.local/lib/python3.9/site-packages (from tensorflow-gpu) (0.12.0)
    Requirement already satisfied: numpy~=1.19.2 in /usr/lib64/python3.9/site-packages (from tensorflow-gpu) (1.19.5)
    Requirement already satisfied: protobuf>=3.9.2 in ./.local/lib/python3.9/site-packages (from tensorflow-gpu) (3.17.1)
    Requirement already satisfied: tensorflow-estimator<2.6.0,>=2.5.0rc0 in /usr/lib/python3.9/site-packages (from tensorflow-gpu) (2.5.0)
    Requirement already satisfied: gast==0.4.0 in /usr/lib/python3.9/site-packages (from tensorflow-gpu) (0.4.0)
    Collecting typing-extensions~=3.7.4
    Downloading typing_extensions-3.7.4.3-py3-none-any.whl (22 kB)
    Requirement already satisfied: astunparse~=1.6.3 in /usr/lib/python3.9/site-packages (from tensorflow-gpu) (1.6.3)
    Requirement already satisfied: opt-einsum~=3.3.0 in /usr/lib/python3.9/site-packages (from tensorflow-gpu) (3.3.0)
    Collecting tensorboard~=2.5
    Downloading tensorboard-2.5.0-py3-none-any.whl (6.0 MB)
         |████████████████████████████████| 6.0 MB 7.4 MB/s 
    Collecting grpcio~=1.34.0
    Downloading grpcio-1.34.1-cp39-cp39-manylinux2014_x86_64.whl (4.0 MB)
         |████████████████████████████████| 4.0 MB 7.2 MB/s 
    Requirement already satisfied: wheel~=0.35 in ./.local/lib/python3.9/site-packages (from tensorflow-gpu) (0.36.2)
    Requirement already satisfied: markdown>=2.6.8 in ./.local/lib/python3.9/site-packages (from tensorboard~=2.5->tensorflow-gpu) (3.3.4)
    Requirement already satisfied: tensorboard-data-server<0.7.0,>=0.6.0 in /usr/lib/python3.9/site-packages (from tensorboard~=2.5->tensorflow-gpu) (0.6.1)
    Requirement already satisfied: setuptools>=41.0.0 in ./.local/lib/python3.9/site-packages (from tensorboard~=2.5->tensorflow-gpu) (57.0.0)
    Requirement already satisfied: werkzeug>=0.11.15 in ./.local/lib/python3.9/site-packages (from tensorboard~=2.5->tensorflow-gpu) (2.0.1)
    Requirement already satisfied: tensorboard-plugin-wit>=1.6.0 in ./.local/lib/python3.9/site-packages (from tensorboard~=2.5->tensorflow-gpu) (1.8.0)
    Requirement already satisfied: requests<3,>=2.21.0 in ./.local/lib/python3.9/site-packages (from tensorboard~=2.5->tensorflow-gpu) (2.25.1)
    Requirement already satisfied: google-auth-oauthlib<0.5,>=0.4.1 in ./.local/lib/python3.9/site-packages (from tensorboard~=2.5->tensorflow-gpu) (0.4.4)
    Requirement already satisfied: google-auth<2,>=1.6.3 in ./.local/lib/python3.9/site-packages (from tensorboard~=2.5->tensorflow-gpu) (1.30.1)
    Requirement already satisfied: chardet<5,>=3.0.2 in ./.local/lib/python3.9/site-packages (from requests<3,>=2.21.0->tensorboard~=2.5->tensorflow-gpu) (4.0.0)
        Requirement already satisfied: certifi>=2017.4.17 in ./.local/lib/python3.9/site-packages (from requests<3,>=2.21.0->tensorboard~=2.5->tensorflow-gpu) (2021.5.30)
    Requirement already satisfied: idna<3,>=2.5 in ./.local/lib/python3.9/site-packages (from requests<3,>=2.21.0->tensorboard~=2.5->tensorflow-gpu) (2.10)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in ./.local/lib/python3.9/site-packages (from requests<3,>=2.21.0->tensorboard~=2.5->tensorflow-gpu) (1.26.5)
    Requirement already satisfied: requests-oauthlib>=0.7.0 in ./.local/lib/python3.9/site-packages (from google-auth-oauthlib<0.5,>=0.4.1->tensorboard~=2.5->tensorflow-gpu) (1.3.0)
    Requirement already satisfied: cachetools<5.0,>=2.0.0 in ./.local/lib/python3.9/site-packages (from google-auth<2,>=1.6.3->tensorboard~=2.5->tensorflow-gpu) (4.2.2)
    Requirement already satisfied: rsa<5,>=3.1.4; python_version >= "3.6" in ./.local/lib/python3.9/site-packages (from google-auth<2,>=1.6.3->tensorboard~=2.5->tensorflow-gpu) (4.7.2)
    Requirement already satisfied: pyasn1-modules>=0.2.1 in ./.local/lib/python3.9/site-packages (from google-auth<2,>=1.6.3->tensorboard~=2.5->tensorflow-gpu) (0.2.8)
    Requirement already satisfied: oauthlib>=3.0.0 in ./.local/lib/python3.9/site-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib<0.5,>=0.4.1->tensorboard~=2.5->tensorflow-gpu) (3.1.0)
    Requirement already satisfied: pyasn1>=0.1.3 in ./.local/lib/python3.9/site-packages (from rsa<5,>=3.1.4; python_version >= "3.6"->google-auth<2,>=1.6.3->tensorboard~=2.5->tensorflow-gpu) (0.4.8)
    ERROR: pytorch-lightning 1.3.3 has requirement tensorboard!=2.5.0,>=2.2.0, but you'll have tensorboard 2.5.0 which is incompatible.
    Installing collected packages: h5py, typing-extensions, grpcio, tensorboard
    Attempting uninstall: h5py
        Found existing installation: h5py 3.2.1
        Uninstalling h5py-3.2.1:
          Successfully uninstalled h5py-3.2.1
    Attempting uninstall: typing-extensions
        Found existing installation: typing-extensions 3.10.0.0
        Uninstalling typing-extensions-3.10.0.0:
          Successfully uninstalled typing-extensions-3.10.0.0
    Attempting uninstall: grpcio
        Found existing installation: grpcio 1.38.0
        Uninstalling grpcio-1.38.0:
          Successfully uninstalled grpcio-1.38.0
    Attempting uninstall: tensorboard
        Found existing installation: tensorboard 2.4.1
        Uninstalling tensorboard-2.4.1:
          Successfully uninstalled tensorboard-2.4.1
    WARNING: The script tensorboard is installed in '/home/test/.local/bin' which is not on PATH.
    Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
    Successfully installed grpcio-1.34.1 h5py-3.1.0 tensorboard-2.5.0 typing-extensions-3.7.4.3
    intel-x86-64:~$ 

    intel-x86-64:~$ python3
    Python 3.9.2 (default, May  8 2021, 05:14:08) 
    [GCC 10.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import tensorflow as tf
    2021-06-18 11:17:27.768258: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcudart.so.11.0
    >>> tf.__version__
    '2.5.0'
    >>> tf.__path__
    ['/usr/lib64/python3.9/site-packages/tensorflow', '/usr/lib/python3.9/site-packages/tensorflow_estimator/python/estimator/api/_v2', '/home/test/.local/lib/python3.9/site-packages/tensorboard/summary/_tf', '/usr/lib64/python3.9/site-packages/tensorflow', '/usr/lib64/python3.9/site-packages/tensorflow/_api/v2']
    >>>   
    
    >>> tf.test.is_gpu_available()
    WARNING:tensorflow:From <stdin>:1: is_gpu_available (from tensorflow.python.framework.test_util) is deprecated and will be removed in a future version.
    Instructions for updating:
    Use `tf.config.list_physical_devices('GPU')` instead.
    2021-06-18 11:43:23.127096: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
    To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
    2021-06-18 11:43:23.128168: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcuda.so.1
    2021-06-18 11:43:23.154542: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
    2021-06-18 11:43:23.154848: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1733] Found device 0 with properties: 
    pciBusID: 0000:01:00.0 name: GeForce GTX 1650 SUPER computeCapability: 7.5
    coreClock: 1.755GHz coreCount: 20 deviceMemorySize: 3.79GiB deviceMemoryBandwidth: 178.84GiB/s
    2021-06-18 11:43:23.154865: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcudart.so.11.0
    2021-06-18 11:43:23.157500: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcublas.so.11
    2021-06-18 11:43:23.157576: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcublasLt.so.11
    2021-06-18 11:43:23.158331: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcufft.so.10
    2021-06-18 11:43:23.158598: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcurand.so.10
    2021-06-18 11:43:23.159289: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcusolver.so.11
    2021-06-18 11:43:23.159835: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcusparse.so.11
    2021-06-18 11:43:23.159935: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcudnn.so.8
    2021-06-18 11:43:23.160017: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
    2021-06-18 11:43:23.160386: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
    2021-06-18 11:43:23.160648: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1871] Adding visible gpu devices: 0
    2021-06-18 11:43:23.160671: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcudart.so.11.0
    2021-06-18 11:43:23.563317: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1258] Device interconnect StreamExecutor with strength 1 edge matrix:
    2021-06-18 11:43:23.563344: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1264]      0 
    2021-06-18 11:43:23.563351: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1277] 0:   N 
    2021-06-18 11:43:23.563502: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
    2021-06-18 11:43:23.563819: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
    2021-06-18 11:43:23.564135: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
    2021-06-18 11:43:23.564469: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1418] Created TensorFlow device (/device:GPU:0 with 2425 MB memory) -> physical GPU (device: 0, name: GeForce GTX 1650 SUPER, pci bus id: 0000:01:00.0, compute capability: 7.5)
    True
    >>> 
### References 
* https://www.tensorflow.org/install/gpu




## Setup Steps (jupyterlab)

```
test@intel-x86-64:~$ pip3 install jupyterlab
```
```
test@intel-x86-64:~$ /home/test/.local/bin/jupyter-lab
[I 2021-06-18 10:16:56.698 ServerApp] jupyterlab | extension was successfully linked.
[I 2021-06-18 10:16:56.706 ServerApp] Writing notebook server cookie secret to /home/test/.local/share/jupyter/runtime/jupyter_cookie_secret
[I 2021-06-18 10:16:56.717 LabApp] JupyterLab extension loaded from /home/test/.local/lib/python3.9/site-packages/jupyterlab
[I 2021-06-18 10:16:56.717 LabApp] JupyterLab application directory is /home/test/.local/share/jupyter/lab
[I 2021-06-18 10:16:56.719 ServerApp] jupyterlab | extension was successfully loaded.
[I 2021-06-18 10:16:56.720 ServerApp] Serving notebooks from local directory: /home/test
[I 2021-06-18 10:16:56.720 ServerApp] Jupyter Server 1.8.0 is running at:
[I 2021-06-18 10:16:56.720 ServerApp] http://localhost:8888/lab?token=782af267be27eadae7fda0cf0f81733d1cdf22e286ab06de
[I 2021-06-18 10:16:56.720 ServerApp]     http://127.0.0.1:8888/lab?token=782af267be27eadae7fda0cf0f81733d1cdf22e286ab06de
[I 2021-06-18 10:16:56.720 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[W 2021-06-18 10:16:56.723 ServerApp] No web browser found: could not locate runnable browser.
[C 2021-06-18 10:16:56.723 ServerApp] 
    
    To access the server, open this file in a browser:
        file:///home/test/.local/share/jupyter/runtime/jpserver-39589-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/lab?token=782af267be27eadae7fda0cf0f81733d1cdf22e286ab06de
        http://127.0.0.1:8888/lab?token=782af267be27eadae7fda0cf0f81733d1cdf22e286ab06de

```

### References

* https://jupyter.org/install.html

