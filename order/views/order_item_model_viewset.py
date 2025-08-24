from rest_framework.viewsets import ModelViewSet
from order.models.order_item_model import OrderItem
from order.serializers.order_item_model_seiralizer import (
    OrderItemSerializer,
    OrderItemListSerializer,
    OrderItemUpdateSerializer,
)


class OrderItemModelViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return OrderItemListSerializer
        elif self.action in ["update", "partial_update"]:
            return OrderItemUpdateSerializer
        return super().get_serializer_class()
