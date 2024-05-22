from django.db import models
from django.conf import settings
from stocks.models import Stock


class Portfolio(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    purchase_price = models.DecimalField(
        verbose_name="цена покупки",
        decimal_places=3,
        max_digits=10,
    )
    volume = models.PositiveIntegerField(default=0)
    purchase_date = models.DateField(auto_now_add=True)


class Notifications(models.Model):
    """Table, stores notification about price changes, setted by user"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    watching_price = models.DecimalField(
        verbose_name="цена для наблюдения",
        decimal_places=3,
        max_digits=10,
    )
    started_at = models.DateTimeField(auto_now_add=True)
