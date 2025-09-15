from fastapi import FastAPI, UploadFile, File
import whisper, os

app = FastAPI()
model = whisper.load_model("tiny")  # हल्का मॉडल ताकि Render Free Plan पर चल सके

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    # Save temp file
    filename = "temp.mp3"
    with open(filename, "wb") as f:
        f.write(await file.read())

    # Run transcription
    result = model.transcribe(filename, language=None)  # Auto detect Hindi + Hinglish

    # Cleanup
    os.remove(filename)

    return {
        "text": result["text"],
        "segments": result["segments"]
  }
