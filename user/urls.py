from rest_framework.routers import DefaultRouter
from user.views.user_model_viewset import CustomUserViewSet, AuthViewSets
from rest_framework_simplejwt.views import TokenRefreshView
from user.views.address_model_viewset import AddressViewSet

from django.urls import path

router = DefaultRouter()
router.register(r"auth", AuthViewSets, basename="auth"),
router.register(r"users", CustomUserViewSet, basename="user")
router.register(r"address", AddressViewSet, basename="address")

urlpatterns = [
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + router.urls
