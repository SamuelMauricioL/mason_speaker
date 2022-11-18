import os
from gtts import gTTS

def respond(audioString):
    tts = gTTS(text=audioString, lang="en")
    tts.save("./util/audio/speech.wav")
    # replace comando with mpg321 if is linux
    os.system("afplay ./util/audio/speech.wav >/dev/null 2>&1")