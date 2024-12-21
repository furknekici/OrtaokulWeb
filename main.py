from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import db
from ogrenci.ogrenci_api import ogr_api_router


@asynccontextmanager
async def life_span(app: FastAPI):
    await db.connect("postgresql+asyncpg://fiko:271453@127.0.0.1:5432/ogrenci")
    yield
    await db.disconnect()
app = FastAPI(lifespan=life_span)

app.include_router(ogr_api_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
