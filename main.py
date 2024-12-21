from contextlib import asynccontextmanager
from fastapi import FastAPI
from api import  v1
from database import db



@asynccontextmanager
async def life_span(app: FastAPI):
    await db.connect("postgresql+asyncpg://fiko:271453@127.0.0.1:5432/ogrenci")
    yield
    await db.disconnect()

app = FastAPI(lifespan=life_span)

app.include_router(v1)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
