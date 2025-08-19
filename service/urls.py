from rest_framework.routers import DefaultRouter
from service.views.serive_modelviewset import ServiceViewSet

router = DefaultRouter()
router.register("services", ServiceViewSet, basename="service")

urlpatterns = router.urls
