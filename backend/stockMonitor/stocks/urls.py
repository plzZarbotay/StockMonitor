from django.urls import path

import stocks.views

__all__ = []

app_name = "stocks"

urlpatterns = [
    path("", stocks.views.MarketView.as_view()),
]
