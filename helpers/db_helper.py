import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, create_engine, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_mixin

from settings import settings


def generate_id():
    return uuid.uuid4().hex




@declarative_mixin
class BaseModelMixin:
    id = Column(String(256), primary_key=True, default=generate_id, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)


Base = declarative_base()

engine = create_engine(settings.DATABASE_URL, connect_args={})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
