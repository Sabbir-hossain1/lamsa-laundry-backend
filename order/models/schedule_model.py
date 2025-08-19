from common_bases.base_model import BaseModel
from django.db import models


class Schedule(BaseModel):
    class ProposedBy(models.TextChoices):
        CLIENT = "client", "Client"
        PROVIDER = "provider", "Service Provider"

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        ACCEPTED = "accepted", "Accepted"
        REJECTED = "rejected", "Rejected"

    order = models.ForeignKey(
        "order.Order", on_delete=models.CASCADE, related_name="schedules"
    )
    pickup_date = models.DateField(blank=True, null=True)
    pickup_time = models.TimeField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    delivery_time = models.TimeField(blank=True, null=True)

    proposed_by = models.CharField(
        max_length=20, choices=ProposedBy.choices, default=ProposedBy.CLIENT
    )
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )

    def __str__(self):
        return f"Schedule (Order {self.order.id}) - {self.status}"
