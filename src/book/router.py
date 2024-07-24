from fastapi import APIRouter
from book.service import BookService
from book.models import BookRequest, BookResponse
from uuid import UUID
from typing import List


class BookRouter:
    def __init__(self):
        self.service = BookService()
        self.router = APIRouter()
        self.router.post("/", response_model=BookResponse)(self.save)
        self.router.get("/{book_id}", response_model=BookResponse)(self.find_by_id)
        self.router.get("", response_model=List[BookResponse])(self.find_all)


    def save(self, book_data: BookRequest) -> BookResponse:
        return self.service.save(book_data)

    def find_by_id(self, book_id: UUID) -> BookResponse:
        return self.service.find_by_id(book_id)
    
    def find_all(self) -> List[BookResponse]:
        return self.service.find_all()


book_router = BookRouter().router
