import pytest
from app.main import app
from httpx import AsyncClient
from asgi_lifespan import LifespanManager  # Handles startup/shutdown events

@pytest.mark.asyncio
async def test_health():
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_get_nonexistent_employee():
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.get("/employees/9999")
    assert response.status_code == 404
