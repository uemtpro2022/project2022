import os
from pocketsphinx import LiveSpeech, get_model_path

def wakeup_co():
    model_path = get_model_path()
    speech = LiveSpeech(
        verbose=False,
        sampling_rate=16000,
        buffer_size=2048,
        no_search=False,
        full_utt=False,
        hmm=os.path.join(model_path, 'en-us'),
        lm=os.path.join('.\\PROJECT2022\\python\\switch test\\', '7961.lm'),
        dic=os.path.join('.\\PROJECT2022\\python\\switch test\\', '7961.dic')
    )
    for phrase in speech:
        if str(phrase) in [ "COCO", "KOKO","MOMO",
                           "NONO", "JOJO"]:
              print('&#x6211;&#x662F;COCO')