
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src.config import setting

Base = declarative_base()

engine = create_async_engine(setting.DB_URL)

def get_async_session():
    async_session = async_sessionmaker(engine)
    return async_session

