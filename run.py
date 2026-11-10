from app.detect_highlights import detect_highlights
from app.transcribe import transcribe
from app.render import export_clip

video = "data/input/sample.mp4"
highlights = detect_highlights(video, threshold=0.35)
print("Detected highlight timestamps:", highlights)

segments = transcribe(video)
print("Transcribed segments:", segments[:3])

# Ambil highlight pertama sebagai demo
if highlights:
    start, end = highlights[0], min(highlights[0] + 20, max(s["end"] for s in segments))
    export_clip(video, start, end, "data/output/clip_1.mp4")
    print("Exported:", "data/output/clip_1.mp4")
