from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID


class UserBase(BaseModel):
    email: EmailStr
    phone: str
    name: str
    age: Optional[int] = None
    gender: Optional[str] = None
    language_preference: str = "en"
    consent_agreed: bool = False


class UserCreate(UserBase):
    pass

class UserCreate(UserBase):
    password: str
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(UserBase):
    id: UUID
    is_active: bool

    class Config:
        from_attributes = True