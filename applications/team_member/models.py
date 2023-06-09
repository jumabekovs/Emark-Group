from django.db import models
from django.utils.translation import gettext_lazy as _


class JobCategoryChoices(models.TextChoices):
    board_of_directors = ('совет директоров', _('совет директоров'))
    ceo = ('правление', _('правление'))
    management = ('менеджмент', _('менеджмент'))
    investors = ('инвесторы', _('инвесторы'))
    partners = ('партнеры', _('партнеры'))


class Member(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=256)
    job_category = models.CharField(verbose_name='категория', choices=JobCategoryChoices.choices,
                                     max_length=256, blank=True, null=True)
    position = models.CharField(verbose_name='должность', max_length=256, blank=True, null=True)
    title = models.TextField(verbose_name='заголовок')
    quote = models.TextField(verbose_name='цитата')
    bio = models.TextField(verbose_name='биография', blank=True, null=True)
    photo = models.ImageField(verbose_name='фото', upload_to='team', blank=True, null=True)

    def __str__(self):
        return f'{self.name}-{self.position}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Partner(models.Model):
    company = models.CharField(verbose_name='компания', max_length=256)
    title = models.TextField(verbose_name='описание', blank=True, null=True)
    quote = models.TextField(verbose_name='цитата',  blank=True, null=True)
    bio = models.TextField(verbose_name='био', blank=True, null=True)
    photo = models.ImageField(verbose_name='фото', upload_to='team', blank=True, null=True)

    def __str__(self):
        return f'{self.company}-{self.title}'

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
