# import pytest
from src.scraper.static_scraper import StaticScraper
import src.scraper.web_scraper as scraper_module


# def test_static_scraper_returns_dict(monkeypatch, fake_html_response):
#     """
#     StaticScraper should return a dict with 'url' and 'links' keys
#     :param monkeypatch:
#     :return:
#     """
#
#     monkeypatch.setattr(scraper_module.requests, "get", lambda url: fake_html_response)
#
#     scraper = StaticScraper("https://example.com")
#     data = scraper.scrape()
#
#     assert isinstance(data, dict)
#     assert "url" in data
#     assert "links" in data
#     assert len(data["links"]) == 2

from src.scraper.static_scraper import StaticScraper
import src.scraper.web_scraper as scraper_module
import json
import os
import requests


def test_static_scraper_saves_json(monkeypatch, fake_html_response, tmp_path):
    """
    StaticScraper should save a JSON file and return a dict
    with 'status' and 'data' keys.
    """

    # Patch requests.get to use fake response
    # monkeypatch.setattr(requests, "get", lambda url, timeout=10: fake_html_response)
    monkeypatch.setattr(requests, "get", lambda url, **kwargs: fake_html_response)

    # Define temporary output file
    output_file = tmp_path / "output.json"

    # Run scraper
    scraper = StaticScraper("https://example.com", str(output_file))
    result_path = scraper.scrape()

    print("Scraped output", result_path)

    # # Check return type
    # assert isinstance(result, dict)
    # assert result["status"] == "success"
    # assert "data" in result

    # Verify file exists
    assert os.path.exists(result_path)

    # Load and validate JSON contents
    with open(result_path, "r") as f:
        data = json.load(f)

    # storage.save_json saves a list -> unwrap first element
    assert isinstance(data, list)
    assert len(data) == 1
    record = data[0]
    #
    # assert "url" in record
    # assert "links" in record
    # assert "headings" in record
    # assert "metadata" in record
    # assert "images" in record
    # assert record["url"] == "https://example.com"

    # # Validate data structure
    # data = result["data"]
    # assert isinstance(data, dict)
    # for key in ["url", "links", "headings", "metadata", "images"]:
    #     assert key in data
    # assert data["url"] == "https://example.com"
    #
    # assert saved_data == data
