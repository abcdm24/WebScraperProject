# 🚀 Azure FastAPI Deployment Notes

## ⚙️ Overview
When deploying a FastAPI app (such as the **SmartScraper backend**) to **Azure Container Apps**, HTTPS traffic is terminated at Azure’s load balancer and forwarded to your container using plain HTTP.  
Because of this, FastAPI may incorrectly assume requests are **HTTP** instead of **HTTPS**, which can cause:
- ⚠️ “Mixed Content” errors in browsers  
- Incorrect request scheme detection (`request.url.scheme == "http"`)  
- Redirects or CORS rules behaving unexpectedly  

---

## ✅ Solution: Enable Proxy Header Support

Add the following lines to your **`main.py`**:

```python
from fastapi import FastAPI
from starlette.middleware.proxy_headers import ProxyHeadersMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from .routes.scraper_routes import router as scraper_router
from .routes.history_routes import router as history_router
from .utils.config import API_PREFIX

app = FastAPI(title="SmartScraper API")

# ✅ Fix for Azure HTTPS → HTTP internal forwarding
app.add_middleware(ProxyHeadersMiddleware, trusted_hosts="*")
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

# CORS setup
origins = [
    "http://localhost:4200",
    "https://green-ocean-0c329510f.3.azurestaticapps.net"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(scraper_router, prefix=f"{API_PREFIX}/scraper", tags=["Scraper"])
app.include_router(history_router, prefix=f"{API_PREFIX}/history", tags=["History"])

@app.get("/")
def root():
    return {"status": "ok", "message": "SmartScraper API is running"}
