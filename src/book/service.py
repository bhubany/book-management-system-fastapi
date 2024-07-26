from book.models import BookRequest, BookResponse
from book.repository import BookRepository
from uuid import UUID
from typing import List
from logger.config import get_logger


class BookService:
    def __init__(self):
        self.repository = BookRepository()
        self.logger = get_logger(__name__)

    def save(self, data: BookRequest) -> BookResponse:
        book = self.repository.save(data)
        self.logger.info("Book saved successfully")
        return book

    def find_by_id(self, id: UUID) -> BookResponse:
        return self.repository.find_by_id(id)

    def find_all(self) -> List[BookResponse]:
        self.logger.info("All books fetched successfully")
        return self.repository.find_all()
