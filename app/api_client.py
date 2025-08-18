import openai
from config.settings import PERPLEXITY_API_KEY, API_BASE_URL, MODEL_NAME

# Set OpenAI client config to use Perplexity's API
openai.api_key = PERPLEXITY_API_KEY
openai.api_base = API_BASE_URL

def get_response(messages):
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=messages,
        max_tokens=1024,
        temperature=0.7
    )
    return response
