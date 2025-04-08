from django.db import models

# Create your models here.

# models.py

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Remember: store hashed passwords!
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Event(models.Model):
    name = models.CharField(max_length=40)
    desc = models.CharField(max_length=3000)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    notify = models.BooleanField(default=False)
    
    def __str__(self):
        return f"[EVENT]:{self.name}\nBegins from: {self.date_start}\nEnds at: {self.date_end}"
    
    