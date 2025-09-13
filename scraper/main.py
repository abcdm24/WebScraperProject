import requests
from bs4 import BeautifulSoup
import pandas as pd

# First Basic Scraper
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

page = 1
all_quotes = []

while True:
    url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    if "No quotes found!" in response.text:
        break
    soup = BeautifulSoup(response.text, "html.parser")
    for q in soup.find_all("div", class_="quote"):
        text = q.find("span", class_="text").get_text()
        author = q.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in q.find_all("a", class_="tag")]
        all_quotes.append({"text": text, "author": author, "tags": tags})

    page += 1

print("Scraped total:", len(all_quotes))

