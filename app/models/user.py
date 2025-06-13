from typing import List
from typing import TYPE_CHECKING

from pydantic import EmailStr
from sqlalchemy import (
        Boolean, Integer, String
    )
from sqlalchemy.orm import (
        Mapped, mapped_column, relationship
    )

# local

from app.models.base import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True,
        autoincrement=True
    )
    username: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True
    )
    email: Mapped[EmailStr] = mapped_column(
        String,
        nullable=False,
        unique=True,
        index=True
    )
    password: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=False,
    )
    avatar: Mapped[str] = mapped_column(
        String,
        nullable=True
    )

    # СВЯЗЬ
    requests = relationship(
        "UserRequest",
        back_populates="user"
    )
    tasks = relationship(
        "Task",
        back_populates="user"
    )
