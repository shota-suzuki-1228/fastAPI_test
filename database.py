from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./fastapi-app.db"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,echo=True
)

Base = declarative_base()

db_session = sessionmaker(
    autocommit = False, 
    autoflush=False, 
    bind=engine,
    class_=AsyncSession
    )

async def get_db():
    async with db_session() as session:
        yield session