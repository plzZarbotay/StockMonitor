from rest_framework import serializers

from core.models import User

__all__ = []


class UpdateFirstNameSerializer(serializers.Serializer):
    """Serializer for updating the first name of a user"""

    first_name = serializers.CharField(max_length=100)


class GetUserProfileSerializer(serializers.ModelSerializer):
    """Serializer for getting a user profile"""

    class Meta:
        """Meta class"""

        model = User
        fields = ("first_name", "email", "theme")
