import os
import glob
import shutil
# ph = '/mnt/users/hccl.local/dcyang/StableTTS2/v2_base_lumina/out/mos.scp'
# f = open(ph)
names = ['common_voice_en_13900-common_voice_en_13901.wav',
         'common_voice_en_15265-common_voice_en_15266.wav',
         'common_voice_en_15265-common_voice_en_15268.wav',
         'common_voice_en_103675-common_voice_en_103676.wav',
         'common_voice_en_15903802-common_voice_en_15903807.wav',
         'emo_0.wav',
         'emo_1.wav',
         'emo_2.wav',
         'emo_3.wav',
         'emo_4.wav',
         'en_4404-B_072759-073171.wav',
         'en_6282-B_013447-013580.wav',
         'p225_084.wav',
         'p229_020.wav',
         'prompt_18.wav',
        ]

source_path = '/mnt/users/hccl.local/dcyang/code/SimpleSpeech2_demo/compare_baseline_mos/ref'
tg_path = '/mnt/users/hccl.local/dcyang/code/SimpleSpeech2_demo/compare_baseline_mos/ref2'
os.makedirs(tg_path, exist_ok=True)
for name in names:
    tmp_path = os.path.join(source_path, name)
    t_path = os.path.join(tg_path, name)
    shutil.copy(tmp_path, t_path)



