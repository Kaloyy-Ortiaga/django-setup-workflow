from django.urls import path
from . import views

urlpatterns = [
    path('', views.Add_employee_form, name='Add_employee_form'),
]
