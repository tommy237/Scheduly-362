from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout

# for database
from django.shortcuts import render, redirect
from .forms import CustomUserForm

# def makePage(name):
#     template=loader.get_template(name)
#     return HttpResponse(template.render())

def makePage(request, template_name, context=None):
    if context is None:
        context = {}
    template = loader.get_template(template_name)
    # Notice we pass `request` as the second argument to `template.render()`
    return HttpResponse(template.render(context, request))


def home(request):
    return makePage(request, "home.html")

def about_page(request):
    return makePage(request, 'about.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, f"Welcome back, {fname}!")
            return redirect("home")
            
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('home')
        
    return makePage(request, "signin.html")

def sign_up(request):
    return makePage(request, 'signup.html')

# Create your views here.

# for sign up DATABASE
# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserForm(request.POST)
#         if form.is_valid():
#             form.save()  # Saves the data to the corresponding MySQL table columns
#             return redirect('home')
#     else:
#         form = CustomUserForm()
#     return render(request, 'signup.html', {'form': form})
#hi

def signup(request):
    
    if request.method== "POST":
        # username = request.POST.get("username")
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        passkey = request.POST.get("passkey")
        
        # Check if a username has already been created
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another.")
            return redirect("signup")
        
        if pass1 != passkey:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        
        messages.success(request, "Your account has successfully been created.")
        return redirect("login/")
        
    return makePage(request, "signup.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("home")