from uuid import UUID
from typing import List, Optional
from src.book.schemas import BookRequest, BookResponse
from src.book.repository import BookRepository
from src.book.models import Book
from src.common.schemas.generic_success import GenericSuccess
from src.common.schemas.paginated_response import PaginatedResponse


class BookService:
    def __init__(self):
        self.repository = BookRepository()

    def save(self, data: BookRequest) -> BookResponse:
        book = Book(
            title=data.title,
            author=data.author,
            description=data.description,
            publisher=data.publisher,
            published_date=data.published_date,
            isbn=data.isbn,
            page_count=data.page_count,
            cover_url=data.cover_url,
            language=data.language,
            book_type=data.book_type,
            status=data.status,
            condition=data.condition,
            price=data.price,
        )
        res: Book = self.repository.save(book)
        return GenericSuccess(success=res is not None)

    def find_by_id(self, id: UUID) -> BookResponse:
        return self.repository.find_by_id(id)

    def find_all(self) -> List[BookResponse]:
        return self.repository.find_all()

    def find_paginated(self, page: Optional[int], limit: Optional[int]) -> PaginatedResponse[List[BookResponse]]:
        return self.repository.find_paginated(page, limit)
