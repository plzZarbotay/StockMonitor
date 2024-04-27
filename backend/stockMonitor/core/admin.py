from django.contrib import admin

from core import models

__all__ = []


class UserAdmin(admin.ModelAdmin):
    """Admin for User model"""
    search_fields = ("uuid", "email")


admin.site.register(models.User, UserAdmin)
