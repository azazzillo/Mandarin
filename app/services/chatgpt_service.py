import openai
from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def chat_with_gpt(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response["choices"][0]["message"]["content"]
