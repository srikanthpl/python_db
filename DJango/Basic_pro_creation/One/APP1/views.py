from django.shortcuts import render

# Create your views here.


def index(req):
    customer={"Cid":101,"Cname":"Surya","Cnum":9870653430}
    return render(req,"index.html",context=customer)
    