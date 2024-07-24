# Book Management System using FastAPI

- Create a system where users can manage a collection of books.

## Features

- ### CRUD Operations (Books):

  - create
  - Read
  - Update
  - Delete
- ### User Authentication:

  - Register
  - Login
  - JWT token-based authentication
- ### Search Functionality:

  - Search books by title, author, genre.
- ### Pagination:

  - Handle large datasets with pagination.
- ### Review System:

  - Users can add reviews to books.
- ### Role-Based Access Control:

  - Different access levels for users and admins

## Steps to run server

- ### To create virtual environment

  ```
  python3 -m venv venv
  OR,
  python -m venv venv

  ```
- ### To start virtual environnment

  ```
  source ./venv/bin/activate
  ```
- ### Install dependencies/requirements

  ` pip install -r requirements.txt`
- ### To run server

  `fastapi dev main.py`

## Using shell script

- ### Make file executable

  ```
   chmod +x start_server.sh

  ```
- ### Execute script

  ```
  ./start_server.sh
  ```
- ### All done! see log message server must had started now

  - Api
    [http://localhost:8000](http://localhost:8000)
  - Api docs
    [localhost:8000/docs](http://localhost:8000/docs)
