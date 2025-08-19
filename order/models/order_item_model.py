from common_bases.base_model import BaseModel
from django.db import models
from order.models.order_model import Order
from service.models.service_model import Service
from service.models.product_model import Product


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="order_items"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="order_items"
    )
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def __str__(self):
        return f"{self.quantity} × {self.product.name} ({self.service.title})"
