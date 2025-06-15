from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CHARACTER_CHOICES

# 회원가입 폼 (캐릭터 선택 포함)
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    character = forms.ChoiceField(
        choices=CHARACTER_CHOICES,
        widget=forms.RadioSelect,
        label="캐릭터 선택"
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "character")


# 마이페이지 캐릭터 변경 폼
class CharacterUpdateForm(forms.Form):
    character = forms.ChoiceField(
        choices=CHARACTER_CHOICES,
        widget=forms.RadioSelect,
        label="캐릭터 변경"
    )
