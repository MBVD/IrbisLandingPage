# Generated by Django 4.0.8 on 2023-01-07 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IrbisPage', '0003_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='for_solution',
            field=models.BooleanField(default=False),
        ),
    ]