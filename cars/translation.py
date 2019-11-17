from modeltranslation.translator import translator, TranslationOptions
from .models import Car

class CarTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(Car, CarTranslationOptions)
