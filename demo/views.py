from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Book
def home(request):
    books = Book.objects.all()
    output = "<br/>".join([book.title for book in books])
    return HttpResponse(output)