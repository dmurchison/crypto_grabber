from pydantic import BaseModel

class CryptoData(BaseModel):
    symbol: str

