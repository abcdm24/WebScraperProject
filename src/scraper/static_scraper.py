from .web_scraper import WebScraper


class StaticScraper(WebScraper):
    """
    For scraping static HTML pages (basic requests + BeautifulSoup).
    """

    def scrape(self) -> dict:
        print("🔎 Using StaticScraper...")
        return super().scrape()
