# Generated by Django 4.2 on 2023-05-01 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction_object', '0006_construction_is_completed_construction_is_selling'),
    ]

    operations = [
        migrations.AddField(
            model_name='construction',
            name='class_obj',
            field=models.CharField(choices=[('эконом', 'эконом'), ('комфорт', 'комфорт'), ('бизнес', 'бизнес'), ('премиум', 'премиум')], default='эконом', max_length=25, verbose_name='класс'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='construction',
            name='construction_starting_year',
            field=models.DateField(blank=True, null=True, verbose_name='год начала строительства'),
        ),
        migrations.AlterField(
            model_name='construction',
            name='offer',
            field=models.CharField(blank=True, choices=[('Новый', 'Новый'), ('в процессе', 'в процессе'), ('в завершении', 'в завершении')], max_length=256, null=True, verbose_name='предложение'),
        ),
        migrations.AlterField(
            model_name='construction',
            name='selling_status',
            field=models.CharField(choices=[('в продаже', 'в продаже'), ('построено', 'построено')], default='selling', max_length=25, verbose_name='Статус'),
        ),
    ]
