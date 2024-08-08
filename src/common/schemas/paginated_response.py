from typing import TypeVar, Generic
from pydantic import BaseModel
from src.common.schemas.page_info import PageInfo

T = TypeVar("T")


class PaginatedResponse(BaseModel, Generic[T]):
    data: T
    page_info: PageInfo
