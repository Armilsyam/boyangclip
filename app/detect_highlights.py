import cv2
import os

def detect_highlights(video_path: str, threshold: float = 0.35):
    cap = cv2.VideoCapture(video_path)
    frames = []
    prev = None

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if prev is not None:
            diff = cv2.absdiff(gray, prev)
            score = diff.mean() / 255.0
            if score > threshold:
                frames.append(round(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0))
        prev = gray

    cap.release()
    return frames
