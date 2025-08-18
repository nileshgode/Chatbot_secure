from pydantic import BaseModel

class UserPrompt(BaseModel):
    prompt: str

class BotResponse(BaseModel):
    response: str
