from fastapi import FastAPI, status
from src.book.router import book_router
from src.common.schemas.response import SuccessResponse, AppResponse
from src.config.database_config import init_db
from contextlib import asynccontextmanager
from typing import Any
from src.common.exceptions.handler import exception_handlers

'''No need to create tables manually as we have already used alembic for migrations. so commenting this code'''

# init db and create tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

# app = FastAPI()


# registering exception handlers to app
for exc_class, handler in exception_handlers:
    app.add_exception_handler(exc_class, handler)

# Routes
app.include_router(book_router, prefix="/books")


@app.get("/health", response_model=AppResponse[Any])
def health():
    return SuccessResponse(data={"message": "Server is up and healthy !"})
