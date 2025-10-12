import tempfile
import json
from fastapi.testclient import TestClient
from src.backend.main import app
from src.tests.conftest import API_PREFIX

client = TestClient(app)

# --- Success Cases ---


def create_temp_json(data: dict) -> str:
    """Helper to create a temporary JSON file and return its path"""
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".json", mode="w", encoding="utf-8")
    json.dump(data, tmp)
    tmp.close()
    return tmp.name


def test_scrape_static_success(monkeypatch):
    test_data = {"title": "Test Static Scrape"}
    tmp_file = create_temp_json(test_data)

    def mock_services(url: str) -> str:
        return tmp_file

    monkeypatch.setattr("src.backend.routes.scraper_routes.scrape_static_service", mock_services)

    response = client.post(f"{API_PREFIX}/static", json={"url": "https://example.com"})
    data = response.json()
    print('Scraper data: ', data)
    assert response.status_code == 200
    assert data["status"] == "success"
    assert data["data"] == test_data

    # assert isinstance(data["data"], dict)
    # assert data["data"]["title"] == "Test Static Scrape"
    # assert data["error"] is None


def test_scrape_dynamic_success(monkeypatch):
    test_data = {"title": "Dynamic Page Scrape"}
    tmp_file = create_temp_json(test_data)

    def mock_services(url: str) -> dict:
        return tmp_file

    monkeypatch.setattr("src.backend.routes.scraper_routes.scrape_dynamic_service", mock_services)

    response = client.post(f"{API_PREFIX}/dynamic", json={"url": "https://example.com"})
    data = response.json()
    print('Scraper data: ', data)
    assert response.status_code == 200
    assert data["status"] == "success"
    assert data["data"] == test_data
    # assert data["data"]["title"] == "Dynamic Page Scrape"
    # assert data["error"] is None


def test_scrape_api_success(monkeypatch):
    test_data = {"result": "API data fetched"}
    tmp_file = create_temp_json(test_data)

    def mock_services(url: str) -> str:
        return tmp_file

    monkeypatch.setattr("src.backend.routes.scraper_routes.scrape_api_service", mock_services)

    response = client.post(f"{API_PREFIX}/api", json={"url": "https://jsonplaceholder.typicode.com/todos/1"})
    data = response.json()
    print('Scraper data: ', data)
    assert response.status_code == 200
    assert data["status"] == "success"
    assert data["data"]["result"] == "API data fetched"
    assert data["error"] is None


# --- Error Cases ---


def test_scrape_static_error(monkeypatch):
    def mock_service(url: str) -> dict:
        raise RuntimeError("Failed to scrape static page")

    monkeypatch.setattr("src.backend.routes.scraper_routes.scrape_static_service", mock_service)

    response = client.post(f"{API_PREFIX}/static", json={"url": "https://bad-url.com"})
    data = response.json()

    assert response.status_code == 200
    assert data["status"] == "error"
    assert data["data"] is None
    assert "Failed to scrape static page" in data["error"]


def test_scrape_dynamic_error(monkeypatch):
    def mock_service(url: str) -> dict:
        raise ValueError("Dynamic scraper crashed")

    monkeypatch.setattr("src.backend.routes.scraper_routes.scrape_dynamic_service", mock_service)

    response = client.post(f"{API_PREFIX}/dynamic", json={"url": "https://bad-url.com"})
    data = response.json()

    assert response.status_code == 200
    assert data["status"] == "error"
    assert data["data"] is None
    assert "Dynamic scraper crashed" in data["error"]


def test_scrape_api_error(monkeypatch):
    def mock_service(ur: str) -> dict:
        raise Exception("API not reachable")

    monkeypatch.setattr("src.backend.routes.scraper_routes.scrape_api_service", mock_service)

    response = client.post(f"{API_PREFIX}/api", json={"url": "https://bad-api.com"})
    data = response.json()

    assert response.status_code == 200
    assert data["status"] == "error"
    assert data["data"] is None
    assert "API not reachable" in data["error"]
