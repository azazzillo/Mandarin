from typing import List
from typing import TYPE_CHECKING

from pydantic import EmailStr
from sqlalchemy import (
        Boolean, Integer, String, ForeignKey, Text, DateTime,
        func
    )
from sqlalchemy.orm import (
        Mapped, mapped_column, relationship
    )

from app.models.base import Base


# очередная моделька для бд - Запрос (настреоение) пользователя
class UserRequest(Base):
    __tablename__ = "user_request"

    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True,
        autoincrement=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        nullable=False
    )
    mood: Mapped[Text] = mapped_column(
        Text,
        nullable=False
    )
    chat_gpt_response: Mapped[Text] = mapped_column(
        Text,
        nullable=True
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        default=func.now()
    )

    # здесь прописываем связи с другими моделями
    user = relationship(
        "User",
        back_populates="requests"
    )
    places = relationship(
        "Place",
        back_populates="request"
    )
