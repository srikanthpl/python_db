from django.shortcuts import render

# Create your views here.
def money(req):
    emp={"eid":101,"ename":"Srikanth"}
    return render(req,"index.html",context=emp)
