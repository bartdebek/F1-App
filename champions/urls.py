from django.urls import path
from .views import (
    AboutPageView, 
    DriversListView, 
    DriversDetailView,
)


urlpatterns = [
    path('',DriversListView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('<int:pk>/',DriversDetailView.as_view(),name='driver_detail'),
]
