import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker


DATABASE_URL = os.environ.get("DATABASE_URL")
#DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/todo_app_vue"

engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine, class_=AsyncSession)