import os

# Set Guardrails API key here or load from .env before any Guardrails usage
os.environ["GUARDRAILS_API_KEY"] = "your_guardrails_hub_api_key_here"

from fastapi import FastAPI
from app.router import router

app = FastAPI(title="Perplexity Chatbot")

app.include_router(router, prefix="/api")
