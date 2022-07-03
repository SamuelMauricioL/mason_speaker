import speech_recognition as sr

def recognize_speech_from_mic(recognizer, microphone):
    
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
        
    with microphone as source:
        print("I'm listening 👂")
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
        # response["error"] = "Request Failed; {0}".format(e)
        response["ok"] = None
        response["error"] = "I didn't understand"
    except sr.UnknownValueError:
        response["ok"] = None
        response["error"] = "Can you say it again?"
    
    return response