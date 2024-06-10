from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import CryptoCreate, Crypto
from app.crud import create_crypto, get_crypto, get_all_cryptos, update_crypto, delete_crypto

router = APIRouter()

@router.post("/", response_model=Crypto)
def create_crypto_endpoint(crypto: CryptoCreate):
    return create_crypto(crypto)

@router.get("/{name}", response_model=Crypto)
def read_crypto(name: str):
    crypto = get_crypto(name)
    if crypto is None:
        raise HTTPException(status_code=404, detail="Cryptocurrency not found")
    return crypto

@router.get("/", response_model=List[Crypto])
def read_all_cryptos():
    return get_all_cryptos()

@router.put("/{name}", response_model=Crypto)
def update_crypto_endpoint(name: str, crypto: CryptoCreate):
    updated_crypto = update_crypto(name, crypto)
    if updated_crypto is None:
        raise HTTPException(status_code=404, detail="Cryptocurrency not found")
    return updated_crypto

@router.delete("/{name}")
def delete_crypto_endpoint(name: str):
    success = delete_crypto(name)
    if not success:
        raise HTTPException(status_code=404, detail="Cryptocurrency not found")
    return {"message": "Cryptocurrency deleted successfully"}
