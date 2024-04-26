from django.contrib import admin
from django.urls import include
from django.urls import path

import core.urls

__all__ = []

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(core.urls)),
]
