from django.urls import path

import portfolio.views

__all__ = []

app_name = "portfolio"


urlpatterns = [
    path("make_transaction/", portfolio.views.TransactionsView.as_view()),
    path("get_owned/", portfolio.views.OwnedStocksView.as_view()),
    path("get_balance/", portfolio.views.BalanceView.as_view()),
]
