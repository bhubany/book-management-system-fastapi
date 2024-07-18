from fastapi import APIRouter, Depends
from .service import BookService
from .models import Book

book_router = APIRouter()


@book_router.post("/")
def save_book(book_data: Book, service: BookService = Depends(BookService)) -> Book:
    return service.save(book_data)


@book_router.get("/{book_id}")
def get_book(book_id: str, service: BookService = Depends(BookService)) -> Book:
    return service.get(book_id)
