from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.models.book import BookCreate, Book

from src.routes import books_router, users_router
from src.db import get_engine, get_session
from src.utils.gutendex import list_of_books

engine = get_engine()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await bulk_create_books()
    try:
        yield
    finally:
        await engine.dispose()


async def bulk_create_books() -> None:
    books: list[BookCreate] = await list_of_books()
    with get_session() as session:
        for book in books:
            session.add(Book(**book.model_dump()))
        session.commit()

    
    print("I've inserted {} books".format(len(books)))


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=3600
)

app.include_router(books_router, prefix="/books", tags=["books"])
app.include_router(users_router, prefix="/users", tags=["users"])


