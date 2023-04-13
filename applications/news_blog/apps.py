from django.apps import AppConfig


class NewsBlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.news_blog'
    verbose_name = "Блог"