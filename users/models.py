from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class CustomUser(AbstractUser):
    user_lang = (('ru', 'Russian'), ('en', 'English'),)
    user_lang = models.CharField(max_length=2, default='ru', verbose_name=_('Язык'))
