from django.db import models

from portfolio.enums import TranscationDirection
from stocks.models import StockData
from core.models import User

__all__ = []


class PortfolioManager(models.Manager):
    """Manager for portfolio model"""

    def get_portfolio_by_user(self, user):
        """Function for getting all stocks from user profile"""
        q = models.Q(user=user, volume__gt=0)
        return self.filter(q)

    def execute_operation(self, user, direction, stock, cost, volume):
        """Function for executing adding/deleting stocks in user portfolio"""
        data = self.filter(user=user, stock=stock)
        if direction == TranscationDirection.BUY:
            if user.balance >= cost * volume:
                if data.count() == 0:
                    stock_data = self.create(
                        user=user, stock=stock, volume=volume
                    )
                else:
                    stock_data = data.first()
                    stock_data.volume += volume
            else:
                return {"detail": "Not enough money on balance"}
        else:
            data = self.filter(user=user, stock=stock)
            if data.count() == 0:
                return {"detail": "No stock with this ticker in portfolio"}
            stock_data = data.first()
            if volume > stock_data.volume:
                return {"detail": "Not enough stocks in portfolio"}
            stock_data.volume -= volume

        stock_data.save()
        return None

    def get_day_profit(self, user):
        """Function for getting daily profit of user's portfolio"""
        total = 0
        amount = 0
        for stock in self.get_portfolio_by_user(user):
            total += StockData.objects.get_day_change(stock.stock)
            amount += 1
        return round(total / amount, 2)

    def get_number_of_stock(self, user, stock):
        """Function for getting amount of user's distinct stock"""
        filtered_stocks = self.filter(user=user, stock=stock).first()
        if filtered_stocks is None:
            return 0
        return filtered_stocks.volume

    def get_portfolio_value(self, user):
        """Get total value of user's portfolio"""
        total = 0
        for stock in self.get_portfolio_by_user(user):
            total += StockData.objects.get_last_price(stock.stock) * self.get_number_of_stock(user, stock.stock)
        return total

    def get_user_balance(self, user):
        return User.objects.filter(user=user).balance


class NotificationManager(models.Manager):
    """Notification manager for notification model"""

    def get_active_notifications(self, user):
        """Function for getting active notifications from user portfolio"""
        return self.filter(user=user, is_active=True)

    def get_number_of_stocks(self, user, stock):
        """Function for getting amount of user's distinct stock"""
        filtered_stocks = self.filter(user=user, stock=stock).first()
        if filtered_stocks is None:
            return 0
        return filtered_stocks.volume
