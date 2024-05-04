from stockMonitor.admin import admin
from stocks import models

__all__ = []


class StockDataAdmin(admin.ModelAdmin):
    """Admin model for StockData model."""
    list_display = ("stock_id", "begin", "end")
    search_fields = ("stock_id__ticker", "id")
    list_filter = ("stock_id", "begin", "end")


admin.site.register(models.Stock)
admin.site.register(models.StockData, StockDataAdmin)
