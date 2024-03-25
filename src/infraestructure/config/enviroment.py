from typing import Callable

from dotenv import load_dotenv
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str = 'DEBUG'
    PYTHONPATH: str = '/app/'
    LOG_LEVEL: str = 'info'
    DATABASE_URL: str = 'postgresql://fastapi:fastapi@app-database:5432/fastapi'
    DEBUG: bool = True
    HOST: str = '0.0.0.0'
    PORT: int = '8000'
    TITLE: str = 'Sprocket API'
    DESCRIPTION: str = 'Sprocket API'
    VERSION: str = '0.1.0'
    RELOAD: bool = True
    CELERY_BROKER_URL: str = "redis://app-redis:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://app-redis:6379/0"


def _configure_initial_settings() -> Callable[[], Settings]:
    load_dotenv()
    settings = Settings()

    def fn() -> Settings:
        return settings

    return fn


get_settings = _configure_initial_settings()
