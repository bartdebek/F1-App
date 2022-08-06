from django.urls import path
from .views import DriversListView


urlpatterns = [
    path('',DriversListView.as_view(),name='home')
]
