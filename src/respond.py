import os
from gtts import gTTS

def respond(audioString):
    tts = gTTS(text=audioString, lang="en")
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3 >/dev/null 2>&1")