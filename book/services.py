from .repository import BookRepository
from .models import Book
from author.models import Author
from django.core.exceptions import ObjectDoesNotExist

class BookService:
    @staticmethod
    def get_all_books():
        return BookRepository.get_all_books()

    @staticmethod
    def get_book_by_id(book_id):
        try:
            return BookRepository.get_book_by_id(book_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create_book(title, author_id, genre, isbn, quantity):
        try:
            author = Author.objects.get(AuthorId=author_id) 
            return BookRepository.create_book(title, author, genre, isbn, quantity)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def update_book(book_id, title, author_id, genre, isbn, quantity):
        try:
            author = Author.objects.get(AuthorId=author_id) 
            return BookRepository.update_book(book_id, title, author, genre, isbn, quantity)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def delete_book(book_id):
        return BookRepository.delete_book(book_id)
