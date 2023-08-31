from fastapi import HTTPException
from sqlalchemy.orm import Session

from apps.wallet.models import Wallet

class WalletService:
    @classmethod
    def create_wallet(cls, db:Session, user):
        wallet = db.query(Wallet).filter(Wallet.user_id == user.id).first()
        if wallet:
            HTTPException(
                detail="Wallet already created for this user",
                status_code=409
            )
        wallet = Wallet(user_id=user.id)
        db.add(wallet)
        db.commit()

    @classmethod
    def get_wallet(cls, db:Session, user):
        wallet = db.query(Wallet).filter(Wallet.user_id == user.id).first()
        if not wallet:
            raise HTTPException(detail="Wallet not found", status_code=404)
        return wallet

    @classmethod
    def fund_wallet(cls, db:Session, user, amount:float):
        wallet = cls.get_wallet(db, user)
        wallet.balance += amount
        db.add(wallet)
        db.commit()
        db.refresh(wallet)
        return wallet