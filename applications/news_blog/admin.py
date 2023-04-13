from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin

from .models import Post, PostImage


class PostImageAdmin(admin.TabularInline):
    model = PostImage
    max_num = 2
    extra = 1


class PostAdmin(SummernoteModelAdmin, TranslationAdmin):
    summernote_fields = ('title', 'content', )
    inlines = [PostImageAdmin]


admin.site.register(Post, PostAdmin)
