from .book import Book
from .borrow import Borrow
from .user import User

from sqlmodel import SQLModel


metadata = SQLModel.metadata