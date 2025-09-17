from bs4 import BeautifulSoup


def parse_links(html: str) -> list[str]:
    soup = BeautifulSoup(html,"html.parser")
    return [a["href"] for a in soup.find_all("a", href=True)]
