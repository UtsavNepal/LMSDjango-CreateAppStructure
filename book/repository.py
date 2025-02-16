from .models import Book
from django.core.exceptions import ObjectDoesNotExist

class BookRepository:
    @staticmethod
    def get_all_books():
        return Book.objects.all()

    @staticmethod
    def get_book_by_id(book_id):
        return Book.objects.get(id=book_id)

    @staticmethod
    def create_book(title, author, genre, isbn, quantity):
        return Book.objects.create(Title=title, Author=author, Genre=genre, ISBN=isbn, Quantity=quantity)

    @staticmethod
    def update_book(book_id, title, author, genre, isbn, quantity):
        try:
            book = Book.objects.get(book_id=book_id)
            book.Title = title
            book.Author = author
            book.Genre = genre
            book.ISBN = isbn
            book.Quantity = quantity
            book.save()
            return book
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def delete_book(book_id):
        try:
            book = Book.objects.get(book_id=book_id)
            book.delete()
            return True
        except ObjectDoesNotExist:
            return False
