from rest_framework.routers import DefaultRouter
from order.views.order_model_viewset import OrderViewSet

router = DefaultRouter()
router.register("orders", OrderViewSet, basename="order")

urlpatterns = router.urls
