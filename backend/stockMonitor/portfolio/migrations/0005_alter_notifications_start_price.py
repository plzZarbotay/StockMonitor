# Generated by Django 5.0.3 on 2024-05-24 22:17

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        (
            "portfolio",
            "0004_rename_watching_price_notifications_start_price_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="notifications",
            name="start_price",
            field=models.DecimalField(
                decimal_places=3,
                max_digits=10,
                verbose_name="цена начала наблюдения",
            ),
        ),
    ]
