
# pydantic схемы для валидации данных
from pydantic import(
    BaseModel, EmailStr, Field
)


class UserCreate(BaseModel):
    """
    Kinda registration???????????
    """

    username: str = Field(..., max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6)
    name: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    name: str
    avatar: str | None

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    """
    Для логииина
    """
    email: str = Field(..., max_length=100)
    password: str = Field(..., min_length=6)


class UserOut(BaseModel):
    id: int
    name: str
    email: str
    username: str

    class Config:
        orm_mode = True

