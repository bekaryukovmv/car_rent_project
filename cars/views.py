from django.utils import translation
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from .models import Car


class CarCreateView(UserPassesTestMixin, CreateView):
    model = Car
    template_name = "create_car.html"
    fields = ['name', 'name_en', 'year', 'owner']
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.is_superuser


@login_required
def home(request):
    object_list = Car.free_cars.all()

    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'page': page, 'cars': cars})
