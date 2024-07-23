from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine
from .models import Book
from .schema import Book as BookSchema

engine = create_engine("postgresql://pg-admin:password123@localhost:5432/bms")

SQLModel.metadata.create_all(engine)


def save(data: Book):
    print(f"From save of repository  {data} ")
    with Session(engine) as session:
        book = BookSchema(id=1, title="Science", year="2024", author="bhuban")
        session.add(book)
        session.commit()
        session.refresh(book)
        return book

