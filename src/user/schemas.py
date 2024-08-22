from pydantic import BaseModel, ConfigDict


class UserRequest(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    email: str
    password: str
    model_config = ConfigDict(from_attributes=True)
