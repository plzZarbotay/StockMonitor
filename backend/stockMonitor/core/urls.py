from django.urls import include
from django.urls import path
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView

import authentification.urls
import core.views
from core.views import GetUserNameView
from core.views import SetUserNameView
from core.views import ToggleUserThemeView
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
    path("get_username/", GetUserNameView.as_view(), name="get_username"),
    path("set_username/", SetUserNameView.as_view(), name="set_username"),
    path("toggle_theme/", ToggleUserThemeView.as_view(), name="toggle_theme"),
]
