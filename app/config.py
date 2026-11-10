from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "data" / "input"
OUTPUT_DIR = BASE_DIR / "data" / "output"
TEMP_DIR = BASE_DIR / "data" / "temp"

MODEL_SIZE = "small"  # small = ringan, medium = lebih akurat tapi lebih berat
MIN_CLIP_SECONDS = 10
MAX_CLIP_SECONDS = 60
TARGET_ASPECT = "9:16"
