from sqlmodel import Session, select
from uuid import uuid4, UUID
from src.config.database_config import engine
from src.book.models import Book


class BookRepository():
    def __init__(self):
        self.session: Session = Session(engine)

    def save(self, data: Book):
        with self.session as session:
            book = Book(id=uuid4(), title=data.title,
                        year=data.year, author=data.author)
            session.add(book)
            session.commit()
            session.refresh(book)
            return book

    def find_by_id(self, id: UUID):
        with self.session as session:
            book = session.get(Book, id)
            return book

    def find_all(self):
        with self.session as session:
            books = session.exec(select(Book)).all()
            return books
