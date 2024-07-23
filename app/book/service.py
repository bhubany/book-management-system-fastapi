from typing import Annotated
from .models import Book
from fastapi import Depends
import config.models as models
from config.database import engine, SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    print(db)
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


class BookService:
    def __init__(self):
        self.database = db_dependency

    def save(self, data: Book, db: Session) -> dict:
        book = models.Books(name=data.author)
        db.add(book)
        db.commit()
        db.refresh(book)
        print(f"Book saved with details: {book}")
        return book
        # return data

    def get(self, id: str, db: Session) -> dict:
        # book = Book.get(id)
        print(f"Book retrieved with details: {id}")
        return {
            "id": id,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "year": 1925,
            "isbn": "978-0-14-118116-4"
        }
