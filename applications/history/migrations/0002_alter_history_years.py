# Generated by Django 4.2 on 2023-05-11 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='years',
            field=models.CharField(max_length=256, verbose_name='год'),
        ),
    ]