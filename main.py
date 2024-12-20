from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import db

@asynccontextmanager
async def life_span(app: FastAPI):
    db.connect("postgresql+asyncpg://fiko:271453@127.0.0.1:5432/ogrenci")
    yield
    db.disconnect()
app = FastAPI(lifespan=life_span)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
