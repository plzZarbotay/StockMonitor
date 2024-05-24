from datetime import datetime
import decimal
import json

from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.core.mail import send_mail
from django_celery_beat.models import IntervalSchedule
from django_celery_beat.models import PeriodicTask
import pytz

from core.parser import get_candles
from core.parser import load_companies
from portfolio.models import Notifications
from stockMonitor import celery_app
from stocks.models import Stock
from stocks.models import StockData

__all__ = []


@celery_app.task
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


@celery_app.task
def delete_all_stock_data_task():
    """Task for deleting all stock data records"""
    StockData.objects.all().delete()
    PeriodicTask.objects.filter(name__contains="make periodic").delete()


def get_mytimezone_date(original_datetime):
    """Function for converting string to datetime with timezone"""
    new_datetime = datetime.strptime(original_datetime, "%Y-%m-%d %H:%M:%S")
    moscow = pytz.timezone("Europe/Moscow")
    return moscow.localize(new_datetime)


def create_task(ticker):
    """Function for creating a task periodic parsing"""
    schedule = IntervalSchedule.objects.filter(
        every=settings.PARSING_INTERVAL,
        period=IntervalSchedule.MINUTES,
    )
    if len(schedule) == 0:
        schedule = IntervalSchedule.objects.create(
            every=settings.PARSING_INTERVAL,
            period=IntervalSchedule.MINUTES,
        )
    else:
        schedule = schedule[0]
    PeriodicTask.objects.create(
        interval=schedule,
        name=f"<make periodic parsing for {ticker}>",
        task="core.tasks.periodic_get_candles_task",
        args=json.dumps([ticker]),
    )


@celery_app.task
def notify_users(ticker):
    """Task for notificating users about price change"""
    stock = Stock.objects.get_stock_by_ticker(ticker=ticker)
    notifications = Notifications.objects.filter(stock=stock).values(
        "start_price", "percent", "user__email"
    )
    last_price = StockData.objects.get_last_price(stock=stock)
    for notification in notifications:
        start_price, percent, email = (
            notification["start_price"],
            notification["percent"],
            notification["user__email"],
        )
        decimal.getcontext().prec = 6
        part = decimal.Decimal(percent / 100)
        if part < 1:
            part += 1
        watching_price = start_price * part
        if last_price >= watching_price:
            send_mail(
                "Notification about changing price",
                "Here is the message.",
                "from@example.com",
                [email],
                fail_silently=False,
            )


@celery_app.task
def get_candles_task(ticker, from_data=None, make_task=True):
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
        stock = Stock.objects.get_stock_by_ticker(ticker=ticker)
        last_date = get_mytimezone_date(records[-1]["end"]) + relativedelta(
            seconds=1
        )
        model_instances = [
            StockData(
                stock=stock,
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
        get_candles_task.delay(
            ticker=ticker, from_data=last_date, make_task=make_task
        )
    else:
        if make_task:
            create_task(ticker)
        else:
            notify_users.delay(ticker=ticker)


@celery_app.task
def periodic_get_candles_task(ticker: str):
    """Task for periodic parsing candles data for last n minutes"""
    last_date = (
        StockData.objects.filter(stock__ticker=ticker).order_by("-end")[0].end
    )
    get_candles_task(ticker, from_data=last_date, make_task=False)
