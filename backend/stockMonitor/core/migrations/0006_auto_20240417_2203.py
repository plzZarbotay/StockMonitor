# Generated by Django 5.0.3 on 2024-04-17 19:03
import uuid

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_auto_20240417_2203"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, null=True
            ),
        )
    ]
