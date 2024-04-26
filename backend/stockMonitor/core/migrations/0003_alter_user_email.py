# Generated by Django 5.0.3 on 2024-04-09 18:57

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_user_managers_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=254,
                unique=True,
                verbose_name="адрес электронной почты",
            ),
        ),
    ]
