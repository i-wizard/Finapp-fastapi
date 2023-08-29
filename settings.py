from pathlib import Path
import os

from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Settings, cls).__new__(cls)
        return cls.instance

    DB_NAME = os.environ.get("POSTGRES_DB")
    DB_USER = os.environ.get("POSTGRES_USER")
    DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    DB_PORT = os.environ.get("POSTGRES_PORT")
    DB_HOST = os.environ.get("POSTGRES_HOST")
    DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@db:{DB_PORT}/{DB_NAME}"


settings: Settings = Settings()
