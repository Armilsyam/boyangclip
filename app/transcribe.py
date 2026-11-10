from faster_whisper import WhisperModel

from app.config import MODEL_SIZE

model = WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8")

def transcribe(video_path: str):
    segments, info = model.transcribe(video_path, beam_size=5)
    text = []
    for segment in segments:
        text.append({
            "start": segment.start,
            "end": segment.end,
            "text": segment.text
        })
    return text
