import os
from gtts import gTTS

def respond(audioString):
    tts = gTTS(text=audioString, lang="en")
    tts.save("./util/audio/speech.mp3")
    os.system("mpg321 ./util/audio/speech.mp3 >/dev/null 2>&1")