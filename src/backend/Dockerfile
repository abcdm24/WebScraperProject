# Use official Python Base
FROM python:3.11-slim-bullseye

WORKDIR /app

# Environment variables
ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# system deps (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# Debugging
RUN echo "Listing context contents:" && ls -R .
# RUN echo "Checcking for requirements.txt:" && ls -l ./backend/


# copy requirements
COPY backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy app code
COPY backend /app/backend
COPY scraper /app/scraper
COPY utils /app/utils

# Debugging
RUN echo "Listing context contents:" && ls -R .
RUN echo "Checcking for requirements.txt:" && ls -l /app/
RUN echo "=== Confirm backend structure ===" && ls -R /app/backend

# expose port (App Service uses PORT env var but we expose 8000)
EXPOSE 8000

# Use Gunicorn with Uvicorn workers
CMD ["gunicorn", "backend.main:app", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "--log-level", "info"]

