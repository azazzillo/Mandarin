
from fastapi import APIRouter, HTTPException
from app.services.chatgpt_service import chat_with_gpt


api_router = APIRouter

@api_router.post("/chat")
async def chat(prompt: str):
    try:
        response = chat_with_gpt(prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
