# Generated by Django 5.0.3 on 2024-05-07 08:51

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("stocks", "0004_alter_stock_ticker"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stockdata",
            name="volume",
            field=models.PositiveIntegerField(
                verbose_name="объем торгов(в акциях)"
            ),
        ),
    ]