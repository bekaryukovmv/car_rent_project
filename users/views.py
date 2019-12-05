from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserFormForEdit
from cars.models import Car


class UserDetail(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()
    context_object_name = 'current_user'
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data(**kwargs)
        context['cars'] = self.object.cars.all()
        return context

    def get_object(self):
        user = super(UserDetail, self).get_object()
        if not user == self.request.user:
            raise Http404
        return user


class UserUpdate(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = UserFormForEdit
    template_name = 'user_edit.html'

    def get_object(self):
        user = super(UserUpdate, self).get_object()
        if not user == self.request.user:
            raise Http404
        return user

    def get_success_url(self):
        return reverse_lazy('users:dashboard', kwargs={'pk': self.object.id})


class UserDelete(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    template_name = 'delete_user.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        user = super(UserDelete, self).get_object()
        if not user == self.request.user:
            raise Http404
        return user
