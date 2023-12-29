from enum import Enum
from typing import Optional
from sqlmodel import Relationship, SQLModel, Field


class Role(str, Enum):
    ADMIN = "admin"
    STUDENT = "student"

class UserBase(SQLModel):
    email: str = Field(unique=True, index=True, min_length=3, max_length=100, regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    password: str = Field(min_length=8, max_length=100)


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(min_length=3, max_length=100)
    last_name: str = Field(min_length=3, max_length=100)
    role: Optional[Role] = Field(default=Role.STUDENT)
    address: str = Field(min_length=3, max_length=100)
    age: int = Field(ge=1, lt=200)
    borrows: list["Borrow"] = Relationship(back_populates="user")




class UserLogin(UserBase):
    pass