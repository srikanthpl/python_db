from django.contrib import admin
from customers.models import Employee

# Register your models here.class MemberAdmin(admin.ModelAdmin):
class MemberAdmin(admin.ModelAdmin):
    list_display = ("eno", "ename", "esal","eloc")

admin.site.register(Employee,MemberAdmin)
