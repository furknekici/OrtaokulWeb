from fastapi import APIRouter
from sqlalchemy import select, func
from schemas.schemas import Istatistik
from database import Db_Bagimlilik
from database.modeller import Ogretmen, Ogrenci, Sinif, Ders, Veli

istatistik_router = APIRouter(prefix='/istatistik',tags=['istatistik'])


@istatistik_router.get("/")
async def istatistik_olusturucu(db:Db_Bagimlilik) -> list[Istatistik]:
    return[
        {
        'istatistik': (await db.execute(select(func.count(Ogretmen.id)))).scalars().first(),
        'istatistikadi' : 'Öğretmen',
        'simge' : 'fa-chalkboard-user'
        },
        {
            'istatistik': (await db.execute(select(func.count(Ogrenci.id)))).scalars().first(),
            'istatistikadi': 'Öğrenci',
            'simge': 'fa-user-graduate'
        },
        {
            'istatistik': (await db.execute(select(func.count(Sinif.id)))).scalars().first(),
            'istatistikadi': 'Sınıf',
            'simge': 'fa-person-chalkboard'
        },
        {
            'istatistik': (await db.execute(select(func.count(Ders.id)))).scalars().first(),
            'istatistikadi': 'Ders',
            'simge': 'fa-book'
        },
        {
            'istatistik': (await db.execute(select(func.count(Veli.id)))).scalars().first(),
            'istatistikadi': 'Veli',
            'simge': 'fa-children'
        }]