# api/serializers.py
from rest_framework import serializers
from library.models import BookRating
from game.models import DoomPlayRecord

class BookRatingSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = BookRating
        fields = ['id', 'username', 'rating', 'review', 'created_at']
        read_only_fields = ['id', 'created_at', 'username']

class DoomPlayRecordSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = DoomPlayRecord
        fields = ['id', 'username', 'start_time', 'end_time', 'duration', 'score', 'created_at']
        read_only_fields = ['id', 'created_at', 'username']
