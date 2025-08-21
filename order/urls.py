from rest_framework.routers import DefaultRouter
from order.views.order_model_viewset import OrderViewSet
from order.views.order_item_model_viewset import OrderItemModelViewset

router = DefaultRouter()
router.register("orders", OrderViewSet, basename="order")
router.register("order-items", OrderItemModelViewset, basename="order-items")

urlpatterns = router.urls
