from typing import Annotated, Union
from book.routes import book_router
from fastapi import Depends, FastAPI, status
from utils.response import ApiResponse
import config.models as models
# from config.database import engine, SessionLocal
# from sqlalchemy.orm import Session

app = FastAPI()
# models.Base.metadata.create_all(bind=engine)


app.include_router(book_router)


@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return ApiResponse(400, "message", {"name": "full name"})


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# db_dependency = Annotated[Session, Depends(get_db)]
