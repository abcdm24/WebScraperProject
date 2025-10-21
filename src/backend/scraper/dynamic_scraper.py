# # from .scraper import WebScraper
# from .base_scraper import BaseScraper
#
#
# class DynamicScraper(BaseScraper):
#     """
#     For scraping JavaScript-heavy pages (later: Salenium, Playwright, etc.)
#     """
#
#     def scrape(self) -> dict:
#         print("⚡ Using DynamicScraper (future: JS rendering)...")
#         return {"url": self.url, "content": "Dynamic scraping not implemented yet"}
#         # return super().scrape()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ..utils import parser
from ..utils import storage
from .base_scraper import BaseScraper


class DynamicScraper(BaseScraper):
    """Scraper for dynamic (JavaScript-rendered) pages."""

    def scrape(self) -> str:
        print(f"Fetching dynamic page: {self.url}")

        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get(self.url)
        html = driver.page_source

        data = {
            "url": self.url,
            "metadata": parser.extract_metadata(html, base_url=self.url),
            "headings": parser.extract_headings(html),
            "links": parser.extract_links(html, base_url=self.url),
            "images": parser.extract_images(html, base_url=self.url)
        }

        storage.save_json([data], self.output)
        print(f"Saved dynamic scrape results tp {self.output}")
        return self.output
