# Library's system

> A simple replica of a library system.

## TODO

- [ ] Make it more robust with proper error handling
- [ ] Add endpoints to borrow and return books 
- [x] consume a gutenberg API to fetch books
- [x] Make a bulk insertion of gutenberg API
- [x] Make a basic client to use in local development
- [x] Make a easy deployment with docker compose and docker
- [x] create containers for database, frontend and backend
- [x] create docker-compose file


Unifies frontend & backend, and an easy deploy to production with docker.

## Technologies
- Python
- FastAPI
- Docker
- Docker Compose
- Solid-js
- Typescript
- TailwindCSS
- Mysql
- Pydantic
- PyJWT
- SQLModel
- PyMySQL
- Alembic(tool to manage migrations)


## Installation
I recommend to install (docker and docker-compose.)[https://docs.docker.com/compose/]
```bash
docker compose build
# if you want to watch the logs run 
docker compose up
# if you want to start the containers in background (without watching the logs)
docker compose up -d
# if you want to stop the containers
docker compose down
#
```

## Post installation
You have to check the ports after installation and deployment with docker on the following ports:

- http://localhost:3000 for the web client
- http://localhost:80/docs for API documentation
- http://localhost:80/redoc for another version of the API documentation
- http://localhost:3306 for connection to the mysql database

## API design
For your Book Tracking/Library System RESTful API, here are the proposed endpoints, structured to handle various functionalities:

### Books Endpoints
1. **List All Books**
   - Method: `GET`
   - Endpoint: `/books`
   - Description: Retrieve a list of all books in the library.

2. **Get Book Details**
   - Method: `GET`
   - Endpoint: `/books/{book_id}`
   - Description: Get detailed information about a specific book.

3. **Add New Book**
   - Method: `POST`
   - Endpoint: `/books`
   - Description: Add a new book to the library system.

4. **Update Book Information**
   - Method: `PUT`
   - Endpoint: `/books/{book_id}`
   - Description: Update the details of an existing book.

5. **Delete a Book**
   - Method: `DELETE`
   - Endpoint: `/books/{book_id}`
   - Description: Remove a book from the library system.

### User Endpoints
1. **List All Users**
   - Method: `GET`
   - Endpoint: `/users`
   - Description: Retrieve a list of all users.

2. **Get User Details**
   - Method: `GET`
   - Endpoint: `/users/{user_id}`
   - Description: Get detailed information about a specific user.

3. **Register New User**
   - Method: `POST`
   - Endpoint: `/users`
   - Description: Add a new user to the system.

4. **Update User Information**
   - Method: `PUT`
   - Endpoint: `/users/{user_id}`
   - Description: Update the details of an existing user.

5. **Delete a User**
   - Method: `DELETE`
   - Endpoint: `/users/{user_id}`
   - Description: Remove a user from the system.

### Borrowing Endpoints
1. **Borrow a Book**
   - Method: `POST`
   - Endpoint: `/borrow`
   - Description: Record the borrowing of a book by a user.

2. **Return a Book**
   - Method: `POST`
   - Endpoint: `/return`
   - Description: Record the return of a borrowed book.

3. **List Borrowings**
   - Method: `GET`
   - Endpoint: `/borrowings`
   - Description: View all borrowings, with optional filters (like user, book, overdue).


4. **User Borrowing History**
   - Method: `GET`
   - Endpoint: `/users/{user_id}/borrowings`
   - Description: Get the borrowing history of a specific user.


