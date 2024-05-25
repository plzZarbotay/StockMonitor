from django.db import models

from portfolio.enums import TranscationDirection

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
