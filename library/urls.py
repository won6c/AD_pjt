from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    # 홈 / 맵
    path('', views.map_view, name='library_home'),
    path('map/', views.map_view, name='map'),

    # 책 검색 및 상세
    path('books/search/', views.book_search_view, name='book_search'),
    path('books/<int:book_id>/', views.book_detail_view, name='book_detail'),

    # 책 대출 / 반납
    path('books/<int:book_id>/borrow/', views.borrow_book_view, name='borrow_book'),
    path('return/<int:record_id>/', views.return_book_view, name='return_book'),
    path('my-borrows/', views.my_borrows_view, name='my_borrows'),  # ✅ 복구 및 추가

    # 책 평점
    path('books/<int:book_id>/rate/', views.rate_book_view, name='rate_book'),

    # AI 추천
    path('books/ai-recommend/', views.ai_recommend_view, name='book_recommend'),

    # 리뷰 수정/삭제
    path('books/<int:book_id>/review/<int:review_id>/edit/', views.edit_review_view, name='edit_review'),
    path('books/<int:book_id>/review/<int:review_id>/delete/', views.delete_review_view, name='delete_review'),
]
