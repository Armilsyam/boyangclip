"""Local transcription helpers. The model loads only when transcription is requested."""

from faster_whisper import WhisperModel

from app.config import DEFAULT_MODEL_SIZE


def transcribe(video_path: str, model_size: str = DEFAULT_MODEL_SIZE, language: str | None = None):
    """Transcribe a media file and return serializable timestamped segments."""
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, info = model.transcribe(
        video_path,
        beam_size=5,
        language=language or None,
        vad_filter=True,
    )
    result = [
        {"start": float(segment.start), "end": float(segment.end), "text": segment.text.strip()}
        for segment in segments
        if segment.text.strip()
    ]
    return result, info.language
