# Generated by Django 5.0.3 on 2024-05-01 13:01

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("stocks", "0003_rename_close_stockdata_close_cost_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="ticker",
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
