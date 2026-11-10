"""FFmpeg-based clip export. FFmpeg must be installed and available on PATH."""

import shutil
import subprocess
from pathlib import Path


def require_ffmpeg() -> str:
    executable = shutil.which("ffmpeg")
    if not executable:
        raise RuntimeError("FFmpeg was not found. Install FFmpeg and add it to PATH.")
    return executable


def export_clip(input_path: str, start: float, end: float, output_path: str, aspect: str = "source"):
    if end <= start:
        raise ValueError("Clip end must be later than clip start.")
    ffmpeg = require_ffmpeg()
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    command = [ffmpeg, "-hide_banner", "-loglevel", "error", "-y", "-ss", str(max(0, start)), "-i", input_path, "-t", str(end - start)]
    if aspect == "9:16":
        command += ["-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920"]
    elif aspect == "1:1":
        command += ["-vf", "scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080"]
    elif aspect != "source":
        raise ValueError("Aspect must be source, 9:16, or 1:1.")
    command += ["-c:v", "libx264", "-preset", "medium", "-crf", "21", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(output)]
    completed = subprocess.run(command, capture_output=True, text=True)
    if completed.returncode:
        raise RuntimeError(completed.stderr.strip() or "FFmpeg export failed.")
    return output
