from rest_framework.routers import DefaultRouter
from service.views.serive_modelviewset import ServiceViewSet
from service.views.product_model_viewset import ProductViewSet
from service.views.price_model_viewsets import PriceViewSet

router = DefaultRouter()
router.register("services", ServiceViewSet, basename="service")
router.register("products", ProductViewSet, basename="product")
router.register("prices", PriceViewSet, basename="price")


urlpatterns = router.urls
