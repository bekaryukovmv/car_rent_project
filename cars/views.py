from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Car

# Create your views here.
class HomePageView(LoginRequiredMixin, ListView):
    queryset = Car.free_cars.all()
    context_object_name = 'car_list'
    paginate_by = 10
    template_name = 'home.html'
