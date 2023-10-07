from django.contrib import admin
from django.urls import path
from cakes import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("Login/",views.Login),
    path("Logout/",views.logout),
    path("contact/",views.contact)
]