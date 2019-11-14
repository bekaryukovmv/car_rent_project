from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Название'))
    year = models.IntegerField(verbose_name=_('Год'))
    add_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата добавления'))
    owners = models.ManyToManyField(get_user_model(), related_name='cars', verbose_name=_('Владелец'))

    class Meta:
        verbose_name=_('Автомобиль')
        verbose_name_plural = _('Автомобили')

    def __str__(self):
        return self.name
