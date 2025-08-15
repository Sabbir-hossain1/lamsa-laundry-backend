from rest_framework import viewsets

from user.models import CustomUser
from user.serializers.user_model_serializers import (
    CustomUserListSerializer,
    CustomUserDetailSerializer,
    CustomUserCreateSerializer,
    CustomUserUpdateSerializer,
)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CustomUserListSerializer
        elif self.action == "retrieve":
            return CustomUserDetailSerializer
        elif self.action == "create":
            return CustomUserCreateSerializer
        elif self.action in ["update", "partial_update"]:
            return CustomUserUpdateSerializer
        return CustomUserDetailSerializer
