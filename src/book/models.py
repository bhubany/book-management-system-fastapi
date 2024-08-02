from sqlmodel import Field
from typing import Optional
from datetime import datetime, timezone as tz
from src.common.models.baseModel import BaseModel


class Book(BaseModel, table=True):
    __tablename__ = "books"
    title: str = Field(index=True, nullable=False)
    author: str = Field(index=True, nullable=False)
    description: Optional[str] = Field(nullable=True)
    publisher: Optional[str] = Field(nullable=True)
    published_date: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(tz.utc))
    isbn: str = Field(unique=True, nullable=False)
    page_count: Optional[int] = Field(nullable=True)
    cover_url: Optional[str] = Field(nullable=True)
    language: Optional[str] = Field(nullable=True)
    book_type: Optional[str] = Field(nullable=True)
    status: Optional[str] = Field(nullable=True)
    condition: Optional[str] = Field(nullable=True)
    price: Optional[float] = Field(nullable=True)
