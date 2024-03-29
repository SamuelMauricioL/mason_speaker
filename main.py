from src.voice_assistant.voice_assistant import voice_assistant
from src.recognizers.recognize_speech import RecognizeSpeech, TypeOfRecognizer

from src.core.languages import Translate, TypeOfLanguage
from src.core.global_configuration import GlobalConfiguration
from src.utils.respond import respond

if __name__ == "__main__":
    configuration = GlobalConfiguration()
    configuration.set_language(TypeOfLanguage.ENGLISH)
    configuration.set_recognizer(TypeOfRecognizer.WHISPER)

    translate = Translate()

    respond(translate.get_world('hi'))
    recognize_speech = RecognizeSpeech()

    isListening = True
    while isListening == True:
        response = recognize_speech.from_mic()
        if (response['ok'] != None):
            isListening = voice_assistant(response['ok'])

        if (response['error'] != None):
            respond(response['error'])
