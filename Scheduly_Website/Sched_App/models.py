from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# models.py

# class CustomUser(models.Model):
class CustomUser(AbstractUser):  
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Remember: store hashed passwords!
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
