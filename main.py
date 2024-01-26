import uvicorn
import requests
from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI(title="Crypto API", version="1.0.0", description="A simple API to get crypto data")


class CryptoData(BaseModel):
    coin_id: str


@app.get("/")
def index():
    return {"message": "Welcome to the Crypto API"}


@app.get("/crypto/{coin_id}")
async def crypto_info(coin_id: str):
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/{coin_id}")
    return response.json()


@app.get("/companies/public_treasury/{coin_id}")
async def companies(coin_id: str):
    response = requests.get(f"https://api.coingecko.com/api/v3/companies/public_treasury/{coin_id}")
    return response.json()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

