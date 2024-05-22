import rest_framework.serializers

import stocks.models

__all__ = []


class MarketDetailSerializer(rest_framework.serializers.Serializer):
    """Serializer for getting candels"""

    from_date = rest_framework.serializers.DateTimeField()
    till_date = rest_framework.serializers.DateTimeField()
    interval = rest_framework.serializers.IntegerField()


class StockSerializer(rest_framework.serializers.ModelSerializer):
    """Serializer for data about stocks"""

    class Meta:
        """Meta class"""

        model = stocks.models.Stock
        fields = "__all__"


class StockDataSerializer(rest_framework.serializers.ModelSerializer):
    """Serializer for getting candles"""

    class Meta:
        """Meta class"""

        model = stocks.models.StockData
        exclude = ("id", "stock_id")


class PingSerializer(rest_framework.serializers.Serializer):
    """Serializer for getting candles by pinging"""

    from_date = rest_framework.serializers.DateTimeField()
    interval = rest_framework.serializers.IntegerField()
