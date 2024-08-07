from fastapi import Request
from src.common.exceptions.app_exception import AppException
from src.common.schemas.response import ErrorResponse, Error
from src.common.enums.error import ErrorType


class ExceptionHandler:
    @staticmethod
    async def app_exception_handler(request: Request, exc: AppException):
        return ErrorResponse(status_code=exc.status_code, http_status=exc.http_status,
                             error=Error(
                                 type=exc.type,
                                 support_message="Hello this is support message",
                                 title="Some resource not found",
                                 user_message="User message",
                                 sub_code=exc.code
                             ))


exception_handlers = [
    (AppException, ExceptionHandler.app_exception_handler),
]
