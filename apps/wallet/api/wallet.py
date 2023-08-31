import fastapi
from fastapi import Depends
from sqlalchemy.orm import Session

from helpers.db_helper import get_db
from apps.wallet.service import WalletService
from apps.wallet.schema import WalletSchema, FundWalletSchema
from apps.user.models import User
from helpers.auth_util import get_current_user

router = fastapi.APIRouter()


@router.post("/wallet", status_code=201)
def create_wallet(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    WalletService.create_wallet(db, user)
    return

@router.get("/wallet", status_code=200, response_model=WalletSchema)
def get_wallet(db:Session = Depends(get_db), user: User = Depends(get_current_user)):
    return WalletService.get_wallet(db, user)

@router.post("/wallet/fund", status_code=200, response_model=WalletSchema)
def fund_wallet(data:FundWalletSchema, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    amount = data.amount
    wallet = WalletService.fund_wallet(db, user, amount)
    return wallet