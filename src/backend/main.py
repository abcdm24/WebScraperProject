from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.scraper_routes import router as scraper_router
# from src.tests.conftest import API_PREFIX
from .utils.config import API_PREFIX
from .routes.history_routes import router as history_router

app = FastAPI(title="Webscraper API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # allow any origin
    allow_credentials=True,
    allow_methods=["*"],     # allow all HTTP methods
    allow_headers=["*"],     # allow all headers
)


@app.get("/")
def root():
    return {"status": "ok", "message": "WebScraper API is running"}


@app.get("/health")
def health_check():
    return {"health": "healthy"}


app.include_router(scraper_router, prefix=f"{API_PREFIX}/scraper")
app.include_router(history_router, prefix=f"{API_PREFIX}/history")
