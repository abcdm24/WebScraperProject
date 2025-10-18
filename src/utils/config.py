from pathlib import Path

API_PREFIX = "/api"

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

DATA_DIR_PROCESSED = DATA_DIR / "processed"
DATA_DIR_PROCESSED.mkdir(exist_ok=True)

DATA_DIR_RAW = DATA_DIR / "raw"
DATA_DIR_RAW.mkdir(exist_ok=True)

DATA_DIR_HISTORY = DATA_DIR / "history"
