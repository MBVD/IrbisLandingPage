# Generated by Django 4.0.8 on 2022-12-27 17:23

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('IrbisPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'verbose_name': 'Карточка', 'verbose_name_plural': 'Карточки'},
        ),
        migrations.AddField(
            model_name='card',
            name='consists_of_images',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='pretitle',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Перед Карточкой'),
        ),
    ]
