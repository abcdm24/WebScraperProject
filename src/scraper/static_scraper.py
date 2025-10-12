# from .web_scraper import WebScraper
#
#
# class StaticScraper(WebScraper):
#     """
#     For scraping static HTML pages (basic requests + BeautifulSoup).
#     """
#
#     def scrape(self) -> dict:
#         print("🔎 Using StaticScraper...")
#         return super().scrape()

import requests
from src.utils import parser, storage
from src.scraper.base_scraper import BaseScraper


class StaticScraper(BaseScraper):
    """Scraper for static page: {self.url}"""
    def scrape(self) -> str:
        print(f"Fetching static page: {self.url}")

        headers = {
            "user-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64 "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/140.0.0.0 Safari/537.36"
            )
        }

        # response = requests.get(self.url, timeout=10)
        response = requests.get(self.url, headers=headers, timeout=30, stream=False)
        response.raise_for_status()
        html = response.text

        data = {
            "url": self.url,
            "metadata": parser.extract_metadata(html, base_url=self.url),
            "headings": parser.extract_headings(html),
            "links": parser.extract_links(html, base_url=self.url),
            "images": parser.extract_images(html, base_url=self.url),
            "text": parser.extract_text(html)
        }

        storage.save_json([data], self.output)
        print(f" Saved static scrape results to {self.output}")
        return self.output
    