from django.urls import path
from . import views
from .views import calendar_lookup

urlpatterns = [
    # path('', views.home, name='home-page'), 
    path('', views.login_page, name='login-page'), 
    path('about/', views.about_page, name='about-page'),
    path('home/', views.home, name='home-page'),
    path('login/', views.login_page, name='login-page'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('calendar/', views.calendar_lookup, name='calendar_lookup'),
    path('signin/', views.login_page, name='signin'),
    path('logout/', views.signout, name='logout'),
   
# Resetting password urls
    path('password-reset/', views.password_reset_request, name='password_reset'),
    path('password-reset-done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
]

