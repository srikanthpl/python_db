from django.shortcuts import render
from customers.models import Employee
# Create your views here.
def display_Employees(request):
    #get the employee
    emp_list = Employee.objects.all()
    my_emp = {'emp_list':emp_list}
    return render(request,'index.html', context=my_emp)