import json
import shutil
from datetime import datetime, timedelta, UTC
from src.utils.config import DATA_DIR_HISTORY


def test_get_history_empty(client):
    """Should return empty list when no history files exist"""
    # Ensure history directory is clean
    if DATA_DIR_HISTORY.exists():
        shutil.rmtree(DATA_DIR_HISTORY)
    DATA_DIR_HISTORY.mkdir(exist_ok=True)

    response = client.get("/api/history")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 0


def test_get_history_with_files(client):
    """Should return valid list when history files exist."""

    # Prepare mock history files
    DATA_DIR_HISTORY.mkdir(exist_ok=True)

    history_entries = [
        {
            "id": "abc123",
            "url": "https://example.com/1",
            "scrape_type": "static",
            "status": "success",
            "timestamp": (datetime.now(UTC) - timedelta(hours=1)).isoformat(),
            "result_file": "file1.json"
            # {"items": 5}
        },
        {
            "id": "def456",
            "url": "https://example.com/2",
            "scrape_type": "api",
            "status": "failed",
            "timestamp": datetime.now(UTC).isoformat(),
            "result_file": "file2.json"
            # {"items": 0}
        }]

    # Write them to files
    for entry in history_entries:
        file_path = DATA_DIR_HISTORY / f"{entry['id']}.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(entry, f, indent=2)

    response = client.get("/api/history")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2

    # Check that entries aer sorted (newest first)
    assert data[0]["id"] == "def456"
    assert data[1]["id"] == "abc123"

    " Check expected fields"
    for entry in data:
        assert "id" in entry
        assert "url" in entry
        assert "scrape_type" in entry
        assert "status" in entry
        assert "timestamp" in entry
        assert "result_file" in entry
