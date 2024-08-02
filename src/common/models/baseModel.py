from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime, timezone as tz
from uuid import UUID, uuid4


class BaseModel(SQLModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(tz.utc))
    created_by: Optional[UUID] = Field(default=None, nullable=True)
    updated_at: Optional[datetime] = Field(default=None, nullable=True)
    updated_by: Optional[UUID] = Field(default=None, nullable=True)
