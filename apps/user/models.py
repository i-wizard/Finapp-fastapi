import enum

from sqlalchemy import ForeignKey, Column, String, DateTime, Integer, Boolean, Enum
from sqlalchemy.orm import relationship

from helpers.db_helper import Base, BaseModelMixin

class UserRoleEnum(enum.Enum):
    admin = 2
    user = 1

class User(BaseModelMixin, Base):
    __tablename__ = "user"
    first_name = Column(String(256))
    last_name = Column(String(256))
    email = Column(String(256), nullable=False, index=True)
    is_verified = Column(Boolean, default=False)
    password = Column(String(256), nullable=False)
    role = Column(Enum(UserRoleEnum), default=UserRoleEnum.user)
    wallet = relationship("Wallet", uselist=False, back_populates="user", cascade="all, delete")

