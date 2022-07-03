from time import ctime
from src.respond import respond

def digital_assistant(data):
    listening = True
    if "how are you" in data:
        respond("I'm well")

    if "what time is it" in data:
        respond(ctime())
    
    if "create a template" in data:
        data = data.split(" ")
        command = str(data[1])
        if "template" in command:
            brick = str(data[2:])
            respond(brick)

    if "stop listening" in data:
        respond("See you")
        return False
    return listening