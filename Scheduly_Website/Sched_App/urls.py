from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_page, name='About [] Scheduly'),
     path('home/', views.home_page, name='Scheduly'),
      path('login/', views.login_page, name='Login [] Scheduly'),
]