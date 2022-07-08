from time import ctime
from src.respond import respond
from src.recognize_speech_from_mic import RecognizeSpeech

def digital_assistant(data):
    listening = True
    if "how are you" in data:
        respond("I'm well")

    if "what time is it" in data:
        respond(ctime())
    
    if "create a template" in data:
        # data = data.split(" ")
        # command = str(data[1])
        respond("ok, what is the name of the template?")
        recognizeSpeech = RecognizeSpeech();
        response = recognizeSpeech.from_mic()
        if (response['ok'] != None):
            respond("looking for " + response['ok'] + " mason template on brickhub")

        if (response['error'] != None):
            respond("template not found")

    if "see you" in data:
        respond("See you")
        return False
    return listening