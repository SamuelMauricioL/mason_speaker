import os
from gtts import gTTS
from src.utils.logger import logger, TypeOfRemitter


def respond(audioString):
    # register log
    logger(TypeOfRemitter.AI, audioString)
    # convert message to audio
    tts = gTTS(text=audioString, lang="en")
    tts.save("./util/audio/speech.wav")
    # replace comando with mpg321 if is linux
    os.system("afplay ./util/audio/speech.wav >/dev/null 2>&1")