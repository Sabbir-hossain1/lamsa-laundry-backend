from django.contrib import admin
from service.models.service_model import Service
from service.models.product_model import Product
from user.models import Notification

admin.site.register(Service)
admin.site.register(Notification)
admin.site.register(Product)
