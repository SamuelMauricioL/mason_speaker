import speech_recognition as sr
from src.prints.print_verified_microphone import print_verified_microphone

class RecognizeSpeech:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        print_verified_microphone()

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super().__new__(self)
        return self.instance

    def from_mic(self):
        
        if not isinstance(self.recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")

        if not isinstance(self.microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")
            
        with self.microphone as source:
            print("I'm listening 👂")
            self.recognizer.adjust_for_ambient_noise(source) # #  analyze the audio source for 1 second
            audio = self.recognizer.listen(source)
            
        response = {
            "ok": None,
            "error": None,
        }
        try:
            response["ok"] = self.recognizer.recognize_google(audio)
            print("You said: " + response["ok"])
        except sr.RequestError as e:
            # response["error"] = "Request Failed; {0}".format(e)
            response["ok"] = None
            response["error"] = "I didn't understand"
        except sr.UnknownValueError:
            response["ok"] = None
            response["error"] = "Can you say it again?"
        
        return response