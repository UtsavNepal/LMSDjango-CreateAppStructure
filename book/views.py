from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from .repository import BookRepository
from rest_framework.permissions import IsAuthenticated,AllowAny

class BookListView(generics.ListCreateAPIView):
    queryset = BookRepository.get_all_books()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    