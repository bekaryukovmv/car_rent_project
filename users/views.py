from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _

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


@login_required
def userform_edit(request, pk):
    if pk == request.user.id:
        user_form = UserFormForEdit(instance=request.user)
        if request.method == 'POST':
            user_form = UserFormForEdit(request.POST, instance=request.user)

            if user_form.is_valid():
                user_form.save()
                return redirect('users:dashboard', pk=pk)

        return render(request, 'user_edit.html', {
            'user_form': user_form})
    else:
        raise Http404


class DeleteUser(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    template_name = 'delete_user.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        user = super(DeleteUser, self).get_object()
        if not user == self.request.user:
            raise Http404
        return user


@login_required
def add_car(request, car_pk):
    user = request.user
    car = get_object_or_404(Car, pk=car_pk)

    subject = _('Подтверждение аренды машины %(car)s.') % {'car': car.name}
    body = _('Поздравляем Вас с успешной арендой автомобиля %(car)s %(year)s. \nС уважением, команда сайта "Аренда Авто"') % {
        'car': car.name, 'year': car.year}

    if request.method == 'POST':
        car.owner = user
        car.save()
        send_mail(subject, body, 'carrent@admin.ru', [user.email])
        return redirect('users:dashboard', user.id)
    return render(request, 'add_car.html', {'car': car})
