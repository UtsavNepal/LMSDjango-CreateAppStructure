from rest_framework import generics,serializers

from book.repository import BookRepository
from .services import BookService
from .serializers import BookSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.exceptions import ValidationError

class BookListView(generics.ListCreateAPIView):
    queryset = BookRepository.get_all_books()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        book_data = self.request.data
        title = book_data.get("Title")
        author_id = book_data.get("AuthorId")
        genre = book_data.get("Genre")
        isbn = book_data.get("ISBN")
        quantity = book_data.get("Quantity")

        if not title or not author_id:
            raise ValidationError({"error": "Title and Author ID are required."})

        book = BookService.create_book(title, author_id, genre, isbn, quantity)
        if not book:
            raise ValidationError({"error": "Invalid Author ID. Author does not exist."})

        serializer.instance = book

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BookService.get_all_books()

    def perform_update(self, serializer):
        book_data = self.request.data
        updated_book = BookService.update_book(
            self.kwargs["pk"], 
            book_data["Title"],
            book_data.get("AuthorId"),
            book_data["Genre"],
            book_data["ISBN"],
            book_data["Quantity"],
        )
        if updated_book:
            serializer.instance = updated_book
        else:
            raise serializers.ValidationError("Invalid author ID.")

    def perform_destroy(self, instance):
        deleted = BookService.delete_book(instance.book_id)
        if not deleted:
            raise serializers.ValidationError("Book not found.")

    def perform_destroy(self, instance):
        deleted = BookService.delete_book(instance.book_id)
        if not deleted:
            raise serializers.ValidationError("Book not found.")
