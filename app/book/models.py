from pydantic import BaseModel
from uuid import UUID


class BookRequest(BaseModel):
    title: str
    author: str
    year: int


class BookResponse(BookRequest):
    id: UUID