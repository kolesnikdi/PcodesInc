import pytest
import datetime
import random
import string
from django.urls import reverse
from rest_framework import status

from management.models import Books


class TestAddBookView:
    @pytest.mark.django_db
    def test_create_book_valid_data(self, api_client):
        data = {
            'title': ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 100))).title(),
            'author': ''.join(random.choice(string.ascii_letters) for _ in range(5)).title() + ''.join(
                random.choice(string.ascii_letters) for _ in range(10)).title(),
            'published_date': datetime.datetime.utcnow().strftime('%Y-%m-%d'),
            'isbn': ''.join(random.choice(string.digits) for _ in range(13)),
            'pages': random.randint(50, 1000)
        }
        response = api_client.post(reverse('add_book'), data=data, format='json')
        assert response.status_code == status.HTTP_200_OK
        data_for_check = Books.objects.filter(title=data['title']).first()
        assert data_for_check.author == data['author']
        assert data_for_check.published_date.strftime('%Y-%m-%d') == data['published_date']
        assert data_for_check.isbn == data['isbn']
        assert data_for_check.pages == data['pages']

    @pytest.mark.django_db
    def test_create_book_invalid_author(self, api_client):
        data = {
            'title': ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 100))).title(),
            'author': ''.join(random.choice(string.ascii_letters) for _ in range(5)).title() + ''.join(
                random.choice(string.digits) for _ in range(13)),
            'published_date': datetime.datetime.utcnow().strftime('%Y-%m-%d'),
            'isbn': ''.join(random.choice(string.digits) for _ in range(13)),
            'pages': random.randint(50, 1000)
        }
        response = api_client.post(reverse('add_book'), data=data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert b'Only letters are allowed.' in response.content


class TestBookDeleteView:

    @pytest.mark.django_db
    def test_create_book_invalid_author(self, api_client, create_book):
        response = api_client.post(reverse('book_delete', args=[create_book.id]), format='json')
        assert response.status_code == status.HTTP_200_OK
        data_for_check = Books.objects.filter(id=create_book.id).first()
        assert data_for_check is None


class TestBookUpdateView:
    @pytest.mark.django_db
    def test_update_book_valid_data(self, api_client, create_book):
        data = {
            'title': ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 100))).title(),
            'author': ''.join(random.choice(string.ascii_letters) for _ in range(5)).title() + ''.join(
                random.choice(string.ascii_letters) for _ in range(10)).title(),
            'published_date': datetime.datetime.utcnow().strftime('%Y-%m-%d'),
            'isbn': ''.join(random.choice(string.digits) for _ in range(13)),
            'pages': random.randint(50, 1000)
        }
        response = api_client.post(reverse('book_update', args=[create_book.id]), data=data, format='json')
        assert response.status_code == status.HTTP_200_OK
        data_for_check = Books.objects.filter(title=data['title']).first()
        assert data_for_check.author == data['author']
        assert data_for_check.published_date.strftime('%Y-%m-%d') == data['published_date']
        assert data_for_check.isbn == data['isbn']
        assert data_for_check.pages == data['pages']

    @pytest.mark.django_db
    def test_update_book_invalid_author(self, api_client, create_book):
        data = {
            'title': ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 100))).title(),
            'author': ''.join(random.choice(string.ascii_letters) for _ in range(5)).title() + ''.join(
                random.choice(string.digits) for _ in range(13)),
            'published_date': datetime.datetime.utcnow().strftime('%Y-%m-%d'),
            'isbn': ''.join(random.choice(string.digits) for _ in range(13)),
            'pages': random.randint(50, 1000)
        }
        response = api_client.post(reverse('book_update', args=[create_book.id]), data=data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert b'Only letters are allowed.' in response.content


class TestBooksView:

    @pytest.mark.django_db
    def test_create_book_valid_data(self, api_client, create_book):
        data = {
            'title': ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 100))).title(),
            'author': ''.join(random.choice(string.ascii_letters) for _ in range(5)).title() + ''.join(
                random.choice(string.ascii_letters) for _ in range(10)).title(),
            'published_date': datetime.datetime.utcnow().strftime('%Y-%m-%d'),
            'isbn': ''.join(random.choice(string.digits) for _ in range(13)),
            'pages': random.randint(50, 1000)
        }
        response = api_client.post(reverse('add_book'), data=data, format='json')
        assert response.status_code == status.HTTP_200_OK
        response_1 = api_client.get(reverse('list_books'), format='json')
        assert response_1.status_code == status.HTTP_200_OK
        assert len(response_1.data['book_list']) == 2
