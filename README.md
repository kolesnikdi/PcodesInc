# weather_scraping

## Використані інструменти:

- Основний фреймвок: Django, DRF
- БД: SQLite
- Автотестування: Pytest

## Запуск проекту

- git clone https://github.com/kolesnikdi/Compassway.git
- cd .\PcodesInc\book_management
- Скопіюй .env файл до \PcodesInc\book_management
- `python manage.py makemigrations`
- `python manage.py migrate`
- За необхідності додати 30 нових записів в БД -> `python manage.py add_books`
- `python manage.py runserver`
-
    - Запуск end-to-end тестів -> `pytest`

## Endpoints

### Додати книгу.

- [add_book](http://127.0.0.1:8000/books/add/)

### Перегляд та редагування книги.

- [book_update](http://127.0.0.1:8000/books/1/)

### Перегляд та видалення книги.

- [book_delete](http://127.0.0.1:8000/books/1/delete/)

### Перегляд списку всіх книг.

[list_books](http://127.0.0.1:8000/books/)
