from fastapi import Depends
from src.authentication.repository import AuthenticationRepository
from src.authentication.schemas import AuthenticationRequest
from src.authentication.models import Authentication
from src.common.utils.password_hasher import PasswordHasher


class AuthenticationService:
    def __init__(self):
        self.repository = AuthenticationRepository()

    def save(self, data: AuthenticationRequest) -> Authentication:
        auth = Authentication(
            username=data.username,
            email=data.email,
            password=PasswordHasher.hash_password(data.password),
            provider=data.provider,
            user_id=data.user_id
        )
        return self.repository.save(auth)
