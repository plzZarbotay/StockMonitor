from django.conf import settings
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

from portfolio.enums import TranscationDirection
from portfolio.managers import PortfolioManager
from stocks.models import Stock

__all__ = []


class PortfolioStock(models.Model):
    """Portfolio stock model"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    volume = models.PositiveIntegerField(
        verbose_name="количество акций в портфеле"
    )

    objects = PortfolioManager()

    def __str__(self):
        return f"<{self.stock.ticker} for {self.user.email}>"

    class Meta:
        verbose_name = "акция в портфеле"
        verbose_name_plural = "акции в портфеле"


class Transactions(models.Model):
    """Model for saving transactions"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    direction = models.CharField(
        verbose_name="направление транзации",
        choices=TranscationDirection,
        default=None,
    )
    purchase_price = models.DecimalField(
        verbose_name="цена валюты",
        decimal_places=3,
        max_digits=10,
    )
    volume = models.PositiveIntegerField(verbose_name="количество акций")
    purchase_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (
            f"<{TranscationDirection(self.direction).name.capitalize()}"
            f" {self.stock.ticker}>"
        )

    class Meta:
        verbose_name = "транзакция"
        verbose_name_plural = "транзакции"


class Notifications(models.Model):
    """Table, stores notification about price changes, setted by user"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    start_price = models.DecimalField(
        verbose_name="цена начала наблюдения",
        decimal_places=3,
        max_digits=10,
    )
    percent = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99999)], default=0
    )
    started_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "уведомление"
        verbose_name_plural = "уведомления"
