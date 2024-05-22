import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

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
    )
    theme = models.CharField(choices=Themes, default=Themes.LIGHT)
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
    )
    balance = models.DecimalField(
        verbose_name="баланс пользователя",
        decimal_places=4,
        max_digits=12,
        default=10000,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = managers.UserManager()

    class Meta:
        """Meta class"""

        verbose_name = _("user")
        verbose_name_plural = _("users")
        indexes = [
            models.Index(fields=["uuid"]),
        ]

    def __str__(self):
        return self.email
