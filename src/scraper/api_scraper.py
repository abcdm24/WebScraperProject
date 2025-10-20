# import requests
# # from .scraper import WebScraper
# from .base_scraper import BaseScraper
#
#
# class ApiScraper(BaseScraper):
#     """
#     For scraping structured API endpoints (JSON/XML).
#     """
#
#     def scrape(self) -> dict:
#         print(" Using ApiScraper...")
#         response = requests.get(self.url)
#         response.raise_for_status()
#         try:
#             return {"url": self.url, "data": response.json()}
#         except ValueError:
#             return {"url": self.url, "data": response.text}

import json
import requests
from src.utils import storage
from src.scraper.base_scraper import BaseScraper


class ApiScraper(BaseScraper):
    """Scraper for APIs returning JSON."""

    def scrape(self) -> str:
        print(f"Fetching API data: {self.url}")
        response = requests.get(self.url, timeout=10)
        response.raise_for_status()
        data = response.json()

        normalized_output = {
            "metadata": {"ur": self.url, "status_code": response.status_code},
            "headings": [],
            "links": [],
            "images": [],
            "text": json.dumps(data, indent=2)
        }
        storage.save_json(normalized_output, self.output)
        # storage.save_json([{"url": self.url, "api_response": data}], self.output)
        print(f"Saved API scrape results to {self.output}")
        return self.output
