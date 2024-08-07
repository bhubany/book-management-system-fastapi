from fastapi import HTTPException
from typing import Any, Dict
from http import HTTPStatus
from src.common.enums.error import ErrorType


class AppException(HTTPException):
    def __init__(self, http_status: HTTPStatus, status_code: int, error_type: ErrorType,  detail: Any, headers: Dict[str, str] = {}):
        super().__init__(status_code=status_code, detail=detail,
                         headers={**headers, 'Content-Type': 'application/json'})
        self.type = error_type.type
        self.code = error_type.code
        self.http_status = http_status
