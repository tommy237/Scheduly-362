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
import calendar
from datetime import datetime
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.conf import settings
from django.urls import reverse # This is used to reverse the url for password reset to ensure it is correct.

User = get_user_model()
from django.shortcuts import render, redirect
from .forms import CustomUserForm, PasswordResetRequestForm
from .models import CustomUser

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
    print("🔥 LOGIN POST:", request.POST.dict())

    if request.method == 'POST':
        username = request.POST['USERNAME']
        pass1 = request.POST['PASSWORD']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, f"Welcome back, {fname}!")
            # return redirect("home")
            return redirect("home-page")
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login-page')
        
    # return makePage(request, "login.html")
    return render(request, 'login.html')

def sign_up(request):
    return makePage(request, 'signup.html')

# helper function for holidays
# Sched_App/views.py
def nth_weekday_of_month(year, month, weekday, n):
    """
    Return the date of the n-th occurrence of `weekday` in the given year/month.
    weekday: Monday=0 … Sunday=6
    """
    first_wd, days_in_month = calendar.monthrange(year, month)
    # how many days from the 1st until the first desired weekday
    offset = (weekday - first_wd) % 7
    day    = 1 + offset + (n - 1) * 7
    if day <= days_in_month:
        return date(year, month, day)
    return None

from datetime import date, timedelta
import calendar
from types import SimpleNamespace

import holidays
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import CalendarForm
from .models import Event
from .utils import MONTH_NAMES, WEEKDAY_NAMES

@login_required
def home(request):
    # 1) Determine year/month
    if request.method == 'POST':
        year  = int(request.POST['year'])
        month = int(request.POST['month'])
        # delta = int(request.POST.get('delta', 0))
        # year += delta
    else:
        today = date.today()
        year, month = today.year, today.month

    # 2) Hidden-input CalendarForm
    form = CalendarForm(initial={'year': year, 'month': month})

    # 3) Build the month matrix
    cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
    month_days = cal.monthdayscalendar(year, month)

    # 4) Humanize names
    month_name  = MONTH_NAMES[month-1]
    weekday_hdr = [wd[:3] for wd in WEEKDAY_NAMES]

    # 5) Compute start/end of this month
    first_day = date(year, month, 1)
    last_day  = date(year, month, calendar.monthrange(year, month)[1])

    # 6) Fetch all user-created events overlapping this month
    qs = Event.objects.filter(
        user=request.user,
        start_date__lte=last_day,
        end_date__gte=first_day,
    )

    # 7) Paint each event on every day it covers
    events_by_day = {}
    for ev in qs:
        ev_end = ev.end_date or ev.start_date
        start  = max(ev.start_date, first_day)
        end    = min(ev_end, last_day)
        cur    = start
        while cur <= end:
            events_by_day.setdefault(cur.day, []).append(ev)
            cur += timedelta(days=1)

    # 8) Inject U.S. federal holidays
    us_hols = holidays.UnitedStates(years=year)
    for hol_date, hol_name in us_hols.items():
        if hol_date.month == month:
            placeholder = SimpleNamespace(
                id=None,
                title=hol_name,
                description='',
                all_day=True,
                start_date=hol_date,
                start_time=None,
                end_date=None,
                end_time=None,
            )
            events_by_day.setdefault(hol_date.day, []).append(placeholder)

    # ── extra "commercial" holidays ────────────────────────────────
    custom = {}
    custom[date(year, 2, 14)] = "Valentine's Day"
    custom[date(year, 3, 17)] = "St. Patrick's Day"
    custom[date(year, 4, 1)]  = "April Fool's Day"
    custom[date(year,10,31)]  = "Halloween"
    custom[date(year,12,24)]  = "Christmas Eve"
    custom[date(year,12,31)]  = "New Year's Eve"

    # Mother's Day = 2nd Sunday in May, Father's Day = 3rd Sunday in June
    mday = nth_weekday_of_month(year, 5, 6, 2)
    fday = nth_weekday_of_month(year, 6, 6, 3)
    if mday: custom[mday] = "Mother's Day"
    if fday: custom[fday] = "Father's Day"

    for hol_date, hol_name in custom.items():
        if hol_date.month == month:
            placeholder = SimpleNamespace(
                id=None,
                title=hol_name,
                description='',
                all_day=True,
                start_date=hol_date,
                start_time=None,
                end_date=None,
                end_time=None,
            )
            events_by_day.setdefault(hol_date.day, []).append(placeholder)

    # 9) Month abbreviations
    MONTH_ABBREVS = ["Jan","Feb","Mar","Apr","May","Jun",
                     "Jul","Aug","Sep","Oct","Nov","Dec"]

    return render(request, 'home.html', {
        'form':          form,
        'year':          year,
        'month':         month,
        'month_name':    month_name,
        'weekday_hdr':   weekday_hdr,
        'month_days':    month_days,
        'events_by_day': events_by_day,
        'MONTH_ABBREVS': MONTH_ABBREVS,
    })



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

