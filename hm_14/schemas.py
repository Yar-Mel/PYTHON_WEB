from datetime import datetime, date
from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    """Docstring for UserModel class"""
    username: str = Field(min_length=1, max_length=16)
    email: str
    password: str = Field(min_length=6, max_length=16)


class UserDb(BaseModel):
    """Docstring for UserDb class"""
    id: int
    username: str
    email: str
    created_at: datetime
    avatar: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    """Docstring for UserResponse class"""
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    """Docstring for TokenModel class"""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class ContactRequest(BaseModel):
    """Docstring for ContactRequest class"""
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birthday: date


class ContactResponse(BaseModel):
    """Docstring for ContactResponse class"""
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birthday: date


class RequestEmail(BaseModel):
    """Docstring for RequestEmail class"""
    email: EmailStr
