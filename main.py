from src.digital_assistant import digital_assistant
from src.recognizers.recognize_speech import RecognizeSpeech, TypeOfRecognizer

from src.utils.print_hi import print_hi
from src.utils.print_error import print_error

if __name__ == "__main__":
    print_hi()
    recognize_speech = RecognizeSpeech(TypeOfRecognizer.WHISPER).recognizer

    while True:
        response = recognize_speech.from_mic()
        if (response['ok'] != None):
            isListening = digital_assistant(response['ok'])

        if (response['error'] != None):
            print_error(response['error'])
