# Generated by Django 4.2 on 2023-05-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction_object', '0009_alter_construction_selling_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='construction',
            name='selling_status',
            field=models.CharField(choices=[('selling', 'в продаже'), ('built', 'построено')], default='в продаже', max_length=25, verbose_name='Статус'),
        ),
    ]
