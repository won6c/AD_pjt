# common/admin.py
from django.contrib import admin
from .models import UserSession

@admin.register(UserSession)
class UserSessionAdmin(admin.ModelAdmin):
    list_display = ['user', 'ip_address', 'user_agent', 'login_time']
    list_filter = ['user', 'ip_address', 'login_time']
