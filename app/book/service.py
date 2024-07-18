from .models import Book


class BookService:
    def __init__(self):
        pass

    def save(self, data: Book) -> dict:
        # book = Book(data)
        print(f"Book saved with details: {data}")
        return data

    def get(self, id: str) -> dict:
        # book = Book.get(id)
        print(f"Book retrieved with details: {id}")
        return {
            "id": id,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "year": 1925,
            "isbn": "978-0-14-118116-4"
        }
