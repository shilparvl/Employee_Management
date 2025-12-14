from fastapi import FastAPI
from .routers import employees, departments
from .logging_config import configure_logging
from .config import settings
from contextlib import asynccontextmanager
from .database import engine
from .models import Base
# from .db_init import init_db

configure_logging()
# app = FastAPI(title=settings.PROJECT_NAME)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables at startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created!")
    yield


app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)

# @app.on_event("startup")
# async def startup_event():
#     await init_db()

app.include_router(employees.router)
app.include_router(departments.router)


@app.get("/health")
async def health():
    return {"status": "ok"}