from django.db import models


class Document(models.Model):
    name = models.CharField(verbose_name='название документа', max_length=256)
    document = models.CharField(verbose_name='ссылка на документ', max_length=1000)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
