from src.respond import respond
from src.digital_assistant import digital_assistant
from src.recognize_speech_from_mic import RecognizeSpeech

from src.prints.print_hi import print_hi
from src.prints.print_error import print_error

if __name__ == "__main__":
    print_hi()
    # recognizeSpeech = RecognizeSpeech();

    # isListening = True
    # while isListening == True:
    #     response = recognizeSpeech.from_mic()
    #     if (response['ok'] != None):
    #         isListening = digital_assistant(response['ok'])

    #     if (response['error'] != None):
    #         print_error(response['error'])