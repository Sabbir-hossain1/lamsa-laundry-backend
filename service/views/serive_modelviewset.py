from rest_framework import viewsets, permissions
from service.models.service_model import Service
from service.serializers.service_model_serializers import (
    ServiceListSerializer,
    ServiceDetailSerializer,
    ServiceCreateUpdateSerializer,
)


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()

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
        if self.action == "list":
            return ServiceListSerializer
        elif self.action == "retrieve":
            return ServiceDetailSerializer
        return ServiceCreateUpdateSerializer
