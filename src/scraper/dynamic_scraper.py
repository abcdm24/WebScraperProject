# from .scraper import WebScraper
from .base_scraper import BaseScraper


class DynamicScraper(BaseScraper):
    """
    For scraping JavaScript-heavy pages (later: Salenium, Playwright, etc.)
    """

    def scrape(self) -> dict:
        print("⚡ Using DynamicScraper (future: JS rendering)...")
        return {"url": self.url, "content": "Dynamic scraping not implemented yet"}
        #return super().scrape()
