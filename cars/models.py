from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
# Create your models here.

class FreeCarManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(owner=None)


class Car(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Название'))
    year = models.IntegerField(verbose_name=_('Год'))
    add_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата добавления'))
    owner = models.ForeignKey(get_user_model(), blank=True, null=True, on_delete=models.SET_NULL, related_name='cars', verbose_name=_('Владелец'))
    objects = models.Manager()
    free_cars = FreeCarManager()

    class Meta:
        ordering = ['-add_date']
        verbose_name=_('Автомобиль')
        verbose_name_plural = _('Автомобили')

    def __str__(self):
        return self.name
