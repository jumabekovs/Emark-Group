from modeltranslation.translator import register, TranslationOptions
from .models import Construction, Flat, Feature, Advantage


@register(Construction)
class ConstructionTranslationOptions(TranslationOptions):
    fields = ('installment', 'description')


@register(Flat)
class FlatTranslationOptions(TranslationOptions):
    fields = ('type', 'rooms', 'mortgage')


@register(Feature)
class FeatureTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Advantage)
class AdvantageTranslationOptions(TranslationOptions):
    fields = ('description',)