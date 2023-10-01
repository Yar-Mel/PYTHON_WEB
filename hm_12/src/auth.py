from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta

from db.connect import get_db
from src.models import User

app = FastAPI()

JWT_SECRET_KEY = "4dc8a552026c16d34c1fafb8064f834c088ddbd2f75bcb09df40a6f094d2f5f6"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

token_auth_scheme = HTTPBearer()


class Hash:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str):
        return self.pwd_context.hash(password)


async def generate_token(
    data: dict, expires_delta: timedelta = None, is_access_token=True
):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        if is_access_token:
            expire = datetime.utcnow() + timedelta(minutes=15)
        else:
            expire = datetime.utcnow() + timedelta(days=7)
    to_encode.update(
        {"exp": expire, "scope": "access_token" if is_access_token else "refresh_token"}
    )
    token = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return token


async def create_access_token(data: dict, expires_delta: timedelta = None):
    encoded_access_token = await generate_token(data, expires_delta)
    return encoded_access_token


async def create_refresh_token(data: dict, expires_delta: timedelta = None):
    encoded_refresh_token = await generate_token(
        data, expires_delta, is_access_token=False
    )
    return encoded_refresh_token


async def get_email_from_refresh_token(refresh_token):
    try:
        payload = jwt.decode(refresh_token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        if payload["scope"] == "refresh_token":
            email = payload["sub"]
            return email
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not find valid scope",
        )
    except JWTError as error:
        print(error)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not find valid credentials",
        )


async def get_current_user(
    token: HTTPAuthorizationCredentials = Depends(token_auth_scheme),
    db: Session = Depends(get_db),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Decode JWT
        payload = jwt.decode(token.credentials, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        email = payload["sub"]
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user: User | None = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception
    return user
