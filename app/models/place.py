from typing import List
from typing import TYPE_CHECKING

from pydantic import EmailStr
from sqlalchemy import (
        Boolean, Integer, String, ForeignKey, Text, DateTime,
        func, Float
    )
from sqlalchemy.orm import (
        Mapped, mapped_column, relationship
    )

from app.models.base import Base


class Place(Base):
    __tablename__ = "place"

    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True, 
        autoincrement=True
    )
    request_id: Mapped[int] = mapped_column(
        ForeignKey("user_request.id"), 
        nullable=False
    )
    name: Mapped[str] = mapped_column(
        String, 
        nullable=False
    ) 
    address: Mapped[str] = mapped_column(
        String, 
        nullable=False
    )  
    description: Mapped[Text] = mapped_column(
        Text, 
        nullable=True
    )  
    rating: Mapped[float] = mapped_column(
        Float, 
        nullable=True
    )
    link: Mapped[Text] = mapped_column(
        Text,
        nullable=True
    )

    # КООРДИНАТЫ
    latitude: Mapped[float] = mapped_column(
        Float, 
        nullable=True
    )  
    longitude: Mapped[float] = mapped_column(
        Float, 
        nullable=True
    )
    

    # Связь с запросом
    request = relationship(
        "UserRequest", 
        back_populates="places"
    )
