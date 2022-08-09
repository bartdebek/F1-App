from lib2to3.pgen2.driver import Driver
from django.views.generic import ListView, TemplateView

from .models import Driver

# Create your views here.
class DriversListView(ListView):
    model = Driver
    context_object_name = 'driver_list'
    template_name = 'drivers/driver_list.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'