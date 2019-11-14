from django.contrib import admin

from modeltranslation.admin import TabbedTranslationAdmin

from .models import Car

class CarAdmin(TabbedTranslationAdmin):
    pass

admin.site.register(Car, CarAdmin)
