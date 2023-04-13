from django.db import models
from django.utils.translation import gettext_lazy as _


class JobCategoryChoices(models.TextChoices):
    board_of_directors = ('совет директоров', _('совет директоров'))
    ceo = ('генеральный директор', _('генеральный директор'))
    management = ('менеджмент', _('менеджмент'))


class Member(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=256)
    position = models.CharField(verbose_name='должность', max_length=256, blank=True, null=True)
    job_category = models.CharField(verbose_name='категория', choices=JobCategoryChoices.choices,
                                     max_length=256, blank=True, null=True)
    bio = models.TextField(verbose_name='био', blank=True, null=True)
    photo = models.ImageField(verbose_name='фото', upload_to='team', blank=True, null=True)

    def __str__(self):
        return f'{self.name}-{self.position}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
