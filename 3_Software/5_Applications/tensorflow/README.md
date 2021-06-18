## Demo Video:
> None

## TensorFlow Example 1
### Run example 1
```
python3 mnist2.py
```
### Result
```
intel-x86-64:~$ python3 mnist2.py
2021-06-18 09:32:48.241195: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcudart.so.11.0
x_train shape: (60000, 28, 28, 1)
60000 train samples
10000 test samples
2021-06-18 09:32:51.645899: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcuda.so.1
2021-06-18 09:32:51.682367: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-06-18 09:32:51.682892: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1733] Found device 0 with properties: 
pciBusID: 0000:01:00.0 name: GeForce GTX 1650 SUPER computeCapability: 7.5
coreClock: 1.755GHz coreCount: 20 deviceMemorySize: 3.79GiB deviceMemoryBandwidth: 178.84GiB/s
2021-06-18 09:32:51.683067: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcudart.so.11.0
2021-06-18 09:32:51.687324: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcublas.so.11
2021-06-18 09:32:51.687567: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcublasLt.so.11
2021-06-18 09:32:51.688972: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcufft.so.10
2021-06-18 09:32:51.689623: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcurand.so.10
2021-06-18 09:32:51.690911: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcusolver.so.11
2021-06-18 09:32:51.691950: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcusparse.so.11
2021-06-18 09:32:51.692482: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcudnn.so.8
2021-06-18 09:32:51.692668: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-06-18 09:32:51.693212: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-06-18 09:32:51.694344: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1871] Adding visible gpu devices: 0
2021-06-18 09:32:51.694741: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2021-06-18 09:32:51.695565: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-06-18 09:32:51.695985: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1733] Found device 0 with properties: 
pciBusID: 0000:01:00.0 name: GeForce GTX 1650 SUPER computeCapability: 7.5
coreClock: 1.755GHz coreCount: 20 deviceMemorySize: 3.79GiB deviceMemoryBandwidth: 178.84GiB/s
2021-06-18 09:32:51.696104: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-06-18 09:32:51.696563: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-06-18 09:32:51.696932: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1871] Adding visible gpu devices: 0
2021-06-18 09:32:51.697772: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcudart.so.11.0
2021-06-18 09:32:53.147764: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1258] Device interconnect StreamExecutor with strength 1 edge matrix:
2021-06-18 09:32:53.147814: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1264]      0 
2021-06-18 09:32:53.147833: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1277] 0:   N 
2021-06-18 09:32:53.148058: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-06-18 09:32:53.148585: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-06-18 09:32:53.149075: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-06-18 09:32:53.149486: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1418] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 1925 MB memory) -> physical GPU (device: 0, name: GeForce GTX 1650 SUPER, pci bus id: 0000:01:00.0, compute capability: 7.5)
WARNING:tensorflow:Please add `keras.layers.InputLayer` instead of `keras.Input` to Sequential model. `keras.Input` is intended to be used by Functional model.
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 26, 26, 32)        320       
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 13, 13, 32)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 11, 11, 64)        18496     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 5, 5, 64)          0         
_________________________________________________________________
flatten (Flatten)            (None, 1600)              0         
_________________________________________________________________
dropout (Dropout)            (None, 1600)              0         
_________________________________________________________________
dense (Dense)                (None, 10)                16010     
=================================================================
Total params: 34,826
Trainable params: 34,826
Non-trainable params: 0
_________________________________________________________________
2021-06-18 09:32:53.827260: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:176] None of the MLIR Optimization Passes are enabled (registered 2)
2021-06-18 09:32:53.842993: I tensorflow/core/platform/profile_utils/cpu_utils.cc:114] CPU Frequency: 3591865000 Hz
Epoch 1/15
2021-06-18 09:32:54.550320: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcudnn.so.8
2021-06-18 09:32:55.765658: I tensorflow/stream_executor/cuda/cuda_dnn.cc:359] Loaded cuDNN version 8200
2021-06-18 09:32:57.327531: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcublas.so.11
2021-06-18 09:32:58.587734: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcublasLt.so.11
422/422 [==============================] - 8s 6ms/step - loss: 0.3668 - accuracy: 0.8889 - val_loss: 0.0834 - val_accuracy: 0.9762
Epoch 2/15
422/422 [==============================] - 2s 5ms/step - loss: 0.1114 - accuracy: 0.9657 - val_loss: 0.0618 - val_accuracy: 0.9820
Epoch 3/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0827 - accuracy: 0.9738 - val_loss: 0.0459 - val_accuracy: 0.9877
Epoch 4/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0700 - accuracy: 0.9777 - val_loss: 0.0427 - val_accuracy: 0.9872
Epoch 5/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0630 - accuracy: 0.9807 - val_loss: 0.0392 - val_accuracy: 0.9885
Epoch 6/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0563 - accuracy: 0.9825 - val_loss: 0.0369 - val_accuracy: 0.9890
Epoch 7/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0525 - accuracy: 0.9832 - val_loss: 0.0402 - val_accuracy: 0.9868
Epoch 8/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0474 - accuracy: 0.9852 - val_loss: 0.0332 - val_accuracy: 0.9902
Epoch 9/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0456 - accuracy: 0.9855 - val_loss: 0.0342 - val_accuracy: 0.9903
Epoch 10/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0401 - accuracy: 0.9872 - val_loss: 0.0304 - val_accuracy: 0.9905
Epoch 11/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0376 - accuracy: 0.9878 - val_loss: 0.0306 - val_accuracy: 0.9917
Epoch 12/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0363 - accuracy: 0.9884 - val_loss: 0.0299 - val_accuracy: 0.9915
Epoch 13/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0359 - accuracy: 0.9883 - val_loss: 0.0308 - val_accuracy: 0.9908
Epoch 14/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0337 - accuracy: 0.9894 - val_loss: 0.0271 - val_accuracy: 0.9923
Epoch 15/15
422/422 [==============================] - 2s 5ms/step - loss: 0.0321 - accuracy: 0.9894 - val_loss: 0.0281 - val_accuracy: 0.9922
Test loss: 0.02429191768169403
Test accuracy: 0.9922999739646912
```
## TensorFlow Example 2
### Run example 2
```
python3 keras-elephone.py 
```
### Results

<img src="./example2/integrated_gradients_3_1.png" width="300">

<img src="./example2/integrated_gradients_9_1.png" width="900">

### Issues

* TODO

## References
* https://keras.io/examples/vision/mnist_convnet/#setup
* https://keras.io/examples/vision/integrated_gradients/


