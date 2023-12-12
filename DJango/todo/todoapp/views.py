from django.shortcuts import render,redirect
from .models import Todolist

# Create your views here.

def assign(req):
    data=Todolist.objects.all()
    return render(req,'todo.html',{'data':data})

def storetask(request):
    if request.method == 'POST':
        data=request.POST['task']
        data=Todolist(data=data)
        data.save()
        return redirect('/')
    
    return render(request,'todo.html')

def deletetask(req,id):
    deltask=Todolist.objects.get(id=id)
    deltask.delete()
    return redirect('/')
    
    
