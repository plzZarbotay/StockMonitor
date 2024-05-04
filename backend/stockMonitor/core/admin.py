from core import models
from stockMonitor.admin import admin

__all__ = []


class UserAdmin(admin.ModelAdmin):
    """Admin for User model"""

    search_fields = ("uuid", "email")


admin.site.register(models.User, UserAdmin)
