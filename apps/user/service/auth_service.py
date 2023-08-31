from typing import Union, Any
from datetime import datetime, timedelta

import bcrypt
from jose import jwt
from sqlalchemy.orm import Session

from apps.user.models import User
from settings import settings

class AuthService:
    @classmethod
    def get_user(cls, db:Session, email:str) -> User:
        user = db.query(User).filter(User.email.ilike(email)).first()
        return user

    @classmethod
    def create_user(cls, db:Session, data:dict) -> None:
        password = data["password"]
        data["password"] = AuthHelper.hash_password(password)
        # noinspection PyArgumentList
        db_user = User(**data)
        db.add(db_user)
        db.commit()

class AuthHelper:
    @staticmethod
    def hash_password(password: str) -> str:
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

        # Convert the hashed password to a utf-8 encoded string
        return hashed_password.decode("utf-8")

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))


    @staticmethod
    def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, settings.ALGORITHM)
        return encoded_jwt

    @staticmethod
    def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)

        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, settings.JWT_REFRESH_SECRET_KEY, settings.ALGORITHM)
        return encoded_jwt


