from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import  v1
from database import db



@asynccontextmanager
async def life_span(app: FastAPI):
    await db.connect("postgresql+asyncpg://fiko:271453@127.0.0.1:5432/ogrenci")
    yield
    await db.disconnect()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:5173",
]

app = FastAPI(lifespan=life_span, openapi_url="/api/openapi.json") #openapi_url dikkat!
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(v1)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
