
from django.urls import path
from customers import views

urlpatterns=[
    path("index/",views.index_page),
    path("contact/",views.contact_page)
]