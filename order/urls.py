from rest_framework.routers import DefaultRouter
from order.views.order_model_viewset import OrderViewSet
from order.views.order_item_model_viewset import OrderItemModelViewSet

router = DefaultRouter()
router.register("orders", OrderViewSet, basename="order")
router.register("order-items", OrderItemModelViewSet, basename="order-items")

urlpatterns = router.urls
