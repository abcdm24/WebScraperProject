import os
from datetime import datetime
from ..scraper.web_scraper import WebScraper
from ..utils.config import DATA_DIR_PROCESSED


def _make_output_path(prefix: str = "scrape") -> str:
    """Generate a timestamped output path inside the data folder."""
    os.makedirs(DATA_DIR_PROCESSED, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(DATA_DIR_PROCESSED, f"{prefix}_{timestamp}.json")


def scrape_static_service(url: str) -> str:
    """Run static scraper and return saved file path."""
    output = _make_output_path("static")
    scraper = WebScraper("static", url, output)
    return scraper.scrape()


def scrape_dynamic_service(url: str) -> str:
    """Run dynamic scraper and return saved file path."""
    output = _make_output_path("dynamic")
    scraper = WebScraper("dynamic", url, output)
    return scraper.scrape()


def scrape_api_service(url: str) -> str:
    """Run API scraper and return saved file path."""
    output = _make_output_path("api")
    scraper = WebScraper("api", url, output)
    return scraper.scrape()
