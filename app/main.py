from fastapi import FastAPI
import uvicorn
from app.database import Base, engine
from app.auth.auth import router as auth_router
from app.redis_client import create_redis_client
from app.routers import crypto

app = FastAPI()
app.include_router(crypto.router, prefix="/cryptos", tags=["cryptos"])

Base.metadata.create_all(bind=engine)
redis_client = create_redis_client()

app.include_router(auth_router)


@app.get("/")
def read_root():
    return {"Hello World"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
