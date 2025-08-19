from common_bases.base_model import BaseModel
from django.db import models


class Product(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="assests/products/", blank=True, null=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
