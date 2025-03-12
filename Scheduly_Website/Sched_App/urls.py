from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_page, name='about-page'),
     path('home/', views.home_page, name='home-page'),
      path('login/', views.login_page, name='login-page'),
]