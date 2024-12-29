from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field
from database.modeller import SinifYili, Cinsiyet



class SorguSchema(BaseModel):
    sayfa: int = Field(default=0, ge=0)
    kayit_sayisi: int = Field(default=10, ge=5, le=100)
    #Sıralama Kuralları:
    #Sıralamayı dizi olarak alacağız
    #Her bir eleman sıralanacak alanın adını ve yönünü içermeli
    # + ve - işaretleri alan adanını önüne gelerek artan veya azalan sıralamayı ifade eder.
    siralama : list[str] = Field(default_factory=list)


class TemelSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[UUID] = None
    olusturma_zamani: Optional[datetime] = None
    guncelleme_zaman: Optional[datetime] = None


class OgretmenSchema(TemelSchema):
    adi: str
    soyadi: str
    tel_no: str
    cinsiyet: Cinsiyet
    dogum_tarihi: datetime
    brans: str


class OgretmenWithSinifSchema(OgretmenSchema):
    sinifi: Optional[list['SinifSchema']] = Field(default_factory=list)


class OgretmenWithDersSchema(OgretmenSchema):
    dersler: Optional[list['DersSchema']] = Field(default_factory=list)


class SinifSchema(TemelSchema):
    kacinci_sinif: SinifYili
    sube: str
    ogretmen_id: UUID


class SinifWithOgrenci(SinifSchema):
    ogrenciler: Optional[list['OgrenciSchema']] = Field(default_factory=list)


class VeliSchema(TemelSchema):
    adi: str
    soyadi: str
    tel_no: str
    cinsiyet: Cinsiyet


class VeliWithOgrenciSchema(VeliSchema):
    ogrenciler: Optional[list['OgrenciSchema']] = Field(default_factory=list)


class OgrenciSchema(TemelSchema):
    tc_no: str
    adi: str
    soyadi: str
    numara: str
    cinsiyet: Cinsiyet
    dogum_tarihi: datetime
    veli_id: UUID
    sinif_id: UUID


class DersSchema(TemelSchema):
    adi: str
    ogretmen_id: UUID


class Istatistik(BaseModel):
    istatistik: int=0
    istatistikadi: str = ""
    simge: str = ""


