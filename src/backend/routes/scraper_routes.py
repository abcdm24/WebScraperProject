import json
import uuid

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, HttpUrl
from ..services.scraper_services import (
    scrape_static_service,
    scrape_dynamic_service,
    scrape_api_service
)
from datetime import datetime, UTC

# from src.tests.conftest import API_PREFIX

from ..utils.config import DATA_DIR_HISTORY

router = APIRouter()


class ScrapeRequest(BaseModel):
    url: HttpUrl
# output: str = None
# f"{DATA_DIR_PROCESSED}/output.json"


class ScrapeRequestAPI(BaseModel):
    url: str = "https://jsonplaceholder.typicode.com/todos/1"


# class ScrapeResponse(BaseModel):
#     status: str
#     output: str

class ScrapeResponse(BaseModel):
    status: str
    data: dict | None = None
    error: str | None = None


# def wrap_response(func, url: str) -> ScrapeResponse:
#     """
#     Helper to ensure consistent success/error response.
#
#     """
#     try:
#         result_path = func(url)
#         return ScrapeResponse(status="success", output=result_path)
#     except Exception as e:
#         return ScrapeResponse(status="error", output=str(e))


def save_scrape_history(url: str, scrape_type: str, status: str, result_summary: dict):
    DATA_DIR_HISTORY.mkdir(exist_ok=True)

    scrape_id = str(uuid.uuid4())[:8]
    history_file = DATA_DIR_HISTORY / f"{scrape_id}.json"

    record = {
        "id": scrape_id,
        "url": url,
        "scrape_type": scrape_type,
        "status": status,
        "timestamp": datetime.now(UTC).isoformat(),
        "data": result_summary
    }
    with open(history_file, "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)

    return scrape_id


def load_scraped_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        if isinstance(data, list):
            return data[0] if len(data) > 0 else {}
        return data


def wrap_response(func, url: str, scrape_type: str) -> ScrapeResponse:
    """
    Helper to ensure consistent success/error response.
    """
    try:
        result_path = func(url)
        content = load_scraped_json(result_path)
        save_scrape_history(
            url,
            scrape_type=scrape_type,
            status="success",
            result_summary={"items": len(content) if isinstance(content, list) else 1})
        return ScrapeResponse(status="success", data=content)
    except Exception as e:
        return ScrapeResponse(status="error", error=str(e), data=None)


@router.post("/static", response_model=ScrapeResponse)
def scrape_static(request: ScrapeRequest):
    try:
        # result_path = scrape_static_service(str(request.url))
        # return ScrapeResponse(status="success", output=result_path)
        return wrap_response(scrape_static_service, str(request.url), "static")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/dynamic", response_model=ScrapeResponse)
def scrape_dynamic(request: ScrapeRequest):
    """Scrape a dynamic page and return output path."""
    try:
        # result_path = scrape_dynamic_service(str(request.url))
        # return ScrapeResponse(status="success", output=result_path)
        return wrap_response(scrape_dynamic_service, str(request.url), "dynamic")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/api", response_model=ScrapeResponse)
def scrape_api(request: ScrapeRequestAPI):
    """Scrape from an API endpoint and return output path/"""
    try:
        # print(f"URL: {request.url}")
        # result_path = scrape_api_service(str(request.url))
        # return ScrapeResponse(status="success", output=result_path)
        return wrap_response(scrape_api_service, str(request.url), "api")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
