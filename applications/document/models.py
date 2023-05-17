from django.db import models
from django.utils.translation import gettext_lazy as _


class DocumentCategory(models.TextChoices):
    history = ('история', _('история'))
    corporate_management = ('корпоративное управление', _('корпоративное управление'))
    for_investors = ('инвесторам', _('инвесторам'))
    for_partners = ('партнерам', _('партнерам'))
    standard_ISO = ('стандарт ISO 9001', _('стандарт ISO 9001'))


class Document(models.Model):
    category = models.CharField(verbose_name='категория', max_length=256, choices=DocumentCategory.choices)
    name = models.CharField(verbose_name='название документа', max_length=256)
    date = models.DateField(verbose_name='дата', blank=True, null=True)
    document = models.CharField(verbose_name='ссылка на документ', max_length=1000)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
