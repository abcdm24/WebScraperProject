# import pytest
# from src.scraper.api_scraper import ApiScraper
#
#
# def test_api_scraper_return_json(monkeypatch, fake_json_response):
#     """ApiScraper should parse JSON response"""
#
#     # fake_json = {"id": 1, "title": "test"}
#
#     # class FakeResponse:
#     #     def raise_for_status(self): pass
#     #     def json(self): return fake_json
#
#     monkeypatch.setattr("requests.get", lambda url: fake_json_response)
#
#     scraper = ApiScraper("https://fakeapi.com/data")
#     data = scraper.scrape()
#
#     assert isinstance(data, dict)
#     assert data["url"] == "https://fakeapi.com/data"
#     assert "data" in data
#     assert data["data"]["title"] == "test"

import json
import os
from ..scraper.api_scraper import ApiScraper


def test_api_scraper_saves_json(monkeypatch, tmp_path):
    """
    ApiScraper should save a JSON file containing the API response
    and return its path
    :param monkeypatch:
    :param tmp_path:
    :return:
    """

    # Fake API response object
    class FakeResponse:
        def __init__(self):
            self.status_code = 200
            
        def raise_for_status(self):
            pass

        def json(self):
            return {"status": "ok", "items": [1, 2, 3]}

    # Patch requests.get to return fake response
    monkeypatch.setattr("backend.scraper.api_scraper.requests.get", lambda url, timeout=10: FakeResponse())

    # Temporary output file
    output_file = tmp_path / "api.json"

    scraper = ApiScraper("https://api.example.com/data", str(output_file))
    result_path = scraper.scrape()

    # Validate output file
    assert os.path.exists(result_path)

    with open(result_path, "r") as f:
        data = json.load(f)

    assert isinstance(data, dict)
    assert len(data) == 5
    # record = data[0]
    #
    # assert "url" in record
    # assert "api_response" in record
    # assert record["url"] == "https://api.example.com/data"
    # assert record["api_response"]["status"] == "ok"
    # assert record["api_response"]["items"] == [1, 2, 3]

    metadata = data.get("metadata")
    text_json = data.get("text")

    assert metadata is not None
    assert metadata["url"] == "https://api.example.com/data"
    assert metadata["status_code"] == 200

    api_response = json.loads(text_json)
    assert api_response["status"] == "ok"
    assert api_response["items"] == [1, 2, 3]
