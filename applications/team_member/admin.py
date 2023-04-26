from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin

from .models import Member


class MemberAdmin(SummernoteModelAdmin, TranslationAdmin):
    summernote_fields = ('bio', 'title', 'quote')


admin.site.register(Member, MemberAdmin)
