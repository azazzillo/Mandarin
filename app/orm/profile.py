from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
import os

# Local
from app.services.dependencies import get_current_user
from app.schemas.user import UserOut
from app.models.user import User
from app.database import get_db



UPLOAD_FOLDER = "uploads/avatars"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def upload_avatar(
        file: UploadFile = File(...), 
        db: Session = Depends(get_db), 
        user: User = Depends(get_current_user)
    ):
    """
    Подгрузить аватар
    """
    try:
        filename = f"{user['id']}_{file.filename}"
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        with open(filename, "wb") as buffer:
            buffer.write(file.file.read())
        
        user.avatar = filepath
        db.commit()

        return {
            "message": "Аватар успешно загружен",
            "file": filename
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ошибка загрузки аватара")


