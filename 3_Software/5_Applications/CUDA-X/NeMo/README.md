## NeMo Demo Introduction:
This demo is used to recogize Chinese language in (WAV ) audio file to plan text, and translate it into English.

A typical conversational AI application uses three subsystems to do the steps of processing and transcribing the audio, understanding (deriving meaning) of the question asked, generating the response (text) and speaking the response back to the human. These steps are achieved by multiple deep learning solutions working together. First, automatic speech recognition (ASR) is used to process the raw audio signal and transcribing text from it. Second, natural language processing (NLP) is used to derive meaning from the transcribed text (ASR output). Last, speech synthesis or text-to-speech (TTS) is used for the artificial production of human speech from text. Optimizing this multi-step process is complicated, as each of these steps requires building and using one or more deep learning models. When developing a deep learning model to achieve the highest performance and accuracy for each of these areas, a developer will encounter several approaches and experiments that can vary by domain application.

<img src="https://developer-blogs.nvidia.com/wp-content/uploads/2019/12/Conversation_AI_Workflow_v02-625x275.png">

Below is the code snippet of Audio Translator application that uses three subsystems to do the steps of processing and transcribing the audio.
```
# Import NeMo and it's ASR, NLP and TTS collections
import nemo
# Import Speech Recognition collection
import nemo.collections.asr as nemo_asr
# Import Natural Language Processing colleciton
import nemo.collections.nlp as nemo_nlp
# Import Speech Synthesis collection
import nemo.collections.tts as nemo_tts

# Next, we instantiate all the necessary models directly from NVIDIA NGC
# Speech Recognition model - QuartzNet trained on Russian part of MCV 6.0
quartznet = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name="stt_ru_quartznet15x5").cuda()
# Neural Machine Translation model
nmt_model = nemo_nlp.models.MTEncDecModel.from_pretrained(model_name='nmt_ru_en_transformer6x6').cuda()
# Spectrogram generator which takes text as an input and produces spectrogram
spectrogram_generator = nemo_tts.models.Tacotron2Model.from_pretrained(model_name="tts_en_tacotron2").cuda()
# Vocoder model which takes spectrogram and produces actual audio
vocoder = nemo_tts.models.WaveGlowModel.from_pretrained(model_name="tts_waveglow_88m").cuda()
# Transcribe an audio file
# IMPORTANT: The audio must be mono with 16Khz sampling rate
# Get example from: https://nemo-public.s3.us-east-2.amazonaws.com/mcv-samples-ru/common_voice_ru_19034087.wav
russian_text = quartznet.transcribe(['Path_to_audio_file'])
print(russian_text)
# You should see russian text here. Let's translate it to English
english_text = nmt_model.translate(russian_text)
print(english_text)
# After this you should see English translation
# Let's convert it into audio
# A helper function which combines Tacotron2 and WaveGlow to go directly from
# text to audio
def text_to_audio(text):
  parsed = spectrogram_generator.parse(text)
  spectrogram = spectrogram_generator.generate_spectrogram(tokens=parsed)
  audio = vocoder.convert_spectrogram_to_audio(spec=spectrogram)
  return audio.to('cpu').numpy()
audio = text_to_audio(english_text[0])
```
As a result, a CTC (Connectionist Temporal Classification) based ASR pipeline consists of the following blocks, shown below:
<img src="https://developer-blogs.nvidia.com/wp-content/uploads/2019/12/ASR-Pipeline-1.png">
```
Feature extraction: Audio signal preprocessing using normalization, windowing, (log) spectrogram 
(or mel scale spectrogram, or MFCC).
```
```
Acoustic Model: A CTC-based network that predicts the probability distributions P_t(c) over vocabulary characters c 
per each time step t. For this block we use NVIDIA’s high performing acoustic models: Jasper and QuartzNet.
```
```
Decoding/Decoder:

    Greedy (argmax): Is the simplest strategy for a decoder. The letter with the highest probability
    (temporal softmax output layer) is chosen at each time-step, without regard to any semantic 
    understanding of what was being communicated. Then, the repeated characters are removed or 
    collapsed, and blank tokens are discarded.
    A language model can be used to add contex,t and therefore correct mistakes in the acoustic model.  
    A beam search decoder weights the relative probabilities the softmax output against the likelihood 
    of certain words appearing in context and tries to determine what was spoken by combining both what 
    the acoustic model thinks it heard with what is a likely next word
```
To facilitate the implementation and domain adaptation of the complete ASR pipeline, we created the Domain Specific – NeMo ASR Application. This application is developed using NeMo and it enables you to train or fine-tune pre-trained (acoustic and language) ASR models with your own data. Through this application, we empower you to train, evaluate and compare ASR models built on your own domain specific audio data. This gives you the ability to progressively create better performing ASR models specifically built for your data.

