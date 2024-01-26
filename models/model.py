from typing import List, Optional
import uuid
from pydantic import BaseModel, Field


class CryptoData(BaseModel):
    coin_id: str
