from pydantic import BaseModel
from datetime import datetime


class CryptoCreate(BaseModel):
    name: str
    price: float


class Crypto(CryptoCreate):
    timestamp: datetime
