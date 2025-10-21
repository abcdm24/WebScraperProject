from fastapi import APIRouter
import json
from datetime import datetime
from ..utils.config import DATA_DIR_HISTORY

router = APIRouter()

# HISTORY_DIR = Path("data/history")


@router.get("/")
def get_history():
    history = []

    if not DATA_DIR_HISTORY.exists():
        DATA_DIR_HISTORY.mkdir(parents=True, exist_ok=True)
        return []

    for file_path in DATA_DIR_HISTORY.glob("*.json"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                history.append({
                    "id": file_path.stem,
                    "url": data.get("url", ""),
                    "scrape_type": data.get("scrape_type", "static"),
                    "status": data.get("status", "unknown"),
                    "timestamp": data.get("timestamp", datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()),
                    "result_file": str(file_path)
                })
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue
    history.sort(key=lambda x: x["timestamp"], reverse=True)
    return history
