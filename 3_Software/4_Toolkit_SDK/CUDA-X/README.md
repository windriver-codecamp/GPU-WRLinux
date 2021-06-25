# CUDA-X AI Installation

There are multiple features under CUDA-X AI platform as below. We only pick few of them (NeMo, cuDNN) for NVIDIA Geforce GTX 1650 Supper Graphic Card in this project.

```
TensorRT           (TODO)
NeMo               (Selected)
cuDNN              (Selected)
NCCL               (not applicable for NVIDIA Geforce GTX 1650 Supper Graphic Card)
DALI               (TODO)
cuBLAS             (already installed in CUDA Toolkit)
cuSPARSE           (already installed in CUDA Toolkit)
Optical Flow SDK   (TODO)
```
## Setup Steps

### cuDNN (8.2)


Go to: [NVIDIA cuDNN home page](https://developer.nvidia.com/cudnn). Click Download.

```
$ tar -xzvf cudnn-x.x-linux-x64-v8.x.x.x.tgz
```

Copy the following files into the CUDA Toolkit directory.

```
$ sudo cp cuda/include/cudnn*.h /usr/local/cuda/include 
$ sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda/lib64 
$ sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*
```

* [More details](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html)

### NeMo
```
1. git clone https://github.com/NVIDIA/NeMo
   cd NeMo/
2. Comment out lines that contain “${PIP} uninstall”
3. ./reinstall.sh
```
```
$ conda create --name nemo
$ conda activate nemo
```

NeMo Deps
```
$ conda install ffmpeg
$ conda install -c conda-forge libsndfile
$ conda install Cython
```

```python
import nemo
import nemo.collections.asr as nemo_asr
import nemo.collections.nlp as nemo_nlp
 
citrinet = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name="stt_zh_citrinet_512")
mandarin_text = citrinet.transcribe(paths2audio_files=["/mnt/sdb/xhou/run/NeMo_cn_test.wav"])
print(mandarin_text)
nmt_model = nemo_nlp.models.MTEncDecModel.from_pretrained(model_name="nmt_zh_en_transformer6x6")
print(nmt_model.translate(mandarin_text))
```

Installing NeMo with Source
```
$ python -m pip install git+https://github.com/NVIDIA/NeMo.git@v1.0.1#egg=nemo_toolkit[all]
```
* [More details](https://confluence.wrs.com/display/~xhou/Install+NeMo+on+WRLCD#InstallNeMoonWRLCD-Setup)

### FAQ
##### How does NeMo Toolkit invoke CUDA and GPU?
```
NVIDIA GPU Cloud (NGC) is a software repository that has containers and models optimized for deep learning. NGC hosts many conversational AI models developed with NeMo that have been trained to state-of-the-art accuracy on large datasets. NeMo models on NGC can be automatically downloaded and used for transfer learning tasks. Pretrained models are the quickest way to get started with conversational AI on your own data. NeMo has many example scripts and Jupyter Notebook tutorials showing step-by-step how to fine-tune pretrained NeMo models on your own domain-specific datasets.

For BERT based models, the model weights provided are ready for downstream NLU tasks. For speech models, it can be helpful to start with a pretrained model and then continue pretraining on your own domain-specific data. Jasper and QuartzNet base model pretrained weights have been known to be very efficient when used as base models. For an easy to follow guide on transfer learning and building domain specific ASR models, you can follow this blog. All pre-trained NeMo models can be found on the NGC NeMo Collection. Everything needed to quickly get started with NeMo ASR, NLP, and TTS models is there.

Pre-trained models are packaged as a .nemo file and contain the PyTorch checkpoint along with everything needed to use the model. NeMo models are trained to state-of-the-art accuracy and trained on multiple datasets so that they are robust to small differences in data. NeMo contains a large variety of models such as speaker identification and Megatron BERT and the best models in speech and language are constantly being added as they become available. NeMo is the premier toolkit for conversational AI model building and training.
```
Following log shows how Nemo can schedule a CUDA/GPU via PyTorch 
```
Instantiating model from pre-trained checkpoint
[NeMo I 2021-06-22 05:52:37 tokenizer_utils:129] Getting YouTokenToMeTokenizer with model: /tmp/tmpmr9jstqg/tokenizer.decoder.32000.BPE.model.
[NeMo I 2021-06-22 05:52:37 tokenizer_utils:129] Getting YouTokenToMeTokenizer with model: /tmp/tmpmr9jstqg/tokenizer.encoder.32000.BPE.model.
[NeMo W 2021-06-22 05:52:37 modelPT:138] If you intend to do training or fine-tuning, please call the ModelPT.setup_training_data() method and provide a valid configuration file to setup the train data loader.
    Train config :
    src_file_name: /raid/tarred_data_accaligned_16k_tokens_32k_vocab_cov_0.999/batches.tokens.16000._OP_1..144_CL_.tar
    tgt_file_name: /raid/tarred_data_accaligned_16k_tokens_32k_vocab_cov_0.999/batches.tokens.16000._OP_1..144_CL_.tar
    tokens_in_batch: 16000
    clean: true
    max_seq_length: 512
    cache_ids: false
    cache_data_per_node: false
    use_cache: false
    shuffle: true
    num_samples: -1
    drop_last: false
    pin_memory: false
    num_workers: 8
    load_from_cached_dataset: false
    reverse_lang_direction: true
    load_from_tarred_dataset: true
    metadata_path: /raid/tarred_data_accaligned_16k_tokens_32k_vocab_cov_0.999/metadata.json
    tar_shuffle_n: 100

[NeMo W 2021-06-22 05:52:37 modelPT:145] If you intend to do validation, please call the ModelPT.setup_validation_data() or ModelPT.setup_multiple_validation_data() method and provide a valid configuration file to setup the validation data loader(s).
    Validation config :
    src_file_name: /raid/wmt19-zh-en.clean.tok.src
    tgt_file_name: /raid/wmt19-zh-en.clean.tok.ref
    tokens_in_batch: 512
    clean: false
    max_seq_length: 512
    cache_ids: false
    cache_data_per_node: false
    use_cache: false
    shuffle: false
    num_samples: -1
    drop_last: false
    pin_memory: false
    num_workers: 8
    load_from_cached_dataset: false
    reverse_lang_direction: false
    load_from_tarred_dataset: false
    metadata_path: null
    tar_shuffle_n: 100

[NeMo W 2021-06-22 05:52:37 modelPT:152] Please call the ModelPT.setup_test_data() or ModelPT.setup_multiple_test_data() method and provide a valid configuration file to setup the test data loader(s).
    Test config :
    src_file_name: /raid/wmt20-zh-en.clean.tok.src
    tgt_file_name: /raid/wmt20-zh-en.clean.tok.src
    tokens_in_batch: 512
    clean: false
    max_seq_length: 512
    cache_ids: false
    cache_data_per_node: false
    use_cache: false
    shuffle: false
    num_samples: -1
    drop_last: false
    pin_memory: false
    num_workers: 8
    load_from_cached_dataset: false
    reverse_lang_direction: false
    load_from_tarred_dataset: false
    metadata_path: null
    tar_shuffle_n: 100

[NeMo W 2021-06-22 05:52:37 modelPT:1285] World size can only be set by PyTorch Lightning Trainer.
Traceback (most recent call last):
  File "/mnt/sdd/renfeiqu/NeMo37/NeMo/nemo_demo.py", line 8, in <module>
    nmt_model = nemo_nlp.models.MTEncDecModel.from_pretrained(model_name="nmt_zh_en_transformer6x6")
  File "/mnt/sdd/renfeiqu/NeMo37/NeMo/nemo/core/classes/common.py", line 679, in from_pretrained
    instance = class_.restore_from(
  File "/mnt/sdd/renfeiqu/NeMo37/NeMo/nemo/collections/nlp/models/nlp_model.py", line 429, in restore_from
    return super().restore_from(restore_path, override_config_path, map_location, strict, return_config)
  File "/mnt/sdd/renfeiqu/NeMo37/NeMo/nemo/core/classes/modelPT.py", line 482, in restore_from
    return cls._default_restore_from(restore_path, override_config_path, map_location, strict, return_config)
  File "/mnt/sdd/renfeiqu/NeMo37/NeMo/nemo/core/classes/modelPT.py", line 436, in _default_restore_from
    instance = instance.to(map_location)
  File "/home/test/.local/lib/python3.9/site-packages/pytorch_lightning/utilities/device_dtype_mixin.py", line 109, in to
    return super().to(*args, **kwargs)
  File "/home/test/.local/lib/python3.9/site-packages/torch/nn/modules/module.py", line 673, in to
    return self._apply(convert)
  File "/home/test/.local/lib/python3.9/site-packages/torch/nn/modules/module.py", line 387, in _apply
    module._apply(fn)
  File "/home/test/.local/lib/python3.9/site-packages/torch/nn/modules/module.py", line 387, in _apply
    module._apply(fn)
  File "/home/test/.local/lib/python3.9/site-packages/torch/nn/modules/module.py", line 387, in _apply
    module._apply(fn)
  [Previous line repeated 3 more times]
  File "/home/test/.local/lib/python3.9/site-packages/torch/nn/modules/module.py", line 409, in _apply
    param_applied = fn(param)
  File "/home/test/.local/lib/python3.9/site-packages/torch/nn/modules/module.py", line 671, in convert
    return t.to(device, dtype if t.is_floating_point() or t.is_complex() else None, non_blocking)
RuntimeError: CUDA out of memory. Tried to allocate 20.00 MiB (GPU 0; 3.79 GiB total capacity; 388.86 MiB already allocated; 7.69 MiB free; 392.00 MiB reserved in total by PyTorch)

```
The ASR collection has checkpoints of several models trained on various datasets for a variety of tasks. These checkpoints are obtainable via NGC NeMo Automatic Speech Recognition collection. The model cards on NGC contain more information about each of the checkpoints available.

You can get the collections with commands:
```
wget --content-disposition https://api.ngc.nvidia.com/v2/models/nvidia/nemospeechmodels/versions/1.0.0a5/zip -O nemospeechmodels_1.0.0a5.zip
```
The tables below list the ASR models available from NGC. The models can be accessed via the from_pretrained() method inside the ASR Model class. In general, you can load any of these models with code in the following format:
```python
import nemo.collections.asr as nemo_asr
model = nemo_asr.models.ASRModel.from_pretrained(model_name="<MODEL_NAME>")
```
Where the model name is the value under “Model Name” entry in the tables below.

For example, to load the base English QuartzNet model for speech recognition, run:
```
model = nemo_asr.models.ASRModel.from_pretrained(model_name="QuartzNet15x5Base-En")
```
You can also call from_pretrained() from the specific model class (such as EncDecCTCModel for QuartzNet) if you need to access a specific model functionality.

If you would like to programatically list the models available for a particular base class, you can use the list_available_models() method.
```
nemo_asr.models.<MODEL_BASE_CLASS>.list_available_models()
```


## References
* https://developer.nvidia.com/
* https://developer.nvidia.com/tensorrt-getting-started
* https://developer.nvidia.com/nvidia-tensorrt-8x-download
* https://docs.nvidia.com/deeplearning/tensorrt/quick-start-guide/index.html
* https://developer.nvidia.com/nvidia-nemo
* https://github.com/NVIDIA/NeMo
* https://developer.nvidia.com/cudnn
* https://developer.nvidia.com/rdp/cudnn-download
* https://developer.nvidia.com/dali
* https://developer.nvidia.com/cublas
* https://developer.nvidia.com/cusparse
* https://developer.nvidia.com/opticalflow-sdk
* https://github.com/nvidia/cudalibrarysamples
* https://developer.nvidia.com/nvidia-sdk-manager

