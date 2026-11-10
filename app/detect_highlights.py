"""Scene-change helper for optional visual inspection."""

import cv2


def detect_highlights(video_path: str, threshold: float = 0.35, sample_every: int = 3):
    """Return timestamps with a large visual change; these are hints, not semantic highlights."""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Could not open video: {video_path}")
    timestamps = []
    previous = None
    frame_index = 0
    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            frame_index += 1
            if frame_index % max(1, sample_every):
                continue
            small = cv2.resize(frame, (160, 90))
            gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
            if previous is not None:
                score = cv2.absdiff(gray, previous).mean() / 255.0
                if score >= threshold:
                    timestamps.append(round(frame_index / fps, 2))
            previous = gray
    finally:
        cap.release()
    return timestamps
