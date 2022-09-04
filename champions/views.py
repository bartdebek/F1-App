from lib2to3.pgen2.driver import Driver
from django.views.generic import (
    ListView, 
    TemplateView, 
    DetailView,
)

from .models import Driver


class DriversListView(ListView):
    model = Driver
    context_object_name = 'driver_list'
    template_name = 'drivers/driver_list.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class DriversDetailView(DetailView):
    model = Driver
    template_name = 'drivers/driver_detail.html'


class DriversListCurrentView(ListView):
    model = Driver
    context_object_name = 'driver_list_current'
    queryset = Driver.objects.filter(active=True)
    template_name = 'drivers/driver_current.html'


class DriversListPastView(ListView):
    model = Driver
    context_object_name = 'driver_list_past'
    queryset = Driver.objects.filter(active=False)
    template_name = 'drivers/driver_past.html'