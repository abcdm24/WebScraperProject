import sys
import os
import pytest
from fastapi.testclient import TestClient

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from ..main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def fake_html():
    """Reusable fake HTML with two links"""
    return """
    <html>
        <body>
            <a href="https://test.com/page1">Link1</a>
            <a href="https://test.com/page2">Link2</a>
        </body>
    </html>
    """


@pytest.fixture
def fake_json():
    """Reusable fake JSON data"""
    return {"id": 1, "title": "test"}


class FakeHTMLResponse:
    """Fake requests.Response for HTML pages"""
    def __init__(self, text):
        self.text = text

    def raise_for_status(self): pass


class FakeJSONResponse:
    """Fake requests.Response for JSON APIs"""
    def __init__(self, data):
        self.data = data

    def raise_for_status(self):
        pass

    def json(self):
        return self.data


@pytest.fixture
def fake_html_response(fake_html):
    return FakeHTMLResponse(fake_html)


@pytest.fixture
def fake_json_response(fake_json):
    return FakeJSONResponse(fake_json)
