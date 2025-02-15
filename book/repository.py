from .models import Book
from author.models import Author

class BookRepository:
    @staticmethod
    def get_all_books():
        return Book.objects.all()

    @staticmethod
    def get_book_by_id(book_id):
        return Book.objects.get(book_id=book_id)

    @staticmethod
    def create_book(title, author_id, genre, isbn, quantity):
        author = Author.objects.get(AuthorId=author_id)
        return Book.objects.create(Title=title, Author=author, Genre=genre, ISBN=isbn, Quantity=quantity)

    @staticmethod
    def update_book(book_id, title, author_id, genre, isbn, quantity):
        book = Book.objects.get(book_id=book_id)
        author = Author.objects.get(AuthorId=author_id)
        book.Title = title
        book.Author = author
        book.Genre = genre
        book.ISBN = isbn
        book.Quantity = quantity
        book.save()
        return book
