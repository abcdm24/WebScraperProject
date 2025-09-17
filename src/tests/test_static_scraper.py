# import pytest
from src.scraper.static_scraper import StaticScraper
import src.scraper.scraper as scraper_module


def test_static_scraper_returns_dict(monkeypatch, fake_html_response):
    """
    StaticScraper should return a dict with 'url' and 'links' keys
    :param monkeypatch:
    :return:
    """

    monkeypatch.setattr(scraper_module.requests, "get", lambda url: fake_html_response)

    scraper = StaticScraper("https://example.com")
    data = scraper.scrape()

    assert isinstance(data, dict)
    assert "url" in data
    assert "links" in data
    assert len(data["links"]) == 2
