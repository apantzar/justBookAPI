from rest_framework import serializers
from .models import Book, BookNumber


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']


class BookSerilizer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)

    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'publish_date',
                  'is_published', 'created_at', 'updated_at', 'cover', 'number']
