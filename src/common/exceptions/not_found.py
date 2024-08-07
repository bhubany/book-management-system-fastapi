from fastapi import status
from typing import Any
from src.common.exceptions.app_exception import AppException
from src.common.enums.error import ErrorType
from http import HTTPStatus

# """ Excepton to be raised when resource is not found"""


class NotFoundException(AppException):
    def __init__(self, detail: Any) -> None:
        super().__init__(http_status=HTTPStatus.NOT_FOUND._name_, status_code=status.HTTP_404_NOT_FOUND,
                         error_type=ErrorType.NOT_FOUND, detail=detail)
