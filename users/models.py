from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

# Create your models here.
class CustomUser(AbstractUser):
    STATUS_CHOICES = (
        ('ru', 'Русский'),
        ('en', 'English'),
    )

    email = models.EmailField(unique=True, blank=False)
    username = models.CharField(max_length=30, unique=False, verbose_name=_('Имя пользователя'))
    user_lang = models.CharField(max_length=2, choices=STATUS_CHOICES, blank=False, default='ru', verbose_name=_('Язык'))

    def get_absolute_url(self):
        return reverse('dashboard', kwargs={'pk': self.pk})
