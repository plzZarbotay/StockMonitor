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

    day_change = rest_framework.serializers.DecimalField(
        max_digits=5, decimal_places=2, default=0
    )
    day_value = rest_framework.serializers.DecimalField(
        decimal_places=14, max_digits=25, default=0
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
        ]

    def to_representation(self, instance):
        day_change = stocks.models.StockData.objects.get_day_change(instance)
        day_value = stocks.models.StockData.objects.get_day_value(instance.ticker)
        representation = super().to_representation(instance)
        print(type(representation), type(instance))
        representation["day_change"] = day_change
        representation["day_value"] = day_value
        print(instance)
        return representation


class StockDataSerializer(rest_framework.serializers.ModelSerializer):
    """Serializer for getting candles"""

    class Meta:
        """Meta class"""

        model = stocks.models.StockData
        exclude = ("id", "stock")


class PingSerializer(rest_framework.serializers.Serializer):
    """Serializer for getting candles by pinging"""

    from_date = rest_framework.serializers.DateTimeField()
    interval = rest_framework.serializers.IntegerField()
