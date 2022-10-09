from django.contrib.contenttypes.fields import GenericRelation
from django.shortcuts import render
from django.db.models import Avg, Count, Min, Sum
from django.views.generic import (
    ListView, 
    TemplateView, 
    DetailView,
)

from .models import Driver, Team



class DriversListView(ListView):
    model = Driver
    context_object_name = 'driver_list'
    queryset = Driver.objects.order_by('-number_of_championships')
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


class DriversCompareResultsView(TemplateView):
    template_name = 'drivers/compare_results.html'


class TeamsListView(ListView):
    model = Team
    context_object_name = 'team_list'
    template_name = 'teams/team_list.html'


class TeamsDetailView(DetailView):
    model = Team
    template_name = 'teams/team_detail.html'
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'


class DriverRatingsView(ListView):
    model = Driver
    queryset = Driver.objects.order_by('-ratings__average')
    context_object_name = 'driver_list'
    template_name = 'drivers/driver_ratings.html'


class DriversClassificationView(ListView):
    model = Driver
    context_object_name = 'driver_list'
    queryset = Driver.objects.filter(active=True).annotate(
        total_points=Sum('seasonresults__points')
        ).order_by('-total_points')
    template_name = 'season/driver_classification.html'


class TeamsClassificationView(ListView):
    model = Team
    context_object_name = 'team_list'
    queryset = Team.objects.filter(active=True).annotate(
        total_points=Sum('seasonresults__points')
        ).order_by('-total_points')
    template_name = 'season/team_classification.html'


# def season_admin_view(request):
#     if request.method == "POST":
#         form = PostRaceForm(request.POST)
#         queryset = Driver.objects.filter(active=True) 
#         context = {
#             'form':form,
#             'queryset':queryset
#             } 
#         if form.is_valid():
#             print(form.cleaned_data)
#     else:
#         form = PostRaceForm()
#         queryset = Driver.objects.filter(active=True)  
#         context = {
#             'form':form,
#             'queryset':queryset}
#     return render(request, 'season/admin_page.html', context)
