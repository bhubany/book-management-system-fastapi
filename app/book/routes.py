from fastapi import APIRouter, Depends
from .service import BookService, db_dependency
from .models import Book


class BookRouter():
    def __init__(self, service: BookService = Depends()):
        self.service = service
        self.router = APIRouter()
        self.router.post("/", response_model=Book)(self.save_book)
        self.router.get("/{book_id}", response_model=Book)(self.get_book)

    def save_book(self, book_data: Book, db: db_dependency) -> Book:
        return self.service.save(book_data, db)

    def get_book(self, book_id: str, db: db_dependency) -> Book:
        return self.service.get(book_id, db)


book_router = BookRouter().router
