from rest_framework import viewsets, permissions
from user.models import Address
from user.serializers.address_serializer import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset()

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)

    def get_permissions(self):
        return super().get_permissions()
