from django.db import transaction
from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import inline_serializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import CharField
from rest_framework.views import APIView

from portfolio.enums import TranscationDirection
from portfolio.models import PortfolioStock
from portfolio.models import Transactions
import portfolio.serializers
from stocks.models import Stock
from stocks.models import StockData

__all__ = []


class TransactionsView(APIView):
    """Transactions View"""

    permission_classes = [IsAuthenticated]
    serializer_class = portfolio.serializers.TransactionsSerializer

    @extend_schema(
        responses={
            200: inline_serializer(
                name="transaction_200",
                fields={
                    "detail": CharField(),
                },
            ),
            400: inline_serializer(
                name="transaction_failed_400",
                fields={
                    "detail": CharField(),
                },
            ),
        }
    )
    @transaction.atomic
    def post(self, request):
        """Endpoint for making transactions"""
        serializer = portfolio.serializers.TransactionsSerializer(
            data=request.data
        )
        serializer.is_valid()
        data = serializer.validated_data
        stock = Stock.objects.get_stock_by_ticker(ticker=data["ticker"])
        if stock is None:
            return JsonResponse(
                {"detail": "Ticker not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        price = StockData.objects.get_last_price(stock=stock)
        user = request.user
        volume, direction = (
            data["volume"],
            data["direction"],
        )
        output = PortfolioStock.objects.execute_operation(
            user, direction, stock, price, volume
        )
        if isinstance(output, dict):
            return JsonResponse(
                output,
                status=status.HTTP_400_BAD_REQUEST,
            )
        money_amount = price * volume
        if direction == TranscationDirection.BUY:
            user.balance -= money_amount
        else:
            user.balance += money_amount
        user.save()
        Transactions.objects.create(
            user=user,
            stock=stock,
            purchase_price=price,
            volume=data["volume"],
            direction=direction,
        )
        return JsonResponse(
            {"detail": "Successful operation"}, status=status.HTTP_200_OK
        )


class OwnedStocksView(APIView):
    """OwnedStocksView"""

    permission_classes = [IsAuthenticated]
    serializer_class = portfolio.serializers.PortfolioStockSerializer

    def get(self, request):
        """Endpoint which returns portfolio of user"""
        data = PortfolioStock.objects.get_portfolio_by_user(user=request.user)
        return JsonResponse(
            portfolio.serializers.PortfolioStockSerializer(
                data, many=True
            ).data,
            safe=False,
        )


class BalanceView(APIView):
    """Balance view"""

    permission_classes = [IsAuthenticated]
    serializer_class = portfolio.serializers.BalanceSerializer

    def get(self, request):
        """Endpoint for getting user balance"""
        return JsonResponse(
            portfolio.serializers.BalanceSerializer(request.user).data
        )
