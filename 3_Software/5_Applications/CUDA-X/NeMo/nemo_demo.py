import nemo
import nemo.collections.asr as nemo_asr
import nemo.collections.nlp as nemo_nlp

citrinet = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name="stt_zh_citrinet_512")
mandarin_text = citrinet.transcribe(paths2audio_files=["/mnt/sdb/xhou/run/test.wav"])
print(mandarin_text)
nmt_model = nemo_nlp.models.MTEncDecModel.from_pretrained(model_name="nmt_zh_en_transformer6x6")
print(nmt_model.translate(mandarin_text))
