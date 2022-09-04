from django.urls import path
from .views import (
    AboutPageView, 
    DriversListView, 
    DriversDetailView,
    DriversListCurrentView,
    DriversListPastView,
)


urlpatterns = [
    path('', DriversListView.as_view(), name='home'),
    path('current/', DriversListCurrentView.as_view(), name='driver_current' ),
    path('past/', DriversListPastView.as_view(), name='driver_past' ),
    path('about/', AboutPageView.as_view(), name='about'),
    path('<int:pk>/', DriversDetailView.as_view(), name='driver_detail'),
]
