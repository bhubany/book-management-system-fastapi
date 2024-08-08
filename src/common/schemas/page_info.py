from pydantic import BaseModel
from typing import Optional


class PageInfo(BaseModel):
    page: int
    per_page: int
    total_pages: int
    total_items: int
    next_page: Optional[int] = None
    previous_page: Optional[int] = None
