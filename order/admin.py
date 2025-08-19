from django.contrib import admin
from order.models.order_model import Order
from order.models.order_item_model import OrderItem

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
