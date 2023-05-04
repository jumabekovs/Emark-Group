from django.contrib import admin
from django_summernote.admin import SummernoteModelAdminMixin, SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin
from .models import History, MileStone


class MileStoneAdmin(SummernoteModelAdminMixin, admin.TabularInline):
    model = MileStone
    max_num = 5
    extra = 1


class HistoryAdmin(SummernoteModelAdmin, TranslationAdmin):
    summernote_fields = ('description', )
    inlines = [MileStoneAdmin]


admin.site.register(History, HistoryAdmin)