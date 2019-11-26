from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    username = models.CharField(max_length=30, unique=False, verbose_name=_('Имя пользователя'))
    user_lang = models.CharField(max_length=2, choices=settings.LANGUAGES, blank=False, default='ru', verbose_name=_('Язык'))

    REQUIRED_FIELDS = ['email', 'user_lang']

    def get_absolute_url(self):
        return reverse('users:dashboard', kwargs={'pk': self.pk})
