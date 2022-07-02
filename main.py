import speech_recognition as sr
from time import ctime
from gtts import gTTS
import os
import requests


if __name__ == "__main__":
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=1)