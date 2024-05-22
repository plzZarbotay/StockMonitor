from django.db import models
from datetime import datetime, timedelta

__all__ = []

import pytz


def get_mytimezone_date(original_datetime):
    """Function for converting string to datetime with timezone"""
    new_datetime = datetime.strptime(original_datetime, "%Y-%m-%d %H:%M:%S")
    moscow = pytz.timezone("Europe/Moscow")
    return moscow.localize(new_datetime)


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

    def get_company_name(self, ticker):
        return self.filter(ticker=ticker).values()[0]["name"]


class StockDataManager(models.Manager):
    """Manager for stock data model"""

    def get_candles(
        self, ticker, from_date, till_date, interval, max_candles=1000
    ):
        """interval: 5m: 5, 60m: 60, 1d: 24, 1w: 7, 1m: 31, 1y: 4"""
        candles_by_ticker = self.get_queryset().filter(
            stock__ticker__exact=ticker
        )
        candles_range = candles_by_ticker.filter(
            begin__gte=from_date,
            end__lte=till_date,
        )
        match interval:
            case 1:
                q = models.Q(end__minute=0)
                for i in range(1, 61):
                    q |= models.Q(end__minute=i)
                candles = candles_range.filter(q)
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

    def get_day_value(self, ticker):
        from_date = datetime.now().replace(hour=00, minute=00, second=00)
        # if self.annotate(models.Count()):

        candles = self.get_candles(
            ticker, from_date, datetime.now(), 1, max_candles=1440
        )
        return candles.aggregate(models.Sum("value", default=0))["value__sum"]

    def get_last_price(self, stock):
        """Function for getting last price of a stock"""
        return self.filter(stock=stock).latest("begin").close_cost

    def get_day_change(self, stock):
        yesterday_date = datetime.now() - timedelta(days=1)
        yesterday_date = get_mytimezone_date(
            yesterday_date.replace(hour=23, minute=59, second=59).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )
        yesterday_price = self.filter(
            stock=stock, end=yesterday_date
        ).values()[0]["close_cost"]
        now_price = self.get_last_price(stock=stock)
        print(yesterday_price)  # убрать при коммите
        if now_price >= yesterday_price:
            return round(now_price / yesterday_price * 100, 2) - 100
        return -round(now_price / yesterday_price * 100, 2)
