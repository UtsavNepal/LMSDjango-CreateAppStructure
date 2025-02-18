from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
import uuid
from django.core.exceptions import ValidationError

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if self.model.objects.exists():
            raise ValidationError("Only one librarian can be created.")
        
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.access_token = uuid.uuid4().hex  
        user.save(using=self._db)
        return user

class UserSignup(AbstractBaseUser):
    ROLE_CHOICES = [('librarian', 'Librarian')]

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='librarian')
    access_token = models.CharField(max_length=32, unique=True, editable=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        if UserSignup.objects.exists() and not self.pk:
            raise ValidationError("Only one librarian can be created.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
