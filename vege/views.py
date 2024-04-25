from django.shortcuts import render, redirect
from .models import *

def employees(request):
    if request.method == "POST":
        data = request.POST
        employee_name = data.get("employee_name")
        employee_id = data.get("employee_id")
        hours_worked=data.get("hours_worked")
        overtime_hours=data.get("overtime_hours")

        Employee.objects.create(employee_name=employee_name, employee_id=employee_id,
                                hours_worked=hours_worked
                                ,overtime_hours=overtime_hours)

        return redirect('/employee/')  # Redirect to the appropriate URL after recipe creation

    queryset = Employee.objects.all()
    context = {'employee': queryset}

    return render(request, 'employee.html',context)


def delete_employee(request, employee_id):
    queryset= Employee.objects.get(employee_id=employee_id)
    queryset.delete()
    return redirect('/employee/')
