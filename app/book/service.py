from .models import Book
from . import repository
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BookService:
    def save(self, data: Book) -> dict:
        print("################ from save of")
        book = repository.save(data)
        print(f"Book saved with details: {book}")
        logger.info(book)
        return book

    def get(self, id: str) -> dict:
        book = Book.objects.get(id=id)
        if not book:
            return {"error": "Book not found"}

        print(f"Book retrieved with details: {book}")
        return {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "isbn": book.isbn
        }
