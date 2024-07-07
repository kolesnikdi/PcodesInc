import datetime
import random
import string
from django.core.management.base import BaseCommand

from management.models import Books


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


class Command(BaseCommand):
    help = 'Adds books to the database'

    def handle(self, *args, **kwargs):
        for _ in range(30):
            create_book()
        self.stdout.write(self.style.SUCCESS('Successfully added books to the database.'))
