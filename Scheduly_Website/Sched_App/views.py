from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# for database
from django.shortcuts import render, redirect
from .forms import CustomUserForm

def makePage(name):
    template=loader.get_template(name)
    return HttpResponse(template.render())

def home_page(request):
    return makePage('home.html')

def about_page(request):
    return makePage('about.html')

def login_page(request):
    return makePage('login.html')

# Create your views here.

# for sign up DATABASE
def signup(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the data to the corresponding MySQL table columns
            return redirect('home')
    else:
        form = CustomUserForm()
    return render(request, 'signup.html', {'form': form})
