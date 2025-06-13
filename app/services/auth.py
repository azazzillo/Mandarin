from fastapi.security import OAuth2PasswordBearer

import os
import jwt
from typing import Optional
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext


load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY") 
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_EXPIRE_MINUTES = os.getenv("JWT_EXPIRE_MINUTES")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    print("---функция create access token---")

    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=int(JWT_EXPIRE_MINUTES)))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


def verify_password(plain_password, hashed_password):
    print("Я хеши сравниваю выаыладыа")
    print(plain_password, " ?= ", hashed_password)
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)
