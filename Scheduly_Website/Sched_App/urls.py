from django.urls import path
from . import views
#from django.http import HttpResponse

urlpatterns = [
    path('', views.home, name='home-page'), 
    path('about/', views.about_page, name='about-page'),
    path('home/', views.home, name='home-page'),
    path('login/', views.login_page, name='login-page'),
    path('signup/', views.sign_up, name='signup'),
    
# Resetting password urls
    path('password-reset/', views.password_reset_request, name='password_reset'),
    path('password-reset-done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
]

