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
    user_lang = models.CharField(max_length=2, choices=STATUS_CHOICES, default='ru', verbose_name=_('Язык'))

    def get_absolute_url(self):
        return reverse('dashboard', kwargs={'pk': self.pk})
