import whisper

model = whisper.load_model("base")
result = model.transcribe(
    "speech.wav",
    fp16=False,
)
print(result["text"])