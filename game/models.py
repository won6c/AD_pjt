# game/models.py

from django.db import models
from django.contrib.auth.models import User

class DoomPlayRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.FloatField(help_text="Seconds played")
    score = models.IntegerField(default=0)  # 나중에 커스터마이즈
    created_at = models.DateTimeField(auto_now_add=True)
