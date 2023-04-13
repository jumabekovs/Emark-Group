from modeltranslation.translator import register, TranslationOptions
from .models import Member


@register(Member)
class FlatTranslationOptions(TranslationOptions):
    fields = ('position', 'bio', )
