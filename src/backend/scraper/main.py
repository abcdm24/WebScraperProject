# import requests

import argparse

from .web_scraper import WebScraper
from src.utils.parser import extract_links
from src.utils.storage import save_json

# from bs4 import BeautifulSoup
# from pathlib import Path
# import pandas as pd

# First Basic Scraper test
# url ="https://quotes.toscrape.com"
# response = requests.get(url)
#
# soup = BeautifulSoup(response.text, "html.parser")
#
# quotes = []
# for q in soup.find_all("div", class_="quote"):
#     text = q.find("span", class_="text").get_text()
#     author = q.find("small", class_="author").get_text()
#     tags = [tag.get_text() for tag in q.find_all("a", class_="tag")]
#     quotes.append({"text": text, "author": author, "tags": tags})
#
# df = pd.DataFrame(quotes)
# df.to_csv("quotes.csv", index=False)
#
# print("scraped", len(quotes), "quotes")

# multi page scraping test

# page = 1
# all_quotes = []
#
# while True:
#     url = f"https://quotes.toscrape.com/page/{page}/"
#     response = requests.get(url)
#     if "No quotes found!" in response.text:
#         break
#     soup = BeautifulSoup(response.text, "html.parser")
#     for q in soup.find_all("div", class_="quote"):
#         text = q.find("span", class_="text").get_text()
#         author = q.find("small", class_="author").get_text()
#         tags = [tag.get_text() for tag in q.find_all("a", class_="tag")]
#         all_quotes.append({"text": text, "author": author, "tags": tags})
#
#     page += 1
#
# print("Scraped total:", len(all_quotes))


# parser, storage test
# def scrape_static(url: str, output: str):
#     """Fetch a static page and save extracted data to JSON."""
#     print(f"Fetching {url}...")
#     response = requests.get(url, timeout=10)
#     response.raise_for_status()
#
#     html = response.text
#
#     data = {
#         "url": url,
#         "metadata": parser.extract_metadata(html, base_url=url),
#         "headings": parser.extract_headings(html),
#         "links": parser.extract_links(html, base_url=url),
#         "images": parser.extract_images(html, base_url=url)
#     }
#
#     storage.save_json(data, output)
#     print(f"✅ Save results to {output}")
#
#
# def main():
#     parser_cli = argparse.ArgumentParser(description="WebScraper CLI")
#     subparsers = parser_cli.add_subparsers(dest="command")
#
#     static_parser = subparsers.add_parser("static", help="Scrape a static web page")
#     static_parser.add_argument("url", help="URL to scrape")
#     static_parser.add_argument(
#         "--output",
#         "-o",
#         default="output.json",
#         help="Path to save JSON results (default: output.json)",
#     )
#
#     args = parser_cli.parse_args()
#
#     if args.command == "static":
#         scrape_static(args.url, args.output)
#     else:
#         parser_cli.print_help()
#
#
# if __name__ == "__main__":
#     main()


def main():
    parser_cli = argparse.ArgumentParser(prog="scraper")
    parser_cli.add_argument("mode", choices=["static", "dynamic"], help="Scraping mode")
    parser_cli.add_argument("url", help="URL to scrape")
    parser_cli.add_argument("--output", "-o", help="Output file", default="data/output.json")

    args = parser_cli.parse_args()

    scraper = WebScraper(args.url)
    html = scraper.scrape_returnhtml()
    # print(html)
    links = extract_links(html)
    save_json({"url": args.url, "links": links}, args.output)

    print(f"✅ Scraped {len(links)} links from {args.url}")
    print(f"💾 Saved to {args.output}")


if __name__ == "__main__":
    main()
