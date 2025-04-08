# for DATABASE
# forms.py
from django import forms
from .models import CustomUser,Event

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 
                  'password', 
                  'email', 
                  'first_name', 
                  'last_name']
        widgets = {
            'password': forms.PasswordInput(),  # Mask the password input
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name',
                  'desc',
                  "date_start",
                  'date_end',
                  'notify']
        widgets = {
            'date_start': forms.DateInput(),
            'date_end': forms.DateInput(),
        }