from bs4 import BeautifulSoup
from urllib.parse import urljoin


def parse_links(html: str) -> list[str]:
    soup = BeautifulSoup(html,"html.parser")
    return [a["href"] for a in soup.find_all("a", href=True)]


def extract_links(html: str, base_url: str = "") -> list[str]:
    """extract all links from HTML and return absolute URLs."""
    soup = BeautifulSoup(html,"html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        abs_url = urljoin(base_url, a["href"])
        links.append(abs_url)
    return links


def extract_headings(html: str) -> list[str]:
    """Extract text from all heading tags (h1-h6)"""
    soup = BeautifulSoup(html, "html.parser")
    headings = []
    for level in range(1, 7):
        for h in soup.find_all(f"h{level}"):
            headings.append(h.get_text(strip=True))
    return headings


def extract_metadata(html: str, base_url: str = "") -> dict:
    """Extract basic metadata like title and description"""
    soup = BeautifulSoup(html, "html.parser")
    metadata = {}

    # Title
    title_tag = soup.find("title")
    if title_tag:
        metadata["description"] = title_tag.get_text(strip=True)

    # Description
    description = soup.find("meta", attrs={"name": "description"})
    if description and description.get("content"):
        metadata["description"] = description["content"]

    # Canonical
    canonical = soup.find("link", rel="canonical")
    if canonical and canonical.get("href"):
        metadata["canonical"] = urljoin(base_url, canonical["href"])

    # OpenGraph tags
    for prop in ["og:title", "og:description", "og:image", "og:url"]:
        tag = soup.find("meta", property=prop)
        if tag and tag.get("content"):
            metadata[prop] = urljoin(base_url, tag["content"]) if prop in ("og:image", "og:url") else tag["content"]

    return metadata


def extract_images(html: str, base_url: str = "") -> list[str]:
    """Extract all image sources and return absolute URLs."""
    soup = BeautifulSoup(html, "html.parser")
    images = []
    for img in soup.find_all("img", src=True):
        abs_url = urljoin(base_url, img["src"])
        images.append(abs_url)
    return images

