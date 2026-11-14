# This file contains the API.
# app is a common convention used with FastAPI applications.

from fastapi import FastAPI
from src.amt import add_tax

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/amount")
def amount(amount: float):
    return {"total": add_tax(amount)}
