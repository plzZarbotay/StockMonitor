from stockMonitor.admin import admin
from stocks import models

__all__ = []


class StockDataAdmin(admin.ModelAdmin):
    """Admin model for StockData model."""
    
    list_display = ("stock", "begin", "end")
    search_fields = ("stock__ticker", "id")
    list_filter = ("stock", "begin", "end")


admin.site.register(models.Stock)
admin.site.register(models.StockData, StockDataAdmin)
