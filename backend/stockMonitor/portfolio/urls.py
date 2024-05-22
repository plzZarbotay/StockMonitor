from django.urls import path
import portfolio.views

__all__ = []

app_name = "portfolio"


urlpatterns = [
    path(
        "transactions/",
        portfolio.TransactionsView.as_view(),
        name="transactions",
    ),
    path(
        "portfolio/",
        portfolio.PortfolioTableView.as_view(),
        name="portfolio_table",
    ),
]
