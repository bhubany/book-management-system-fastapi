from sqlmodel import SQLModel, Field


class Book(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    title: str
    author: str
    year: int
    


# class Category(SQLModel, table=True):
#     id: int = Field(primary_key=True, index=True)
#     name: str = Field(index=True)
#     # book_id = Field( ForeignKey('books.id'))
#     is_correct = Field(default=False)
