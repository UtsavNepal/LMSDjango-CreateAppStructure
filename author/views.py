from rest_framework import generics
from .models import Author
from .serializers import AuthorSerializer
from .repository import AuthorRepository
from rest_framework.permissions import IsAuthenticated,AllowAny

class AuthorListView(generics.ListCreateAPIView):
    queryset = AuthorRepository.get_all_authors()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

    

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

