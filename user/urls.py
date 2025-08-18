from rest_framework.routers import DefaultRouter
from user.views.user_model_viewset import CustomUserViewSet, AuthViewSets

router = DefaultRouter()
router.register(r"auth", AuthViewSets, basename="auth"),
router.register(r"users", CustomUserViewSet, basename="user")
urlpatterns = router.urls
