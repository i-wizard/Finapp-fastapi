from __future__ import annotations

from sqlalchemy.orm import Session

from apps.user.models import  User


class UserService:
    @classmethod
    def get_user(cls, db:Session, id:str) -> User | None:
        return db.query(User).filter(User.id == id).first()