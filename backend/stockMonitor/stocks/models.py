from django.db import models

from stocks.managers import StockDataManager
from stocks.managers import StockManager

__all__ = []


class Stock(models.Model):
    """Model for stock"""

    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=8, unique=True)
    description = models.TextField()
    emitent_country = models.CharField(max_length=50)
    market = models.CharField(max_length=100)

    objects = StockManager()

    def __str__(self):
        return f"<{self.name}>"

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        """Save method"""
        self.ticker = self.ticker.upper()
        super(Stock, self).save(
            force_insert, force_update, using, update_fields
        )


class StockData(models.Model):
    """Model for stock data"""

    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    open_cost = models.DecimalField(
        verbose_name="цена открытия",
        decimal_places=3,
        max_digits=10,
    )
    close_cost = models.DecimalField(
        verbose_name="цена закрытия",
        decimal_places=3,
        max_digits=10,
    )
    high = models.DecimalField(
        verbose_name="самая высокая цена",
        decimal_places=3,
        max_digits=10,
    )
    low = models.DecimalField(
        verbose_name="самая низкая цена",
        decimal_places=3,
        max_digits=10,
    )
    value = models.DecimalField(
        verbose_name="объем торгов(в деньгах)",
        decimal_places=14,
        max_digits=25,
    )
    volume = models.IntegerField(verbose_name="объем торгов(в акциях)")
    begin = models.DateTimeField(verbose_name="время открытия")
    end = models.DateTimeField(verbose_name="время закрытия")

    objects = StockDataManager()

    def __str__(self):
        return f"<StockData: {self.stock} {self.begin} {self.end}>"
