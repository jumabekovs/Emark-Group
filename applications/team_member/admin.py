from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin

from .models import Member, Partner


class MemberAdmin(SummernoteModelAdmin, TranslationAdmin):
    summernote_fields = ('bio', 'title', 'quote')
    list_display = ('name', 'job_category', 'position')


class PartnerAdmin(TranslationAdmin):
    list_display = ('company', 'title')


admin.site.register(Member, MemberAdmin)
admin.site.register(Partner, PartnerAdmin)