## NGC instruction

NVIDIA GPU Cloud (NGC) is a software repository that has containers and models optimized for deep learning. NGC hosts many conversational AI models developed with NeMo that have been trained to state-of-the-art accuracy on large datasets. NeMo models on NGC can be automatically downloaded and used for transfer learning tasks. Pretrained models are the quickest way to get started with conversational AI on your own data. NeMo has many example scripts and Jupyter Notebook tutorials showing step-by-step how to fine-tune pretrained NeMo models on your own domain-specific datasets.

For BERT based models, the model weights provided are ready for downstream NLU tasks. For speech models, it can be helpful to start with a pretrained model and then continue pretraining on your own domain-specific data. Jasper and QuartzNet base model pretrained weights have been known to be very efficient when used as base models. For an easy to follow guide on transfer learning and building domain specific ASR models, you can follow this blog. All pre-trained NeMo models can be found on the NGC NeMo Collection. Everything needed to quickly get started with NeMo ASR, NLP, and TTS models is there.

Pre-trained models are packaged as a .nemo file and contain the PyTorch checkpoint along with everything needed to use the model. NeMo models are trained to state-of-the-art accuracy and trained on multiple datasets so that they are robust to small differences in data. NeMo contains a large variety of models such as speaker identification and Megatron BERT and the best models in speech and language are constantly being added as they become available. NeMo is the premier toolkit for conversational AI model building and training.

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


## Run NeMo Demo Steps
### 1. Install the NeMo Toolkit
```
a. add/install libsndfile1 ffmpeg (already installed by other application parts)
```
```
b. # git clone https://github.com/NVIDIA/NeMo
   # cd NeMo
```
```
c. comment out all uninstall steps in reinstall.sh
   # ./reinstall.sh
```

### 2. Run the testdemo
```
   # python nemo_demo.py or python3 nemo_demo.py
```
### 3. Result
```
[NeMo W 2021-06-09 09:21:20 patch_utils:49] torch.stft() signature has been updated for PyTorch 1.7+
    Please update PyTorch to remain compatible with later versions of NeMo.
Transcribing: 100%|█████████| 1/1 [00:00<00:00,  1.94it/s]
['一天黄昏我过一条河走到一半时突然河里的水沸腾起来水猪门从河里跳到半空中他们喊着墨言过言你暂住']
[NeMo I 2021-06-09 09:21:20 cloud:56] Found existing object /mnt/sdb/xhou/HOME/.cache/torch/NeMo/NeMo_1.0.1/nmt_zh_en_transformer6x6/eff3792e6f4420ba83436be889e92d79/nmt_zh_en_transformer6x6.nemo.
[NeMo I 2021-06-09 09:21:20 cloud:62] Re-using file from: /mnt/sdb/xhou/HOME/.cache/torch/NeMo/NeMo_1.0.1/nmt_zh_en_transformer6x6/eff3792e6f4420ba83436be889e92d79/nmt_zh_en_transformer6x6.nemo
[NeMo I 2021-06-09 09:21:20 common:675] Instantiating model from pre-trained checkpoint
[NeMo I 2021-06-09 09:21:30 tokenizer_utils:129] Getting YouTokenToMeTokenizer with model: /tmp/tmp_zkz0zea/tokenizer.decoder.32000.BPE.model.
[NeMo I 2021-06-09 09:21:30 tokenizer_utils:129] Getting YouTokenToMeTokenizer with model: /tmp/tmp_zkz0zea/tokenizer.encoder.32000.BPE.model.
[NeMo W 2021-06-09 09:21:30 modelPT:137] If you intend to do training or fine-tuning, please call the ModelPT.setup_training_data() method and provide a valid configuration file to setup the train data loader.
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
    
[NeMo W 2021-06-09 09:21:30 modelPT:1198] World size can only be set by PyTorch Lightning Trainer.
[NeMo I 2021-06-09 09:21:34 modelPT:434] Model MTEncDecModel was successfully restored from /mnt/sdb/xhou/HOME/.cache/torch/NeMo/NeMo_1.0.1/nmt_zh_en_transformer6x6/eff3792e6f4420ba83436be889e92d79/nmt_zh_en_transformer6x6.nemo.
['One day the yellow twilight I walked across a river to a half-hour when the water in the suddenly the river rose up and the water pig door jumped from the river to the half empty. They shouted ink and said, "You']
```

### Issues
* Cannot display Chinese charactors from the terminal
#### Solution
Set Encoding on the terminal to Unicode UTF-8


## References
* https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/


## Demo Video:
> None