from django.contrib.auth.forms import PasswordResetForm

def pswr_request(request):
    print("🏁 GOT HERE → password_reset_request:", request.method, request.path)

    if request.method == 'POST':
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = CustomUser.objects.get(email=email)
                
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))

                reset_path = reverse('password_reset_confirm', kwargs={
                    'uidb64': uid,
                    'token': token,
                })
                reset_url = request.build_absolute_uri(reset_path)

                subject = "Password Reset"
                message = render_to_string('pswr_email.html', {
                    'user': user,
                    'reset_url': reset_url,
                })

                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
                return render(request, 'pswr_done.html')
            except CustomUser.DoesNotExist:
                messages.error(request, "Email not found.")
                return redirect('password_reset')
    else:
        form = PasswordResetRequestForm()
        
    return render(request, 'pswr_request.html', {'form':form})

def pswr_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()  # Save the new password
                return redirect('password_reset_complete')  # Redirect to the password reset complete page
            else:
                print("⚠️ Form errors:", form.errors)
        else:
            form = SetPasswordForm(user)
        return render(request, 'pswr_confirm.html', {'form': form})
    else:
        messages.error(request, "The reset link is invalid or has expired.")
        return redirect('password_reset')

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


import calendar
from datetime import date
from django.shortcuts import render
from .forms import CalendarForm
from .utils import MONTH_NAMES, WEEKDAY_NAMES

def calendar_lookup(request):
    today = date.today()

    if request.method == "POST":
        form = CalendarForm(request.POST)
        if form.is_valid():
            year  = form.cleaned_data["year"]
            month = form.cleaned_data["month"]
        else:
            year, month = today.year, today.month
    else:
        # first page load: default to today
        year, month = today.year, today.month
        form = CalendarForm(initial={"year": year, "month": month})

    # build calendar matrix (weeks)
    cal         = calendar.Calendar(firstweekday=calendar.SUNDAY)
    month_days  = cal.monthdayscalendar(year, month)
    month_name  = MONTH_NAMES[month - 1]
    # abbreviate weekdays: ["Sun","Mon",…"]
    weekday_hdr = [wd[:3] for wd in WEEKDAY_NAMES]

    return render(request, "calendar_lookup.html", {
        "form":        form,
        "month_days":  month_days,
        "month_name":  month_name,
        "weekday_hdr": weekday_hdr,
        "year":        year,     # ← make sure to pass this!
    })


# Sched_App/views.py

# Sched_App/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import EventForm

@login_required
def create_event(request):
    # pre-fill date if clicked from calendar
    date_str = request.GET.get('date')
    initial  = {}
    if date_str:
        initial['start_date'] = date_str
        initial['end_date']   = date_str

    if request.method == 'POST':
        # make a mutable copy of POST so we can inject the start/end dates for all-day
        data = request.POST.copy()
        if data.get('all_day'):
            sd = data.get('single_date')
            data['start_date'] = sd
            data['end_date']   = sd
            # clear times (the form fields are blankable anyway)
            data['start_time'] = ''
            data['end_time']   = ''

        form = EventForm(data)
        if form.is_valid():
            ev = form.save(commit=False)
            ev.user = request.user
            ev.save()
            return redirect('home-page')
    else:
        form = EventForm(initial=initial)

    return render(request, 'create_event.html', {'form': form})

from django.shortcuts import get_object_or_404
from .forms import EventForm

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventForm

@login_required
def edit_event(request, pk):
    ev = get_object_or_404(Event, pk=pk, user=request.user)

    if request.method == 'POST':
        # copy POST so we can massage the data
        data = request.POST.copy()
        if data.get('all_day'):
            # if it's all day, use the single_date field for both start & end
            sd = data.get('single_date')
            data['start_date'] = sd
            data['end_date']   = sd
            # clear out times (form allows blank)
            data['start_time'] = ''
            data['end_time']   = ''

        form = EventForm(data, instance=ev)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = EventForm(instance=ev)

    return render(request, 'edit_event.html', {
        'form': form,
        'event': ev
    })


@login_required
def delete_event(request, pk):
    ev = get_object_or_404(Event, pk=pk, user=request.user)
    if request.method == 'POST':
        ev.delete()
        return redirect('home-page')
    return render(request, 'delete_event.html', {'event': ev})


def pswr_done(request):
    return render(request, 'pswr_done.html')

def pswr_complete(request):
    return render(request, 'pswr_complete.html')
