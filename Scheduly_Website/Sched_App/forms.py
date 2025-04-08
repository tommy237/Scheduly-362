# forms.py
from django import forms
from .models import CustomUser
from django.contrib.auth import get_user_model

# class CustomUserForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password', 'email', 'first_name', 'last_name', 'date_of_birth']
#         widgets = {
#             'password': forms.PasswordInput(),  # Masks the password input
#         }
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
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'date_of_birth']
        widgets = {
            'password': forms.PasswordInput(),  # Masks the password input
        }