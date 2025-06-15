from django import forms
from .models import BookRating

class BookRatingForm(forms.ModelForm):
    class Meta:
        model = BookRating
        fields = ['rating', 'review']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, '⭐' * i) for i in range(1, 6)]),
            'review': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': '리뷰 내용을 입력하세요'}),
        }
        labels = {
            'rating': '별점',
            'review': '리뷰 내용',
        }
