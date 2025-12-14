from .database import get_db
from .cache import get_redis


async def get_db_dep():
    async for s in get_db():
        yield s


async def get_cache_dep():
    yield await get_redis()