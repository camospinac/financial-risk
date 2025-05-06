from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    user_id: int
    amount: float
    location: str
    ip_address: str

class TransactionOut(TransactionCreate):
    id: int
    timestamp: datetime

    model_config = {
        "from_attributes": True
    }