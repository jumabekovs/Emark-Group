# Generated by Django 4.2 on 2023-05-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0004_document_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='дата'),
        ),
    ]
