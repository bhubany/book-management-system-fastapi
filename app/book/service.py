from .models import BookRequest, BookResponse
from .repository import BookRepository 
import logging
from uuid import UUID
from typing import List

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BookService:
    def __init__(self):
        self.repository = BookRepository()

    def save(self, data: BookRequest) -> BookResponse:
        book = self.repository.save(data)
        logger.info(book)
        return book

    def find_by_id(self, id: UUID) -> BookResponse:
        return self.repository.find_by_id(id)
    
    def find_all(self):
        return self.repository.find_all()
