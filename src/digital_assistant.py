from time import ctime
from src.respond import respond

def digital_assistant(data):
    if "how are you" in data:
        listening = True
        respond("I'm well")

    if "what time is it" in data:
        listening = True
        respond(ctime())
    
    if "create" in data:
        data = data.split(" ")
        command = str(data[1])
        if "template" in command:
            listening = True
            brick = str(data[2:])
            respond(brick)

    if "stop listening" in data:
        respond("See you")
        return False
    return listening