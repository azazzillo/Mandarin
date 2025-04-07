
from typing import Annotated, List
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status

# Local
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.services.dependencies import get_current_user
from app.services.auth import create_access_token, verify_password, get_password_hash
from app.orm.user import create_new_user, get_user_by_email, get_user_by_username, show_users
from app.exceptions import UniqueUserEmailException, UniqueUsernameException, UserInstanceException


api_router = APIRouter(prefix="/auth", tags=["Auth"])


@api_router.post("/register", status_code=201)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    create_new_user(user_data, db)

    return {"message": "Регистрация прошла успешно. Пожалуйста, войдите в аккаунт."}


@api_router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = get_user_by_email(db, user_data.email)

    if not user or not verify_password(user_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.email})
  
    return {
        "access_token": access_token, 
        "token_type": "bearer"
    }


@api_router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user
