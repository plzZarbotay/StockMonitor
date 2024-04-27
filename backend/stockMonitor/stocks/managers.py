from django.db import models


__all__ = []


class StockManager(models.Manager):
    """Manager for stock model"""
    def search_for_stock(self, stock_name):
        """Search for stock by name or ticker"""
        if stock_name is None:
            return self.filter()
        q = models.Q(name__icontains=stock_name) | models.Q(
            ticker__icontains=stock_name
        )
        return self.filter(q)


class StockDataManager(models.Manager):
    """Manager for stock data model"""
    ...
