from datetime import datetime

from django.http import Http404
from django.http import JsonResponse
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import OpenApiExample
from drf_spectacular.utils import OpenApiParameter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

import core.models
from portfolio.models import PortfolioStock
from stocks.models import Stock
from stocks.models import StockData
import stocks.serializers

__all__ = []


class MarketView(APIView):
    """Market view"""

    authentication_classes = []

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="q",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Parameter for entering query",
                examples=[
                    OpenApiExample(
                        "Example 1",
                        summary="Yandex short name",
                        description="Yandex shortname not cutted",
                        value="Yandex",
                    ),
                    OpenApiExample(
                        "Example 2",
                        summary="Yandex ticker",
                        description="Yandex ticker not cutted",
                        value="YNDX",
                    ),
                    OpenApiExample(
                        "Example 3",
                        summary="Yandex ticker cutted",
                        description="Yandex ticker cutted",
                        value="YN",
                    ),
                ],
            ),
        ],
        responses={200: stocks.serializers.StockSerializer(many=True)},
    )
    def get(self, request):
        """Method for getting list of stocks
        relevant for data in `q` parameter"""
        search_stock = request.GET.get("q", None)
        stocks_data = Stock.objects.search_for_stock(search_stock)
        serializer = stocks.serializers.StockSerializer(
            stocks_data.values(), many=True
        )
        return JsonResponse(serializer.data, safe=False)


class MarketDetailView(APIView):
    """Market view"""

    permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(
        responses={200: stocks.serializers.StockSerializer(), 404: None},
    )
    def get(self, request, ticker=None):
        """Method for getting stock data by `ticker` parameter"""
        stock = Stock.objects.get_stock_by_ticker(ticker)
        if stock is None:
            raise Http404()
        serializer = stocks.serializers.StockSerializer(stock)
        data = serializer.data
        if isinstance(request.user, core.models.User):
            volume_of_stocks = PortfolioStock.objects.get_number_of_stocks(
                request.user, stock
            )
            data["volume"] = volume_of_stocks
        return JsonResponse(data)


class StocksDetailView(APIView):
    """Market view"""

    authentication_classes = []
    serializer_class = stocks.serializers.MarketDetailSerializer

    @extend_schema(
        responses={200: stocks.serializers.StockDataSerializer(many=True)}
    )
    def post(self, request, ticker):
        """Endpoint for getting candles of stock"""
        stock = Stock.objects.get_stock_by_ticker(ticker)
        if stock is None:
            raise Http404()
        serializer = stocks.serializers.MarketDetailSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=False)
        data = serializer.validated_data
        candles = StockData.objects.get_candles(
            ticker,
            data.get("from_date"),
            data.get("till_date", datetime.now()),
            data.get("interval"),
            data.get("max_candles"),
        )
        candles_serializer = stocks.serializers.StockDataSerializer(
            candles,
            many=True,
        )
        return JsonResponse(candles_serializer.data, safe=False)


class PingView(APIView):
    """Ping view for getting new info"""

    authentication_classes = []
    serializer_class = stocks.serializers.PingSerializer

    @extend_schema(
        responses={200: stocks.serializers.StockDataSerializer(many=True)}
    )
    def post(self, request, ticker):
        """Method for getting with ticket parameter"""
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
