from django.shortcuts import render,redirect
from app.models import Employee


def index(req):
    data=Employee.objects.all()
    return render(req,"index.html",{'data':data})

def registration(req):
    if req.method=="POST":
        name=req.POST.get('name')
        loc=req.POST.get('loc')
        sal=req.POST.get('sal')
        Edetails=Employee(Ename=name,Esal=sal,Eloc=loc)
        Edetails.save()
        print(Edetails)
        return redirect("/")
    
    return render(req,"index.html")

def update(req):
    return render(req,"update.html")