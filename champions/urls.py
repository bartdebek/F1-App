from django.urls import path
from .views import AboutPageView, DriversListView


urlpatterns = [
    path('',DriversListView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about')
]
