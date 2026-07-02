from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class RegisterModel(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['EMAIL_FIELD']

    def __str__(self):
        return self.username

