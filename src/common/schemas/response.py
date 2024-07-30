from fastapi.responses import JSONResponse, Response
from typing import Dict, TypeVar, Generic, Optional
from pydantic import BaseModel

T = TypeVar('T')


class Error(BaseModel):
    """Base model for error responses."""
    type: str
    sub_code: int
    title: str
    user_message: str
    support_message: str


class ApiResponse(BaseModel, Generic[T]):
    """Base model for app responses."""
    data: Optional[T]
    error: Error | None = None
    status_code: int = 200


# class ApiResponse(BaseModel, Generic[T]):

#     def __init__(self, status: int, data: Optional[T] = None, error: Error = None, headers: Dict[str, str] = None):
#         response = AppResponse(
#             status_code=status, data=data, error=error).model_dump()
#         super().__init__(content=response, status_code=status, headers=headers)
