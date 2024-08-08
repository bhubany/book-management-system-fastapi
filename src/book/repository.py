from sqlmodel import Session, select, func
from uuid import UUID
from typing import Optional, List
from src.config.database_config import engine
from src.book.models import Book
from src.common.schemas.paginated_response import PaginatedResponse
from src.common.schemas.page_info import PageInfo


class BookRepository():
    def __init__(self):
        self.session: Session = Session(engine)

    def save(self, book: Book) -> Book:
        with self.session as session:
            session.add(book)
            session.commit()
            session.refresh(book)
            return book

    def find_by_id(self, id: UUID) -> Book:
        with self.session as session:
            return session.get(Book, id)

    def find_all(self) -> List[Book]:
        with self.session as session:
            return session.exec(
                select(Book)
                .order_by(Book.updated_at.desc())
                .order_by(Book.created_at.desc())
            ).all()

    def find_paginated(self, page: Optional[int], limit: Optional[int]) -> PaginatedResponse[List[Book]]:
        page = page if page != None and page > 0 else 1
        limit = limit if limit != None and limit > 0 else 10
        offset = (page-1)*limit

        with self.session as session:
            total_items = session.exec(select(func.count(Book.id))).one()
            books = session.exec(
                select(Book)
                .order_by(Book.updated_at.desc())
                .order_by(Book.created_at.desc())
                .offset(offset)
                .limit(limit)
            ).all()

            total_pages = (total_items + limit - 1) // limit
            next_page = (None, page+1)[page < total_pages]
            previous_page = (None, page-1)[page > 1]
            page_info = PageInfo(
                page=page,
                per_page=limit,
                total_pages=total_pages,
                total_items=total_items,
                next_page=next_page,
                previous_page=previous_page
            )

            return PaginatedResponse(data=books, page_info=page_info)
