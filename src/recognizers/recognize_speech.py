from enum import Enum
# from .google.google_recognizer_speech import GoogleRecognizerSpeech
from .whisper.whisper_recognizer_speech import WhishperRecognizerSpeech
from src.core.global_configuration import GlobalConfiguration


class TypeOfRecognizer(Enum):
    GOOGLE = "GOOGLE"
    WHISPER = "WHISPER"


class RecognizeSpeech(object):

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super().__new__(self)
            type_of_recognizer = GlobalConfiguration().get_recognizer()
            if type_of_recognizer == TypeOfRecognizer.GOOGLE:
                # self.recognizer = GoogleRecognizerSpeech()
                self.recognizer = WhishperRecognizerSpeech()
            elif type_of_recognizer == TypeOfRecognizer.WHISPER:
                self.recognizer = WhishperRecognizerSpeech()
        return self.recognizer
