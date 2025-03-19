from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
     path('login', views.login_page, name='login-page'),
      path('about', views.about_page, name='about-page'),
      path('signup', views.sign_up, name='signup-page'),
]