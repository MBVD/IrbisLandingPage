# Generated by Django 4.0.8 on 2023-01-08 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IrbisPage', '0007_alter_card_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'verbose_name': 'Карточка', 'verbose_name_plural': 'Карточки'},
        ),
    ]
