import httpx

from src.models.book import BookCreate

# {
#   "id": <number of Project Gutenberg ID>,
#   "title": <string>,
#   "subjects": <array of strings>,
#   "authors": <array of Persons>,
#   "translators": <array of Persons>,
#   "bookshelves": <array of strings>,
#   "languages": <array of strings>,
#   "copyright": <boolean or null>,
#   "media_type": <string>,
#   "formats": <Format>,
#   "download_count": <number>
# }
# https://gutendex.com/



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

            title = book.get("title")
            author = book.get("authors")[0].get("name")

            books.append(BookCreate(title=title, author=author))


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

            books.append(BookCreate(title=title, author=author))


        return books


