from django.shortcuts import redirect
from django.urls import path, include
from .views import (
    AboutPageView, 
    DriversListView, 
    DriversDetailView,
    DriversListCurrentView,
    DriversListPastView,
    TeamsListView,
    TeamsDetailView,
)


urlpatterns = [
    path('', lambda request: redirect('driver/', permanent=True)),
    path('driver/', DriversListView.as_view(), name='home'),
    path('driver/current/', DriversListCurrentView.as_view(), name='driver_current' ),
    path('driver/past/', DriversListPastView.as_view(), name='driver_past' ),
    path('about/', AboutPageView.as_view(), name='about'),
    path('driver/<int:pk>/', DriversDetailView.as_view(), name='driver_detail'),

    path('team/', TeamsListView.as_view(), name='team_list'),
    path('team/current/', DriversListCurrentView.as_view(), name='team_current' ),
    path('team/past/', DriversListPastView.as_view(), name='team_past' ),
    path('team/<int:pk>/', TeamsDetailView.as_view(), name='team_detail'),
]
