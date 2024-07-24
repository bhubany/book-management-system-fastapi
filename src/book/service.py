from book.models import BookRequest, BookResponse
from book.repository import BookRepository 
from uuid import UUID
from typing import List


class BookService:
    def __init__(self):
        self.repository = BookRepository()

    def save(self, data: BookRequest) -> BookResponse:
        book = self.repository.save(data)
        return book

    def find_by_id(self, id: UUID) -> BookResponse:
        return self.repository.find_by_id(id)
    
    def find_all(self) -> List[BookResponse]:
        return self.repository.find_all()
