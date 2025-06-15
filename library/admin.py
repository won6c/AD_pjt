# admin.py
from django.contrib import admin
from .models import Book, BorrowRecord, BookRating

admin.site.register(Book)
admin.site.register(BorrowRecord)
admin.site.register(BookRating)
