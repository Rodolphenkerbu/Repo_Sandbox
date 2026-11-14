# This file contains the API.
# app is a common convention used with FastAPI applications.
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
