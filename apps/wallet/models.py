from sqlalchemy import Column, Float, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship

from helpers.db_helper import Base, BaseModelMixin
from apps.user.models import User


class Wallet(BaseModelMixin, Base):
    __tablename__ = "wallet"
    balance = Column(Float, default=0)
    is_active = Column(Boolean, default=True)
    user_id = Column(String(256), ForeignKey(User.id, ondelete="CASCADE"))
    user = relationship(User, back_populates="wallet")
    transaction = relationship("Transaction", back_populates="wallet")


class Transaction(BaseModelMixin, Base):
    __tablename__ = "transaction"
    amount = Column(Float, nullable=False)
    balance = Column(Float, nullable=False)
    note = Column(String(256), nullable=True)
    wallet_id = Column(String(256), ForeignKey("wallet.id", ondelete="CASCADE"))
    wallet = relationship("Wallet", back_populates="transaction")