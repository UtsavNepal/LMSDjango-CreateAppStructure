from django.db import models
from author.models import Author

class Book(models.Model):
    book_id  = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255, unique=True)
    Author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    Genre = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=13, unique=True)
    Quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.Title
