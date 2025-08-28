from rest_framework import serializers
from service.models.price_model import Price
from service.models.product_model import Product
from service.models.service_model import Service


class ServiceDropdownSerializer(serializers.ModelSerializer):

    label = serializers.CharField(source="title")
    value = serializers.IntegerField(source="id")

    class Meta:
        model = Service
        fields = ["label", "value"]


class ProductDropdownSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source="name", read_only=True)
    value = serializers.IntegerField(source="id", read_only=True)
    # image = serializers.ImageField(use_url=True, read_only=True)

    class Meta:
        model = Product
        fields = ["label", "value"]


class PriceListSerializer(serializers.ModelSerializer):
    """For listing prices (lightweight)."""

    service = ServiceDropdownSerializer()
    product = ProductDropdownSerializer()

    class Meta:
        model = Price
        fields = ["id", "service", "product", "sell_price"]


class PriceDetailSerializer(serializers.ModelSerializer):
    """For retrieving full price details."""

    service = ServiceDropdownSerializer()
    product = ProductDropdownSerializer()

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
