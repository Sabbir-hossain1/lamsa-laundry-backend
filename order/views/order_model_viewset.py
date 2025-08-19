from rest_framework import viewsets, permissions
from order.models.order_model import Order
from order.serializers.order_model_serializers import (
    OrderListSerializer,
    OrderDetailSerializer,
    OrderCreateUpdateSerializer,
)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    def get_queryset(self):
        """
        Control queryset per action.
        - Admins see all orders
        - Normal users see only their orders
        - Support filtering by status/payment_status
        """
        qs = Order.objects.all()

        # Non-admin users see only their orders
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)

        # Optional filtering by query params
        status = self.request.query_params.get("status")
        payment_status = self.request.query_params.get("payment_status")

        if status:
            qs = qs.filter(status=status)
        if payment_status:
            qs = qs.filter(payment_status=payment_status)

        return qs.order_by("-created_at")

    def get_permissions(self):
        """
        Control permissions per action.
        """
        if self.action in ["list", "retrieve", "create"]:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAdminUser()]  # Only admins can update/delete

    def get_serializer_class(self):
        """
        Use different serializer depending on action.
        """
        if self.action == "list":
            return OrderListSerializer
        elif self.action == "retrieve":
            return OrderDetailSerializer
        return OrderCreateUpdateSerializer
