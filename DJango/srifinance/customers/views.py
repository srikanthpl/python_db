from django.shortcuts import render

# Create your views here.

def index_page(req):
    return render(req,"customers/index.html")
def contact_page(req):
    return render(req,"customers/contact.html")