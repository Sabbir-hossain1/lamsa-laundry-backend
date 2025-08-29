from rest_framework import permissions, viewsets

from service.models.service_model import Service
from service.serializers.service_model_serializers import (
    AdminServiceDetailSerializer,
    ServiceCreateUpdateSerializer,
    ServiceDetailSerializer,
    ServiceDropdownSerializer,
    ServiceListSerializer,
)


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()

    def get_serializer_context(self):
        """Pass request to serializer context."""
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def get_queryset(self):
        """
        Customize queryset based on action.
        Example: list only active services.
        """
        qs = Service.objects.all()
        if self.action == "list":
            return qs.order_by("-id")  # newest first
        return qs

    def get_permissions(self):
        """
        Control permissions per action.
        """
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]  # public
        return [permissions.IsAuthenticated()]  # write requires auth

    def get_serializer_class(self):
        """
        Use different serializer depending on action.
        """
        admin_site = self.request.query_params.get("admin_site")
        if self.action == "list":
            if self.request.query_params.get("dropdown", None):
                return ServiceDropdownSerializer
            return ServiceListSerializer
        elif self.action == "retrieve":
            if admin_site:
                return AdminServiceDetailSerializer
            return ServiceDetailSerializer
        return ServiceCreateUpdateSerializer
