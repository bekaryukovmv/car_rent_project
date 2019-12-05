from __future__ import absolute_import, unicode_literals
from celery import task
from django.core.mail import send_mail
from cars.models import Car
from django.utils.translation import gettext as _


@task
def order_created(car_pk, user_email):
    car = Car.objects.get(id=car_pk)
    subject = _('Подтверждение аренды машины %(car)s.') % {'car': car.name}
    message = _('Поздравляем Вас с успешной арендой автомобиля %(car)s %(year)s. \nС уважением, команда сайта "Аренда Авто"') % {
            'car': car.name, 'year': car.year}

    mail_sent = send_mail(subject, message, 'carrent@admin.ru', [user_email])

    return mail_sent
