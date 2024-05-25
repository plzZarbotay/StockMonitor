from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db import models

__all__ = []


class StockManager(models.Manager):
    """Manager for stock model"""

    def search_for_stock(self, stock_name):
        """Search for stock by name or ticker"""
        stocks = self.get_traded()
        if stock_name is None:
            return stocks
        q = models.Q(name__icontains=stock_name) | models.Q(
            ticker__icontains=stock_name
        )
        return stocks.filter(q)

    def get_stock_by_ticker(self, ticker):
        """Get one stock by ticker"""
        stocks = self.get_traded()
        q = models.Q(ticker__icontains=ticker)
        try:
            stock = stocks.get(q)
        except (self.model.DoesNotExist, self.model.MultipleObjectsReturned):
            stock = None
        return stock

    def get_company_name(self, ticker):
        """Function for getting name of a company by ticker"""
        return self.filter(ticker=ticker).values()[0]["name"]

    def get_traded(self):
        """Function for getting traded stocks"""
        return self.filter(is_active=True)


class StockDataManager(models.Manager):
    """Manager for stock data model"""

    def get_candles(self, ticker, from_date, till_date, interval, max_candles):
        """interval: 5m: 5, 60m: 60, 1d: 24, 1w: 7, 1m: 31, 1y: 4"""
        candles_by_ticker = self.get_queryset().filter(
            stock__ticker__exact=ticker
        )
        candles_range = candles_by_ticker.filter(
            begin__gte=from_date,
            end__lte=till_date,
        )
        candles_range = candles_range.order_by("end")
        match interval:
            case 1:
                candles = candles_range
            case 5:
                candles = candles_range[::5]
            case 60:
                candles = candles_range[::60]
            case 24:
                candles = candles_range[::1440]
            case _:
                return None
        if len(candles) > max_candles:
            candles = candles[:max_candles]
        return candles

    def get_day_value(self, stock):
        """Function for getting day value of a stock"""
        today = datetime.now()
        today_midnight = datetime(today.year, today.month, today.day)
        candles_by_stock = self.filter(stock=stock)
        candles = candles_by_stock.filter(
            begin__gt=today_midnight,
            end__lte=datetime.now(),
        )
        return candles.aggregate(models.Sum("value", default=0))["value__sum"]

    def get_day_change(self, stock):
        """Function for getting day price change of a stock"""
        yesterday_date = datetime.now() - relativedelta(days=1)
        data = self.filter(
            stock=stock,
            end__year=yesterday_date.year,
            end__month=yesterday_date.month,
            end__day=yesterday_date.day,
        )
        if not data:
            return 0
        yesterday_price = data.latest("end").close_cost
        now_price = self.get_last_price(stock=stock)
        price_change = now_price - yesterday_price
        price_change_percent = (price_change / yesterday_price) * 100
        return round(price_change_percent, 2)

    def get_last_price(self, stock):
        """Function for getting last price of a stock"""
        return self.filter(stock=stock).latest("begin").close_cost

    def get_year_change(self, stock):
        """Function for getting year change of stock price"""
        old_date = datetime.now() - relativedelta(years=1)
        data = self.filter(
            stock=stock,
            end__year=old_date.year,
            end__month=old_date.month,
            end__day=old_date.day,
        )
        if not data:
            return 0
        old_price = data.latest("end").close_cost
        now_price = self.get_last_price(stock=stock)
        price_change = now_price - old_price
        price_change_percent = (price_change / old_price) * 100
        return round(price_change_percent, 2)
