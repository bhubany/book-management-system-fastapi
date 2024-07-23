from pydantic import BaseModel


class Book(BaseModel):
    id: str
    title: str
    author: str
    year: int

    class Config:
        orm_mode = True

    def dump(self):
        return self.model_dump()
