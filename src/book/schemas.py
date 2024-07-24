from sqlmodel import SQLModel, Field
from uuid import uuid4, UUID 

class Book(SQLModel, table=True):
    id: UUID = Field(default_factory= uuid4,primary_key=True, index=True)
    title: str
    author: str
    year: int
    