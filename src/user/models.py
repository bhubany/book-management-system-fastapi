from sqlmodel import Relationship, Field
from src.common.models.baseModel import BaseModel
from sqlalchemy import Enum, Column
from src.user.enums import UserStatus
class User(BaseModel, table=True):
    __tablename__ = "users"
    status: str = Field(sa_column= Column(Enum(UserStatus)))
    first_name: str = Field(index=True, nullable=False)
    last_name: str = Field(index=True, nullable=False)
    address: str = Field(nullable=True)
    authentication: "Authentication" = Relationship(back_populates="user")

from src.authentication.models import Authentication