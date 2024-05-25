from stockMonitor.admin import admin
from stocks import models

__all__ = []


class StockAdmin(admin.ModelAdmin):
    """Admin model for Stock model"""

    list_display = ("name", "ticker", "is_active")
    search_fields = ("name", "ticker")
    list_filter = ("name", "ticker")


class StockDataAdmin(admin.ModelAdmin):
    """Admin model for StockData model"""

    list_display = ("stock", "begin", "end")
    search_fields = ("stock__ticker", "id")
    list_filter = ("stock", "begin", "end")


admin.site.register(models.Stock, StockAdmin)
admin.site.register(models.StockData, StockDataAdmin)
