# import os.path

# from src.scraper.dynamic_scraper import DynamicScraper


# def test_dynamic_scraper_placeholder():
#     """DynamicScraper should return placeholdr data"""
#     scraper = DynamicScraper("https://example.com")
#     data = scraper.scrape()
#
#     assert isinstance(data, dict)
#     assert data["url"] == "https://example.com"
#     assert "content" in data

import json
import os
# import types
from src.scraper.dynamic_scraper import DynamicScraper


def test_dynamic_scraper_saves_json(monkeypatch, fake_html_response, tmp_path):
    """
    DynamicScraper should save a JSON file with expected keys and return its path
    :param monkeypatch:
    :param fake_html_response:
    :param tmp_path:
    :return:
    """

    # Fake driver class
    class FakeDriver:

        # def __init__(self, *args, **kwargs):
        def __init__(self):
            self.page_source = fake_html_response.text

        @staticmethod
        def get(self):
            return None

        @staticmethod
        def quit(self):
            return None

    # Patch webdriver.Chrome to return fake driver
    monkeypatch.setattr("src.scraper.dynamic_scraper.webdriver.Chrome", lambda *a, **kw: FakeDriver())

    output_file = tmp_path / "dynamic.json"
    scraper = DynamicScraper("https://example.com/dynamic", str(output_file))
    result_path = scraper.scrape()

    assert os.path.exists(result_path)

    with open(result_path, "r") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert len(data) == 1
    record = data[0]

    assert "url" in record
    assert "links" in record
    assert "headings" in record
    assert "metadata" in record
    assert "images" in record
    assert record["url"] == "https://example.com/dynamic"
