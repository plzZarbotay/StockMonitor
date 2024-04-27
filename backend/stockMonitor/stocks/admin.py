from django.contrib import admin

from stocks import models

__all__ = []


admin.site.register(models.Stock)
