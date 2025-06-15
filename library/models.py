# ✅ models.py (Book 확장 및 대출/평점 모델 포함)
from django.db import models
from django.db.models import Q, Avg
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    keyword = models.CharField(max_length=100)  # "판타지 액션 SF" 같은 장르/테마
    description = models.TextField(blank=True, null=True)  # 콘텐츠 기반 추천용 필드
    published_date = models.DateField()

    def __str__(self):
        return f"{self.title} ({self.author})"

    @classmethod
    def search_books(cls, query: str, field: str):
        if field == 'title':
            return cls.objects.filter(title__icontains=query)
        elif field == 'author':
            return cls.objects.filter(author__icontains=query)
        elif field == 'keyword':
            return cls.objects.filter(keyword__icontains=query)
        else:
            return cls.objects.filter(
                Q(title__icontains=query) |
                Q(author__icontains=query) |
                Q(keyword__icontains=query) |
                Q(description__icontains=query)
            )

    @classmethod
    def sort_books(cls, order: str):
        if order == 'title':
            return cls.objects.order_by('title')
        elif order == 'author':
            return cls.objects.order_by('author')
        elif order == 'date':
            return cls.objects.order_by('published_date')
        else:
            return cls.objects.all()

    @property
    def average_rating(self):
        return self.bookrating_set.aggregate(avg=Avg('rating'))['avg'] or 0

    @property
    def is_borrowed(self):
        return self.borrowrecord_set.filter(is_returned=False).exists()

class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

class BookRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()  # 1~5
    review = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')
