from sqlalchemy.orm import Session
import cloudinary.uploader
import cloudinary
from fastapi import APIRouter, Depends, UploadFile, File, Request
from starlette.background import BackgroundTasks
from src.db.models import User
from src.repository import users as repository_users
from src.services.auth import auth_service
from src.services.email import send_reset_email
from src.db.connection import get_db
from src.config.config import settings
from schemas import UserDb

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/current-user/", response_model=UserDb)
async def get_current_user(current_user: User = Depends(auth_service.get_current_user)):
    """
Retrieve the current user's profile.
    :param current_user: The current user.
    :type current_user: User
    :return: The current user's profile.
    :rtype: UserDb
    """
    return current_user


@router.patch("/avatar", response_model=UserDb)
async def update_user_avatar(
    file: UploadFile = File(),
    current_user: User = Depends(auth_service.get_current_user),
    db: Session = Depends(get_db),
):
    """
Update the current user's avatar.
    :param file: The uploaded image file.
    :type file: UploadFile
    :param current_user: The current user.
    :type current_user: User
    :param db: The database session.
    :type db: Session
    :return: The updated user profile.
    :rtype: UserDb
    """
    cloudinary.config(
        cloud_name=settings.cloudinary_name,
        api_key=settings.cloudinary_api_key,
        api_secret=settings.cloudinary_api_secret,
        secure=True,
    )

    r = cloudinary.uploader.upload(
        file.file, public_id=f"FastAPI_app/{current_user.username}", overwrite=True
    )
    src_url = cloudinary.CloudinaryImage(
        f"FastAPI_app/{current_user.username}"
    ).build_url(width=250, height=250, crop="fill", version=r.get("version"))
    user = await repository_users.update_avatar(current_user.email, src_url, db)
    return user


@router.post("/reset-password")
async def send_password_reset_email(
    request: Request,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(auth_service.get_current_user),
):
    """
Update the current user's avatar.
    :param request: Request.
    :type request: Request
    :param background_tasks: BackgroundTasks service.
    :type background_tasks: BackgroundTasks
    :param current_user: Current user from DB.
    :type current_user: User
    :return: The updated user profile.
    :rtype: UserDb
    """
    password_reset_link = auth_service.generate_password_reset_link(
        current_user.email, 30
    )
    background_tasks.add_task(
        send_reset_email,
        current_user.email,
        current_user.username,
        request.base_url,
        password_reset_link,
    )
    return {"message": "Password Reset Email Has Been Sent."}
