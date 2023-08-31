import fastapi
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from apps.user.schema.auth import RegisterSchema, LoginResponseSchema
from apps.user.service.auth_service import AuthService, AuthHelper
from helpers.db_helper import get_db

router = fastapi.APIRouter()


@router.post("/auth/register", status_code=201)
def register(user: RegisterSchema, db: Session = Depends(get_db)):
    if AuthService.get_user(db, user.email):
        raise HTTPException(status_code=409, detail="User with this email already exist")
    data = user.model_dump(mode='json')
    AuthService.create_user(db, data)
    return


@router.post("/auth/login", status_code=200, summary="User login", response_model=LoginResponseSchema)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = AuthService.get_user(db, form_data.username)
    if user is None:
        raise HTTPException(
            detail="User not found",
            status_code=404
        )
    if not AuthHelper.verify_password(form_data.password, user.password):
        raise HTTPException(detail="Invalid password", status_code=403)
    return {
        "access_token": AuthHelper.create_access_token(user.id),
        "refresh_token": AuthHelper.create_refresh_token(user.id)
    }

