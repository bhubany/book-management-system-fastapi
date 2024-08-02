from fastapi import APIRouter
from uuid import UUID
from typing import List
from src.book.service import BookService
from src.book.schemas import BookRequest, BookResponse
from src.common.schemas.response import SuccessResponse, AppResponse
from src.common.schemas.generic_success import GenericSuccess


class BookRouter:
    def __init__(self):
        self.service = BookService()
        self.router = APIRouter()
        self.router.post(
            "", response_model=AppResponse[GenericSuccess])(self.save)
        self.router.get(
            "/{book_id}", response_model=AppResponse[BookResponse])(self.find_by_id)
        self.router.get("", response_model=AppResponse[List[BookResponse]])(
            self.find_all)

    def save(self, book_data: BookRequest) -> SuccessResponse[GenericSuccess]:
        return SuccessResponse(data=self.service.save(book_data))

    def find_by_id(self, book_id: UUID) -> SuccessResponse[BookResponse]:
        return SuccessResponse(data=self.service.find_by_id(book_id))

    def find_all(self) -> SuccessResponse[List[BookResponse]]:
        return SuccessResponse(data=self.service.find_all())


book_router = BookRouter().router
