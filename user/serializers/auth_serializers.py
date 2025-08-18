from rest_framework import serializers
from user.models import CustomUser
from user.serializers.user_model_serializers import CustomUserDetailSerializer


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        try:
            user = CustomUser.objects.get(
                phone_number__iexact=attrs["phone_number"], is_active=True
            )
            if not user.check_password(attrs["password"]):
                raise Exception("Wrong password!")
        except Exception:
            raise serializers.ValidationError(
                {"password": "Email or password is incorrect"}
            )
        return attrs


class LoginResponseSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
    user = CustomUserDetailSerializer()


class DefaultSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ("phone_number", "password")

    def validate(self, attrs):
        if (
            attrs["phone_number"]
            and CustomUser.objects.filter(
                phone_number__iexact=attrs["phone_number"]
            ).exists()
        ):
            raise serializers.ValidationError(
                {"phone_number": "An account already exists with this phone_number."}
            )
        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = CustomUser.objects.create(is_active=True, **validated_data)
        user.set_password(password)
        user.save()

        # group, created = CustomGroup.objects.get_or_create(name="Customer")
        # user.groups.add(group)

        # user_service = UserService(user)
        # user_service.send_welcome_email()
        # user_service.send_verification_email()

        return user


# class ResetPasswordSerializer(serializers.Serializer):
#     uuid = serializers.CharField(required=True)
#     token = serializers.CharField(required=True)
#     password = serializers.CharField(required=True)
#     password2 = serializers.CharField(required=True)

#     def validate(self, attrs):
#         if attrs["password"] != attrs["password2"]:
#             raise serializers.ValidationError({"password2": "Password do not match."})

#         if attrs["uuid"] is not None and attrs["token"] is not None:
#             decoded_value = force_str(urlsafe_base64_decode(attrs["uuid"]))
#             user_id, _ = decoded_value.split("-")
#             user = Account.objects.get(pk=user_id)
#             if not reset_password_token_generator.check_token(user, attrs["token"]):
#                 raise serializers.ValidationError(
#                     {"non_field_errors": ["Given token or uuid has expired"]}
#                 )
#         return attrs


# class ChangePasswordSerializer(serializers.Serializer):
#     old_password = serializers.CharField()
#     new_password = serializers.CharField()
#     new_password_confirmation = serializers.CharField()

#     def validate_old_password(self, value):
#         current_user = self.context["request"].user
#         if not current_user.check_password(value):
#             raise serializers.ValidationError("Old password do not match")

#         return value

#     def validate(self, attrs):
#         new_password = attrs.get("new_password", None)
#         new_password_confirmation = attrs.get("new_password_confirmation", None)

#         if not new_password == new_password_confirmation:
#             raise serializers.ValidationError(
#                 {"new_password_confirmation": ["The confirm password does not match"]}
#             )

#         return attrs
