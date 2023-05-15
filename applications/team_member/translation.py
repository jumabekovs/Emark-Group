from modeltranslation.translator import register, TranslationOptions
from .models import Member, Partner


@register(Member)
class FlatTranslationOptions(TranslationOptions):
    fields = ('position', 'bio', 'title', 'quote')


@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ('title', 'bio', 'quote')
