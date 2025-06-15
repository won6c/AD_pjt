# borrow_service.py
from django.shortcuts import get_object_or_404
from django.utils import timezone
from library.models import Book, BorrowRecord

def borrow_book(user, book_id):
    if BorrowRecord.objects.filter(book_id=book_id, user=user, is_returned=False).exists():
        raise Exception("You have already borrowed this book and haven't returned it yet.")
    BorrowRecord.objects.create(book_id=book_id, user=user)

def return_book(user, record_id):
    record = get_object_or_404(BorrowRecord, id=record_id, user=user)
    if not record.is_returned:
        record.is_returned = True
        record.return_date = timezone.now().date()
        record.save()
    return record
