from book.router import book_router
from fastapi import FastAPI, status
from utils.response import ApiResponse
from config.database_config import create_tables
from contextlib import asynccontextmanager


# init db and create tables
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)

# Routes
app.include_router(book_router, prefix="/books")



@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return ApiResponse(400, "message", {"name": "full name"})