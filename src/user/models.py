from sqlmodel import Relationship, Field
from src.common.models.baseModel import BaseModel


class User(BaseModel, table=True):
    __tablename__ = "users"
    status: str = Field(index=True, nullable=False)
    first_name: str = Field(index=True, nullable=False)
    last_name: str = Field(index=True, nullable=False)
    address: str = Field(nullable=True)
    authentication: "Authentication" = Relationship(
        back_populates="authentications")

from src.authentication.models import Authentication