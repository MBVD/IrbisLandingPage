# Generated by Django 4.0.8 on 2023-01-08 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IrbisPage', '0006_card_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['pk'], 'verbose_name': 'Карточка', 'verbose_name_plural': 'Карточки'},
        ),
    ]