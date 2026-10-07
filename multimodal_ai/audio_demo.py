from faster_whisper import WhisperModel

model = WhisperModel("base")
segments, info = model.transcribe("sample.mp3")

print("Transcription:")
for segment in segments:
    print(segment.text)