# Chatbot API Project

## Overview
An industry-ready Python chatbot application using Perplexity API. FastAPI backend with modular structure, input/output guardrails, secure config, and best practices.

## Quick Start

1. Install requirements:
    ```
    pip install -r requirements.txt
    ```
2. Add your Perplexity API key to `.env`:
    ```
    PERPLEXITY_API_KEY=your-own-key
    ```

3. Run server:
    ```
    uvicorn main:app --reload
    ```

## Folder Structure
See codebase, each module described in-context.

## Features
- Modular code
- Secure API key management
- Guardrails for input/output
- Extensible for production

## Testing
Place unit tests in `tests/`. Run with your preferred test runner.
