from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from data.config import DATABASE_URL


engine = create_async_engine(DATABASE_URL, future=True)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession)