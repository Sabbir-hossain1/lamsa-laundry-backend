from user.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken


def login_user(phone_number):
    user = CustomUser.objects.get(phone_number__iexact=phone_number)
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "user": {
            "id": user.id,
            "phone_number": user.phone_number,
            "is_staff": user.is_staff,
            "is_active": user.is_active,
            "is_superuser": user.is_superuser,
        },
    }
