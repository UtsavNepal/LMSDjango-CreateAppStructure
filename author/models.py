from django.db import models

class Author(models.Model):
    AuthorId = models.AutoField(primary_key=True)
    Author_Name = models.CharField(max_length=255, unique=True)
    Bio = models.TextField()

    def __str__(self):
        return self.Author_Name
