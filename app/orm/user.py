from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import insert, select
from sqlalchemy.orm import Session
from jose import JWTError, jwt
import os

# Local
from app.schemas.user import UserCreate, UserOut
from app.services.hashing import Hasher
from app.models.user import User
from app.database import get_db


def get_user_by_email(db: Session, email: str):
    """
    Получение пользователя по email.
    """
    query = select(User).filter(User.email == email)
    return db.execute(query).scalar_one_or_none()  # Лучше scalar_one_or_none()


def get_user_by_username(db: Session, username: str):
    """
    Получение пользователя по username.
    """
    query = select(User).filter(User.username == username)
    return db.execute(query).scalar_one_or_none()


def create_new_user(user: UserCreate, db: Session):
    """
    Создание нового пользователя.
    """
    new_user = User(
        username=user.username,
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        name=user.name,  # Добавил поле name, чтобы соответствовало модели
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Чтобы обновить объект после сохранения
    return new_user


def show_users(db: Session):
    """
    Получение списка всех пользователей.
    """
    query = select(User)
    return db.execute(query).scalars().all()


