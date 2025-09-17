# import pytest
from src.scraper.api_scraper import ApiScraper


def test_api_scraper_return_json(monkeypatch, fake_json_response):
    """ApiScraper should parse JSON response"""

    # fake_json = {"id": 1, "title": "test"}

    # class FakeResponse:
    #     def raise_for_status(self): pass
    #     def json(self): return fake_json

    monkeypatch.setattr("requests.get", lambda url: fake_json_response)

    scraper = ApiScraper("https://fakeapi.com/data")
    data = scraper.scrape()

    assert isinstance(data, dict)
    assert data["url"] == "https://fakeapi.com/data"
    assert "data" in data
    assert data["data"]["title"] == "test"
