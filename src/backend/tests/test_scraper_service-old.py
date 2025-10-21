# # import pytest
# # from fastapi import FastAPI
# from fastapi.testclient import TestClient
# from src.backend.main import app
# # import src.backend.routes.scraper_routes
# from src.tests.conftest import API_PREFIX
#
# client = TestClient(app)
#
# print(app.routes)
# # --- Success Cases ---
#
#
# def test_scrape_static_success(monkeypatch):
#     def mock_services(url: str) -> str:
#         return "static_output.json"
#
#     print(app.routes)
#
#     monkeypatch.setattr("src.backend.routes.scraper_routes.scrape_static_service", mock_services)
#
#     response = client.post(f"{API_PREFIX}/static", json={"url": "https://example.com"})
#     data = response.json()
#
#     assert response.status_code == 200
#     assert data["status"] == "success"
#     assert data["output"] == "static_output.json"
#
#
# def test_scrape_dynamic_success(monkeypatch):
#     def mock_service(url: str) -> str:
#         return "dynamic_output.json"
#
#     monkeypatch.setattr("src.backend.routes.scraper_routes.scrape_dynamic_service", mock_service)
#
#     response = client.post(f"{API_PREFIX}/dynamic", json={"url": "https://example.com"})
#     data = response.json()
#
#     assert response.status_code == 200
#     assert data["status"] == "success"
#     assert data["output"] == "dynamic_output.json"
#
#
# def test_scrape_api_success(monkeypatch):
#     def mock_service(url: str) -> str:
#         return "api_output.json"
#
#     monkeypatch.setattr("src.backend.routes.scraper_routes.scrape_api_service", mock_service)
#
#     response = client.post(f"{API_PREFIX}/api", json={"url": "https://jsonplaceholder.typicode.com/todos/1"})
#     data = response.json()
#
#     assert response.status_code == 200
#     assert data["status"] == "success"
#     assert data["output"] == "api_output.json"
#
# # --- Error Cases ---
#
#
# def test_scrape_static_error(monkeypatch):
#     def mock_service(utl: str) -> str:
#         raise RuntimeError("Failed to scrape static page")
#
#     monkeypatch.setattr("src.backend.routes.scraper_routes.scrape_static_service", mock_service)
#
#     response = client.post(f"{API_PREFIX}/static", json={"url": "https://bad-url.com"})
#     data = response.json()
#
#     assert response.status_code == 200
#     assert data["status"] == "error"
#     assert "Failed to scrape static page" in data["output"]
#
#
# def test_scrape_dynamic_error(monkeypatch):
#     def mock_service(url: str) -> str:
#         raise ValueError("Dynamic scraper crashed")
#
#     monkeypatch.setattr("src.backend.routes.scraper_routes.scrape_dynamic_service", mock_service)
#
#     response = client.post(f"{API_PREFIX}/dynamic", json={"url": "https://bad-url.com"})
#     data = response.json()
#
#     assert response.status_code == 200
#     assert data["status"] == "error"
#     assert "Dynamic scraper crashed" in data["output"]
#
#
# def test_scrape_api_error(monkeypatch):
#     def mock_service(url: str) -> str:
#         raise Exception("API not reachable")
#
#     monkeypatch.setattr("src.backend.routes.scraper_routes.scrape_api_service", mock_service)
#
#     response = client.post(f"{API_PREFIX}/api", json={"url": "https://bad-api.com"})
#     data = response.json()
#
#     assert response.status_code == 200
#     assert data["status"] == "error"
#     assert "API not reachable" in data["output"]
