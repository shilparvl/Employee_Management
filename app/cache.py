import json
import redis.asyncio as redis
from .config import settings
from datetime import date

_redis = None


async def get_redis():
    global _redis
    if _redis is None:
        _redis = redis.from_url(
            settings.REDIS_URL,
            encoding="utf-8",
            decode_responses=True
        )
    return _redis


async def get_employee_cache(emp_id: int):
    r = await get_redis()
    data = await r.get(f"employee:{emp_id}")
    if data:
        return json.loads(data)
    return None


# async def set_employee_cache(emp_id: int, payload: dict, ttl: int = 60):
#     r = await get_redis()
#     await r.set(
#         f"employees:{emp_id}",
#         json.dumps(payload),
#         ex=ttl
#     )

async def set_employee_cache(emp_id: int, payload: dict, ttl: int = 60):
    # Convert any date objects to string
    def default_converter(o):
        if isinstance(o, date):
            return o.isoformat()
        raise TypeError(f"Type {type(o)} not serializable")
    
    r = await get_redis()
    await r.set(f"employee:{emp_id}", json.dumps(payload, default=default_converter), ex=ttl)