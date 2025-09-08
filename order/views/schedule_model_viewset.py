from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from order.models.schedule_model import Schedule
from order.serializers.schedule_model_serializer import (
    ScheduleModelSerializer,
    ScheduleModelCreateSerializer,
)


class ScheduleModelViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return ScheduleModelCreateSerializer
        return ScheduleModelSerializer

    def get_queryset(self):
        return Schedule.objects.all()
