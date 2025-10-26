# Web Scraper Project

A simple Python-based web scraper with pagination and SQLAlchemy for persistence.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>

   ```

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/Scripts/activate # On Windows (Git Bash)

   # OR

   source venv/bin/activate # On Linux/Mac

3. Install dependencies:
   pip install -r requirements.txt

   Usage
   Run the scraper:
   python main.py

   Data is stored in the database defined in config.py (default: SQLite).

   Features

   Static page scraping

   Pagination handling

   SQLAlchemy integration

## 🌐 Azure Deployment Notes

For details on deploying the SmartScraper FastAPI backend to Azure Container Apps and fixing HTTPS-related issues, see:

➡️ [Azure FastAPI Deployment Notes](./notes/azure-deployment-notes.md)
