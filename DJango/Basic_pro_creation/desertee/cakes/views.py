from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Login(request):
    return HttpResponse("<h1>Login Page</h1>")

def logout(request):
    return HttpResponse("<h1>logout Page</h1>")

def contact(request):
    return HttpResponse("<h1>Contact Page</h1>")