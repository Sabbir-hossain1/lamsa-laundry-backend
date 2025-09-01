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
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["label", "value", "image"]

    def get_image(self, obj):
        """Return absolute URL for image."""
        if obj.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image.url)
            # Fallback for when request is not available
            return f"http://ll.softmaxshop.com/{obj.image.url}"
        return None


class PriceListSerializer(serializers.ModelSerializer):
    """For listing prices (lightweight)."""

    services = serializers.SerializerMethodField()
    product = ProductDropdownSerializer()

    class Meta:
        model = Price
        fields = [
            "services",
            "product",
        ]

    def get_services(self, obj):
        product_services = []
        product_services_objects = Price.objects.filter(product=obj.product)

        for product_service in product_services_objects:
            product_services.append(
                {
                    "service_id": product_service.service.id,
                    "service_title": product_service.service.title,
                    "price_id": product_service.id,
                    "sell_price": product_service.sell_price,
                }
            )
        return product_services


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
