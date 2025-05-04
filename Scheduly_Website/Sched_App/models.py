from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

# for Calender
from .utils import first_weekday_of_month, MONTH_NAMES, WEEKDAY_NAMES

# for Event
from django.conf import settings

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

class Event(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title       = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    all_day     = models.BooleanField(default=False)
    start_date = models.DateField(null=True, blank=True)
    start_time  = models.TimeField(null=True, blank=True)
    end_date   = models.DateField(null=True, blank=True)
    end_time    = models.TimeField(null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.all_day:
            return f"{self.title} on {self.start_date} (all day)"
        return f"{self.title} from {self.start_date} {self.start_time.strftime('%H:%M')} to {self.end_date} {self.end_time.strftime('%H:%M')}"

