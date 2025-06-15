from django.shortcuts import get_object_or_404
from library.models import Book, BookRating

# services/rating_service.py
def rate_book(user, book_id, data):
    book = get_object_or_404(Book, id=book_id)
    rating_value = data.get("rating")
    review_text = data.get("review", "")

    if not rating_value:
        raise ValueError("평점을 입력하세요.")

    # ⭐ get_or_create 시 rating도 같이 전달해야 NOT NULL 위반 방지됨
    rating, created = BookRating.objects.get_or_create(
        book=book,
        user=user,
        defaults={"rating": rating_value, "review": review_text}
    )
    if not created:
        rating.rating = rating_value
        rating.review = review_text
        rating.save()


def edit_review(user, book_id, review_id, data):
    review = get_object_or_404(BookRating, id=review_id, book__id=book_id, user=user)
    for key, value in data.items():
        setattr(review, key, value)
    review.save()
    return review

def delete_review(user, book_id, review_id):
    review = get_object_or_404(BookRating, id=review_id, book__id=book_id, user=user)
    review.delete()