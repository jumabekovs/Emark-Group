# Generated by Django 4.2 on 2023-05-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction_object', '0008_alter_construction_class_obj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='construction',
            name='selling_status',
            field=models.CharField(choices=[('в продаже', 'в продаже'), ('построено', 'построено')], default='в продаже', max_length=25, verbose_name='Статус'),
        ),
    ]
