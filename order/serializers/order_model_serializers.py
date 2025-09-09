from django.db import transaction
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
            "payment_method",
            "created_at",
            "updated_at",
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


class OrderUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"


class OrderCreateSerializer(serializers.Serializer):
    """Serializer for creating & updating orders."""

    products = serializers.ListField(child=serializers.DictField(), required=True)
    schedule = serializers.DictField(required=True)
    notes = serializers.CharField(required=False, allow_blank=True)

    def validate(self, data):
        user = self.context["request"].user
        if not user:
            raise serializers.ValidationError("User are required")
        return data

    def create(self, validated_data):
        user = self.context["request"].user
        try:
            order = Order.create_order(
                user=user,
                products=validated_data.get("products", []),
                schedule=validated_data.get("schedule", {}),
                notes=validated_data.get("notes", ""),
                discount=0,
                payment_method="CASH",
            )
            return order
        except Exception as e:
            print("Error in creating order", e)
            raise serializers.ValidationError("Failed to create order")
