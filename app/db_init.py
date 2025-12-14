from sqlalchemy.ext.asyncio import AsyncEngine
from .database import engine
from .models import Base
import asyncio

async def init_db():
    async with engine.begin() as conn:
        # Create all tables
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created!")

if __name__ == "__main__":
    asyncio.run(init_db())
