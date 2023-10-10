from django.contrib import admin
from django.urls import path
from Loan import views


urlpatterns = [
    path("Loan/",views.Amount),
]