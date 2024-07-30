from fastapi import APIRouter
from book.service import BookService
from book.models import BookRequest, BookResponse
from uuid import UUID
from typing import List
from common.schemas.response import ApiResponse


class BookRouter:
    def __init__(self):
        self.service = BookService()
        self.router = APIRouter()
        self.router.post(
            "/", response_model=ApiResponse[BookResponse])(self.save)

        self.router.get(
            "/{book_id}", response_model=ApiResponse[BookResponse])(self.find_by_id)

        self.router.get("", response_model=ApiResponse[List[BookResponse]])(
            self.find_all)

    def save(self, book_data: BookRequest) -> ApiResponse:
        res = self.service.save(book_data)
        return ApiResponse(status=200, data=res)

    def find_by_id(self, book_id: UUID) -> ApiResponse:
        res = self.service.find_by_id(book_id)
        return ApiResponse(status=200, data=res)

    def find_all(self) -> ApiResponse:
        res = self.service.find_all()
        return ApiResponse(status=200, data=res)


book_router = BookRouter().router
