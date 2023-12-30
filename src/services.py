from sqlmodel import select

from src.utils.pyjwt import JwtPayload, encode_jwt

from .models.user import User, UserLogin
from .models.borrow import Borrow
from .models.book import Book, BookCreate
from .db import get_session
from .config import get_config

def list_books(title: str | None, author: str | None) -> list[Book]:
    books = []

    with get_session() as session:
        query = select(Book)
        if title:
            query = query.where(Book.title == title)
        if author:
            query = query.where(Book.author == author)
        books = session.exec(query).all()

    return books


def get_book_by_id(book_id: int) -> Book:
    with get_session() as session:
        return session.get(Book, book_id)

def update_book(book_id: int, book: Book) -> Book:
    with get_session() as session:
        db_book = session.get(Book, book_id)
        db_book.model_validate(book)
        session.add(db_book)
        session.commit()
        session.refresh(db_book)
    return db_book


def create_book(book: BookCreate) -> Book:
    with get_session() as session:
        db_book = Book.model_validate(book)
        session.add(db_book)
        session.commit()
        session.refresh(db_book)
    return db_book 


def delete_book(book_id: int) -> None:
    with get_session() as session:
        session.delete(session.get(Book, book_id))
        session.commit()



def get_users(first_name: str | None, last_name: str | None) -> list[User]:
    users = []

    with get_session() as session:
        query = select(User)
        if first_name:
            query = query.where(User.first_name == first_name)
        if last_name:
            query = query.where(User.last_name == last_name)
        users = session.exec(query).all()
    return users


def login(user: UserLogin) -> dict | None:
    user_id: None
    user_role: None
    with get_session() as session:
        db_user = session.exec(select(User).where(User.email == user.email)).first()
        if db_user and user.password == db_user.password:
            user_id = db_user.id
            user_role = db_user.role

        session.close()

    if user_id:
        return encode_jwt(JwtPayload(user_id=user_id, role=user_role), get_config().JWT_SECRET) 

    return None
        

def signup(user: User) -> User:    
    print(user)
    with get_session() as session:
        db_user = User.model_validate(user)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
    return db_user
    

def get_user_by_id(user_id: int) -> User:
    with get_session() as session:
        # TODO: find a way to just return the user without password
        return session.get(User, user_id)


def update_user(user_id: int, user: User) -> User:
    with get_session() as session:
        db_user = session.get(User, user_id)
        db_user.first_name = user.first_name
        db_user.last_name = user.last_name
        db_user.age = user.age
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
    return db_user


def delete_user(user_id: int) -> None:
    with get_session() as session:
        session.delete(session.get(User, user_id))
        session.commit()


def patch_user(user_id: int, user: User) -> User:
    with get_session() as session:
        db_user = session.get(User, user_id)
        db_user.first_name = user.first_name
        db_user.last_name = user.last_name
        db_user.age = user.age
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
    return db_user



def create_borrow_record(borrow: Borrow) -> Borrow:
    db_borrow = None
    with get_session() as session:
        db_borrow = Borrow.model_validate(borrow)
        session.add(db_borrow)
        session.commit()
        session.refresh(db_borrow)
    return db_borrow


def return_borrowed_book(borrow_id: int):
    with get_session() as session:
        db_borrow = session.get(Borrow, borrow_id)
        db_borrow.returned_at = int(time.time())
        session.add(db_borrow)
        session.commit()
        session.refresh(db_borrow)
    return db_borrow