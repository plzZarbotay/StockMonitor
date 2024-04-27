from django.urls import include
from django.urls import path

import authentification.urls
import stocks.urls
import core.views

urlpatterns = [
    path("auth/", include(authentification.urls)),
    path("market/", include(stocks.urls)),
    path("get_site_name", core.views.GetNameView.as_view(), name="get_site_name"),
]
