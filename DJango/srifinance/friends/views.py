from django.shortcuts import render

# Create your views h

def index_page(req):
    return render(req,"friends/index.html")
def contact_page(req):
    return render(req,"friends/contact.html")
