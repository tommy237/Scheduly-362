from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home_page(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())

def about_page(request):
    template=loader.get_template('about.html')
    return HttpResponse(template.render())

def login_page(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())

# Create your views here.
