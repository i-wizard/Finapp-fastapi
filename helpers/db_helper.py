import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, create_engine, String
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.orm import sessionmaker

from settings import settings

def generate_id():
    return uuid.uuid4

Base = declarative_base()

class BaseModelMixin:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {'mysql_engine': 'InnoDB'}
    __mapper_args__ = {'always_refresh': True}

    id = Column(String(256), primary_key=True, default=generate_id, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)


engine = create_engine(settings.DATABASE_URL, connect_args={}, future=True)

SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine, future=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()