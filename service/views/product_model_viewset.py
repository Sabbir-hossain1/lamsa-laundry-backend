from rest_framework import viewsets, permissions
from service.models.product_model import Product

from service.serializers.price_model_serializers import ProductDropdownSerializer
from service.serializers.product_model_serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    ProductCreateUpdateSerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_queryset(self):
        """
        Customize queryset per action.
        Example: list only latest products.
        """
        qs = Product.objects.all()
        if self.action == "list":
            return qs.order_by("-created_at")
        return qs

    def get_permissions(self):
        """
        Control permissions per action.
        """
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]  # Public access
        return [permissions.IsAuthenticated()]  # Only logged-in users can modify

    def get_serializer_class(self):
        """
        Use different serializer depending on action.
        """
        if self.action == "list":
            if self.request.query_params.get("dropdown", None):
                return ProductDropdownSerializer
            return ProductListSerializer
        elif self.action == "retrieve":
            return ProductDetailSerializer
        return ProductCreateUpdateSerializer
