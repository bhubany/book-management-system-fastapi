from fastapi import Depends, APIRouter
from src.user.service import UserService
from src.common.schemas.generic_success import GenericSuccess
from src.common.schemas.response import SuccessResponse
from src.user.schemas import UserRequest
from src.common.schemas.response import SuccessResponse, AppResponse
from src.common.schemas.generic_success import GenericSuccess
from typing import List, Optional
from src.common.schemas.paginated_response import PaginatedResponse
from src.user.models import User


class UserRouter:
    def __init__(self, service: UserService = Depends(UserService)):
        self.service = service
        self.router = APIRouter()

        self.router.post(
            "", response_model=AppResponse[GenericSuccess])(self.save)
        self.router.get(
            "", response_model=AppResponse[PaginatedResponse[List[User]]])(self.find_paginated)

    def save(self, user_request: UserRequest) -> SuccessResponse[GenericSuccess]:
        return SuccessResponse(data=self.service.save(user_request))

    def find_paginated(self, page: Optional[int] = None, limit: Optional[int] = None) -> SuccessResponse[PaginatedResponse[List[User]]]:
        return SuccessResponse(data=self.service.find_paginated(page, limit))


user_router = UserRouter(service=UserService()).router
