from abc import ABC, abstractmethod


class BaseScraper(ABC):
    """
    Abstract base class for all scrapers.
    Enforces that all scrapers implement `scrape()`.
    """

    def __init__(self, url: str, output: str):
        self.url = url
        self.output = output

    # @abstractmethod
    # def scrape(self) -> dict:
    #     """
    #     Each scraper must implement this method.
    #     Should return a dictionary containing scraped data.
    #     :return:
    #     """
    #     pass

    @abstractmethod
    def scrape(self) -> str:
        """Perform scraping and return path of saved JSON file."""
        pass
