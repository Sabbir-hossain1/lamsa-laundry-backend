from common_bases.base_model import BaseModel
from django.db import models


class Service(BaseModel):
    title = models.CharField(max_length=255)
    primary_image = models.ImageField(
        upload_to="assests/services/primary/", blank=True, null=True
    )
    secondary_image = models.ImageField(
        upload_to="assests/services/secondary/", blank=True, null=True
    )

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title
