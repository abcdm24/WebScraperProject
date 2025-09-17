from scraper.scraper import WebScraper
from scraper.static_scraper import StaticScraper
from scraper.dynamic_scraper import DynamicScraper
from scraper.api_scraper import ApiScraper
from utils.storage import save_as_json, save_as_csv


def run():
    url = "https://example.com"

    # Try basic scraper
    # scraper = WebScraper(url)
    # data = scraper.scrape()
    # print("Scraped data:", data)
    # save_as_json(data, "example.json")
    # save_as_csv(data, "example.csv")

    # Try static scraper
    # scraper = StaticScraper(url)
    # data = scraper.scrape()
    # save_as_json(data, "static_example.json")

    # Try dynamic scraper
    # scraper = DynamicScraper(url)
    # data = scraper.scrape()
    # save_as_json(data, "dynamic_example.json")

    # Try API scraper
    # api_url = "https://jsonplaceholder.typicode.com/todos/1"
    # scraper = ApiScraper(api_url)
    # data = scraper.scrape()
    # save_as_json(data, "api_example.json")

    scrapers = [
        StaticScraper(url),
        DynamicScraper(url),
        ApiScraper("https://jsonplaceholder.typicode.com/todos/1")
    ]

    for scraper in scrapers:
        data = scraper.scrape()
        filename = scraper.__class__.__name__.lower() + ".json"
        save_as_json(data, filename)


if __name__ == "__main__":
    run()
