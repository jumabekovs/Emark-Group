from django.contrib import admin
from django.contrib.auth.models import Group, User
from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin

from .models import District, Construction, ConstructionImage, Advantage, Feature, Flat, Year
from django_summernote.utils import get_attachment_model

from modeltranslation.admin import TranslationAdmin


class ConstructionImageAdmin(admin.TabularInline):
    model = ConstructionImage
    max_num = 2
    extra = 1


class FeatureAdmin(SummernoteModelAdminMixin, admin.TabularInline):
    model = Feature
    max_num = 4
    extra = 1
    summernote_fields = 'description'


class FeatureSummernoteAdmin(SummernoteModelAdmin):
    summernote_fields = 'description'


class ConstructionAdmin(SummernoteModelAdmin, TranslationAdmin):
    summernote_fields = 'description'
    inlines = [ConstructionImageAdmin, FeatureAdmin]


class FlatAdmin(TranslationAdmin):
    model = Flat
    list_display = ['construction', 'type', 'square_meters']


admin.site.register(District)
admin.site.register(Construction, ConstructionAdmin)
admin.site.register(Advantage)
admin.site.register(Feature, FeatureSummernoteAdmin)
admin.site.register(Flat, FlatAdmin)
admin.site.register(Year)
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(get_attachment_model())
