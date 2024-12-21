from uuid import UUID

from fastapi import APIRouter
from sqlalchemy import select

from database import Db_Bagimlilik


def genel_api_olusturucu(adres: str , etiketler: list[str], schema: type, model: type):
    api_router = APIRouter(prefix=adres, tags=etiketler)

    @api_router.get("/")
    async def tum_veri(vt: Db_Bagimlilik) -> list[schema]:
        ogretmenler = (await vt.execute(select(model))).scalars().all()
        return ogretmenler

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