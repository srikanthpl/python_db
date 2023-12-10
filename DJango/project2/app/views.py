from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *
from django.contrib import messages 
from app.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout
import json
# Create your views here.


def home(req):
    return render(req,'shop/index.html')

def add_to_cart(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_qty=data['product_qty']
            product_id=data['pid']
            #print(request.user.id)
            product_status=Product.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status':'Product Already in Cart'}, status=200)
                else:
                    if product_status.quantity>=product_qty:
                        Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'Product Added to Cart'}, status=200)
                    else:
                        return JsonResponse({'status':'Product Stock Not Available'}, status=200)
        else:
            return JsonResponse({'status':'Login to Add Cart'}, status=200)
   else:
       return JsonResponse({'status':'Invalid Access'}, status=200)
        

def login_page(req):
    if req.user.is_authenticated:
        return redirect('/')
    else:
        if req.method=='POST':
            name=req.POST.get('username')
            pwd=req.POST.get('password')
            user=authenticate(req,username=name,password=pwd)
            if user is not None:
                login(req,user)
                messages.success(req,'Login in Successfully')
                return redirect('/')
            else:
                messages.error(req,'invalid User Name or Password')
                return redirect('/login')
        return render(req,'shop/login.html')

def logout_page(req):
    if req.user.is_authenticated:
        logout(req)
        messages.success(req,'Logout Out Successfully')
        return redirect('/')

def register(req):
    form=CustomUserForm()
    if req.method=='POST':
        form=CustomUserForm(req.POST)
        if (form.is_valid()):
            form.save()
            messages.success(req,'Registration Success You can Login Now...!')
            return redirect('/login')
    return render(req,'shop/register.html',{'form':form})

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
    
    
def product_details(req,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(req,'shop/products/product_detail.html',{'products':products})
        else:
            messages.error(req,'No such Catagory Found')
            return redirect('collections')
    else:
            messages.error(req,'No such Catagory Found')
            return redirect('collections')
        
    
    