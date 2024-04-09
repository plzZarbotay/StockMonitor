from rest_framework import serializers

from core import models

__all__ = []


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for registration"""

    class Meta:
        """Meta class"""

        model = models.User
        fields = (
            "email",
            "password",
        )

    def create(self, validated_data):
        """Create a new user"""
        return models.User.objects.create_user(**validated_data)


class CheckEmailExistanceSerializer(serializers.Serializer):
    """Serializer for checking email"""

    email = serializers.EmailField(max_length=200)
