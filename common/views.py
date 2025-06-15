from library.models import BorrowRecord  # 대출 모델명에 따라 다를 수 있음
from pybo.models import Question, Answer  # import 추가
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserForm, CharacterUpdateForm
from .models import UserProfile

# 회원가입
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            character = form.cleaned_data.get('character')
            UserProfile.objects.create(user=user, character=character)

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


@login_required
def mypage(request):
    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)

    # 캐릭터 변경 처리
    if request.method == "POST":
        form = CharacterUpdateForm(request.POST)
        if form.is_valid():
            profile.character = form.cleaned_data['character']
            profile.save()
            messages.success(request, "캐릭터가 변경되었습니다.")
            return redirect('common:mypage')
    else:
        form = CharacterUpdateForm(initial={'character': profile.character})

    # 대출 기록
    records = BorrowRecord.objects.filter(user=user).order_by('-borrow_date')

    # 사용자가 작성한 질문 및 답변
    my_questions = Question.objects.filter(author=user).order_by('-create_date')
    my_answers = Answer.objects.filter(author=user).order_by('-create_date')

    return render(request, 'common/mypage.html', {
        'form': form,
        'profile': profile,
        'records': records,
        'my_questions': my_questions,
        'my_answers': my_answers,
    })
