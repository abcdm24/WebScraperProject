import json
import os
import requests
import pytest
from src.scraper.web_scraper import WebScraper


def test_webscraper_statis(monkeypatch, fake_html_response, tmp_path):
    """WebScraper with 'static' should delegate
    to Static Scraper and save json"""

    # Patch requests.get for StaticScraper
    monkeypatch.setattr(requests, "get", lambda url, timeout=10: fake_html_response)

    output_file = tmp_path / "static.json"
    scraper = WebScraper("static", "https://example.com", str(output_file))
    result_path = scraper.scrape()

    assert os.path.exists(result_path)

    with open(result_path, "r") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert data[0]["url"] == "https://example.com"
    assert "links" in data[0]


def test_webscraper_dynamic(monkeypatch, fake_html_response, tmp_path):
    """
    WebScraper with 'dynamic' should delegate to DynamicScraper and save JSON.
    :param monkeypatch:
    :param fake_html_response:
    :param tmp_path:
    :return:
    """

    # Fake Selenium driver
    class FakeDriver:

        def __init__(self):
            self.page_source = fake_html_response.text

        def get(self, url): return None
        def quit(self): return None

    import src.scraper.dynamic_scraper as dynamic_module
    monkeypatch.setattr(dynamic_module.webdriver, "Chrome", lambda *a, **kw: FakeDriver())
    # monkeypatch.setattr("src.scraper.dynamic_scraper.webdriver.Chrome", lambda *a, **kw: FakeDriver())

    output_file = tmp_path / "dynamic.json"
    scraper = WebScraper("dynamic", "https://example.com/dynamic", str(output_file))
    result_path = scraper.scrape()

    assert os.path.exists(result_path)

    with open(result_path, "r") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert data[0]["url"] == "https://example.com/dynamic"
    assert "headings" in data[0]


def test_webscraper_api(monkeypatch, tmp_path):
    """
    WebScraper with 'api' should delegate to ApiScraper and save JSON.
    :param monkeypatch:
    :param tmp_path:
    :return:
    """

    # Fake API response
    class FakeResponse:
        def raise_for_status(self): return None
        def json(self): return {"status": "ok", "items": [1, 2, 3]}

    monkeypatch.setattr(requests, "get", lambda url, timeout=10: FakeResponse())

    output_file = tmp_path / "api.json"
    scraper = WebScraper("api", "https://api.example.com/data", str(output_file))
    result_path = scraper.scrape()

    assert os.path.exists(result_path)

    with open(result_path, "r") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert data[0]["url"] == "https://api.example.com/data"
    assert data[0]["api_response"]["status"] == "ok"
    assert data[0]["api_response"]["items"] == [1, 2, 3]


def test_webscraper_invalid_type(tmp_path):
    """
    WebScraper with invalid type should raise ValueError.
    :param tmp_path:
    :return:
    """

    scraper = WebScraper("unknown", "https://example.com", str(tmp_path / "bad.json"))
    with pytest.raises(ValueError):
        scraper.scrape()
