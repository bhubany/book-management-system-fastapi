from fastapi import FastAPI, status
from src.book.router import book_router
from src.common.schemas.response import SuccessResponse, AppResponse
from src.config.database_config import create_tables
from typing import Any

'''No need to create tables manually as we have already used alembic for migrations. so commenting this code'''

# init db and create tables
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     create_tables()
#     yield
# app = FastAPI(lifespan=lifespan)

app = FastAPI()

# Routes
app.include_router(book_router, prefix="/books")


@app.get("/health", response_model=AppResponse[Any])
def health():
    return SuccessResponse(data={"message": "Server is up and healthy !"})
