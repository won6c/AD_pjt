from django.db import models
from django.contrib.auth.models import User

CHARACTER_CHOICES = [
    ('char1', 'Character 1'),
    ('char2', 'Character 2'),
    ('char3', 'Character 3'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    character = models.CharField(max_length=20, choices=CHARACTER_CHOICES, default='char1')

    def __str__(self):
        return f"{self.user.username} - {self.character}"


class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.ip_address} @ {self.login_time}"
