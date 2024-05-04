from datetime import datetime

from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework.views import APIView

from stocks.models import Stock
from stocks.models import StockData
import stocks.serializers

__all__ = []


class MarketView(APIView):
    """Market view"""

    def get(self, request, ticker=None):
        """Get method with q parameter"""
        if ticker is None:
            search_stock = request.GET.get("q", None)
            stocks = Stock.objects.search_for_stock(search_stock)
            json_data = list(stocks.values())
            return JsonResponse(json_data, safe=False)
        stock = Stock.objects.get_stock_by_ticker(ticker)
        if stock is None:
            return JsonResponse({})
        return JsonResponse(model_to_dict(stock), safe=False)


class MarketDetailView(APIView):
    """Market view"""
    serializer_class = stocks.serializers.MarketDetailSerializer

    def post(self, request, ticker):
        """Post method with ticket parameter"""
        serializer = stocks.serializers.MarketDetailSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=False)
        data: dict = serializer.validated_data
        candles = StockData.objects.get_candles(
            ticker,
            data.get("from_date"),
            data.get("till_date", datetime.now()),
            data.get("interval"),
        )
        candles_serializer = stocks.serializers.StockDataSerializer(
            candles, many=True
        )
        return JsonResponse(candles_serializer.data, safe=False)


class PingView(APIView):
    """Ping view for getting new info"""
    serializer_class = stocks.serializers.PingSerializer

    def post(self, request, ticker):
        """Post method with ticket parameter"""
        serializer = stocks.serializers.PingSerializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        data = serializer.validated_data
        candles = StockData.objects.get_candles(
            ticker,
            data.get("from_date"),
            datetime.now(),
            data.get("interval"),
        )
        candles_serializer = stocks.serializers.StockDataSerializer(
            candles, many=True
        )
        return JsonResponse(candles_serializer.data, safe=False)
