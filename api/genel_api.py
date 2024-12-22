from typing import Annotated
from uuid import UUID

from fastapi import APIRouter
from fastapi.params import Query
from sqlalchemy import select

from database import Db_Bagimlilik
from schemas.schemas import SorguSchema


def genel_api_olusturucu(adres: str , etiketler: list[str], schema: type, model: type):
    api_router = APIRouter(prefix=adres, tags=etiketler)

    @api_router.get("/")
    async def tum_veri(vt: Db_Bagimlilik, sorgu_param:Annotated[SorguSchema, Query()]) -> list[schema]:
        sorgu = select(model)
        sorgu = sorgu.limit(sorgu_param.kayit_sayisi)
        sorgu = sorgu.offset(sorgu_param.kayit_sayisi*sorgu_param.sayfa)
        sorgu_sonucu = await vt.execute(sorgu)
        return sorgu_sonucu.scalars().all()

    @api_router.post("/")
    async def veri_ekle(vt: Db_Bagimlilik, ogretmen: schema) -> schema:
        data = ogretmen.model_dump(mode="python")
        object = model(**data)
        vt.add(object)
        await vt.commit()
        await vt.refresh(object)
        return object

    @api_router.get("/{id]")
    async def veri(vt: Db_Bagimlilik, id: UUID) -> schema:
        sorgu_sonucu = await vt.execute(select(model).where(model.id == id))
        return sorgu_sonucu.scalars().first()

    @api_router.put("/{id}")
    async def veri_guncelle(vt: Db_Bagimlilik, id: UUID, ogretmen: schema) -> schema:
        data = ogretmen.model_dump(mode="python")
        sorgu_sonucu = await vt.execute(select(model).where(model.id == id))
        object = sorgu_sonucu.scalars().first()
        for field in data:
            if data[field] is not None:
                setattr(object, field, data[field])
        await vt.commit()
        await vt.refresh(object)
        return object

    @api_router.delete("/{id}")
    async def veri_sil(vt: Db_Bagimlilik, id: UUID) -> dict[str, bool]:
        sorgu_sonucu = await vt.execute(select(model).where(model.id == id))
        ogretmen_obj = sorgu_sonucu.scalars().first()
        await vt.delete(ogretmen_obj)
        await vt.commit()
        return {"Silindi": True}
    return api_router