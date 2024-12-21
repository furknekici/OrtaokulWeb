from fastapi import APIRouter
from sqlalchemy import select
from database import Db_Bagimlilik
from database.modeller import Ogrenci
from schemas.schemas import OgrenciSchema

ogr_api_router = APIRouter(prefix="/ogrenci", tags=["Öğrenci"])

@ogr_api_router.get("/")
async def ogrenciler(vt: Db_Bagimlilik) -> list[OgrenciSchema]:
    ogrencilers = (await vt.execute(select(Ogrenci))).scalars().all()
    return ogrencilers
