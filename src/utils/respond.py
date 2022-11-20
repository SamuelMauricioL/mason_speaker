import os
from gtts import gTTS
from src.utils.logger import logger, TypeOfRemitter
from src.core.global_configuration import GlobalConfiguration
from src.core.languages import TypeOfLanguage


def respond(audioString):
    # register log
    logger(TypeOfRemitter.AI, audioString)

    # convert message to audio
    type_of_language = GlobalConfiguration().get_language()
    language = get_gTTS_language(type_of_language)
    try:
        tts = gTTS(text=audioString, lang=language)
        tts.save("./util/audio/speech.wav")

        # replace comando with mpg321 if is linux
        os.system("afplay ./util/audio/speech.wav >/dev/null 2>&1")
    except:
        return


def get_gTTS_language(type_of_language):
    if type_of_language == TypeOfLanguage.ENGLISH:
        return 'en'
    elif type_of_language == TypeOfLanguage.SPANISH:
        return 'es'
    elif type_of_language == TypeOfLanguage.PORTUGUESE:
        return 'pt'