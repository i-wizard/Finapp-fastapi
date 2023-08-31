import fastapi
from fastapi import Depends

from apps.user.schema.auth import UserSchema
from apps.user.models import User
from helpers.auth_util import get_current_user

router = fastapi.APIRouter()


@router.get("/user/me", status_code=200, summary="User login", response_model=UserSchema)
def get_profile(user: User = Depends(get_current_user)):
    return user
