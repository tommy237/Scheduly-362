from django.urls import path
from . import views
from .views import calendar_lookup
#from django.http import HttpResponse

urlpatterns = [
    path('', views.home, name='home-page'), 
    path('about/', views.about_page, name='about-page'),
    path('home/', views.home, name='home-page'),
    path('login/', views.login_page, name='login-page'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('calendar/', views.calendar_lookup, name='calendar_lookup'),
    path('signin/', views.login_page, name='signin'),
    path('logout/', views.signout, name='logout')
]

