from django.contrib import admin
from order.models.order_model import Order
from order.models.order_item_model import OrderItem
from order.models.schedule_model import Schedule

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Schedule)
