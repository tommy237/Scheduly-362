from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def makePage(name):
    template=loader.get_template(name)
    return HttpResponse(template.render())

def home_page(request):
    return makePage('home.html')

def about_page(request):
    return makePage('about.html')

def login_page(request):
    return makePage('login.html')

# Create your views here.
