from django.urls import path
from .views import BookRatingListCreateView, DoomPlayRecordListCreateView

urlpatterns = [
    path('books/<int:pk>/rating/', BookRatingListCreateView.as_view(), name='book-rating'),
    path('game/records/', DoomPlayRecordListCreateView.as_view(), name='doom-records'),
]
