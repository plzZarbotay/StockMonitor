from stockMonitor.celery import app
from stocks.models import Stock

__all__ = []


@app.task
def get_data(stock):
    """Test task"""
    stock


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    """Setup celery periodic tasks"""
    for stock in Stock.objects.all():
        sender.add_periodic_task(
            10,
            get_data.s(stock.ticker),
            name=f"<make periodic parsing for {stock.ticker}>",
        )
