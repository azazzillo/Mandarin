import uvicorn
from typing import Union
from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

# Local
from app.api.route_auth import api_router as auth_router
from app.api.route_profile import api_router as profile_router


app = FastAPI(
    title="MANDARIN",
    description="recommendation platform",
    docs_url="/"
)

origins = [
    "http://localhost:5173",  # Например, фронтенд на React/Vite
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Список разрешённых источников
    allow_credentials=True,  # Разрешить отправку кук и заголовков авторизации
    allow_methods=["*"],     # Разрешить все методы (GET, POST и т.д.)
    allow_headers=["*"],     # Разрешить все заголовки
)

# ------------- МАРШРУУУТЫ К ЭНДПОИНТАМ ----------------
app.include_router(auth_router)     # REG/LOG
app.include_router(profile_router)  # PROFILE



if __name__ == "__main__":
    uvicorn.run(
        app, 
        host="localhost", 
        port=8080
    )