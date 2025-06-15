from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from library.models import Book, BookRating
from .serializers import BookRatingSerializer
from game.models import DoomPlayRecord
from .serializers import DoomPlayRecordSerializer

class BookRatingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookRatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        book_id = self.kwargs['pk']
        return BookRating.objects.filter(book_id=book_id)

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, book=book)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        book = get_object_or_404(Book, pk=kwargs['pk'])
        avg_rating = book.average_rating
        return Response({
            "book_id": book.id,
            "title": book.title,
            "average_rating": round(avg_rating, 2),
            "ratings": serializer.data
        })

class DoomPlayRecordListCreateView(generics.ListCreateAPIView):
    queryset = DoomPlayRecord.objects.all().order_by('-created_at')
    serializer_class = DoomPlayRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
