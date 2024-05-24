from datetime import datetime

from django.conf import settings
import pandas as pd
import requests

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
            {
                k: r[i]
                for i, k in enumerate(response["securities"]["columns"])
                if k in ["secid", "shortname", "name", "is_traded", "type"]
            }
            for r in response["securities"]["data"]
        ]
        params["start"] += 100
    companies = pd.DataFrame(data)
    companies = companies[
        (companies.is_traded == 1) & (companies.type == "common_share")
    ]
    return companies


def get_candles(
    ticker: str,
    from_date: datetime,
    till_date: datetime,
    interval: int,
) -> pd.DataFrame:
    """Get candles data by ticker parameter"""
    if till_date is None:
        till_date = datetime.now()
    url = (
        f"https://iss.moex.com/iss/engines/stock/markets/shares/"
        f"securities/{ticker}/candles.json"
    )
    params = {
        "from": from_date.strftime(settings.DATETIME_FORMAT),
        "till": till_date.strftime(settings.DATETIME_FORMAT),
        "interval": interval,
    }
    response = requests.get(url, params=params).json()
    candles = [
        {k: r[i] for i, k in enumerate(response["candles"]["columns"])}
        for r in response["candles"]["data"]
    ]
    return pd.DataFrame(candles)
