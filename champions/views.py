from lib2to3.pgen2.driver import Driver
from django.shortcuts import render
from django.views.generic import ListView

from .models import Driver

# Create your views here.
class DriversListView(ListView):
    model = Driver
    context_object_name = 'driver_list'
    template_name = 'drivers/driver_list.html'