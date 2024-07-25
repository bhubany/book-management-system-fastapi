from sqlmodel import SQLModel, Field
from uuid import uuid4, UUID 
from datetime import datetime, timezone

class Book(SQLModel, table=True):
    id: UUID = Field(default_factory= uuid4,primary_key=True, index=True)
    title: str
    author: str
    year: int
    created_at: datetime | None = Field(default_factory= lambda:datetime.now(timezone.utc))
    