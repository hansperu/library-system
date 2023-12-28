from sqlmodel import Relationship, SQLModel, Field

from src.models.book import Book
from src.models.user import User


class Borrow(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    book_id: int = Field(foreign_key="book.id", nullable=False, index=True)
    user_id: int = Field(foreign_key="user.id", nullable=False, index=True)
    borrowed_at: int = Field(default=None, index=True)
    due_at: int = Field(default=None, index=True)
    returned_at: int = Field(default=None, index=True)

    book: Book = Relationship(back_populates="borrows")
    user: User = Relationship(back_populates="borrows")
