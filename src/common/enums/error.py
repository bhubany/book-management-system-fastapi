from enum import Enum


class ErrorType(Enum):
    VALIDATION_ERROR = ("Validation Error", 400)
    UNAUTHORIZED = ("Unauthorized", 401)
    NOT_FOUND = ("Not Found", 404)
    AUTHENTICATION_TOKEN_EXPIRED = ("Authentication Token Expired", 401)
    GENERIC_ERROR = ("Generic Exception", -1)

    def __init__(self, type: str, code: int):
        self.type = type
        self.code = code
