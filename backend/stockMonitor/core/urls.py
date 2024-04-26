from django.urls import include
from django.urls import path

import authentification.urls
import stocks.urls

urlpatterns = [
    path("auth/", include(authentification.urls)),
    path("market/", include(stocks.urls)),
]
