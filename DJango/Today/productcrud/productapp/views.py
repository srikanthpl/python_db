from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from productapp.form import ProductForm

def View(req):
    #now we need to write a logic
    if req.method=='POST':
        form=ProductForm(req.POST)
        form.save()
        return redirect("/display/")
    form=ProductForm()
    return render(req,"index.html",{'form':form})
def display(req):
    return render(req,"display.html")
def update(req):
    return render(req,"update.html")
def delete(req):
    return redirect("/display")
