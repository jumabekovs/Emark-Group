# Generated by Django 4.2 on 2023-05-01 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction_object', '0007_construction_class_obj_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='construction',
            name='class_obj',
            field=models.CharField(blank=True, choices=[('эконом', 'эконом'), ('комфорт', 'комфорт'), ('бизнес', 'бизнес'), ('премиум', 'премиум')], max_length=25, null=True, verbose_name='класс'),
        ),
    ]