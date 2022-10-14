from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import CustomUserCreationForm
from star_ratings.models import UserRating


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
