from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from user.models import CustomUser
from user.serializers.auth_serializers import (
    DefaultSignUpSerializer,
    LoginResponseSerializer,
    LoginSerializer,
    AdminLoginSerializer,
)
from user.serializers.user_model_serializers import (
    CustomUserCreateSerializer,
    CustomUserDetailSerializer,
    CustomUserListSerializer,
    CustomUserUpdateSerializer,
    UserProfileSerializer,
)
from user.services.auth_viewset_services import login_user
from user.utils.initialModelVieset import InitialModelViewSet


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()

    def get_permissions(self):
        if self.action in [
            "create",
            "list",
            "retrieve",
            "update",
            "partial_update",
            "destroy",
        ]:
            return [IsAdminUser()]
        elif self.action in ["me"]:
            return [IsAuthenticated()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "list":
            return CustomUserListSerializer
        elif self.action == "retrieve":
            return CustomUserDetailSerializer
        elif self.action == "create":
            return CustomUserCreateSerializer
        elif self.action in ["update", "partial_update"]:
            return CustomUserUpdateSerializer
        elif self.action == "me":
            return UserProfileSerializer
        return CustomUserDetailSerializer

    @action(detail=False, methods=["GET"], name="me", url_path="me")
    def me(self, request):
        # if not request.user.is_authenticated:
        #     return Response(
        #         {"detail": "Authentication credentials were not provided."},
        #         status=status.HTTP_401_UNAUTHORIZED,
        #     )

        # Get the user's profile (assuming OneToOne relationship)
        try:
            profile = request.user.profile
        except AttributeError:
            return Response(
                {"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(profile)
        return Response(serializer.data)


class AuthViewSets(InitialModelViewSet):
    queryset = []

    def get_serializer_class(self):
        if self.action == "login":
            return LoginSerializer
        elif self.action == "admin_login":
            return AdminLoginSerializer
        elif self.action == "signup":
            return DefaultSignUpSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ["login", "signup", "admin_login"]:
            return [AllowAny()]
        return super().get_permissions()

    @extend_schema(
        request=LoginSerializer,
        responses={
            200: LoginResponseSerializer,
        },
        operation_id="login",
        tags=["Authentication"],
        description="Login to the system using phone number and password",
    )
    @action(detail=False, methods=["POST"], name="Login", url_path="login")
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        login_data = login_user(serializer.validated_data["phone_number"])
        return Response(login_data)

    @extend_schema(
        request=AdminLoginSerializer,
        responses={
            200: LoginResponseSerializer,
        },
        operation_id="admin-login",
        tags=["Authentication"],
        description="Login to the system using phone number and password",
    )
    @action(detail=False, methods=["POST"], name="admin_Login", url_path="admin-login")
    def admin_login(self, request):
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
        description="Sign up for a new account using phone number and password",
    )
    @action(detail=False, methods=["POST"], name="SignUp", url_path="signup")
    def signup(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"message": "Your account has been successfully created!"})
