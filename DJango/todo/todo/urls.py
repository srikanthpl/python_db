from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.assign),
    path('store',views.storetask),
    path('delete/<id>',views.deletetask)
]
