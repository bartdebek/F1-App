from django.shortcuts import get_object_or_404
from django.db.models import Sum, Q
from django.views.generic import (
    ListView, 
    TemplateView, 
    DetailView,
)

from .models import Driver, SeasonResults, Team
from star_ratings.models import UserRating




class AboutPageView(TemplateView):
    template_name = 'about.html'


class DriversListView(ListView):
    model = Driver
    context_object_name = 'driver_list'
    queryset = Driver.objects.order_by('-number_of_championships','-active')
    template_name = 'drivers/driver_list.html'


class DriversDetailView(DetailView):
    model = Driver
    template_name = 'drivers/driver_detail.html'
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    queryset = Driver.objects.annotate(
        total_points=Sum('seasonresults__points')
        )

class DriversListCurrentView(ListView):
    model = Driver
    context_object_name = 'driver_list_current'
    queryset = Driver.objects.filter(active=True).order_by('last_name')
    template_name = 'drivers/driver_current.html'


class DriversListPastView(ListView):
    model = Driver
    context_object_name = 'driver_list_past'
    queryset = Driver.objects.filter(active=False)
    template_name = 'drivers/driver_past.html'


class DriverRatingsView(ListView):
    model = Driver
    queryset = Driver.objects.order_by('-ratings__average', '-number_of_championships')
    context_object_name = 'driver_list'
    template_name = 'drivers/driver_ratings.html'


class DriversClassificationView(ListView):
    model = Driver
    context_object_name = 'driver_list'
    queryset = Driver.objects.filter(active=True).annotate(
        total_points=Sum('seasonresults__points')
        ).order_by('-total_points')
    template_name = 'season/driver_classification.html'


class TeamsListView(ListView):
    model = Team
    queryset = Team.objects.order_by('-active','-number_of_championships')
    context_object_name = 'team_list'
    template_name = 'teams/team_list.html'


class TeamsDetailView(DetailView):
    model = Team
    template_name = 'teams/team_detail.html'
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    queryset = Team.objects.annotate(
        total_points=Sum('seasonresults__points')
        )


class TeamsListCurrentView(ListView):
    model = Team
    context_object_name = 'team_list'
    queryset = Team.objects.filter(active=True)
    template_name = 'teams/team_current.html'


class TeamsListPastView(ListView):
    model = Team
    context_object_name = 'team_list'
    queryset = Team.objects.filter(active=False)
    template_name = 'teams/team_past.html'


class TeamRatingsView(ListView):
    model = Team
    queryset = Team.objects.order_by('-ratings__average')
    context_object_name = 'team_list'
    template_name = 'teams/team_ratings.html'


class TeamsClassificationView(ListView):
    model = Team
    context_object_name = 'team_list'
    queryset = Team.objects.filter(active=True).annotate(
        total_points=Sum('seasonresults__points')
        ).order_by('-total_points')
    template_name = 'season/team_classification.html'


class SearchResultsListView(ListView):
    model = Driver
    context_object_name = 'driver_list'
    template_name = 'drivers/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Driver.objects.filter(
        Q(first_name__icontains=query) | 
        Q(team__name__icontains=query) |
        Q(last_name__icontains=query) |
        Q(nationality__name__icontains=query) |
        Q(team__country__name__icontains=query)
        ).distinct()

    def get_context_data(self, **kwargs):
        context = super(SearchResultsListView, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


class MyRatingsView(ListView):
    model = UserRating
    context_object_name = 'rating_list'
    template_name = 'drivers/my_ratings.html'
    def get_queryset(self):
        return UserRating.objects.select_related('rating').filter(user=self.request.user).order_by('-score')
