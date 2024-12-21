from fastapi import APIRouter
from api.genel_api import genel_api_olusturucu
from database.modeller import Ogretmen, Sinif, Veli, Ogrenci, Ders
from schemas.schemas import OgretmenSchema, SinifSchema, VeliSchema, OgrenciSchema, DersSchema

v1 = APIRouter(prefix= "/v1", tags=["Sürüm 1.0"] )
v1.include_router(genel_api_olusturucu("/ogretmen",["Öğretmen"],OgretmenSchema,Ogretmen))
v1.include_router(genel_api_olusturucu("/sinif",["Sınıf"],SinifSchema,Sinif))
v1.include_router(genel_api_olusturucu("/veli",["Veli"],VeliSchema,Veli))
v1.include_router(genel_api_olusturucu("/ogrenci",["Öğrenci"],OgrenciSchema,Ogrenci))
v1.include_router(genel_api_olusturucu("/ders",["Ders"],DersSchema,Ders))