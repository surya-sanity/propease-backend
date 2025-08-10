from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Core settings
    APP_NAME: str = "PropEase"

    # Database
    DATABASE_URL: str = ""

    class Config:
        env_file = ".env"           # load from .env
        env_file_encoding = "utf-8" # read as UTF-8


settings = Settings()

if settings.DATABASE_URL == "":
    raise ValueError("DATABASE_URL is not set")
