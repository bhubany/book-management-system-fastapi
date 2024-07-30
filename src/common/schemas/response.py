from typing import Dict, TypeVar, Generic, Optional, Any
from pydantic import BaseModel
from fastapi import status, Response

T = TypeVar('T')


class Error(BaseModel):
    """Base model for error responses."""
    type: str
    sub_code: int
    title: str
    user_message: str
    support_message: str


class AppResponse(BaseModel, Generic[T]):
    """Base model for app responses."""
    status: str = "OK"
    data: Optional[T] = None
    error: Optional[Error] = None


class ApiResponse(Response, Generic[T]):
    def __init__(self, status_code: int = status.HTTP_200_OK, data: Optional[T] = None, error: Optional[Error] = None, headers: Dict[str, Any] = None):
        response = AppResponse(data=data, error=error)
        super().__init__(content=response.model_dump_json(), status_code=status_code,
                         headers=headers, media_type="application/json")


class SuccessResponse(Response, Generic[T]):
    def __init__(self, data: Optional[T] = None, headers: Dict[str, Any] = None):
        super().__init__(content=AppResponse(data=data).model_dump_json(), status_code=status.HTTP_200_OK,
                         headers=headers, media_type="application/json")
