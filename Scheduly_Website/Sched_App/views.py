from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

# for password reset
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.conf import settings

User = get_user_model()

def makePage(request, template_name, context=None):
    if context is None:
        context = {}
    template = loader.get_template(template_name)
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
        
    return makePage(request, "login.html")

def sign_up(request):
    return makePage(request, 'signup.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        date_of_birth = request.POST.get("date_of_birth")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        passkey = request.POST.get("passkey")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another.")
            return redirect("signup")
        
        if pass1 != passkey:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")
        
        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.date_of_birth = date_of_birth
        myuser.save()
        
        messages.success(request, "Your account has successfully been created.")
        return redirect("login")
        
    return makePage(request, "signup.html")

def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Email not found.")
            return redirect('forgot-password')

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        subject = "Password Reset"
        message = render_to_string('password_reset_email.html', {
            'user': user,
            'uid': uid,
            'token': token,
            'domain': get_current_site(request).domain,
        })

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
        return render(request, 'password_reset_done.html')

    return render(request, 'password_reset.html')

def password_reset_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been reset successfully.")
                return redirect('login')
        else:
            form = SetPasswordForm(user)
        return render(request, 'password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "The reset link is invalid or has expired.")
        return redirect('password_reset')

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("home")

def password_reset_done(request):
    return render(request, 'password_reset_done.html')

def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')
