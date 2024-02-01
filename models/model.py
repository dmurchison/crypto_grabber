from typing import List, Optional
import uuid
from pydantic import BaseModel, Field


class CryptoData(BaseModel):
    coin_id: str

    class Config:
        schema_extra = {
            "example": {
                "coin_id": "bitcoin"
            }
        }
