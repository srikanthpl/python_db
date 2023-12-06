from django.shortcuts import render
from django.shortcuts import redirect

from prewed.forms import CustomerForm
# Create your views here.

def index(req):
    if req.method=="POST":
        form=CustomerForm(req.POST)
        form.save()
        return redirect("/display")
    form = CustomerForm()
    return render(req,"index.html",{"form":form})

def display(req):
    return render(req,"create.html")

def update(req):
    return render(req,"update.html")

def delete(req):
    return redirect("/display")
