from django.urls import path
from management.views import BooksView, AddBookView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BooksView.as_view(), name='list_books'),
    path('books/<int:id>/', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:id>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('books/add/', AddBookView.as_view(), name='add_book'),
]
