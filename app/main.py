from typing import Union
from book.routes import book_router
from fastapi import FastAPI, status
from utils.response import ApiResponse

app = FastAPI()

app.include_router(book_router)


@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return ApiResponse(400, "message", {"name": "full name"})
