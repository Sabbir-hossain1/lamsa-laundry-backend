from rest_framework import permissions, viewsets

from service.models.price_model import Price
from service.serializers.price_model_serializers import (
    AdminPriceDetailSerializer,
    PriceCreateUpdateSerializer,
    PriceDetailSerializer,
    PriceListSerializer,
)


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceListSerializer

    def get_queryset(self):
        """
        Customize queryset per action.
        Example: filter by service or product if query params are provided.
        """
        qs = Price.objects.all()

        service_id = self.request.query_params.get("service")
        product_id = self.request.query_params.get("product")

        if service_id:
            qs = qs.filter(service_id=service_id)
        if product_id:
            qs = qs.filter(product_id=product_id)

        return qs.order_by("-created_at")

    def get_permissions(self):
        """
        Control permissions per action.
        """
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]  # Public can view
        return [permissions.IsAuthenticated()]  # Auth required for create/update/delete

    def get_serializer_class(self):
        """
        Use different serializer depending on action and query params.
        """
        admin_site = self.request.query_params.get("admin_site")

        if self.action == "list":
            return PriceListSerializer
        elif self.action == "retrieve":
            if admin_site in ["true", "1", "yes"]:
                return AdminPriceDetailSerializer
            return PriceDetailSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return PriceCreateUpdateSerializer
        return super().get_serializer_class()
