from fastapi import APIRouter, HTTPException
from app.schemas import UserPrompt, BotResponse
from app.api_client import get_response
from app.guardrails import validate_input

router = APIRouter()

@router.post("/chat", response_model=BotResponse)
def chat_endpoint(item: UserPrompt):
    try:
        validate_input(item.prompt)

        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": item.prompt}
        ]

        response = get_response(messages)
        bot_reply = response.choices[0].message.content

        return BotResponse(response=bot_reply)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
