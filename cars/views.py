from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Car

# Create your views here.
class HomePageView(LoginRequiredMixin, ListView):
    queryset = Car.free_cars.all()
    context_object_name = 'car_list'
    paginate_by = 5
    template_name = 'home.html'



class CarCreateView(UserPassesTestMixin, CreateView):
    model = Car
    template_name = "create_car.html"
    fields = ['name', 'name_en', 'year', 'owner']
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.is_superuser
