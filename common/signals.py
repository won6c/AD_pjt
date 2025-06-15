from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils.timezone import now
from .models import UserSession

@receiver(user_logged_in)
def detect_multiple_logins(sender, request, user, **kwargs):
    ip = get_client_ip(request)
    agent = request.META.get('HTTP_USER_AGENT', '')
    session_key = request.session.session_key

    # 현재 유저의 기존 세션들과 비교
    existing = UserSession.objects.filter(user=user)

    for session in existing:
        if session.session_key != session_key and (session.ip_address != ip or session.user_agent != agent):
            print(f"⚠️ 다중 로그인 탐지: {user.username} from {ip}")

    # 새 세션 기록 추가
    UserSession.objects.create(
        user=user,
        session_key=session_key,
        ip_address=ip,
        user_agent=agent,
        login_time=now()
    )

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
