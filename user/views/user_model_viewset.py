from rest_framework import viewsets
from rest_framework.response import Response
from user.services.auth_viewset_services import login_user

from user.models import CustomUser
from user.serializers.user_model_serializers import (
    CustomUserListSerializer,
    CustomUserDetailSerializer,
    CustomUserCreateSerializer,
    CustomUserUpdateSerializer,
)
from user.utils.initialModelVieset import InitialModelViewSet
from user.serializers.auth_serializers import (
    LoginResponseSerializer,
    LoginSerializer,
    DefaultSignUpSerializer,
)
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CustomUserListSerializer
        elif self.action == "retrieve":
            return CustomUserDetailSerializer
        elif self.action == "create":
            return CustomUserCreateSerializer
        elif self.action in ["update", "partial_update"]:
            return CustomUserUpdateSerializer
        return CustomUserDetailSerializer


class AuthViewSets(InitialModelViewSet):
    queryset = []

    def get_serializer_class(self):
        if self.action == "login":
            return LoginSerializer
        elif self.action == "signup":
            return DefaultSignUpSerializer
        return super().get_serializer_class()

    @extend_schema(
        request=LoginSerializer,
        responses={
            200: LoginResponseSerializer,
        },
        operation_id="login",
        tags=["Authentication"],
    )
    @action(detail=False, methods=["POST"], name="Login", url_path="login")
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        login_data = login_user(serializer.validated_data["phone_number"])
        return Response(login_data)

    @extend_schema(
        request=DefaultSignUpSerializer,
        responses={
            200: None,
        },
        operation_id="signup",
        tags=["Authentication"],
    )
    @action(detail=False, methods=["POST"], name="SignUp", url_path="signup")
    def signup(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"message": "Your account has been successfully created!"})
