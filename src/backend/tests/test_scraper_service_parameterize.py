import tempfile
import json
import pytest
from fastapi.testclient import TestClient
from ..main import app
from ..utils.config import API_PREFIX

client = TestClient(app)


def create_temp_json(data: dict) -> str:
    """Helper to create a temprary JSON file and return its path."""
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".json", mode="w", encoding="utf-8")
    json.dump(data, tmp)
    tmp.close()
    return tmp.name

# --- Success + Error parametrized tests ---


@pytest.mark.parametrize(
    "endpoint, service_name, test_data, request_url",
    [
        ("static", "scrape_static_service", {"title": "Static Test"}, "https://example.com"),
        ("dynamic", "scrape_dynamic_service", {"title": "Dynamic Test"}, "https://example.com"),
        ("api", "scrape_api_service", {"result": "API Test"}, "https://jsonplaceholder.typicode.com/todos/1"),
    ],
)
def test_scraper_success(monkeypatch, endpoint, service_name, test_data, request_url):
    """Test that scraper endpoints return success when service works"""
    tmp_file = create_temp_json(test_data)

    def mock_service(url: str) -> str:
        return tmp_file

    monkeypatch.setattr(f"src.backend.routes.scraper_routes.{service_name}", mock_service)

    response = client.post(f"{API_PREFIX}/scraper/{endpoint}", json={"url": request_url})
    data = response.json()

    assert response.status_code == 200
    assert data["status"] == "success"
    assert data["data"] == test_data


# --- Error cases ---
@pytest.mark.parametrize(
    "endpoint, service_name, exception, message, request_url",
    [
        ("static", "scrape_static_service", RuntimeError("Failed to scrape static page"),
         "Failed to scrape static page",
         "https://bad-url.com"),
        ("dynamic", "scrape_dynamic_service", RuntimeError("Dynamic scraper crashed"), "Dynamic scraper crashed",
         "https://bad-url.com"),
        ("api", "scrape_api_service", RuntimeError("API not reachable"), "API not reachable", "https://bad-api.com")
    ],
)
def test_scraper_error(monkeypatch, endpoint, service_name, exception, message, request_url):
    """Test that scraper endpoints return error when service raises exception."""
    def mock_service(url: str) -> str:
        raise exception

    monkeypatch.setattr(f"src.backend.routes.scraper_routes.{service_name}", mock_service)

    response = client.post(f"{API_PREFIX}/scraper/{endpoint}", json={"url": request_url})
    data = response.json()

    assert response.status_code == 200
    assert data["status"] == "error"
    assert data["data"] is None
    assert message in data["error"]
