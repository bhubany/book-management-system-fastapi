from pydantic import BaseModel
from uuid import UUID
from src.common.enums.provider import Provider


class AuthenticationRequest(BaseModel):
    username: str
    email: str
    password: str
    provider: Provider
    user_id: UUID
