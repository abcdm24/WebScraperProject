from ..utils import parser

html = "<html><head><title>Test</title></head><body><a href='/page'>Link</a></body></html>"


def test_extract_links():
    links = parser.extract_links(html, base_url="https://example.com")
    assert links == ["https://example.com/page"]
