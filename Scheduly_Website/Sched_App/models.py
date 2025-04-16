from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

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

class Event(models.Model):
    name = models.CharField(max_length=40)
    desc = models.CharField(max_length=3000)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    notify = models.BooleanField(default=False)
    
    def __str__(self):
        return f"[EVENT]:{self.name}\nBegins from: {self.date_start}\nEnds at: {self.date_end}"
    

class Year(models.Model):
    year = 2025
    days = {
        "January":31,
        "February":29 if (year%4==0 and (year%100!=0 or year%400==0)) else 28, # Alignment with leap years
        "March":31,
        "April":30,
        "May":31,
        "June":30,
        "July":31,
        "August":31,
        "September":30,
        "October":31,
        "November":30,
        "December":31,
    }
    default_events = {
        "New Year's Day":date(year,1,1),
        "Martin Luther King's Day":date(year,1,18),
        "Valentine's Day":date(year,2,14),
        "St. Patrick's Day":date(year,3,17),
        "April Fool's Day":date(year,4,1),
        "Mother's Day":date(year,5,10),
        "Father's Day":date(year,6,15),
        "Independence Day":date(year,7,4),
        "Labor Day":date(year,9,3),
        "Patriot's Day":date(year,9,11),
        "Halloween Day":date(year,10,31),
        "Thanksgiving Day":date(year,11,28),
        "Christmas Eve":date(year,12,24),
        "Christmas Day":date(year,12,25),
        "New Year's Eve":date(year,12,31),
    }
    
    