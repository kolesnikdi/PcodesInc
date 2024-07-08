# book_management

## Tools used:

- The basic framework: Django, DRF
- DB: SQLite
- Autotesting: Pytest

## Project launch

- git clone https://github.com/kolesnikdi/PcodesInc.git
- cd .\PcodesInc\book_management
- Copy the .env file to \PcodesInc\book_management
- `pip install -r requirements.txt`
- `python manage.py migrate`
- If necessary, add 30 new records to the database -> `python manage.py add_books`
- `python manage.py runserver`
- Run end-to-end tests -> `pytest`

## Endpoints

### Add a book.

- [add_book](http://127.0.0.1:8000/books/add/)

### View and edit your book.

- [book_update](http://127.0.0.1:8000/books/1/)

### View and delete a book.

- [book_delete](http://127.0.0.1:8000/books/1/delete/)

### View a list of all books.
- [list_books](http://127.0.0.1:8000/books/)
