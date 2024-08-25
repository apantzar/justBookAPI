from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .serializers import BookSerilizer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

