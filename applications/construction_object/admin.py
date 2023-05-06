from django.contrib import admin
from django.contrib.auth.models import Group, User
from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin

from .models import District, Construction, ConstructionImage, Advantage, Feature, Flat, FlatImages, Year, \
    Infrastructure, Block, PriceList
from django_summernote.utils import get_attachment_model

from modeltranslation.admin import TranslationAdmin


class PriceListAdmin(admin.TabularInline):
    model = PriceList
    max_num = 6
    extra = 2


class InfrastructureAdmin(admin.TabularInline):
    model = Infrastructure
    max_num = 1


class ConstructionImageAdmin(admin.TabularInline):
    model = ConstructionImage
    max_num = 6
    extra = 2


class FeatureSummernoteAdmin(SummernoteModelAdmin, TranslationAdmin):
    summernote_fields = 'description'


class FeatureAdmin(SummernoteModelAdminMixin, admin.TabularInline):
    model = Feature
    max_num = 4
    extra = 1
    summernote_fields = ('description_ky', 'description_ru')
    exclude = ('title', 'description')


class ConstructionAdmin(SummernoteModelAdmin, TranslationAdmin):
    summernote_fields = 'description'
    inlines = [PriceListAdmin, ConstructionImageAdmin, FeatureAdmin, InfrastructureAdmin]
    list_display = ['title', 'street_address', 'construction_completion_quarter']
    list_filter = ['district', 'cost_per_square_meter', 'offer']


class FlatImagesAdmin(admin.TabularInline):
    model = FlatImages
    max_num = 6
    extra = 2


class FlatAdmin(TranslationAdmin):
    model = Flat
    list_display = ['construction', 'type', 'square_meters']
    inlines = [FlatImagesAdmin, ]


class AdvantageAdmin(TranslationAdmin):
    model = Advantage
    list_display = ['description', 'logo']


admin.site.register(Block)
admin.site.register(District)
admin.site.register(Construction, ConstructionAdmin)
admin.site.register(Advantage, AdvantageAdmin)
admin.site.register(Feature, FeatureSummernoteAdmin)
admin.site.register(Flat, FlatAdmin)
admin.site.register(Year)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(get_attachment_model())
