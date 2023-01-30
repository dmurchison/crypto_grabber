import uvicorn
import requests
from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI(title="Crypto API", version="1.0.0", description="A simple API to get crypto data")


class CryptoData(BaseModel):
    symbol: str


@app.get("/")
def index():
    return {"message": "Welcome to the Crypto API"}


@app.get("/crypto/{symbol}")
async def crypto_info(symbol: str):
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/{symbol}")
    return response.json()


@app.get("/companies/public_treasury/{symbol}")
async def companies(symbol: str):
    response = requests.get(f"https://api.coingecko.com/api/v3/companies/public_treasury/{symbol}")
    return response.json()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

