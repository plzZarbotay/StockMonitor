import rest_framework.serializers

from portfolio.models import Notifications
from portfolio.models import PortfolioStock
from portfolio.models import Transactions
from stocks.serializers import StockShortSerializer

__all__ = []


class TransactionsSerializer(rest_framework.serializers.ModelSerializer):
    """Serializer for Transactions model"""

    ticker = rest_framework.serializers.CharField(
        max_length=8,
    )

    class Meta:
        """Meta class"""

        model = Transactions
        fields = [
            "ticker",
            "direction",
            "volume",
        ]


class PortfolioStockSerializer(rest_framework.serializers.ModelSerializer):
    """Serializer for PortfolioStock model"""

    stock = StockShortSerializer()

    class Meta:
        """Meta class"""

        model = PortfolioStock
        fields = [
            "stock",
            "volume",
        ]


class BalanceSerializer(rest_framework.serializers.Serializer):
    """Balance serialzer"""

    balance = rest_framework.serializers.DecimalField(
        decimal_places=4,
        max_digits=12,
    )


class NotificationSerializer(rest_framework.serializers.ModelSerializer):
    """Notification serializer"""

    class Meta:
        """Meta class"""

        model = Notifications
        fields = [
            "id",
            "stock",
            "start_price",
            "percent",
            "started_at",
        ]


class SetNotificationSerializer(rest_framework.serializers.ModelSerializer):
    """Serializer for setting notification"""

    ticker = rest_framework.serializers.CharField(max_length=10)

    class Meta:
        """Meta class"""

        model = Notifications
        fields = [
            "ticker",
            "percent",
        ]
