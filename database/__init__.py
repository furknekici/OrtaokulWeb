from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.sql.annotation import Annotated


class Database:
    def __init__(self):
        self.__session = None
        self.__engine = None


    def connect(self, db_url: str = None):
        self.__engine = create_async_engine(db_url)
        self.__session = async_sessionmaker(bind=self.__engine, autocommit=False)

    async def disconnect(self):
        await self.__engine.dispose()

    async def get_db(self):
        async with self.__session() as session:
            yield session


db = Database()
Db_Bagimlilik = Annotated[AsyncSession, Depends(db.get_db)]
