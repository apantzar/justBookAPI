from rest_framework import serializers
from .models import Book


class BookSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'publish_date',
                  'is_published', 'created_at', 'updated_at', 'cover']
