import os
from dotenv import load_dotenv

# Load variables from .env file in project root
load_dotenv()

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
GUARDRAILS_API_KEY = os.getenv("GUARDRAILS_API_KEY")

API_BASE_URL = "https://api.perplexity.ai"
MODEL_NAME = "sonar-medium-online"
API_ACCESS_KEY = os.getenv("API_ACCESS_KEY")  # For your app's API key protection
