"""
Modelos de datos para MechBot 2.0x API
"""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List

class User(BaseModel):
    """Modelo de usuario para autenticación"""
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    disabled: Optional[bool] = False

class UserInDB(User):
    """Usuario en base de datos (con password)"""
    hashed_password: str

class Token(BaseModel):
    """Modelo de token de acceso"""
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    """Datos dentro del token"""
    username: Optional[str] = None
