from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.utils import timezone
import pytz

from core.parser import get_candles
from core.parser import load_companies
from stockMonitor.celery import app
from stocks.models import Stock
from stocks.models import StockData

__all__ = []


@app.task
def get_companies():
    """Task for getting all companies to database"""
    frame = load_companies()
    records = frame.to_dict("records")
    model_instances = [
        Stock(
            name=record["shortname"],
            ticker=record["secid"],
            emitent_country="RU",
            market=record["type"],
        )
        for record in records
    ]
    Stock.objects.bulk_create(model_instances)


@app.task
def delete_all_stock_data_task():
    """Task for deleting all stock data records"""
    StockData.objects.all().delete()


def get_mytimezone_date(original_datetime):
    """Function for converting string to datetime with timezone"""
    new_datetime = datetime.strptime(original_datetime, "%Y-%m-%d %H:%M:%S")
    return timezone.make_aware(new_datetime, pytz.timezone("Europe/Moscow"))


@app.task
def get_candles_task(ticker, from_data=None):
    """Task for parsing candles data for 1 year"""
    if from_data is None:
        from_data = datetime.today() - relativedelta(years=1)
    frame = get_candles(
        ticker,
        from_data,
        datetime.now(),
        1,
    )
    records = frame.to_dict("records")
    if len(records) != 0:
        yndx = Stock.objects.get(ticker=ticker)
        last_date = get_mytimezone_date(records[-1]["end"]) + relativedelta(
            seconds=1
        )
        model_instances = [
            StockData(
                stock=yndx,
                open_cost=record["open"],
                close_cost=record["close"],
                high=record["high"],
                low=record["low"],
                value=record["value"],
                volume=record["volume"],
                begin=get_mytimezone_date(record["begin"]),
                end=get_mytimezone_date(record["end"]),
            )
            for record in records
        ]
        StockData.objects.bulk_create(model_instances)
        get_candles_task.delay(ticker, last_date)


def setup_periodic_tasks():
    """Setup celery periodic tasks"""
    task_interval = 10
    for stock in Stock.objects.all():
        app.add_periodic_task(
            task_interval,
            get_candles.s(stock.ticker),
            name=f"<make periodic parsing for {stock.ticker}>",
        )
