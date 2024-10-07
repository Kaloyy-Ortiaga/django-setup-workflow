from django.shortcuts import render
from .forms import AddEmployeeForm

def homepage(request):
    form = AddEmployeeForm()
    return render(request, 'Employee/homepage.html', {'form': form})
