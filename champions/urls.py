from django.urls import path
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
    path('driver/', DriversListView.as_view(), name='home'),
    path('driver/current/', DriversListCurrentView.as_view(), name='driver_current' ),
    path('driver/past/', DriversListPastView.as_view(), name='driver_past' ),
    path('about/', AboutPageView.as_view(), name='about'),
    path('driver/<uuid:uuid>/', DriversDetailView.as_view(), name='driver_detail'),
    # path('driver/<uuid:uuid>/tweets', views.tweet_list, name ='tweet_list'),

    path('team/', TeamsListView.as_view(), name='team_list'),
    path('team/current/', DriversListCurrentView.as_view(), name='team_current' ),
    path('team/past/', DriversListPastView.as_view(), name='team_past' ),
    path('team/<uuid:uuid>/', TeamsDetailView.as_view(), name='team_detail'),
]
