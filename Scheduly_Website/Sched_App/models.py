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

# class Event(models.Model):
#     name = models.CharField(max_length=40)
#     desc = models.CharField(max_length=3000)
#     date_start = models.DateTimeField()
#     date_end = models.DateTimeField()
#     notify = models.BooleanField(default=False)
    
#     def __str__(self):
#         return f"[EVENT]:{self.name}\nBegins from: {self.date_start}\nEnds at: {self.date_end}"
    
from django.db import models
from .utils import first_weekday_of_month, MONTH_NAMES, WEEKDAY_NAMES

class CalendarMonth(models.Model):
    year  = models.PositiveIntegerField()
    month = models.PositiveSmallIntegerField(
        choices=[(i, MONTH_NAMES[i-1]) for i in range(1,13)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def first_weekday(self):
        return first_weekday_of_month(self.year, self.month)

    @property
    def weekday_name(self):
        return WEEKDAY_NAMES[self.first_weekday]

    @property
    def month_name(self):
        return MONTH_NAMES[self.month-1]

    def __str__(self):
        return f"{self.month_name} {self.year} → {self.weekday_name}"
