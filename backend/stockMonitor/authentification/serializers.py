import rest_framework.serializers

import core.models
import core.serializers

__all__ = []


class RegisterSerializer(rest_framework.serializers.ModelSerializer):
    """Serializer for registration"""

    class Meta:
        """Meta class"""

        model = core.models.User
        fields = (
            "email",
            "password",
        )

    def create(self, validated_data):
        """Create a new user"""
        return core.models.User.objects.create_user(**validated_data)


class CheckEmailExistanceSerializer(rest_framework.serializers.Serializer):
    """Serializer for checking email"""

    email = rest_framework.serializers.EmailField(
        max_length=200,
    )


class ChangePasswordSerializer(rest_framework.serializers.Serializer):
    """Serializer for changing password"""
    old_password = core.serializers.PasswordField(
        required=True,
    )
    new_password = core.serializers.PasswordField(
        required=True,
    )


class ResetPasswordEmailSerializer(rest_framework.serializers.Serializer):
    """Serializer for reseting email"""
    email = rest_framework.serializers.EmailField(
        required=True,
        max_length=200,
    )
