from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, HttpUrl
from src.backend.services.scraper_services import (
    scrape_static_service,
    scrape_dynamic_service,
    scrape_api_service
)

# from src.utils.config import DATA_DIR_PROCESSED
router = APIRouter()


class ScrapeRequest(BaseModel):
    url: HttpUrl
# output: str = None
# f"{DATA_DIR_PROCESSED}/output.json"


class ScrapeResponse(BaseModel):
    status: str
    output: str


@router.post("/static")
def scrape_static(request: ScrapeRequest):
    try:
        result_path = scrape_static_service(str(request.url))
        return ScrapeResponse(status="success", output=result_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/dynamic")
def scrape_dynamic(request: ScrapeRequest):
    """Scrape a dynamic page and return output path."""
    try:
        result_path = scrape_dynamic_service(str(request.url))
        return ScrapeResponse(status="success", output=result_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/api")
def scrape_api(request: ScrapeRequest):
    """Scrape from an API endpoint and return output path/"""
    try:
        result_path = scrape_api_service(str(request.url))
        return ScrapeResponse(status="success", output=result_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
