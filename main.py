from fastapi import FastAPI
from app.router import router

app = FastAPI(title="Perplexity Guardrails Chatbot")

app.include_router(router, prefix="/api")
