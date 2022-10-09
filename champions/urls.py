from django.urls import path
from .views import (
    AboutPageView, 
    DriversListView, 
    DriversDetailView,
    DriversListCurrentView,
    DriversListPastView,
    TeamsListView,
    TeamsDetailView,
    DriverRatingsView,
    DriversClassificationView,
    TeamsClassificationView,
)


urlpatterns = [
    path('driver/', DriversListView.as_view(), name='home'),
    path('driver/current/', DriversListCurrentView.as_view(), name='driver_current' ),
    path('driver/past/', DriversListPastView.as_view(), name='driver_past' ),
    # path('driver/compare/results/', DriversCompareResultsView.as_view(), name='compare_results' ),
    path('about/', AboutPageView.as_view(), name='about'),
    path('driver/<uuid:uuid>/', DriversDetailView.as_view(), name='driver_detail'),

    path('team/', TeamsListView.as_view(), name='team_list'),
    path('team/current/', DriversListCurrentView.as_view(), name='team_current' ),
    path('team/past/', DriversListPastView.as_view(), name='team_past' ),
    path('team/<uuid:uuid>/', TeamsDetailView.as_view(), name='team_detail'),

    # path('season/admin-page/', season_admin_view, name='admin_page'),
    path('driver/ratings/', DriverRatingsView.as_view(), name='driver_ratings' ),

    path('driver/season/driver-classification/', DriversClassificationView.as_view(), name='driver_classification'),
    path('driver/season/team-classification/', TeamsClassificationView.as_view(), name='team_classification'),
]
