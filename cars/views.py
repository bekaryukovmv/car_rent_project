from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, redirect

from .models import Car
from .tasks import order_created

class CarCreateView(UserPassesTestMixin, CreateView):
    model = Car
    template_name = "create_car.html"
    fields = ['name_ru', 'name_en', 'year', 'owner']
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.is_superuser


class CarListView(LoginRequiredMixin, ListView):
    queryset = Car.free_cars.all()
    context_object_name = 'cars'
    paginate_by = 5
    template_name = 'home.html'


class AddCarUser(LoginRequiredMixin, UpdateView):
    model = Car
    template_name = 'user_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return render(request, 'add_car.html', {'car': self.object})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.owner = request.user
        self.object.save()
        # start async task
        order_created.delay(self.object.pk, request.user.email)
        return redirect('users:dashboard', request.user.id)
