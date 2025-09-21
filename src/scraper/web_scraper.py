# import requests
# # from src.utils.parser import parse_links
# from src.utils.common import get_headers
# from .base_scraper import BaseScraper
# from bs4 import BeautifulSoup
#
#
# class WebScraper(BaseScraper):
#     """
#     Default implementation for scraping HTML pages.
#     """
#     # def __init__(self, url: str):
#     #     self.url = url
#
#     def fetch_html(self) -> str:
#         response = requests.get(self.url, headers=get_headers())
#         response.raise_for_status()
#         return response.text
#
#     # def parse_html(self, html: str):
#     #     soup = BeautifulSoup(html, "html.parser")
#     #     links = [a["href"]for a in soup.find_all("a", href=True)]
#     #     return {"url": self.url, "links": links}
#
#     # def scrape(self) -> dict:
#     #     html = self.fetch_html()
#     #     links = parse_links(html)
#     #     return {"url": self.url, "links": links}
#     #     # return self.parse_html(html)
#
#     def scrape(self) -> dict:
#         response = requests.get(self.url)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.text, "html.parser")
#         links = [a["href"] for a in soup.find_all("a", href=True)]
#         return {"url": self.url, "links": links}
#
#     def scrape_returnhtml(self):
#         response = requests.get(self.url)
#         response.raise_for_status()
#         return response.text

from src.scraper.static_scraper import StaticScraper
from src.scraper.dynamic_scraper import DynamicScraper
from src.scraper.api_scraper import ApiScraper


class WebScraper:
    """High-level scraper that selects the right scraper type."""

    def __init__(self, scraper_type: str, url:   str, output: str):
        self.scraper_type = scraper_type
        self.url = url
        self.output = output

    def scrape(self) -> str:
        if self.scraper_type == "static":
            return StaticScraper(self.url, self.output).scrape()
        elif self.scraper_type == "dynamic":
            return DynamicScraper(self.url, self.output).scrape()
        elif self.scraper_type == "api":
            return ApiScraper(self.url, self.output).scrape()
        else:
            raise ValueError(f"Unknown scraper type: {self.scraper_type}")
