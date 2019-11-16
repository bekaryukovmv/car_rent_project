from django.contrib import admin

from modeltranslation.admin import TabbedTranslationAdmin

from .models import Car

class CarAdmin(TabbedTranslationAdmin):
    list_display = ("name", "year", "owner", "add_date",)

admin.site.register(Car, CarAdmin)
