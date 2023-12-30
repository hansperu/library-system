from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.routes import books_router, users_router
from src.db import get_engine
from src.utils.gutendex import list_of_books



engine = get_engine()


@asynccontextmanager
async def lifespan(app: FastAPI):
    books = await bulk_create_books()
    print("I've inserted {} books".format(len(books)))
    try:
        yield
    finally:
        await engine.dispose()


async def bulk_create_books():
    return await list_of_books()



app = FastAPI(lifespan=lifespan)

app.include_router(books_router, prefix="/books", tags=["books"])
app.include_router(users_router, prefix="/users", tags=["users"])


