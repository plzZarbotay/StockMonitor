from django.urls import path

import stocks.views

__all__ = []

app_name = "stocks"

urlpatterns = [
    path("", stocks.views.MarketView.as_view()),
    path("<str:ticker>/", stocks.views.MarketView.as_view()),
    path("<str:ticker>/candles/", stocks.views.MarketDetailView.as_view()),
    path("<str:ticker>/ping/", stocks.views.PingView.as_view()),
]
