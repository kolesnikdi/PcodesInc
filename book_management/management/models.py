from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=100, unique=True, db_index=True)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True, db_index=True)
    pages = models.PositiveSmallIntegerField()
