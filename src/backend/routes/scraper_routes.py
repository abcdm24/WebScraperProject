from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, HttpUrl
from src.backend.services.scraper_services import (
    scrape_static_service,
    scrape_dynamic_service,
    scrape_api_service
)
from src.tests.conftest import API_PREFIX

# from src.utils.config import DATA_DIR_PROCESSED
router = APIRouter()


class ScrapeRequest(BaseModel):
    url: HttpUrl
# output: str = None
# f"{DATA_DIR_PROCESSED}/output.json"


class ScrapeRequestAPI(BaseModel):
    url: str = "https://jsonplaceholder.typicode.com/todos/1"


class ScrapeResponse(BaseModel):
    status: str
    output: str


def wrap_response(func, url: str) -> ScrapeResponse:
    """
    Helper tp ensure consistent success/error response.
    :param func:
    :param url:
    :return:
    """
    try:
        result_path = func(url)
        return ScrapeResponse(status="success", output=result_path)
    except Exception as e:
        return ScrapeResponse(status="error", output=str(e))


@router.post("/static", response_model=ScrapeResponse)
def scrape_static(request: ScrapeRequest):
    try:
        # result_path = scrape_static_service(str(request.url))
        # return ScrapeResponse(status="success", output=result_path)
        return wrap_response(scrape_static_service, str(request.url))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/dynamic", response_model=ScrapeResponse)
def scrape_dynamic(request: ScrapeRequest):
    """Scrape a dynamic page and return output path."""
    try:
        # result_path = scrape_dynamic_service(str(request.url))
        # return ScrapeResponse(status="success", output=result_path)
        return wrap_response(scrape_dynamic_service, str(request.url))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/api", response_model=ScrapeResponse)
def scrape_api(request: ScrapeRequestAPI):
    """Scrape from an API endpoint and return output path/"""
    try:
        # print(f"URL: {request.url}")
        # result_path = scrape_api_service(str(request.url))
        # return ScrapeResponse(status="success", output=result_path)
        return wrap_response(scrape_api_service, str(request.url))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
