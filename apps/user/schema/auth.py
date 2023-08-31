from datetime import datetime

from pydantic import BaseModel, EmailStr, field_validator

from apps.user.models import  UserRoleEnum


class RegisterSchema(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name:str
    password: str

    @field_validator("password")
    def validate_password(cls, value):
        if 6 > len(value) or len(value) > 100:
            raise ValueError("Password must be between 6 - 100")
        return value

class UserSchema(BaseModel):
    id: str
    email: str
    first_name: str
    role:UserRoleEnum
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class LoginResponseSchema(BaseModel):
    access_token:str
    refresh_token:str