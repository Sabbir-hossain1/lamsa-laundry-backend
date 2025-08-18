from rest_framework import serializers
from service.models.service_model import Service


class ServiceListSerializer(serializers.ModelSerializer):
    """For listing services (lightweight)."""

    class Meta:
        model = Service
        fields = ["id", "title", "primary_image"]


class ServiceDetailSerializer(serializers.ModelSerializer):
    """For retrieving single service details."""

    class Meta:
        model = Service
        fields = ["id", "title", "primary_image", "secondary_image"]


class ServiceCreateUpdateSerializer(serializers.ModelSerializer):
    """For creating & updating services."""

    class Meta:
        model = Service
        fields = ["title", "primary_image", "secondary_image"]
