from django.db import models
from student.models import Student
from book.models import Book
from datetime import timedelta

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
    ]

    transaction_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=3)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    date_of_borrowed = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    def save(self, *args, **kwargs):
        
        if not self.user_id:
            
            previous_transaction = Transaction.objects.filter(student_id=self.student_id).first()
            if previous_transaction:
                self.user_id = previous_transaction.user_id  
            else:
                
                last_user = Transaction.objects.last()
                new_user_id = str(int(last_user.user_id) + 1 if last_user else 1).zfill(3)
                self.user_id = new_user_id

       
        if not self.due_date:
            self.due_date = self.date_of_borrowed + timedelta(days=30)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Transaction {self.transaction_id} by {self.student_id.Name} - {self.transaction_type}"
