from django.contrib.auth.models import AbstractUser
from django.db import models

from core import managers

__all__ = []


class User(AbstractUser):
    """Override default Django user model."""
    class Themes(models.TextChoices):
        """Choices for theme field"""
        LIGHT = ("LT", "light")
        DARK = ("DR", "dark")
        colorblind = ("CB", "colorblind")

    username = None
    email = models.EmailField(
        "адрес электронной почты",
        unique=True,
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    theme = models.CharField(choices=Themes, default=Themes.LIGHT)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = managers.UserManager()

    def __str__(self):
        return self.email
