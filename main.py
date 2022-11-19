from src.digital_assistant import digital_assistant
from src.recognizers.recognize_speech import RecognizeSpeech, TypeOfRecognizer

from src.utils.respond import respond

if __name__ == "__main__":
    respond("Hi, What can I do for you?")
    recognize_speech = RecognizeSpeech(TypeOfRecognizer.WHISPER).recognizer

    isListening = True
    while isListening == True:
        response = recognize_speech.from_mic()
        if (response['ok'] != None):
            isListening = digital_assistant(response['ok'])

        if (response['error'] != None):
            respond(response['error'])
