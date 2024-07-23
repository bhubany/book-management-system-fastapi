from fastapi import APIRouter, Depends
from .service import BookService
from .models import Book


class BookRouter:
    def __init__(self):
        self.service = BookService()
        self.router = APIRouter()
        self.router.post("/", response_model=Book)(self.save_book)
        self.router.get("/{book_id}", response_model=Book)(self.get_book)

    def save_book(self, book_data: Book) -> Book:
        return self.service.save(book_data)

    def get_book(self, book_id: str) -> Book:
        return self.service.get(book_id)


book_router = BookRouter().router
