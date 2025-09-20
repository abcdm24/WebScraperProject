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


def save_json(data: any, filepath: str | Path):
    """Save list of dicts to JSON file."""
    filepath = Path(filepath)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_json(filepath: str | Path) -> list[dict]:
    """Load list of dicts from JSON file."""
    filepath = Path(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def save_csv(data: list[dict], filepath: str | Path):
    """Save list of dicts from CSV file."""
    filepath = Path(filepath)
    if not data:
        return

    keys = data[0].keys()
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


def load_csv(filepath: str | Path) -> list[dict]:
    """Load list of dicts from csv file."""
    filepath = Path(filepath)
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
