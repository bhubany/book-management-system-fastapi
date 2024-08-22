from fastapi import Depends
from src.config.database_config import engine
from sqlmodel import Session, select, func
from src.user.models import User
from src.common.schemas.page_info import PageInfo
from typing import Optional, List
from src.common.schemas.paginated_response import PaginatedResponse


class UserRepostiory:
    def __init__(self):
        self.session: Session = Session(engine)

    def save(self, user: User) -> User:
        with self.session as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def find_paginated(self, page: Optional[int], limit: Optional[int]) -> PaginatedResponse[List[User]]:
        page = page if page != None and page > 0 else 1
        limit = limit if limit != None and limit > 0 else 10
        offset = (page-1)*limit

        with self.session as session:
            total_items = session.exec(select(func.count(User.id))).one()
            books = session.exec(
                select(User)
                .order_by(User.updated_at.desc())
                .order_by(User.created_at.desc())
                .offset(offset)
                .limit(limit)
            ).all()

            total_pages = (total_items + limit - 1) // limit
            next_page = (None, page+1)[page < total_pages]
            previous_page = (None, page-1)[page > 1]
            page_info = PageInfo(
                page=page,
                per_page=limit,
                total_pages=total_pages,
                total_items=total_items,
                next_page=next_page,
                previous_page=previous_page
            )

            return PaginatedResponse(data=books, page_info=page_info)
