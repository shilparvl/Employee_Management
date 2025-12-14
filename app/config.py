from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str 
    REDIS_URL: str 
    PROJECT_NAME: str = "Employee_Management"
    DEBUG: bool = False


class Config:
    env_file = ".env"
    env_file_encoding = "utf-8"


settings = Settings()