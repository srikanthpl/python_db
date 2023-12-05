from django.shortcuts import render
from .models import *

# Create your views here.


def home(req):
    return render(req,'shop/index.html')
def register(req):
    return render(req,'shop/register.html')
def collections(req):
    catagory=Catagory.objects.filter(status=0)
    return render(req,'shop/collections.html',{"catagory":catagory})