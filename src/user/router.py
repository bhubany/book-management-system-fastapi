from fastapi import Depends, APIRouter
from src.user.service import UserService
from src.common.schemas.generic_success import GenericSuccess
from src.common.schemas.response import SuccessResponse
from src.user.schemas import UserRequest
from src.common.schemas.response import SuccessResponse, AppResponse
from src.common.schemas.generic_success import GenericSuccess


class UserRouter:
    def __init__(self, service: UserService = Depends(UserService)):
        self.service = service
        self.router = APIRouter()

        self.router.post(
            "", response_model=AppResponse[GenericSuccess])(self.save)

    def save(self, user_request: UserRequest) -> SuccessResponse[GenericSuccess]:
        return SuccessResponse(data=self.service.save(user_request))


user_router = UserRouter(service=UserService()).router
