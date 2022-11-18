from enum import Enum
from .google.google_recognizer_speech import GoogleRecognizerSpeech
from .whisper.whisper_recognizer_speech import WhishperRecognizerSpeech


class TypeOfRecognizer(Enum):
    GOOGLE = "GOOGLE"
    WHISPER = "WHISPER"


class RecognizeSpeech(object):

    def __init__(self, typeOfRecognizer):
        self.typeOfRecognizer = typeOfRecognizer
        self.recognizer = None
        self._selectRecognizer()

    def _selectRecognizer(self):
        if self.typeOfRecognizer == TypeOfRecognizer.GOOGLE:
            self.recognizer = GoogleRecognizerSpeech()
        elif self.typeOfRecognizer == TypeOfRecognizer.WHISPER:
            self.recognizer = WhishperRecognizerSpeech()
        else:
            return None
