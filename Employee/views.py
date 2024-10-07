from django.shortcuts import render
from .forms import AddEmployeeForm

def Add_employee_form(request):
    form = AddEmployeeForm()
    return render(request, 'Employee/Add_employee_form.html', {'form': form})
