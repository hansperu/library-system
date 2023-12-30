from typing import Optional
from sqlmodel import Relationship, SQLModel, Field



class BookBase(SQLModel):
    title: str = Field(min_length=3, max_length=500)
    author: str = Field(min_length=3, max_length=500)

class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    borrows: list["Borrow"] = Relationship(back_populates="book")


class BookCreate(BookBase):
    pass
