from portfolio import models
from stockMonitor.admin import admin

__all__ = []


class TransactionsAdmin(admin.ModelAdmin):
    """Admin model for Transactions"""

    list_display = ("name", "user_email", "volume")

    def name(self, obj):
        """Get object name"""
        return str(obj)

    def user_email(self, obj):
        """Get from object user email"""
        return obj.user.email


class NotificationsAdmin(admin.ModelAdmin):
    """Admin model for Notifications"""

    ...


class PortfolioStockAdmin(admin.ModelAdmin):
    """Admin model for PortfolioStock"""

    list_display = ("name", "volume")

    def name(self, obj):
        """Get object name"""
        return str(obj)


admin.site.register(models.Transactions, TransactionsAdmin)
admin.site.register(models.Notifications, NotificationsAdmin)
admin.site.register(models.PortfolioStock, PortfolioStockAdmin)
