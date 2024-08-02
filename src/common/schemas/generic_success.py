from pydantic import BaseModel


class GenericSuccess(BaseModel):
    success: bool
