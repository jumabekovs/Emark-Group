# Generated by Django 4.2 on 2023-05-15 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_blog', '0002_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('Новости компании', 'Новости компании'), ('Партнерам', 'Партнерам'), ('Ход строительства', 'Ход строительства'), ('Вакансии', 'Вакансии'), ('Инвесторам', 'Инвесторам')], max_length=20, null=True, verbose_name='категория'),
        ),
    ]
