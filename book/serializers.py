from rest_framework import serializers
from .models import Book
from author.models import Author

class BookSerializer(serializers.ModelSerializer):
    AuthorId = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source="Author", write_only=True
    )
    Author_Name = serializers.CharField(source="Author.Name", read_only=True)

    class Meta:
        model = Book
        fields = ["book_id", "Title", "AuthorId", "Author_Name", "Genre", "ISBN", "Quantity"]
