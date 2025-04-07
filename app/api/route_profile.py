from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
import os

# Local
from app.services.dependencies import get_current_user
from app.orm.profile import upload_avatar
from app.schemas.user import UserOut
from app.models.user import User
from app.database import get_db


api_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY") 
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_EXPIRE_MINUTES = os.getenv("JWT_EXPIRE_MINUTES")


@api_router.get("/me", response_model=UserOut)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@api_router.post("/upload_avatar")
def new_avatar(file: UploadFile = File(...), db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return upload_avatar(file=file, db=db, user=user)