from django.db import models

class Student(models.Model):
    student_id = models.IntegerField(primary_key=True,unique=True)
    Name = models.CharField(max_length=255)
    Email = models.EmailField(unique=True)
    ContactNumber = models.CharField(max_length=15, unique=True)
    Department = models.CharField(max_length=255)

    def __str__(self):
        return self.Name
