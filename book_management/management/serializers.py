import re
from rest_framework import serializers
from management.models import Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'published_date', 'isbn', 'pages']

    def validate(self, data):
        """The author field should contain only letters"""
        if author := data.get('author', None):
            if not re.match(r'^[A-Za-zА-Яа-я\s]+$', author):
                raise serializers.ValidationError({"author": "Only letters are allowed."})
        return data
