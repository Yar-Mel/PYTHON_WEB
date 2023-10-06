from datetime import datetime, date
from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    username: str = Field(min_length=1, max_length=16)
    email: str
    password: str = Field(min_length=6, max_length=16)


class UserDb(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    avatar: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class ContactRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birthday: date


class ContactResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birthday: date


class RequestEmail(BaseModel):
    email: EmailStr
