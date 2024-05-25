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
# гит ао, смз ао, орг ао, тгк-2, форвард н, ао ак туламаш, удмуртнфт,
# аско ао, дорог бж ао, оао синтезе, сумз ао, газкон ао, газ-сервис, газ-тек ао
BLACKLIST_COMPANIES = [
    "GRNT",
    "MGNZ",
    "ORUP",
    "TGKB",
    "TGKJ",
    "TUMA",
    "UDMN",
    "ACKO",
    "DGBZ",
    "SNTZ",
    "SUMZ",
    "GAZC",
    "GAZS",
    "GAZT",
    "NKSH",
    "ZVEZ",
    "ZAYM",
    "YKEN",
    "VSYD",
    "VLHZ",
    "YRSB",
    "TUZA",
    "TRMK",
    "TGKA",
    "TGKN",
    "VEON-RX",
    "YAKG",
    "VRSB",
    "VJGZ",
    "VGSB",
    "UWGN",
    "UTAR",
    "USBN",
    "URKZ",
    "UPRO",
    "UNKL",
    "UNAC",
    "UKUZ",
    "UGLD",
    "ABIO",
    "ABRD",
    "AKRN",
    "AMEZ",
    "AQUA",
    "ARSA",
    "ASSB",
    "ASTR",
    "BELU",
    "BLNG",
    "BRZL",
    "CARM",
    "BSPB",
    "CHGZ",
    "CHKZ",
    "CHMF",
    "DIAS",
    "ELFV",
    "ELTZ",
    "ENPG",
    "FESH",
    "GEMC",
    "GMKN",
    "IGST",
    "IRAO",
    "IRKT",
    "JNOS",
    "KAZT",
    "KCHE",
    "KGKC",
    "KLSB",
    "KMEZ",
    "KOGK",
    "KRKN",
    "KRSB",
    "LSNG",
    "LSRG",
    "LVHK",
    "MAGE",
    "MFGS",
    "MGKL",
    "KZOS",
    "KUZB",
    "MRKZ",
    "MRKY",
    "MRKV",
    "MRKU",
    "MRKS",
    "MRKP",
    "MRKK",
    "NKHP",
    "NKNC",
    "NLMK",
    "NMTP",
    "NNSB",
    "SNGS",
    "STSB",
    "SVAV",
    "TASB",
    "TTLK",
    "TORS",
    "TNSE",
    "VSMO",
    "TTLK",
    "MISB",
    "DVEC",
    "DZRD",
    "KBSB",
    "KLVZ",
    "KUBE",
    "LPSB",
    "MAGN",
    "CHMK",
    "CBOM",
    "AVAN",
    ""
]


@celery_app.task
def get_companies():
    """Task for getting all companies to database"""
    frame = load_companies()
    records = frame.to_dict("records")
    for record in records:
        if record["secid"].strip().upper() not in BLACKLIST_COMPANIES:
            stock = Stock(
                name=record["shortname"],
                ticker=record["secid"],
                emitent_country="RU",
                market=record["type"],
            )
            stock.save()


@celery_app.task
def delete_all_stock_data_task():
    """Task for deleting all stock data records"""
    StockData.objects.all().delete()
    PeriodicTask.objects.filter(name__contains="make periodic").delete()


def get_mytimezone_date(original_datetime):
    """Function for converting string to datetime with timezone"""
    new_datetime = datetime.strptime(
        original_datetime,
        settings.DATETIME_FORMAT,
    )
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
    tasks = PeriodicTask.objects.all()
    if not tasks.filter(name__contains=ticker):
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
        if stock is None:
            return
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
def set_tasks_task():
    """Function for setting all periodic tasks"""
    tasks = PeriodicTask.objects.all()
    for stock in Stock.objects.all():
        if not tasks.filter(name__contains=stock.ticker):
            create_task(stock.ticker)


@celery_app.task
def periodic_get_candles_task(ticker: str):
    """Task for periodic parsing candles data for last n minutes"""
    stock = Stock.objects.get_stock_by_ticker(ticker)
    if stock is None:
        return
    candles = StockData.objects.filter(stock__ticker=ticker)
    if candles.count() < 300:
        # task = PeriodicTask.objects.filter(name__contains=ticker).first()
        # task.enabled = False
        # task.save()
        stock.is_active = False
        stock.save()
        return
    stock.is_active = True
    stock.save()
    last_date = candles.order_by("-end")[0].end
    get_candles_task(ticker, from_data=last_date, make_task=False)
