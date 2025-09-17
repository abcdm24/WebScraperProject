import json
import csv
from pathlib import Path
from .config import DATA_DIR_PROCESSED

# DATA_DIR = Path(__file__).resolve().parents[2] / "data"
# DATA_DIR.mkdir(exist_ok=True)


def save_as_json(data: dict, filename: str = "output.json") -> None:
    filepath = DATA_DIR_PROCESSED / filename
    with open(Path(filepath), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Saved JSON to {filepath}")


def save_as_csv(data: dict, filename: str = "output.csv") -> None:
    filepath = DATA_DIR_PROCESSED / filename
    with open(Path(filepath), "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["url", "links"])
        writer.writerow([data["url"], " | ".join(data["links"])])
    print(f"Saved CSV to {filepath}")
