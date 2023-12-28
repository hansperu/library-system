from sqlmodel import SQLModel, Field, Relationship
from .book import Book




class UserBase(SQLModel):
    email: str = Field(unique=True, index=True, gt=1, lt=200, regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    password: str = Field(gt=8, lt=200)

class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)


class UserCreate(UserBase):
    pass

class ProfileBase(SQLModel):
    first_name: str = Field(gt=1, lt=200)
    last_name: str = Field(gt=1, lt=200)
    age: int = Field(ge=1, lt=200)


class Profile(ProfileBase, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", nullable=False, index=True)
    role: str
    address: str = Field(gt=1, lt=200)
    user: User = Relationship(back_populates="profile")

class ProfileCreate(ProfileBase):
    pass