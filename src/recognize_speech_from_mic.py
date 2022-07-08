import speech_recognition as sr
from src.prints.print_verified_microphone import print_verified_microphone

'''
   // Voice Recognition (Speech-to-Text) - Google Speech Recognition API
   -> This API converts spoken text (microphone) into written text (Python strings)
   -> Personal or testing purposes only
   -> Generic key is given by default (it may be revoked by Google at any time)
   -> If using API key, quota for your own key is 50 requests per day
'''

class RecognizeSpeech:
    # initializing Recognizer and Microphone instances
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        print_verified_microphone()

    '''
    We override the __new__ method with some logic to check
    if the object already exists. 
    
    The hasattr method is used to check if our object has
    the instance property. 
    
    If so, self.instance is returned;
    otherwise, the existing instance is returned
    '''
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super().__new__(self)
        return self.instance

    def from_mic(self):
        
        # check that recognizer and microphone arguments are appropriate type
        if not isinstance(self.recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")

        if not isinstance(self.microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")
        
        # adjust the recognizer sensitivity to ambient noise and record audio
        # from the microphone
        with self.microphone as source:
            print("I'm listening 👂")
            self.recognizer.adjust_for_ambient_noise(source) # #  analyze the audio source for 1 second
            audio = self.recognizer.listen(source)

        '''
        Transcribe speech from recorded from `microphone`.
        Returns a dictionary with three keys:
        "ok": `None` if speech could not be transcribed,
                otherwise a string containing the transcribed text 
        "error":   `None` if no error occured, otherwise a string containing
                an error message if the API could not be reached or
                speech was unrecognizable
        '''
        
        # set up the response object
        response = {
            "ok": None,
            "error": None,
        }

        # try recognizing the speech in the recording
        # if a RequestError or UnknownValueError exception is caught,
        #   update the response object accordingly
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