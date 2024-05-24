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
    """Serializer for data about stocks"""

    day_change = rest_framework.serializers.DecimalField(
        max_digits=5, decimal_places=2, default=0
    )
    day_value = rest_framework.serializers.DecimalField(
        decimal_places=14, max_digits=25, default=0
    )
    last_price = rest_framework.serializers.DecimalField(
        max_digits=10, decimal_places=3, default=0
    )

    class Meta:
        """Meta class"""

        model = stocks.models.Stock
        fields = [
            "name",
            "ticker",
            "description",
            "emitent_country",
            "market",
            "day_change",
            "day_value",
            "last_price",
        ]

    def to_representation(self, instance):
        """Object instance -> Dict of primitive datatypes."""
        day_change = stocks.models.StockData.objects.get_day_change(instance)
        day_value = stocks.models.StockData.objects.get_day_value(instance)
        last_price = stocks.models.StockData.objects.get_last_price(instance)
        representation = super().to_representation(instance)
        representation["day_change"] = day_change
        representation["day_value"] = day_value
        representation["last_price"] = last_price
        return representation


class StockShortSerializer(StockSerializer):
    """Serializer for getting data about stocks(short edition)"""

    class Meta:
        """Meta class."""

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
