from rest_framework import serializers
from user.models import CustomUser


# Base serializer (common fields)
class CustomUserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "phone_number",
            "created_at",
            "updated_at",
            "is_active",
            "is_staff",
        ]


# List serializer
class CustomUserListSerializer(CustomUserBaseSerializer):
    class Meta(CustomUserBaseSerializer.Meta):
        fields = ["id", "phone_number", "is_active", "created_at"]


# Detail serializer
class CustomUserDetailSerializer(CustomUserBaseSerializer):
    pass  # Inherits all fields


# Create serializer
class CustomUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["phone_number", "password", "is_active", "is_staff"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser.objects.create_user(password=password, **validated_data)
        return user


# Update serializer
class CustomUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["phone_number", "is_active", "is_staff"]
