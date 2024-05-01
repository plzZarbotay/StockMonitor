from datetime import datetime

import pandas as pd
import requests

from stocks.models import Stock

__all__ = []


def load_companies() -> pd.DataFrame:
    base_url = "https://iss.moex.com/iss/securities.json"
    params = {"start": 0, "engine": "stock", "market": "shares"}
    data = []
    while True:
        response = requests.get(base_url, params=params)
        if not response.json()["securities"]["data"]:
            break
        response = response.json()
        data += [
            {k: r[i] for i, k in enumerate(response["securities"]["columns"])}
            for r in response["securities"]["data"]
        ]
        params["start"] += 100
    companies = pd.DataFrame(data)
    companies = companies[
        (companies.is_traded == 1) & (companies.type == "common_share")
    ]
    return companies


def get_candles(
    ticker: str, from_date: datetime, till_date: datetime, interval: int
) -> pd.DataFrame:
    """Get candles data by ticker parameter"""
    url = (
        f"https://iss.moex.com/iss/engines/stock/markets/shares/"
        f"securities/{ticker}/candles.json"
    )
    if till_date is None:
        till_date = datetime.now()
    params = {
        "from": from_date.strftime("%Y-%m-%d %H:%M:%S"),
        "till": till_date.strftime("%Y-%m-%d %H:%M:%S"),
        "interval": interval,
    }
    response = requests.get(url, params=params).json()
    candles = [
        {k: r[i] for i, k in enumerate(response["candles"]["columns"])}
        for r in response["candles"]["data"]
    ]
    return pd.DataFrame(candles)


# def get_frontend_info(ticker: str):
#     t = datetime.datetime.now() - datetime.


def insert_to_database():
    """Put parsed data about companies to database"""
    records = load_companies().to_dict("records")
    model_instances = [
        Stock(
            name=record["shortname"],
            ticker=record["secid"],
            market="Stocks",
            emitent_country="RU",
        )
        for record in records
    ]
    Stock.objects.bulk_create(model_instances)
