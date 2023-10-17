
from django.urls import path
from friends import views

urlpatterns=[
    path("index/",views.index_page),
    path("contact/",views.contact_page)
]