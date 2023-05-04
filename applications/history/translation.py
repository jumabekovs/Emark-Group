from modeltranslation.translator import register, TranslationOptions
from .models import History


@register(History)
class HistoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )
