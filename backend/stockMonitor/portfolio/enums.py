from django.db import models

__all__ = []


class TranscationDirection(models.TextChoices):
    """Enum class for specifying direction of transcation"""

    BUY = "B", "buy"
    SELL = "S", "sell"
