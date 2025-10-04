import pytest
from fastapi.testclient import TestClient
from src.backend.main import app
from src.tests.conftest import API_PREFIX

client = TestClient(app)

# --- Success + Error parametrized tests ---


@pytest.mark.parametrize(
    "endpoint, service_name, mock_return, request_url",
    [
        ("static", "scrape_static_service", "static_output.json", "https://example.com"),
        ("dynamic", "scrape_dynamic_service", "dynamic_output.json", "https://example.com"),
        ("api", "scrape_api_service", "api_output.json", "https://jsonplaceholder.typicode.com/todos/1"),
    ],
)
def test_scraper_success(monkeypatch, endpoint, service_name, mock_return, request_url):
    """Test that scraper endpoints return success when service works"""
    def mock_service(url: str) -> str:
        return mock_return

    monkeypatch.setattr(f"src.backend.routes.scraper_routes.{service_name}", mock_service)

    response = client.post(f"{API_PREFIX}/{endpoint}", json={"url": request_url})
    data = response.json()

    assert response.status_code == 200
    assert data["status"] == "success"
    assert data["output"] == mock_return


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

    response = client.post(f"{API_PREFIX}/{endpoint}", json={"url": request_url})
    data = response.json()

    assert response.status_code == 200
    assert data["status"] == "error"
    assert message in data["output"]
