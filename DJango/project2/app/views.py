from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages 

# Create your views here.


def home(req):
    return render(req,'shop/index.html')
def register(req):
    return render(req,'shop/register.html')
def collections(req):
    catagory=Catagory.objects.filter(status=0)
    return render(req,'shop/collections.html',{"category":catagory})

def collectionsview(req,name):
    if(Catagory.objects.filter(name=name,status=0)):
        products=Product.objects.filter(category__name=name)
        return render(req,'shop/products/index.html',{"products":products,'category_name':name})
    else:
        messages.warning(req,"No such Catagory Found")
        return redirect('collections')
        
    
    