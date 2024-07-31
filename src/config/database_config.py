from sqlmodel import SQLModel, create_engine, Session
from src.config.settings import get_settings

settings = get_settings()
engine = create_engine(settings.database_url)


def create_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
