from typing import List
from typing import TYPE_CHECKING

from pydantic import EmailStr
from sqlalchemy import (
        Boolean, Integer, String, Enum
    )
from sqlalchemy.orm import (
        Mapped, mapped_column, relationship
    )

from app.models.base import Base

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__ = "task"

    id = Column(
        Integer, 
        primary_key=True, 
        autoincrement=True
    )
    task_id = Column(
        String, 
        unique=True, 
        nullable=False
    )  # ID задачи в Celery
    status = Column(
        String, 
        nullable=False, 
        default="PENDING"
    )  # PENDING, STARTED, SUCCESS, FAILURE
    result = Column(
        String, 
        nullable=True
    )  # Сохранение результата
    created_at = Column(
        DateTime, 
        default=func.now()
    )
    updated_at = Column(
        DateTime, 
        onupdate=func.now()
    )

    user_id = Column(
        Integer, 
        ForeignKey("user.id"), 
        nullable=True
    )  # Если задачи привязаны к пользователям
    user = relationship(
        "User", 
        back_populates="tasks"
    )

