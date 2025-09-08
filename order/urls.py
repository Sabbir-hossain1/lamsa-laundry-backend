from rest_framework.routers import DefaultRouter
from order.views.order_model_viewset import OrderViewSet
from order.views.order_item_model_viewset import OrderItemModelViewSet
from order.views.schedule_model_viewset import ScheduleModelViewSet

router = DefaultRouter()
router.register("orders", OrderViewSet, basename="order")
router.register("order-items", OrderItemModelViewSet, basename="order-items")
router.register("schedules", ScheduleModelViewSet, basename="schedules")

urlpatterns = router.urls
