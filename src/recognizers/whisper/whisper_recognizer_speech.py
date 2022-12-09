import whisper
import wavio as wv
import sounddevice as sd
from src.core.global_configuration import GlobalConfiguration
from src.core.global_paths import GlobalPaths
from src.core.languages import TypeOfLanguage


class WhishperRecognizerSpeech:

    def __init__(self):
        self.frequency = 44100
        self.record_duration = 2
        self.audio_path = GlobalPaths.audio_record_wav

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super().__new__(self)
        return self.instance

    def from_mic(self):
        # Start recorder with the given values
        # of duration and sample frequency
        recording = sd.rec(
            int(self.record_duration * self.frequency),
            samplerate=self.frequency,
            channels=1,
        )

        # Record audio for the given number of seconds
        sd.wait()

        # Convert the NumPy array to audio file
        wv.write(
            self.audio_path,
            recording,
            self.frequency,
            sampwidth=2,
        )

        # get language(ENGLISH, SPANISH, PORTUGUESE) selected
        type_of_language = GlobalConfiguration().get_language()
        language = get_whisper_language(type_of_language)

        model = whisper.load_model("base")
        result = model.transcribe(
            self.audio_path,
            fp16=False,
            language=language,
        )

        # set up the response object
        response = {
            "ok": None,
            "error": None,
        }

        if (result["text"] == ""):
            response["ok"] = None
            response["error"] = result["text"]
        else:
            response["ok"] = result["text"]
            response["error"] = None

        return response


def get_whisper_language(type_of_language):
    if type_of_language == TypeOfLanguage.SPANISH:
        return 'Spanish'
    elif type_of_language == TypeOfLanguage.ENGLISH:
        return 'English'
    elif type_of_language == TypeOfLanguage.PORTUGUESE:
        return 'Portuguese'
