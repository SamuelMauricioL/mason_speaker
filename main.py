import speech_recognition as sr

from src.respond import respond
from src.digital_assistant import digital_assistant
from src.recognize_speech_from_mic import recognize_speech_from_mic

from src.prints.print_hi import print_hi
from src.prints.print_error import print_error
from src.prints.print_verified_microphone import print_verified_microphone

if __name__ == "__main__":
    print_hi()
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print_verified_microphone()

    isListening = True
    while isListening == True:
        response = recognize_speech_from_mic(recognizer, mic)
        if (response['ok'] != None):
            isListening = digital_assistant(response['ok'])

        if (response['error'] != None):
            print_error(response['error'])