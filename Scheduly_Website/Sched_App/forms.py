# forms.py
from django import forms
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            format='%m-%d-%Y', 
            attrs={'placeholder': 'MM-DD-YYYY', 'type': 'text'}
        ),
        input_formats=['%m-%d-%Y']
    )

    class Meta:
        model = CustomUser
        fields = ['username', 
                  'password', 
                  'email', 
                  'first_name', 
                  'last_name',
                  'date_of_birth']
        widgets = {
            'password': forms.PasswordInput(),  # Masks the password input
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        # hash the password properly
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['name',
#                   'desc',
#                   "date_start",
#                   'date_end',
#                   'notify']
#         widgets = {
#             'date_start': forms.DateInput(),
#             'date_end': forms.DateInput(),
#         }

from django import forms
from .models import CalendarMonth

class CalendarForm(forms.ModelForm):
    class Meta:
        model = CalendarMonth
        fields = ['year', 'month']

# Sched_App/forms.py

from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'all_day',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date':   forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time':   forms.TimeInput(attrs={'type': 'time'}),
        }
