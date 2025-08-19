from rest_framework import serializers
from service.models.price_model import Price


class PriceListSerializer(serializers.ModelSerializer):
    """For listing prices (lightweight)."""

    service = serializers.StringRelatedField()
    product = serializers.StringRelatedField()

    class Meta:
        model = Price
        fields = ["id", "service", "product", "price", "sell_price"]


class PriceDetailSerializer(serializers.ModelSerializer):
    """For retrieving full price details."""

    service = serializers.StringRelatedField()
    product = serializers.StringRelatedField()

    class Meta:
        model = Price
        fields = [
            "id",
            "service",
            "product",
            "price",
            "sell_price",
            "created_at",
            "updated_at",
        ]


class PriceCreateUpdateSerializer(serializers.ModelSerializer):
    """For creating & updating prices."""

    class Meta:
        model = Price
        fields = ["service", "product", "price", "sell_price"]
