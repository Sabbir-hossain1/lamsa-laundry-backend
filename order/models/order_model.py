from django.db import models
from common_bases.base_model import BaseModel
from service.models.price_model import Price
from service.models.product_model import Product
from service.models.service_model import Service
from user.models import CustomUser
import uuid
from django.db import transaction
from order.models.order_item_model import OrderItem
from order.models.schedule_model import Schedule


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

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order {self.purchase_id} - {self.user.phone_number}"

    @staticmethod
    @transaction.atomic
    def create_order(
        products, schedule, user, notes="", discount=0, payment_method="CASH"
    ):
        """
        products: list of dicts like
        [
            {"service": id, "product": id, "quantity": 2, "price": id},
            {"service": id, "product": id, "quantity": 1, "price": id},
        ]
        """
        order = Order.objects.create(
            user=user,
            notes=notes,
            status=Order.OrderStatus.PENDING,
            payment_status=Order.PaymentStatus.PENDING,
            payment_method=payment_method,
        )

        # create scheudle for the order
        schedule = Schedule.objects.create(
            order=order,
            pickup_date=schedule["pickup_date"],
            pickup_time=schedule["pickup_time"],
            deliver_date=schedule["deliver_date"],
            deliver_time=schedule["delivery_time"],
            proposed_by="provider" if user.is_admin else "client",
            status="pending",
        )

        total_amount = 0

        for product_data in products:
            item = order.create_order_item(order, product_data)
            total_amount += item.total

        final_amount = total_amount - discount

        order.total_amount = total_amount
        order.discount_amount = discount
        order.final_amount = final_amount
        order.save()

        return order

    @staticmethod
    def create_order_item(order, product_data):
        """
        product_data: dict with service, product, quantity, unit_price
        """
        quantity = product_data.get("quantity", 1)
        price = Price.objects.get(id=product_data["price"])
        total = quantity * price.sell_price
        service = Service.objects.get(id=product_data["service"])
        product = Product.objects.get(id=product_data["product"])

        return OrderItem.objects.create(
            order=order,
            service=service,
            product=product,
            quantity=quantity,
            unit_price=price.sell_price,
            total=total,
        )

    @staticmethod
    def create_schedule(
        order, pickup_date=None, picku_time=None, delivery_date=None, delivery_time=None
    ):
        return Schedule.objects.create(
            order=order,
            pickup_date=pickup_date,
            picku_time=picku_time,
            delivery_date=delivery_date,
            delivery_time=delivery_time,
        )
