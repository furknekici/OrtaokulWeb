from datetime import datetime
from enum import StrEnum
from uuid import UUID

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.temel import Temel


class Cinsiyet(StrEnum):
    Erkek = "E"
    Kadin = "K"

class SinifYili(StrEnum):
    Besinci = "5"
    Altinci = "6"
    Yedinci = "7"
    Sekizinci = "8"

class Ogretmen(Temel):
    __tablename__ = "ogretmen"
    adi: Mapped[str] = mapped_column(String(255), nullable=False, default='', index=True)
    soyadi: Mapped[str] = mapped_column(String(255), nullable=False, default='', index=True)
    tel_no: Mapped[str] = mapped_column(String(10), nullable=False, default='', index=True)
    cinsiyet: Mapped[Cinsiyet] = mapped_column(String(1), nullable=False, default='', index=True)
    dogum_tarihi: Mapped[datetime] = mapped_column()
    brans: Mapped[str] = mapped_column(String(255), nullable=False, default='', index=True)
    dersler: Mapped[list['Ders']] = relationship(back_populates='ogretmen', lazy='selectin')
    sinifi: Mapped[list['Sinif']] = relationship(back_populates='ogretmen', lazy='selectin')


class Sinif(Temel):
    __tablename__ = "sinif"
    kacinci_sinif: Mapped[SinifYili] = mapped_column(String(5), nullable=False, default='', index=True)
    sube: Mapped[str] = mapped_column(String(5), nullable=False, default='', index=True)
    sinif_ogrencileri: Mapped[list['Ogrenci']] = relationship(back_populates="sinif", lazy='selectin')
    ogretmen_id: Mapped[UUID] = mapped_column(ForeignKey('ogretmen.id'))
    ogretmen: Mapped[Ogretmen] = relationship(back_populates="sinifi")

class Veli(Temel):
    __tablename__ = "veli"
    adi: Mapped[str] = mapped_column(String(255), nullable=False, default='', index=True)
    soyadi: Mapped[str] = mapped_column(String(255), nullable=False, default='', index=True)
    tel_no: Mapped[str] = mapped_column(String(10), nullable=False, default='', index=True)
    cinsiyet: Mapped[Cinsiyet] = mapped_column(String(1), nullable=False, default='', index=True)
    ogrenciler: Mapped[list['Ogrenci']] = relationship(back_populates='veli', lazy='selectin')

class Ogrenci(Temel):
    __tablename__ = "ogrenci"
    tc_no: Mapped[str] = mapped_column(String(11), nullable=False, default='', index=True)
    adi: Mapped[str] = mapped_column(String(255), nullable=False, default='', index=True)
    soyadi: Mapped[str] = mapped_column(String(255), nullable=False, default='', index=True)
    numara: Mapped[str] = mapped_column(String(11), nullable=False, default='', index=True)
    cinsiyet: Mapped[Cinsiyet] = mapped_column(String(1), nullable=False, default='', index=True)
    dogum_tarihi: Mapped[datetime] = mapped_column()
    veli_id: Mapped[UUID] = mapped_column(ForeignKey('veli.id'))
    veli: Mapped[Veli] = relationship(back_populates='ogrenciler')
    sinif_id: Mapped[UUID] = mapped_column(ForeignKey('sinif.id'))
    sinif: Mapped[Sinif] = relationship(back_populates='sinif_ogrencileri')

class Ders(Temel):
    __tablename__ = "ders"
    adi: Mapped[str] = mapped_column(String(255), nullable=False, default='', index=True)
    ogretmen_id: Mapped[UUID] = mapped_column(ForeignKey('ogretmen.id'))
    ogretmen: Mapped[Ogretmen] = relationship(back_populates='dersler')