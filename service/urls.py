from rest_framework.routers import DefaultRouter
from service.views.serive_modelviewset import ServiceViewSet
from service.views.product_model_viewset import ProductViewSet

router = DefaultRouter()
router.register("services", ServiceViewSet, basename="service")
router.register("products", ProductViewSet, basename="product")

urlpatterns = router.urls
