import os
import numpy as np
import whisper
from scipy.io.wavfile import write
from IPython.display import clear_output


class WhishperRecognizer:

    def from_mic(self):
        model = whisper.load_model("base")
        result = model.transcribe(
            "./util/audio/speech.wav",
            fp16=False,
            language='English',
        )
        print(result["text"])
        # os.system(
        #     'whisper "record.wav" --task "./util/audio/speech.wav" --model medium --verbose False'
        # )
