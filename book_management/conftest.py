import datetime
import pytest
import random
import string
from rest_framework.test import APIClient

from management.models import Books


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture(scope='function')
def create_book():
    book = Books.objects.create(
        title=''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 100))).title(),
        author=''.join(random.choice(string.ascii_letters) for _ in range(5)).title() + ''.join(
            random.choice(string.ascii_letters) for _ in range(10)).title(),
        published_date=datetime.datetime.utcnow(),
        isbn=''.join(random.choice(string.digits) for _ in range(13)),
        pages=random.randint(50, 1000)
    )

    return book
