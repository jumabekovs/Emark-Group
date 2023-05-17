from django.contrib import admin
from .models import History
from modeltranslation.admin import TranslationAdmin


class HistoryAdmin(TranslationAdmin):
    model = History


admin.site.register(History, HistoryAdmin)
