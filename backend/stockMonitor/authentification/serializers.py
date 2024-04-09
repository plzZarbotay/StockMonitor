from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authentification.errors import Errors
from core import models

__all__ = []


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for registration"""

    class Meta:
        model = models.User
        fields = (
            "email",
            "password",
        )


class CheckEmailExistanceSerializer(serializers.Serializer):
    """Serializer for checking email"""

    email = serializers.EmailField(max_length=200)
