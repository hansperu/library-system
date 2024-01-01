import httpx

from src.models.book import BookCreate

async def list_of_books() -> list[BookCreate]:
    async with httpx.AsyncClient() as client:
        response = await client.get("https://gutendex.com/books/")
        if response.status_code != 200:
            return []

        books: list[BookCreate] = []

        if not response.json().get("results"):
            return books
        
        for book in response.json().get("results"):
            if not book.get("title"):
                continue

            if not book.get("authors"):
                continue
            portrait: str = book.get("formats").get("image/jpeg")

            title = book.get("title")
            author = book.get("authors")[0].get("name")

            books.append(BookCreate(title=title, author=author, portrait=portrait))


        if not response.json().get("next"):
            return books

        next_page = response.json().get("next")


        response = await client.get(next_page)
        if response.status_code != 200:
            return books

        if not response.json().get("results"):
            return books

        for book in response.json().get("results"):
            if not book.get("title"):
                continue

            if not book.get("authors"):
                continue

            title = book.get("title")
            author = book.get("authors")[0].get("name")
            portrait: str = book.get("formats").get("image/jpeg")

            books.append(BookCreate(title=title, author=author, portrait=portrait))


        return books