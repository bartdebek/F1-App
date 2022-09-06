from django.views.generic import (
    ListView, 
    TemplateView, 
    DetailView,
)

from .models import Driver, Team


class DriversListView(ListView):
    model = Driver
    context_object_name = 'driver_list'
    template_name = 'drivers/driver_list.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class DriversDetailView(DetailView):
    model = Driver
    template_name = 'drivers/driver_detail.html'
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'


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


class TeamsListView(ListView):
    model = Team
    context_object_name = 'team_list'
    template_name = 'teams/team_list.html'

class TeamsDetailView(DetailView):
    model = Team
    template_name = 'teams/team_detail.html'
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'

    