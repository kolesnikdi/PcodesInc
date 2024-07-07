from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.contrib import messages

from management.models import Books
from management.serializers import BookSerializer


class BooksView(generics.ListAPIView):
    """Displays all books starting from the last one added"""
    queryset = Books.objects.all().order_by('-id')
    serializer_class = BookSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'books_list.html'

    def get(self, request, *args, **kwargs):
        paginator = PageNumberPagination()
        paginated_queryset = paginator.paginate_queryset(queryset=self.get_queryset(), request=request, view=self)
        return Response({'book_list': paginated_queryset, 'is_paginated': True, 'page_obj': paginator.page},
                        status=status.HTTP_200_OK)


class BookUpdateView(generics.ListCreateAPIView):
    """Displays the selected book. Allows the partial update selected book. """
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'book_update.html'

    def get(self, request, *args, **kwargs):
        book = self.get_object()
        return Response({'book': book}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = self.serializer_class(book, data=request.data, partial=True)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            messages.success(request, f'Book "{book.title}" was update successfully.')
            return Response({'book': book}, status=status.HTTP_200_OK)
        except Exception as message:
            messages.error(request, message)
        return Response({'book': book}, status=status.HTTP_400_BAD_REQUEST)


class BookDeleteView(generics.ListCreateAPIView):
    """Displays the selected book. Allows to delete selected book. """
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'book_delete.html'

    def get(self, request, *args, **kwargs):
        book = self.get_object()
        return Response({'book': book}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        book = self.get_object()
        title = book.title
        book.delete()
        return Response({'message': f'Book "{title}" was deleted successfully.'})


class AddBookView(generics.ListCreateAPIView):
    """Allows new book creation."""
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'book_add.html'

    def post(self, request, *args, **kwargs):
        book_data = self.serializer_class(data=request.data)
        try:
            book_data.is_valid(raise_exception=True)
            try:
                book = Books.objects.create(**book_data.validated_data)
                messages.success(request, f'Book "{book.title}" was create successfully.')
                return Response(self.serializer_class(instance=book).data, status=status.HTTP_200_OK)
            except Exception:
                messages.error(request, {'error': 'An error occurred when saving a book'})
        except Exception as message:
            messages.error(request, message)
        return self.get(request, *args, **kwargs, status=status.HTTP_400_BAD_REQUEST)
