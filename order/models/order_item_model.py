from common_bases.base_model import BaseModel
from django.db import models


class OrderItem(BaseModel):
    order = models.ForeignKey(
        "order.Order", on_delete=models.CASCADE, related_name="items"
    )
    service = models.ForeignKey(
        "service.Service", on_delete=models.CASCADE, related_name="order_items"
    )
    product = models.ForeignKey(
        "service.Product", on_delete=models.CASCADE, related_name="order_items"
    )
    price = models.ForeignKey(
        "service.Price",
        related_name="order_items",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def __str__(self):
        return f"{self.quantity} × {self.product.name} ({self.service.title})"
