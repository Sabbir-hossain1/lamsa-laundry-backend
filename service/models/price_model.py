from common_bases.base_model import BaseModel
from django.db import models
from service.models.service_model import Service
from service.models.product_model import Product


class Price(BaseModel):
    service = models.ForeignKey(
        "Service", on_delete=models.CASCADE, related_name="prices"
    )
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="prices"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ("service", "product")  # prevents duplicate entries
        verbose_name = "Price"
        verbose_name_plural = "Prices"

    def __str__(self):
        return f"{self.product.name} ({self.service.title}) - {self.sell_price}"
