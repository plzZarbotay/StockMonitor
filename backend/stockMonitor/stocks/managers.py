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

    def get_stock_by_ticker(self, ticker):
        """Get one stock by ticker"""
        q = models.Q(ticker__icontains=ticker)
        try:
            stock = self.get(q)
        except (self.model.DoesNotExist, self.model.MultipleObjectsReturned):
            stock = None
        return stock


class StockDataManager(models.Manager):
    """Manager for stock data model"""

    def get_candles(
        self, ticker, from_date, till_date, interval, max_candles=1000
    ):
        """interval: 5m: 5, 60m: 60, 1d: 24, 1w: 7, 1m: 31, 1y: 4"""
        candles_by_ticker = self.get_queryset().filter(
            stock_id__ticker__exact=ticker
        )
        candles_range = candles_by_ticker.filter(
            begin__gte=from_date,
            end__lte=till_date,
        )
        match interval:
            case 5:
                q = models.Q(end__minute=0)
                for i in range(1, 13):
                    q |= models.Q(end__minute=i * 5)
                candles = candles_range.filter(q)
            case 60:
                candles = candles_range.filter(end__minute=50)
            case 24:
                candles = candles_range.filter(end__hour=23, end__minute=0)
            case _:
                return None
        if len(candles) > max_candles:
            candles = candles[:max_candles]
        return candles.order_by("end")
