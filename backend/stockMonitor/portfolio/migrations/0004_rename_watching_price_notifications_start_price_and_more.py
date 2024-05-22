# Generated by Django 5.0.3 on 2024-05-21 12:55

import django.core.validators
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0003_rename_amount_portfoliostock_volume"),
    ]

    operations = [
        migrations.RenameField(
            model_name="notifications",
            old_name="watching_price",
            new_name="start_price",
        ),
        migrations.AddField(
            model_name="notifications",
            name="percent",
            field=models.IntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(99999),
                ],
            ),
        ),
    ]