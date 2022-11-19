import whisper
import wavio as wv
import sounddevice as sd


class WhishperRecognizerSpeech:

    def __init__(self):
        self.frequency = 44100
        self.record_duration = 2
        self.audio_path = "./util/audio/record.wav"

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

        model = whisper.load_model("base")
        result = model.transcribe(
            self.audio_path,
            fp16=False,
            language='English',
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
