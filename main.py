from fastapi import FastAPI

from helpers.db_helper import engine
from apps.user import models as user_models
from apps.wallet import models as wallet_models


user_models.Base.metadata.create_all(bind=engine)
wallet_models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Fast API FINAPP",
    description="A simple savings app",
    version="0.0.1",
    contact={
        "name": "Hacker",
        "email": "hacker@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

@app.get("/")
def home():
    return {"message":"Welcome home"}