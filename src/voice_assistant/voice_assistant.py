import os
from time import ctime
from src.utils.respond import respond
from src.utils.logger import logger, TypeOfRemitter
from src.recognizers.recognize_speech import RecognizeSpeech, TypeOfRecognizer
from src.voice_assistant import comands


def voice_assistant(data):

    listening = True
    data = data[1:]
    logger(TypeOfRemitter.ME, data)
    data = data.lower()
    if "how are you" in data:
        respond("I'm well")

    if "what time" in data:
        respond(ctime())

    if "search a template" in data:
        respond("looking on brickhub, what is the name of the brick?")
        recognizeSpeech = RecognizeSpeech(TypeOfRecognizer.WHISPER).recognizer
        response = recognizeSpeech.from_mic()
        # brick = input('What is the name of the brick? 🧱\n')
        if (response['ok'] != None):
            os.system("mason search " + response['ok'])
        # os.system("mason add -g " + brick)
        # os.system("mason make " + brick)

        # if (response['ok'] != None):

    if "create feature" in data:
        respond('Okay, select the brick')
        comands.create_feature()
        respond('New feature generated')

    if "set project" in data:
        respond('Okay, select your project')
        comands.set_project()
        respond('ready, got it')

    if "open project" in data:
        respond('okay')
        comands.open_project()
        respond('ready, got it')

    if "execute" in data:
        data = data.replace('execute', '')
        command = data.lower()
        print("mason search " + command)
        os.system(command)

    if "repository state" in data:
        output = os.popen("git status").read()
        if "no changes added to commit" in output:
            respond("you have changes to upload")
        if "nothing to commit" in output:
            respond("no changes to upload")
        print(output)

    if "upload my changes" in data:
        respond("Which is the message?")
        message = input('git commit --message ')
        os.system("git add .")
        os.system("git commit -m " + '"' + message + '"')
        os.system("git push")
        respond("cool, uploaded changes")

    if "see you" in data:
        respond("See you")
        return False
    return listening
