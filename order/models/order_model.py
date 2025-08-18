from django.db import models
from common_bases.base_model import BaseModel
from user.models import CustomUser
import uuid


class Order(BaseModel):
    class OrderStatus(models.TextChoices):
        PENDING = "PENDING", "Pending"
        PROCESSING = "PROCESSING", "Processing"
        COMPLETED = "COMPLETED", "Completed"
        CANCELED = "CANCELED", "Canceled"

    class PaymentStatus(models.TextChoices):
        PENDING = "PENDING", "Pending"
        PAID = "PAID", "Paid"
        FAILED = "FAILED", "Failed"
        REFUNDED = "REFUNDED", "Refunded"

    class PaymentMethod(models.TextChoices):
        CASH = "CASH", "Cash on Delivery"
        CARD = "CARD", "Credit/Debit Card"
        ONLINE = "ONLINE", "Online Payment"

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="orders"
    )
    purchase_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING
    )
    payment_status = models.CharField(
        max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING
    )
    payment_method = models.CharField(
        max_length=20, choices=PaymentMethod.choices, default=PaymentMethod.CASH
    )
    notes = models.TextField(blank=True, null=True)
    order_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-order_at"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order {self.purchase_id} - {self.user.phone_number}"
