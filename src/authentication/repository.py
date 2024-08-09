from fastapi import Depends
from src.config.database_config import engine
from sqlmodel import Session, select, func
from src.authentication.models import Authentication


class AuthenticationRepository:
    def __init__(self):
        self.session: Session = Session(engine)

    def save(self, auth: Authentication) -> Authentication:
        with self.session as session:
            session.add(auth)
            session.commit()
            session.refresh(auth)
            return auth
