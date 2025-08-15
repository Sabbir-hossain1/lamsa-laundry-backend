from rest_framework.routers import DefaultRouter
from user.views.user_model_viewset import CustomUserViewSet

router = DefaultRouter()
router.register(r"users", CustomUserViewSet, basename="user")

urlpatterns = router.urls
