from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .serializers import BookSerilizer
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer
