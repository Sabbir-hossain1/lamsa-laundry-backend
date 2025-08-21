from rest_framework import serializers
from order.models.order_item_model import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for single OrderItem"""
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderItemListSerializer(serializers.ModelSerializer):
    """Serializer for listing multiple OrderItems"""
    class Meta:
        model = OrderItem
        fields = "__all__"
        # ⚡ if no difference from OrderItemSerializer, you can remove this


class OrderItemUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating OrderItem (only price & quantity)"""
    class Meta:
        model = OrderItem
        fields = ["price", "quantity"]
