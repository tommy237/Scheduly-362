from django.urls import path
from . import views
#from django.http import HttpResponse

urlpatterns = [
    path('', views.home, name='home-page'), 
    path('about/', views.about_page, name='about-page'),
    path('home/', views.home, name='home-page'),
    path('login/', views.login_page, name='login-page'),
    path('signup/', views.sign_up, name='signup'),
]

