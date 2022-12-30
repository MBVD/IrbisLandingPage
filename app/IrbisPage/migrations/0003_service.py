# Generated by Django 4.0.8 on 2022-12-30 11:45

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('IrbisPage', '0002_alter_card_options_card_consists_of_images_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Оглавление')),
                ('content', tinymce.models.HTMLField(blank=True, verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'Сервис',
                'verbose_name_plural': 'Сервисы',
            },
        ),
    ]
