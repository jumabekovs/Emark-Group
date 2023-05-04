from django.db import models


class Configuration(models.Model):
    slug = models.SlugField(primary_key=True, unique=True, max_length=256)
    name = models.CharField(verbose_name='имя настройки', max_length=256, unique=True)
    link_video = models.CharField(verbose_name='ссылка на видео', max_length=1000, blank=True, null=True)
    header = models.TextField(null=True, blank=True)
    footer = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки'
