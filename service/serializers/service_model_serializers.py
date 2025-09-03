from rest_framework import serializers

from service.models.service_model import Service
from service.serializers.price_model_serializers import PriceListSerializer


class ServiceListSerializer(serializers.ModelSerializer):
    """For listing services (lightweight)."""

    class Meta:
        model = Service
        fields = ["id", "title", "primary_image", "secondary_image"]


class AdminServiceDetailSerializer(serializers.ModelSerializer):
    """For retrieving single service details."""

    class Meta:
        model = Service
        fields = ["id", "title", "primary_image", "secondary_image"]


class ServiceDetailSerializer(serializers.ModelSerializer):
    """For retrieving single service details."""

    products = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ["id", "title", "secondary_image", "products"]

    def get_products(self, obj):
        prices = obj.prices
        serializer = PriceListSerializer(prices, many=True)
        return serializer.data


class ServiceCreateUpdateSerializer(serializers.ModelSerializer):
    """For creating & updating services."""

    class Meta:
        model = Service
        fields = ["title", "primary_image", "secondary_image"]


class ServiceDropdownSerializer(serializers.ModelSerializer):

    label = serializers.CharField(source="title")
    value = serializers.IntegerField(source="id")

    class Meta:
        model = Service
        fields = ["label", "value"]
