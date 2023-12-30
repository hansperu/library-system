from fastapi import APIRouter, Body, Query, Path
from fastapi.responses import JSONResponse

from src.models.book import Book, BookCreate
from src.models.user import User, UserLogin
from src.services import create_book, delete_user, get_book_by_id, get_user_by_id, list_books, login, patch_user, signup, update_book, delete_book, get_users


books_router = APIRouter()

@books_router.get("/")
def books(title: str = Query(None, min_length=3), author: str = Query(None, min_length=3), limit: int = Query(10, ge=1, le=100)) -> list[Book]:
    books = list_books(title, author)
    return books

@books_router.get("/{book_id}")
def get_book(book_id: int = Path(..., gt=0)):
    book = get_book_by_id(book_id)
    return book


@books_router.post("/", dependencies=[])
def create_a_book(book: BookCreate) -> Book:
    book = create_book(book)
    return book


@books_router.put("/{book_id}", dependencies=[])
def update_book(book_id: int = Path(..., gt=0), book: BookCreate = Body(...)) -> Book:
    book = update_book(book_id, book)
    return book


@books_router.delete("/{book_id}", dependencies=[])
def remove_book(book_id: int = Path(..., gt=0)):
    delete_book(book_id)
    return {"message": "Book deleted"}


users_router = APIRouter()

@users_router.get("/", dependencies=[])
def list_users(first_name: str = Query(None, min_length=3), last_name: str = Query(None, min_length=3)) -> list[User]:
    users = get_users(first_name, last_name)
    return users


@users_router.get("/{user_id}", dependencies=[])
def get_user_by_id(user_id: int = Path(..., gt=0)) -> User:
    user = get_user_by_id(user_id)
    return user


@users_router.post("/login")
def user_login(user: UserLogin) :
    token = login(user)
    if token:
        return token
    return JSONResponse(status_code=401, content={"message": "Wrong credentials"})


@users_router.post("/signup")
def user_signup(user: User) -> User:
    # add new logic with new model inherating from User to create a new user without id
    db_user = signup(user)
    return db_user

@users_router.patch("/{user_id}")
def patch_user(user_id: int = Path(..., gt=0), user: User = Body(...)):
    new_user = patch_user(user_id, user) 

    return new_user


@users_router.put("/{user_id}")
def update_user(user_id: int = Path(..., gt=0), user: User = Body(...)):
    new_user = update_user(user_id, user) 

    return new_user

@users_router.delete("/{user_id}")
def remove_user(user_id: int = Path(..., gt=0)):
    delete_user(user_id)
    return {"message": "User deleted"}


borrow_router = APIRouter()

@borrow_router.post("/borrow")
def borrow_book():
    pass