from rest_framework import serializers
from service.models.product_model import Product


class ProductListSerializer(serializers.ModelSerializer):
    """For listing products (lightweight)."""

    class Meta:
        model = Product
        fields = ["id", "name", "image"]


class ProductDetailSerializer(serializers.ModelSerializer):
    """For retrieving product details."""

    class Meta:
        model = Product
        fields = ["id", "name", "image", "created_at", "updated_at"]


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    """For creating & updating products."""

    class Meta:
        model = Product
        fields = ["name", "image"]
