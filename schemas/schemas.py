
from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from pydantic.v1 import Field
from database.modeller import SinifYili, Cinsiyet


class TemelSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID | None = None
    olusturma_zamani: datetime | None = None
    guncelleme_zamani: datetime | None = None


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
    dersler: list['DersSchema'] = Field(default_factory=list)

class SinifSchema(TemelSchema):
    kacinci_sinif: SinifYili
    sube: str
    ogretmen_id: UUID


class SinifWithOgrenci(SinifSchema):
    ogrenciler: list['OgrenciSchema'] = Field(default_factory=list)

class VeliSchema(TemelSchema):
    adi: str
    soyadi: str
    tel_no: str
    cinsiyet: Cinsiyet


class VeliWithOgrenciSchema(VeliSchema):
    ogrenciler: list['OgrenciSchema'] = Field(default_factory=list)


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
