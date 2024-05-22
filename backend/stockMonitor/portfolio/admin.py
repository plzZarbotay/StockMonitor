from stockMonitor.admin import admin
from portfolio import models


class PortfolioAdmin(admin.ModelAdmin): ...


class NotificationsAdmin(admin.ModelAdmin): ...


admin.site.register(models.Portfolio, PortfolioAdmin)
admin.site.register(models.Notifications, NotificationsAdmin)
