from django.db import models


class History(models.Model):
    years = models.CharField(verbose_name='годы', max_length=256)
    title = models.CharField(verbose_name='заголовок', max_length=556)
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(verbose_name='картинка', upload_to='history_images', blank=True, null=True)

    def __str__(self):
        return f'{self.years} - {self.title}'

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'


class MileStone(models.Model):
    year = models.ForeignKey(History, related_name='year_milestone', on_delete=models.CASCADE)
    achievements = models.CharField(verbose_name='достижения', max_length=556)

    class Meta:
        verbose_name = 'Этап'
        verbose_name_plural = 'Этапы'
