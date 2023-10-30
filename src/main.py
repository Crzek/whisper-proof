import whisper


MEDIA = "./media/Music.mp3"

model = whisper.load_model("medium")
result = model.transcribe("/media/Music.mp3")
print(f' The text in video: \n {result["text"]}')