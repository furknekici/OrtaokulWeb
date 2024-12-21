import uuid
from datetime import datetime
from uuid import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Temel (DeclarativeBase):
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4, nullable=False)
    olusturma_zamani: Mapped[datetime] = mapped_column(default=datetime.now())
    guncelleme_zaman: Mapped[datetime] = mapped_column(default=datetime.now(), onupdate=datetime.now())