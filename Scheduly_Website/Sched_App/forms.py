# forms.py
from django import forms
from .models import CustomUser,Event

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
                  'last_name']
        widgets = {
            'password': forms.PasswordInput(),  # Masks the password input
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