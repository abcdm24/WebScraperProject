from fastapi import FastAPI
from src.backend.routes.scraper_routes import router as scraper_router

app = FastAPI(title="Webscraper API")


@app.get("/")
def root():
    return {"message": "WebScraper API is running"}


app.include_router(scraper_router, prefix="/scraper")
