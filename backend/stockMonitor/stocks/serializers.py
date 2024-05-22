import rest_framework.serializers

import stocks.models

__all__ = []


class MarketDetailSerializer(rest_framework.serializers.Serializer):
    """Serializer for getting candels"""

    from_date = rest_framework.serializers.DateTimeField()
    till_date = rest_framework.serializers.DateTimeField()
    interval = rest_framework.serializers.ChoiceField(choices=(5, 60, 24))
    max_candles = rest_framework.serializers.IntegerField(default=1000)


class StockSerializer(rest_framework.serializers.ModelSerializer):
    """Serializer for getting data about stocks"""

    class Meta:
        """Meta class"""

        model = stocks.models.Stock
        fields = "__all__"


class StockShortSerializer(StockSerializer):
    """Serializer for getting data about stocks(short edition)"""

    class Meta:
        """Meta class"""

        model = stocks.models.Stock
        fields = ("ticker", "name")


class StockDataSerializer(rest_framework.serializers.ModelSerializer):
    """Serializer for getting candles"""

    class Meta:
        """Meta class"""

        model = stocks.models.StockData
        exclude = ("id", "stock")


class PingSerializer(rest_framework.serializers.Serializer):
    """Serializer for getting candles by pinging"""

    from_date = rest_framework.serializers.DateTimeField()
    interval = rest_framework.serializers.ChoiceField(choices=(5, 60, 24))
