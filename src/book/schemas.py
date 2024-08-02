from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import Optional
from datetime import datetime


class BookRequest(BaseModel):
    title: str
    author: str
    description: Optional[str]
    publisher: Optional[str]
    published_date: Optional[datetime]
    isbn: str
    page_count: Optional[int]
    cover_url: Optional[str]
    language: Optional[str]
    book_type: Optional[str]
    status: Optional[str]
    condition: Optional[str]
    price: Optional[float]


class BookResponse(BaseModel):
    id: UUID
    title: str
    author: str
    description: Optional[str]
    publisher: Optional[str]
    published_date: Optional[datetime]
    isbn: Optional[str]
    page_count: Optional[int]
    cover_url: Optional[str]
    language: Optional[str]
    book_type: Optional[str]
    status: Optional[str]
    condition: Optional[str]
    price: Optional[float]
    created_at: datetime
    updated_at: Optional[datetime]
    created_by: Optional[str]
    updated_by: Optional[str]

    model_config = ConfigDict(from_attributes=True)
