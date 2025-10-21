import os
from pathlib import Path

API_PREFIX = "/api"

# For Azure deployment
AZURE_DATA_ROOT = Path(os.getenv("DATA_DIR","/home/data"))

if not AZURE_DATA_ROOT.exists():
    PROJECT_ROOT = Path(__file__).resolve().parents[2]
    AZURE_DATA_ROOT = PROJECT_ROOT / "data"

DATA_DIR = AZURE_DATA_ROOT
DATA_DIR.mkdir(exist_ok=True)

DATA_DIR_PROCESSED = DATA_DIR / "processed"
DATA_DIR_PROCESSED.mkdir(exist_ok=True)

DATA_DIR_RAW = DATA_DIR / "raw"
DATA_DIR_RAW.mkdir(exist_ok=True)

DATA_DIR_HISTORY = DATA_DIR / "history"
DATA_DIR_HISTORY.mkdir(exist_ok=True)

# For local
# PROJECT_ROOT = Path(__file__).resolve().parents[2]
#
# DATA_DIR = PROJECT_ROOT / "data"
# DATA_DIR.mkdir(exist_ok=True)
#
# DATA_DIR_PROCESSED = DATA_DIR / "processed"
# DATA_DIR_PROCESSED.mkdir(exist_ok=True)
#
# DATA_DIR_RAW = DATA_DIR / "raw"
# DATA_DIR_RAW.mkdir(exist_ok=True)
#
# DATA_DIR_HISTORY = DATA_DIR / "history"
