from rest_framework import serializers
from order.models.order_model import Order


class OrderListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for listing orders."""

    user = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = [
            "id",
            "purchase_id",
            "user",
            "final_amount",
            "status",
            "payment_status",
        ]


class OrderDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for a single order."""

    user = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = [
            "id",
            "purchase_id",
            "user",
            "total_amount",
            "discount_amount",
            "final_amount",
            "status",
            "payment_status",
            "payment_method",
            "notes",
            "created_at",
            "updated_at",
        ]


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating & updating orders."""

    class Meta:
        model = Order
        fields = [
            "user",
            "total_amount",
            "discount_amount",
            "final_amount",
            "status",
            "payment_status",
            "payment_method",
            "notes",
        ]
