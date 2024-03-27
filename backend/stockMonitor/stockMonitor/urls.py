from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "oauth/", include("oauth2_provider.urls", namespace="oauth2_provider")
    ),
]
