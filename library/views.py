from library.services import return_book
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import BookRatingForm
from .models import Book, BookRating, BorrowRecord
from library.services import (
    borrow_book, return_book,
    rate_book, edit_review, delete_review,
    get_recommendations
)

def map_view(request):
    return render(request, "library/library_map.html")

def book_search_view(request):
    query = request.GET.get('query', '')
    field = request.GET.get('field', 'title')
    order = request.GET.get('order', 'title')

    books = Book.search_books(query, field).order_by(order)
    paginator = Paginator(books, 20)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'library/book_list.html', {
        'page_obj': page_obj,
        'query': query,
        'field': field,
        'order': order,
    })

def ai_recommend_view(request):
    query = request.GET.get('query', '').strip()
    recommended_books, base_book = get_recommendations(query)
    return render(request, 'library/ai_recommend.html', {
        'recommended_books': recommended_books,
        'base_book': base_book,
        'query': query,
    })

def book_detail_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.bookrating_set.select_related('user').order_by('-created_at')
    user_borrow = book.borrowrecord_set.filter(user=request.user, is_returned=False).first() if request.user.is_authenticated else None
    return render(request, 'library/book_detail.html', {
        'book': book,
        'reviews': reviews,
        'user_borrow': user_borrow,
    })

@login_required
def borrow_book_view(request, book_id):
    try:
        borrow_book(request.user, book_id)  # ✅ user와 book_id 순서대로 넘김
    except Exception as e:
        return render(request, 'library/error.html', {'error': str(e)})
    return redirect('library:my_borrows')


@login_required
def return_book_view(request, record_id):
    return_book(user=request.user, record_id=record_id)  # ✅ 올바른 인자 순서
    messages.success(request, "도서를 반납했습니다.")
    return redirect('library:my_borrows')

@login_required
def my_borrows_view(request):
    records = BorrowRecord.objects.filter(user=request.user).order_by('-borrow_date')
    return render(request, 'library/my_borrows.html', {'records': records})

@login_required
def rate_book_view(request, book_id):
    if request.method == "POST":
        try:
            data = request.POST
            rate_book(request.user, book_id, data)
        except Exception as e:
            return render(request, "library/error.html", {"error": str(e)})
        return redirect("library:book_detail", book_id=book_id)
    else:
        form = BookRatingForm()
        book = get_object_or_404(Book, id=book_id)
        return render(request, "library/rate_book.html", {"form": form, "book": book})


@login_required
def edit_review_view(request, book_id, review_id):
    if request.method == 'POST':
        form = BookRatingForm(request.POST)
        if form.is_valid():
            edit_review(request.user, book_id, review_id, form.cleaned_data)
            messages.success(request, "리뷰가 수정되었습니다.")
            return redirect('library:book_detail', book_id=book_id)
    else:
        review = get_object_or_404(BookRating, id=review_id)
        form = BookRatingForm(instance=review)
    return render(request, 'library/rate_book.html', {
        'form': form,
        'book': review.book,
        'edit_mode': True,
        'review_id': review.id,
    })

@login_required
def delete_review_view(request, book_id, review_id):
    if request.method == 'POST':
        delete_review(request.user, book_id, review_id)
        messages.success(request, "리뷰가 삭제되었습니다.")
        return redirect('library:book_detail', book_id=book_id)
    review = get_object_or_404(BookRating, id=review_id)
    return render(request, 'library/delete_review_confirm.html', {
        'review': review,
        'book': review.book,
    })