from .config import settings
from fastapi import FastAPI
import os
import requests
import psycopg2

app = FastAPI()

DATABASE_URL = settings.database_url
OLLAMA_URL = settings.ollama_url

@app.get("/health")
def health():
    db_ok = False
    ollama_ok = False
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=2)
        ollama_ok = r.status_code == 200
    except:
        ollama_ok = False
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.close()
        db_ok = True
    except:
        db_ok = False
    return {
        "status": "ok",
        "db": db_ok,
        "ollama": ollama_ok
    }