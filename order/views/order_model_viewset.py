from rest_framework import viewsets, permissions
from order.models.order_model import Order
from order.serializers.order_model_serializers import (
    OrderCreateSerializer,
    OrderListSerializer,
    OrderDetailSerializer,
    OrderUpdateSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

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


        status = self.request.query_params.get("order_status")
        payment_method = self.request.query_params.get("payment_method")
        payment_status = self.request.query_params.get("payment_status")

        if status:
            qs = qs.filter(status=status)
        if payment_status:
            qs = qs.filter(payment_status=payment_status)
        if payment_method:
            qs = qs.filter(payment_method=payment_method)

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
        elif self.action in ["update", "partial_update"]:
            return OrderUpdateSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = OrderCreateSerializer(
                data=request.data, context={"request": request}
            )
            serializer.is_valid(raise_exception=True)
            try:
                order = serializer.save()
                return Response(
                    {
                        "message": "Order has been placed successfully.",
                        "order_id": serializer.instance.id,
                    },
                    status=status.HTTP_201_CREATED,
                )
            except Exception as e:
                print("Error creating order:", e)
                return Response(
                    {"detail": "An error occurred while creating the order."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
