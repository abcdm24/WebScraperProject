import requests
# from src.utils.parser import parse_links
from src.utils.common import get_headers
from .base_scraper import BaseScraper
from bs4 import BeautifulSoup


class WebScraper(BaseScraper):
    """
    Default implementation for scraping HTML pages.
    """
    # def __init__(self, url: str):
    #     self.url = url

    def fetch_html(self) -> str:
        response = requests.get(self.url, headers=get_headers())
        response.raise_for_status()
        return response.text

    # def parse_html(self, html: str):
    #     soup = BeautifulSoup(html, "html.parser")
    #     links = [a["href"]for a in soup.find_all("a", href=True)]
    #     return {"url": self.url, "links": links}

    # def scrape(self) -> dict:
    #     html = self.fetch_html()
    #     links = parse_links(html)
    #     return {"url": self.url, "links": links}
    #     # return self.parse_html(html)

    def scrape(self) -> dict:
        response = requests.get(self.url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        links = [a["href"] for a in soup.find_all("a", href=True)]
        return {"url": self.url, "links": links}

    def scrape_returnhtml(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text
