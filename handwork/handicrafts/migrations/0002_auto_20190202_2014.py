# Generated by Django 2.0.8 on 2019-02-02 17:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('handicrafts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainslider',
            name='text',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Основной текст'),
        ),
    ]
