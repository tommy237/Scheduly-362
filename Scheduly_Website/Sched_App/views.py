from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
import calendar
from datetime import datetime
from django.contrib.auth import get_user_model
User = get_user_model()
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
        username = request.POST['USERNAME']
        pass1 = request.POST['PASSWORD']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            # fname = user.first_name
            # messages.success(request, f"Welcome back, {fname}!")
            # return redirect("home")
            return redirect('dashboard') 
            
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login-page')
        
    # return makePage(request, "login.html")
    return render(request, 'login.html')

def sign_up(request):
    return makePage(request, 'signup.html')

def signup(request):
    if request.method == "POST":
        # Pull form data
        username         = request.POST.get("username")
        first_name       = request.POST.get("first_name")
        last_name        = request.POST.get("last_name")
        dob_str          = request.POST.get("date_of_birth")  # "MM/DD/YYYY"
        email            = request.POST.get("email")
        password         = request.POST.get("pass1")
        password_confirm = request.POST.get("passkey")

        # Validation
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")
        if password != password_confirm:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        # Parse the date of birth
        try:
            dob = datetime.strptime(dob_str, "%m/%d/%Y").date()
        except ValueError:
            messages.error(request, "Birthday must be in MM/DD/YYYY format.")
            return redirect("signup")

        # Create and save the new user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.first_name    = first_name
        user.last_name     = last_name
        user.date_of_birth = dob
        user.save()

        messages.success(request, "Your account has been created!")
        return redirect("login-page")

    # GET → render the signup form
    return render(request, "signup.html")

# KEEP THIS FOR NOW (USED IT FOR DEBUGGING)
# def signup(request):
    
#     if request.method== "POST":
#         print("🔥 GOT SIGNUP POST:", request.POST.dict())
#         # username = request.POST.get("username")
#         username = request.POST.get("username")
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         dob_str = request.POST.get("date_of_birth")
#         email = request.POST.get("email")
#         pass1 = request.POST.get("pass1")
#         passkey = request.POST.get("passkey")
        
#         # Check if a username has already been created
#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists. Please choose another.")
#             return redirect("signup")
        
#         if pass1 != passkey:
#             messages.error(request, "Passwords do not match.")
#             return redirect("signup")
        
#         try:
#             dob = datetime.strptime(dob_str, "%m-%d-%Y").date()
#         except (ValueError, TypeError):
#             messages.error(request, "Date of birth must be in MM-DD-YYYY format.")
#             return redirect("signup")
        
#         myuser = User.objects.create_user(username=username, email=email, password=pass1)
#         myuser.first_name = first_name
#         myuser.last_name = last_name
#         myuser.date_of_birth = dob
#         myuser.save()

        
#         messages.success(request, "Your account has successfully been created.")
#         return redirect("login")
        
#     return makePage(request, "signup.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("login-page")


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    # you can pass any context you like here
    return render(request, 'dashboard.html', {
        'user': request.user
    })


# from django.shortcuts import render
# from .forms import CalendarForm

# def calendar_lookup(request):
#     result = None
#     if request.method == 'POST':
#         form = CalendarForm(request.POST)
#         if form.is_valid():
#             cm = form.save()
#             result = {
#                 'month': cm.month_name,
#                 'year':  cm.year,
#                 'weekday': cm.weekday_name,
#             }
#     else:
#         form = CalendarForm()

#     return render(request, 'Sched_App/calendar_lookup.html', {
#         'form': form,
#         'result': result
#     })


# Sched_App/views.py
# import calendar
from django.shortcuts import render
from .forms import CalendarForm
from .utils import MONTH_NAMES, WEEKDAY_NAMES
from django.http import HttpResponse

def calendar_lookup(request):
    return HttpResponse("🏁 Calendar view is working!")
    # form        = CalendarForm(request.POST or None)
    # month_days  = None
    # month_name  = None
    # weekday_hdr = None

    # if form.is_valid():
    #     cm = form.save()
    #     year, month = cm.year, cm.month

    #     # build a Calendar that starts weeks on Sunday
    #     cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
    #     month_days = cal.monthdayscalendar(year, month)
    #     # e.g. [[0, 0, 1,2,3,4,5], [6,7,8,9,10,11,12], …]

    #     month_name  = MONTH_NAMES[month-1]
    #     weekday_hdr = WEEKDAY_NAMES  # ["Sunday","Monday",…]
    # return render(request, 'calendar_lookup.html', {
    #     'form': form,
    #     'month_days': month_days,
    #     'month_name': month_name,
    #     'weekday_hdr': weekday_hdr,
    # })
