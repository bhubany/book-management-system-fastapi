from fastapi import Depends
from src.config.database_config import engine
from sqlmodel import Session, select, func
from src.user.models import User


class UserRepostiory:
    def __init__(self):
        self.session: Session = Session(engine)

    def save(self, user: User) -> User:
        with self.session as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
