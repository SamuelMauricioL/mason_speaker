import speech_recognition as sr

from src.respond import respond
from src.digital_assistant import digital_assistant

def recognize_speech_from_mic(recognizer, microphone):

    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
        
    with microphone as source:
        print("I am listening...")
        recognizer.adjust_for_ambient_noise(source) # #  analyze the audio source for 1 second
        audio = recognizer.listen(source)
        
    response = {
        "ok": None,
        "error": None,
    }
    try:
        response["ok"] = recognizer.recognize_google(audio)
        print("You said: " + response["ok"])
    except sr.RequestError as e:
        response["error"] = "Request Failed; {0}".format(e)
    except sr.UnknownValueError:
        response["error"] = "Google Speech Recognition did not understand audio"
    
    return response

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