## NeMo Demo Introduction:
This demo is used to recogize Chinese language in (WAV ) audio file to plan text, and translate it into English.

## Run NeMo Demo Steps
### 1. Install the nemo toolkit
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
