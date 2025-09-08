from rest_framework.serializers import ModelSerializer
from order.models.schedule_model import Schedule


class ScheduleModelSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "order"]


class ScheduleModelCreateSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"        
