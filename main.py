import speech_recognition as sr

from src.respond import respond
from src.digital_assistant import digital_assistant
from src.recognize_speech_from_mic import recognize_speech_from_mic

if __name__ == "__main__":
    respond("Hi Samuel, What can I do for you?")
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    isListening = True
    while isListening == True:
        response = recognize_speech_from_mic(recognizer, mic)
        if (response['ok'] != None):
            isListening = digital_assistant(response['ok'])
            continue
        if (response['error'] != None):
            print(response['error'])
            isListening = False
            break