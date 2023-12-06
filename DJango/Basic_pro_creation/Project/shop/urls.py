from django.urls import path
from shop import views

urlpatterns=[
    path('home',views.home),
    path('register',views.register)
]