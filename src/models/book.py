from sqlmodel import SQLModel, Field


class BookBase(SQLModel):
    title: str = Field(min_length=3, max_length=100)
    author: str = Field(min_length=3, max_length=100)

class Book(BookBase, table=True):
    id: int = Field(default=None, primary_key=True)


class BookCreate(BookBase):
    pass
