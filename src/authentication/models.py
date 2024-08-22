from src.user.models import User
from sqlmodel import Field, Relationship
from src.common.models.baseModel import BaseModel
from src.common.enums.provider import Provider
from uuid import UUID


class Authentication(BaseModel, table=True):
    __tablename__ = "authentications"
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    password: str = Field()
    provider: Provider = Field(sa_column_kwargs={"default": Provider.LOCAL})
    user_id: UUID = Field(foreign_key="users.id")
    user: User = Relationship(back_populates="authentication")
