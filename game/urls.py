from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('doom/', views.doom_embed_view, name='doom_embed'),
    path('doom/record/', views.record_doom_play, name='record_doom_play'),
]
