from django.contrib import admin
from .models import Book
from .models import BookNumber


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price']
    list_filter = ['is_published']
    search_fields = ['title', 'author']

admin.site.register(BookNumber)