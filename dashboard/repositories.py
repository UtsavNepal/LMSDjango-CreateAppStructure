from datetime import timedelta
from django.utils import timezone
from student.models import Student
from book.models import Book
from .models import OverdueBorrower, Transaction


class DashboardRepository:
    def __init__(self, student_model=Student, book_model=Book, transaction_model=Transaction, overdue_borrower_model=OverdueBorrower):
      
        self.Student = student_model
        self.Book = book_model
        self.Transaction = transaction_model
        self.OverdueBorrower = overdue_borrower_model

    def get_total_students(self):
        return self.Student.objects.filter(is_deleted=False).count()

    def get_total_books(self):
        return self.Book.objects.filter(is_deleted=False).count()

    def get_total_transactions(self):
        return self.Transaction.objects.filter(is_deleted=False).count()

    def get_borrowed_books_count(self):
        return self.Transaction.objects.filter(
            transaction_type='borrowed', is_deleted=False
        ).count()

    def get_returned_books_count(self):
        return self.Transaction.objects.filter(
            transaction_type='returned', is_deleted=False
        ).count()

    def get_overdue_borrowers(self):
        overdue_transactions = self.Transaction.objects.filter(
            transaction_type="borrowed",
            due_date__lt=timezone.now().date(),
        )

        overdue_borrowers = []
        for transaction in overdue_transactions:
            overdue_borrower = self.OverdueBorrower.objects.filter(
                student=transaction.student_id,
                borrowed_id=transaction.transaction_id
            ).first() 
            
            if not overdue_borrower:
                overdue_borrower = self.OverdueBorrower.objects.create(
                    student=transaction.student_id,
                    borrowed_id=transaction.transaction_id
                )
            
            overdue_borrowers.append(overdue_borrower)

        return overdue_borrowers


