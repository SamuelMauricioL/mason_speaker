import os
from gtts import gTTS

def respond(audioString):
    tts = gTTS(text=audioString, lang="en")
    tts.save("./util/audio/speech.mp3")
    # replace comando with mpg321 if is linux
    os.system("afplay ./util/audio/speech.mp3 >/dev/null 2>&1")