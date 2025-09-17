import requests
# from .scraper import WebScraper
from .base_scraper import BaseScraper


class ApiScraper(BaseScraper):
    """
    For scraping structured API endpoints (JSON/XML).
    """

    def scrape(self) -> dict:
        print(" Using ApiScraper...")
        response = requests.get(self.url)
        response.raise_for_status()
        try:
            return {"url": self.url, "data": response.json()}
        except ValueError:
            return {"url": self.url, "data": response.text}
