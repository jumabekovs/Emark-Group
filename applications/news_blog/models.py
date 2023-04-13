from django.db import models
from applications.construction_object.models import Construction
from django.utils.translation import gettext_lazy as _


class PostCategoryChoice(models.TextChoices):
    NEWS_COMPANY = ('Новости компании', _('Новости компании'))
    PRESS_CENTER = ('Пресс-центр', _('Пресс-центр'))
    CONSTRUCTION_PROGRESS = ('Ход строительства', _('Ход строительства'))


class Post(models.Model):
    category = models.CharField(verbose_name='категория', max_length=20, choices=PostCategoryChoice.choices,
                                blank=True, null=True)
    title = models.CharField(verbose_name='название', max_length=256, blank=True, null=True)
    content = models.TextField(verbose_name='контент', blank=True, null=True)
    image = models.ImageField(verbose_name='картинка поста', upload_to='post_images', blank=True, null=True)
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE, verbose_name='объект',
                                     related_name='post_construction', null=True, blank=True)
    created_date = models.DateField(verbose_name='дата создания поста', auto_now_add=True)

    def __str__(self):
        return f'{self.category}-{self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_image',
                             verbose_name='пост', blank=True, null=True)
    image = models.ImageField(verbose_name='картинка поста', upload_to='post_images')
