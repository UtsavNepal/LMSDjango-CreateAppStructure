from rest_framework import serializers
from .models import Book
from author.models import Author
from author.serializers import AuthorSerializer

class BookSerializer(serializers.ModelSerializer):
    Author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['book_id ', 'Title', 'Author', 'Genre', 'ISBN', 'Quantity']
