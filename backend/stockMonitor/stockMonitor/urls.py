from django.contrib import admin
from django.urls import include
from django.urls import path

import authentification.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(authentification.urls)),
]
