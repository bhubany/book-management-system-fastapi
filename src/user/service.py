from fastapi import Depends
from src.user.repository import UserRepostiory
from src.user.models import User
from src.user.schemas import UserRequest
from src.common.schemas.generic_success import GenericSuccess
from src.authentication.service import AuthenticationService
from src.authentication.schemas import AuthenticationRequest
from src.user.enums import UserStatus
from src.common.enums.provider import Provider
from typing import List, Optional
from src.common.schemas.paginated_response import PaginatedResponse


class UserService:
    def __init__(self):
        self.repository = UserRepostiory()
        self.authenticationService = AuthenticationService()

    def save(self, data: UserRequest) -> GenericSuccess:

        user = User(
            status=UserStatus.PENDING,
            first_name="",
            last_name="",
            address=None,
        )
        res = self.repository.save(user)

        authRequest = AuthenticationRequest(
            user_id=res.id,
            email=data.email,
            password=data.password,
            provider=Provider.LOCAL,
            username=data.email
        )

        authRes = self.authenticationService.save(authRequest)
        return GenericSuccess(success=authRes is not None)

    def find_paginated(self, page: Optional[int], limit: Optional[int]) -> PaginatedResponse[List[User]]:
        return self.repository.find_paginated(page, limit)
