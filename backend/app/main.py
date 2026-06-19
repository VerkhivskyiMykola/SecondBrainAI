from fastapi import FastAPI
import os
import requests

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")
OLLAMA_URL = os.getenv("OLLAMA_URL")

@app.get("/")
def root():
    return {"status": "backend is running"}

@app.get("/ollama")
def test_ollama():
    r = requests.get(f"{OLLAMA_URL}/api/tags")
    return r.json()