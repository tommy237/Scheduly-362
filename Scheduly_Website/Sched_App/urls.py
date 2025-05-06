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
    path('event/new/', views.create_event, name='create_event'),
    path('event/<int:pk>/edit/', views.edit_event, name='edit_event'),
    path('event/<int:pk>/delete/', views.delete_event, name='delete_event'),
    path('signin/', views.login_page, name='signin'),
    path('logout/', views.signout, name='logout'),
   
# Resetting password urls
    path('password-reset/', views.pswr_request, name='pswr-setup'),
    path('password-reset-done/', views.pswr_done, name='pswr-done'),
    path('password-reset/<uidb64>/<token>/', views.pswr_confirm, name='pswr-confirm'),
    path('password-reset-complete/', views.pswr_complete, name='pswr-complete'),
]

