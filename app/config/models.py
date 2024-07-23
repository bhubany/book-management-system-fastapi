from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .database import Base


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Choices(Base):
    __tablename__ = 'choices'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    is_correct = Column(Boolean, default=False)
