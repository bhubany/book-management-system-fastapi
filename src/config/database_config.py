from sqlmodel import SQLModel, create_engine
from config.settings import get_settings
from functools import lru_cache

settings= get_settings()
engine = create_engine(settings.database_url)

@lru_cache
def create_tables():
    SQLModel.metadata.create_all(engine)
