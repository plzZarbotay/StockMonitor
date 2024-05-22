from django.urls import include
from django.urls import path
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from core.views import GetNameView, SetNameView

import authentification.urls
import core.views
import stocks.urls

urlpatterns = [
    path("auth/", include(authentification.urls)),
    path("market/", include(stocks.urls)),
    path(
        "get_site_name",
        core.views.GetNameView.as_view(),
        name="get_site_name",
    ),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="schema-ui",
    ),
    path("get-username/", GetNameView.as_view(), name="get-username"),
    path("set-username/", SetNameView.as_view(), name="set-username"),
]
