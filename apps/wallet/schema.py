from pydantic import BaseModel


class WalletSchema(BaseModel):
    id: str
    balance: float
    is_active: bool
    user_id: str

class FundWalletSchema(BaseModel):
    amount:float