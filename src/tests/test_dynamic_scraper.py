from src.scraper.dynamic_scraper import DynamicScraper


def test_dynamic_scraper_placeholde():
    """DynamicScraper should return placeholdr data"""
    scraper = DynamicScraper("https://example.com")
    data = scraper.scrape()

    assert isinstance(data, dict)
    assert data["url"] == "https://example.com"
    assert "content" in data
