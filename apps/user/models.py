import enum

from sqlalchemy import ForeignKey, Column, String, DateTime, Integer, Boolean, Enum
from sqlalchemy.orm import relationship

from helpers.db_helper import  BaseModelMixin, Base

class UserRoleEnum(enum.Enum):
    admin = 2
    user = 1

class User(BaseModelMixin, Base):
    first_name = Column(String(256))
    last_name = Column(String(256))
    email = Column(String(256), nullable=False, index=True)
    is_verified = Column(Boolean, default=False)
    role = Column(Enum(UserRoleEnum), default=1)
    wallet = relationship("Wallet", uselist=False, back_populates="user", cascade="all, delete")

