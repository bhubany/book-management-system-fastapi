from src.common.models.baseModel import BaseModel
from src.user.enums import UserStatus
from sqlmodel import Relationship


class User(BaseModel, table=True):
    __tablename__ = "users"
    status: UserStatus
    first_name: str
    address: str
    authentication: "Authentication" = Relationship(
        back_populates="authentications")

from src.authentication.models import Authentication